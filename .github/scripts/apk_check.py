#!/usr/bin/env python3
"""Mind It! · check a built APK the way an Android device reads it (build 135).

Why: builds 129–134 installed but showed the name "application" and closed at once on a real Galaxy Tab (Android 16).
The compiled manifest stores every string attribute twice — a raw string index and a typed value (Res_value,
TYPE_STRING, data = string index) — and Android reads the TYPED one. axml_fgs.py had moved only the raw indexes, so
`aapt dump badging` (which prints the raw strings) looked right while the device read the string one place earlier:
label "application", activity class "activity". This checker reads the typed values, like the device does.

Checks (standard library only, so it also runs in the GitHub release workflow):
  · the APK is a zip with AndroidManifest.xml, classes.dex, resources.arsc (stored uncompressed, 4-byte aligned),
    the icon resources and assets/mindit.html + assets/start.html;
  · every string attribute in the manifest: typed value == raw value (no shifted strings);
  · package com.mindit.app, versionName 1.69, versionCode = the expected build, minSdk 24, targetSdk 35;
  · the app and launcher activity are named exactly "Mind It!", the icon is a resource reference;
  · the launcher activity .MainActivity (MAIN + LAUNCHER, exported) and the service .HostService
    (foregroundServiceType connectedDevice) exist as classes in classes.dex;
  · the permissions the app needs are all requested, by their exact names;
  · each element's attributes are in resource-id order (Android's parser expects it).
Usage: python3 apk_check.py <file.apk> [<expected versionCode>]      exit 0 = OK, 1 = problems (listed)
"""
import struct, sys, zipfile

ANDROID_NS = "http://schemas.android.com/apk/res/android"
NONE = 0xFFFFFFFF
T_REF, T_STRING, T_INT_DEC, T_INT_HEX, T_BOOL = 0x01, 0x03, 0x10, 0x11, 0x12
PACKAGE, VERSION_NAME, LABEL, MIN_SDK, TARGET_SDK = "com.mindit.app", "1.69", "Mind It!", 24, 35
PERMISSIONS = ["android.permission.INTERNET", "android.permission.ACCESS_NETWORK_STATE", "android.permission.ACCESS_WIFI_STATE",
               "android.permission.CHANGE_WIFI_MULTICAST_STATE", "android.permission.CAMERA", "android.permission.WAKE_LOCK",
               "android.permission.FOREGROUND_SERVICE", "android.permission.FOREGROUND_SERVICE_CONNECTED_DEVICE",
               "android.permission.POST_NOTIFICATIONS"]
ATTR_IDS = {"label": 0x01010001, "icon": 0x01010002, "name": 0x01010003, "versionCode": 0x0101021B, "versionName": 0x0101021C,
            "minSdkVersion": 0x0101020C, "targetSdkVersion": 0x01010270, "exported": 0x01010010, "foregroundServiceType": 0x01010599}

def u16(b, o): return struct.unpack_from("<H", b, o)[0]
def u32(b, o): return struct.unpack_from("<I", b, o)[0]

def read_pool(b, o):
    typ, hs, size = struct.unpack_from("<HHI", b, o)
    if typ != 0x0001: raise ValueError("no string pool")
    count, styles, flags, sstart, ystart = struct.unpack_from("<IIIII", b, o + 8)
    utf8 = bool(flags & 0x100); out = []
    for i in range(count):
        p = o + sstart + u32(b, o + hs + 4 * i)
        if utf8:
            n = b[p]; p += 1
            if n & 0x80: p += 1
            n = b[p]; p += 1
            if n & 0x80: n = ((n & 0x7F) << 8) | b[p]; p += 1
            out.append(b[p:p + n].decode("utf-8", "replace"))
        else:
            n = u16(b, p); p += 2
            if n & 0x8000: n = ((n & 0x7FFF) << 16) | u16(b, p); p += 2
            out.append(b[p:p + 2 * n].decode("utf-16-le", "replace"))
    return out, size

