#!/usr/bin/env python3
"""Mind It! TV · check the built TV APK the way an Android TV reads it (build 152). Reuses the Galaxy Tab app's reader
(android/apk_check.py: typed manifest values, attribute order, DEX classes) with the TV app's own expectations:
  · package com.mindit.tv, versionName 1.69, versionCode as expected, minSdk 21 (Mi Box 3 and newer), targetSdk 35;
  · the name "Mind It! TV", an icon and a banner (the Android TV home row shows the banner) as resource references;
  · .MainActivity exported with MAIN + LEANBACK_LAUNCHER (the TV home) + LAUNCHER, present in classes.dex;
  · android.software.leanback and android.hardware.touchscreen declared but not required (works with the remote only);
  · plain-http traffic allowed (the laptop and the tablet serve http on the Wi-Fi); the four network permissions and the
    install permission for ⬆ App Update, no camera;
  · resources.arsc stored and 4-byte aligned; the banner and icon files present.
Usage: python3 tv_apk_check.py <file.apk> [<expected versionCode>]     exit 0 = OK, 1 = problems (listed)"""
import importlib.util, os, struct, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
# the Galaxy Tab app's reader: next to this file in MindIt-Downloads' .github/scripts, or android/ in the source repository
_ac = next((p for p in (os.path.join(HERE, "apk_check.py"), os.path.join(HERE, "..", "android", "apk_check.py")) if os.path.exists(p)), None)
_spec = importlib.util.spec_from_file_location("apk_check", _ac)
AC = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(AC)

PACKAGE, VERSION_NAME, LABEL, MIN_SDK, TARGET_SDK = "com.mindit.tv", "1.69", "Mind It! TV", 21, 35
PERMISSIONS = ["android.permission.INTERNET", "android.permission.ACCESS_NETWORK_STATE", "android.permission.ACCESS_WIFI_STATE",
               "android.permission.CHANGE_WIFI_MULTICAST_STATE", "android.permission.REQUEST_INSTALL_PACKAGES"]   # the last: ⬆ App Update (build 152)
ATTR_IDS = dict(AC.ATTR_IDS, banner=0x010103F2, required=0x0101028E, usesCleartextTraffic=0x010104EC)