def parse_manifest(b):
    """→ list of elements: {tag, depth, attrs:{name:(typed python value, dtype, raw string, resid)}}, problems"""
    problems = []
    if u16(b, 0) != 0x0003: raise ValueError("not a compiled XML file")
    strings, psize = read_pool(b, 8)
    o = 8 + psize; resids = []
    if u16(b, o) == 0x0180:
        rhs, rsize = u16(b, o + 2), u32(b, o + 4)
        resids = [u32(b, o + rhs + 4 * i) for i in range((rsize - rhs) // 4)]; o += rsize
    els = []; depth = 0
    def s(i): return None if i == NONE else (strings[i] if i < len(strings) else "<bad index %d>" % i)
    while o < len(b):
        typ, hs, size = struct.unpack_from("<HHI", b, o)
        if size < 8: raise ValueError("broken XML chunk")
        if typ == 0x0102:
            ext = o + hs
            ens, ename, astart, asz, acount = struct.unpack_from("<IIHHH", b, ext)
            tag = s(ename); attrs = {}; order = []
            for i in range(acount):
                a = ext + astart + i * asz
                ans, aname, araw = struct.unpack_from("<III", b, a)
                vsize, vres0, vtype, vdata = struct.unpack_from("<HBBI", b, a + 8 + 4)
                name = s(aname); rid = resids[aname] if aname < len(resids) else 0
                if ans != NONE and s(ans) == ANDROID_NS and rid == 0:
                    problems.append("<%s android:%s> has no resource id (the device would not recognise it)" % (tag, name))
                raw = s(araw)
                if vtype == T_STRING:
                    val = s(vdata)
                    if vdata != araw:
                        problems.append("<%s %s>: the device reads %r but the file was written as %r (shifted string — the build 129–134 fault)" % (tag, name, val, raw))
                elif vtype in (T_INT_DEC, T_INT_HEX): val = vdata
                elif vtype == T_BOOL: val = vdata != 0
                elif vtype == T_REF: val = ("@ref", vdata)
                else: val = ("type%d" % vtype, vdata)
                attrs[name] = (val, vtype, raw, rid); order.append(rid)
            ids = [r for r in order if r]
            if ids != sorted(ids): problems.append("<%s> attributes are not in resource-id order" % tag)
            els.append({"tag": tag, "depth": depth, "attrs": attrs}); depth += 1
        elif typ == 0x0103: depth -= 1
        o += size
    return els, resids, strings, problems

def dex_classes(d):
    if d[:4] != b"dex\n": raise ValueError("classes.dex is not a DEX file")
    sid_size, sid_off, tid_size, tid_off = struct.unpack_from("<IIII", d, 56)
    cdef_size, cdef_off = struct.unpack_from("<II", d, 96)
    def string(i):
        p = u32(d, sid_off + 4 * i)
        while d[p] & 0x80: p += 1                       # skip the ULEB128 length
        p += 1; e = d.index(b"\0", p); return d[p:e].decode("utf-8", "replace")
    out = set()
    for i in range(cdef_size):
        cidx = u32(d, cdef_off + 32 * i); out.add(string(u32(d, tid_off + 4 * cidx)))
    return out

def check(path, expected_code=None):
    P = []; info = {}
    try: z = zipfile.ZipFile(path)
    except Exception as e: return ["not a valid APK (zip): %s" % e], info
    names = set(z.namelist())
    for need in ("AndroidManifest.xml", "classes.dex", "resources.arsc", "assets/mindit.html", "assets/start.html", "res/mipmap-anydpi-v26/icon.xml"):
        if need not in names: P.append("missing %s" % need)
    if not any(n.startswith("res/mipmap-") and n.endswith("/icon.png") for n in names): P.append("missing the launcher icon PNGs")
    if "resources.arsc" in names:
        zi = z.getinfo("resources.arsc")
        if zi.compress_type != zipfile.ZIP_STORED: P.append("resources.arsc is compressed (Android 11+ refuses to install it)")
        with open(path, "rb") as f:
            f.seek(zi.header_offset); h = f.read(30); n, m = struct.unpack_from("<HH", h, 26)
            if (zi.header_offset + 30 + n + m) % 4: P.append("resources.arsc is not 4-byte aligned (run zipalign)")
    if P and "AndroidManifest.xml" not in names: return P, info
    els, resids, strings, mp = parse_manifest(z.read("AndroidManifest.xml")); P += mp
    for nm, rid in ATTR_IDS.items():
        if nm in strings:
            i = strings.index(nm)
            if i < len(resids) and resids[i] != rid: P.append("attribute %s mapped to 0x%08x, expected 0x%08x" % (nm, resids[i], rid))
    def first(tag): return next((e for e in els if e["tag"] == tag), None)
    def val(e, a): return e["attrs"].get(a, (None,))[0] if e else None
    man = first("manifest"); app = first("application"); sdk = first("uses-sdk")
    pkg = val(man, "package"); vname = val(man, "versionName"); vcode = val(man, "versionCode")
    info.update(package=pkg, versionName=vname, versionCode=vcode, label=val(app, "label"))
    if pkg != PACKAGE: P.append("package is %r, expected %r" % (pkg, PACKAGE))
    if vname != VERSION_NAME: P.append("versionName is %r, expected %r" % (vname, VERSION_NAME))
    if expected_code is not None and vcode != int(expected_code): P.append("versionCode is %r, expected %s" % (vcode, expected_code))
    if val(sdk, "minSdkVersion") != MIN_SDK or val(sdk, "targetSdkVersion") != TARGET_SDK:
        P.append("minSdk/targetSdk are %r/%r, expected %d/%d" % (val(sdk, "minSdkVersion"), val(sdk, "targetSdkVersion"), MIN_SDK, TARGET_SDK))
    if val(app, "label") != LABEL: P.append("the app's name on the device would be %r, expected %r" % (val(app, "label"), LABEL))
    icon = val(app, "icon")
    if not (isinstance(icon, tuple) and icon[0] == "@ref" and icon[1] >> 24 == 0x7F): P.append("the app icon is not a resource reference (%r)" % (icon,))
    perms = [val(e, "name") for e in els if e["tag"] == "uses-permission"]
    for p in PERMISSIONS:
        if p not in perms: P.append("permission %s is not requested (the device reads: %s)" % (p, ", ".join(map(str, perms))))
    classes = set()
    try: classes = dex_classes(z.read("classes.dex"))
    except Exception as e: P.append("classes.dex unreadable: %s" % e)
    def cls(name): return "L" + (PACKAGE + name if name and name.startswith(".") else str(name)).replace(".", "/") + ";"
    acts = [e for e in els if e["tag"] == "activity"]; launcher = None
    for i, e in enumerate(els):
        if e["tag"] == "activity":
            sub = []
            for f in els[i + 1:]:
                if f["depth"] <= e["depth"]: break
                sub.append((f["tag"], val(f, "name")))
            if ("action", "android.intent.action.MAIN") in sub and ("category", "android.intent.category.LAUNCHER") in sub: launcher = e
    if not launcher: P.append("no launcher activity (MAIN + LAUNCHER) — the app would have no icon to open")
    else:
        n = val(launcher, "name"); info["activity"] = n
        if n != ".MainActivity": P.append("the launcher activity is %r, expected '.MainActivity'" % n)
        if cls(n) not in classes: P.append("the launcher activity class %s is not in classes.dex — the app would close at once" % cls(n))
        if val(launcher, "exported") is not True: P.append("the launcher activity is not exported")
        if val(launcher, "label") not in (None, LABEL): P.append("the launcher activity's name would be %r" % (val(launcher, "label"),))
    svc = next((e for e in els if e["tag"] == "service"), None)
    if not svc: P.append("the hosting service is missing")
    else:
        if val(svc, "name") != ".HostService" or cls(val(svc, "name")) not in classes: P.append("the hosting service is %r (class missing?)" % (val(svc, "name"),))
        if val(svc, "foregroundServiceType") != 0x10: P.append("the hosting service has no foregroundServiceType connectedDevice (Android 14+ would stop it)")
    for n in z.namelist():
        if n.startswith("assets/") and z.getinfo(n).file_size == 0: P.append("%s is empty" % n)
    return P, info

if __name__ == "__main__":
    probs, info = check(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    print("APK check: %s" % ", ".join("%s=%s" % kv for kv in info.items()))
    for p in probs: print("PROBLEM: " + p)
    print("APK OK — the device will read the name %r and open .MainActivity" % LABEL if not probs else "APK NOT OK (%d problems)" % len(probs))
    sys.exit(1 if probs else 0)