def check(path, expected_code=None):
    P = []; info = {}
    try: z = zipfile.ZipFile(path)
    except Exception as e: return ["not a valid APK (zip): %s" % e], info
    names = set(z.namelist())
    for need in ("AndroidManifest.xml", "classes.dex", "resources.arsc", "res/mipmap-anydpi-v26/icon.xml"):
        if need not in names: P.append("missing %s" % need)
    if not any(n.startswith("res/drawable-xhdpi") and n.endswith("/banner.png") for n in names): P.append("missing the TV banner (res/drawable-xhdpi/banner.png)")
    if not any(n.startswith("res/mipmap-") and n.endswith("/icon.png") for n in names): P.append("missing the launcher icon PNGs")
    if any(n.startswith("assets/") for n in names): P.append("the TV app should carry no web page (it shows the host's /tv page)")
    if "resources.arsc" in names:
        zi = z.getinfo("resources.arsc")
        if zi.compress_type != zipfile.ZIP_STORED: P.append("resources.arsc is compressed (Android 11+ refuses to install it)")
        with open(path, "rb") as f:
            f.seek(zi.header_offset); h = f.read(30); n, m = struct.unpack_from("<HH", h, 26)
            if (zi.header_offset + 30 + n + m) % 4: P.append("resources.arsc is not 4-byte aligned (run zipalign)")
    if "AndroidManifest.xml" not in names: return P, info
    els, resids, strings, mp = AC.parse_manifest(z.read("AndroidManifest.xml")); P += mp
    for nm, rid in ATTR_IDS.items():
        if nm in strings:
            i = strings.index(nm)
            if i < len(resids) and resids[i] != rid: P.append("attribute %s mapped to 0x%08x, expected 0x%08x" % (nm, resids[i], rid))
    def first(tag): return next((e for e in els if e["tag"] == tag), None)
    def val(e, a): return e["attrs"].get(a, (None,))[0] if e else None
    man, app, sdk = first("manifest"), first("application"), first("uses-sdk")
    info.update(package=val(man, "package"), versionName=val(man, "versionName"), versionCode=val(man, "versionCode"), label=val(app, "label"))
    if info["package"] != PACKAGE: P.append("package is %r, expected %r" % (info["package"], PACKAGE))
    if info["versionName"] != VERSION_NAME: P.append("versionName is %r, expected %r" % (info["versionName"], VERSION_NAME))
    if expected_code is not None and info["versionCode"] != int(expected_code): P.append("versionCode is %r, expected %s" % (info["versionCode"], expected_code))
    if val(sdk, "minSdkVersion") != MIN_SDK or val(sdk, "targetSdkVersion") != TARGET_SDK:
        P.append("minSdk/targetSdk are %r/%r, expected %d/%d" % (val(sdk, "minSdkVersion"), val(sdk, "targetSdkVersion"), MIN_SDK, TARGET_SDK))
    if info["label"] != LABEL: P.append("the app's name on the TV would be %r, expected %r" % (info["label"], LABEL))
    for a in ("icon", "banner"):
        v = val(app, a)
        if not (isinstance(v, tuple) and v[0] == "@ref" and v[1] >> 24 == 0x7F): P.append("the app's %s is not a resource reference (%r)" % (a, v))
    if val(app, "usesCleartextTraffic") is not True: P.append("plain http is not allowed (usesCleartextTraffic) — the TV page would not load")
    perms = [val(e, "name") for e in els if e["tag"] == "uses-permission"]
    for p in PERMISSIONS:
        if p not in perms: P.append("permission %s is not requested (the device reads: %s)" % (p, ", ".join(map(str, perms))))
    if "android.permission.CAMERA" in perms: P.append("the TV app asks for the camera (it shouldn't)")
    feats = {val(e, "name"): val(e, "required") for e in els if e["tag"] == "uses-feature"}
    for f in ("android.software.leanback", "android.hardware.touchscreen"):
        if feats.get(f) is not False: P.append("%s must be declared with required=false (got %r)" % (f, feats.get(f, "missing")))
    classes = set()
    try: classes = AC.dex_classes(z.read("classes.dex"))
    except Exception as e: P.append("classes.dex unreadable: %s" % e)
    launcher = None
    for i, e in enumerate(els):
        if e["tag"] != "activity": continue
        sub = []
        for f in els[i + 1:]:
            if f["depth"] <= e["depth"]: break
            sub.append((f["tag"], val(f, "name")))
        if ("action", "android.intent.action.MAIN") in sub and ("category", "android.intent.category.LEANBACK_LAUNCHER") in sub:
            launcher = e; info["also_phone_launcher"] = ("category", "android.intent.category.LAUNCHER") in sub
    if not launcher: P.append("no TV launcher activity (MAIN + LEANBACK_LAUNCHER) — the app would not appear on the TV's home screen")
    else:
        n = val(launcher, "name"); info["activity"] = n
        c = "L" + (PACKAGE + n if n and n.startswith(".") else str(n)).replace(".", "/") + ";"
        if n != ".MainActivity": P.append("the launcher activity is %r, expected '.MainActivity'" % n)
        if c not in classes: P.append("the launcher activity class %s is not in classes.dex — the app would close at once" % c)
        if val(launcher, "exported") is not True: P.append("the launcher activity is not exported")
    if "Lcom/mindit/tv/TvAddr;" not in classes: P.append("TvAddr is not in classes.dex")
    if "Lcom/mindit/tv/TvUpd;" not in classes: P.append("TvUpd (the app's own updates) is not in classes.dex")
    return P, info

if __name__ == "__main__":
    probs, info = check(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
    print("TV APK check: %s" % ", ".join("%s=%s" % kv for kv in info.items()))
    for p in probs: print("PROBLEM: " + p)
    print("TV APK OK — the TV will read the name %r, show the banner on its home screen and open .MainActivity" % LABEL if not probs else "TV APK NOT OK (%d problems)" % len(probs))
    sys.exit(1 if probs else 0)
