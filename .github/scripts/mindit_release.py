#!/usr/bin/env python3
"""Mind It! — publish a build as a GitHub Release (runs inside GitHub Actions; see RELEASING.md).

Subcommands (run in this order by .github/workflows/publish-release.yml):
  validate <staging dir> <build>   check the staged files before anything is published
  history                          publish the earlier verified builds listed in releases/history.json (once; skips existing tags)
  publish  <staging dir> <build>   create the release as a draft, check it, then publish it as the latest release
  verify   <build>                 download every file of the new release and compare fingerprints; if anything is wrong,
                                   the release goes back to draft and the previous release is the latest again
  readme   <build>                 rewrite the download section of README.md for the new latest release
  notices                          put the warnings listed in releases/notices.json at the top of those earlier releases'
                                   notes (build 136; owner: "Do … 5"). Only the notes change — never a file, tag or date.

Rules: never overwrite or delete an existing release or tag; never mark a draft, prerelease or older build as the latest;
a failure before publishing leaves the previous release as the latest.
"""
import glob, hashlib, json, os, re, shutil, subprocess, sys, tempfile, urllib.request, urllib.error
from datetime import datetime, timezone

REPO = os.environ.get("GITHUB_REPOSITORY", "Coolrishi20/MindIt-Downloads")
VERSION = "1.69"
PACKAGE = "com.mindit.app"
APK_CERT_SHA256 = "5f4819e4b15ef1221ad1981219d3d49dbb1ca888df7d05bd45b02e80d3c2637b"   # the original signing certificate (public)
WEB_URL = "https://coolrishi20.github.io/MindIt-Web/"
# (asset name, label shown on the Releases page, kind, required in every release)
PLATFORM = [
    ("Mind-It-Windows.exe", "Mind It! for Windows (portable app, .exe)", "exe"),
    ("Mind-It-Android-Galaxy-Tab.apk", "Mind It! for Android — Galaxy Tab (.apk)", "apk"),
    ("Mind-It-Mac-Apple-Silicon.zip", "Mind It! for Mac — Apple Silicon (.zip)", "mac"),
    ("mindit.html", "Mind It! web version (single page, .html)", "html"),
]
EXTRA = [
    ("Mind-It-Complete-Idiots-Guide.pdf", "The Complete Idiot's Guide (PDF)"),
    ("Mind-It-Quick-Start.pdf", "Quick Start (PDF)"),
    ("Mind-It-Quizmaster-Cheat-Sheet.pdf", "Quizmaster Cheat Sheet (PDF)"),
    ("Mind-It-Rehearsal-Checklist.pdf", "Rehearsal Checklist (PDF)"),
    ("Mind-It-Players-Guide.pdf", "Players' Guide (PDF)"),
    ("Mind-It-QC-Report.pdf", "QC report (PDF)"),
]
# build 152 (owner, 24 Oct 2026: "make it a new apk"): apps a release may carry; when a build doesn't restage one, the previous
# release's file is kept (and marked), the same as the platform files — a release from before it simply doesn't have it
OPTIONAL = [
    ("Mind-It-Android-TV.apk", "Mind It! TV — Mi Box / Android TV audience screen (.apk)", "tvapk"),
]
TV_PACKAGE = "com.mindit.tv"
LABEL = {n: l for n, l, *_ in PLATFORM + EXTRA + OPTIONAL}
SUMS = "SHA256SUMS.txt"


def fail(msg):
    print("::error::" + msg)
    sys.exit(1)


def run(*args, check=True):
    r = subprocess.run(list(args), capture_output=True, text=True)
    if check and r.returncode != 0:
        fail("%s failed: %s" % (" ".join(args[:3]), (r.stderr or r.stdout).strip()[-800:]))
    return r.stdout


def api(path, *extra):
    return json.loads(run("gh", "api", path, *extra) or "null")


def tag_for(build):
    return "v%s-build%s" % (VERSION, build)


def build_of(tag):
    m = re.match(r"^v[\d.]+-build(\d+)$", tag or "")
    return int(m.group(1)) if m else None


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def all_releases():
    """Every release, drafts included (one JSON object per line)."""
    out = run("gh", "api", "--paginate", "repos/%s/releases?per_page=100" % REPO, "--jq", ".[] | tojson")
    return [json.loads(l) for l in out.splitlines() if l.strip()]


def remote_tag_exists(tag):
    return bool(run("git", "ls-remote", "--tags", "origin", "refs/tags/" + tag).strip())


def latest_release():
    r = subprocess.run(["gh", "api", "repos/%s/releases/latest" % REPO], capture_output=True, text=True)
    return json.loads(r.stdout) if r.returncode == 0 else None


def mb(n):
    return "%.1f MB" % (n / 1e6) if n >= 1e6 else "%d KB" % max(1, round(n / 1e3))


# ---------------------------------------------------------------- validate
def join_parts(d):
    """Files bigger than GitHub's 100 MB limit for git are staged as name.000, name.001, …"""
    for first in sorted(glob.glob(os.path.join(d, "*.000"))):
        base = first[:-4]
        parts = sorted(glob.glob(glob.escape(base) + ".[0-9][0-9][0-9]"))
        with open(base, "wb") as out:
            for p in parts:
                with open(p, "rb") as f:
                    shutil.copyfileobj(f, out)
        for p in parts:
            os.remove(p)
        print("joined %d parts → %s" % (len(parts), os.path.basename(base)))


def tool(name):
    home = os.environ.get("ANDROID_HOME") or os.environ.get("ANDROID_SDK_ROOT") or "/usr/local/lib/android/sdk"
    found = sorted(glob.glob(os.path.join(home, "build-tools", "*", name)), key=lambda p: [int(x) if x.isdigit() else 0 for x in re.split(r"[.-]", p.split("/")[-2])])
    if not found:
        fail("%s (Android build-tools) not found on the runner" % name)
    return found[-1]


def check_file(path, kind, build):
    name = os.path.basename(path)
    size = os.path.getsize(path)
    if kind == "exe":
        with open(path, "rb") as f:
            if f.read(2) != b"MZ":
                fail(name + " is not a Windows program")
        if size < 30e6:
            fail(name + " is too small to be the Mind It! app (%s)" % mb(size))
    elif kind == "apk":
        badging = run(tool("aapt"), "dump", "badging", path)
        m = re.search(r"package: name='([^']+)' versionCode='(\d+)' versionName='([^']+)'", badging)
        if not m:
            fail("cannot read the APK's package details")
        pkg, code, vname = m.groups()
        if pkg != PACKAGE or vname != VERSION or int(code) != int(build):
            fail("APK is %s versionCode %s versionName %s — expected %s %s %s" % (pkg, code, vname, PACKAGE, build, VERSION))
        certs = run(tool("apksigner"), "verify", "--print-certs", path)
        if APK_CERT_SHA256 not in certs.replace(":", "").lower():
            fail("the APK is not signed with the original Mind It! key — it would not install over the old app")
        # build 135: read the manifest the way the device does (aapt prints the raw strings, which hid the build 129–134
        # fault: on a tablet those APKs were named "application" and closed at once)
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import apk_check
        problems, info = apk_check.check(path, build)
        if problems:
            fail("the APK would not work on a device:\n  - " + "\n  - ".join(problems[:12]))
        print("APK: %s versionCode %s, versionName %s, original key; on a device: named %r, opens %s" % (pkg, code, vname, info.get("label"), info.get("activity")))
    elif kind == "tvapk":
        # Mind It! TV (build 152): its own package, versionCode = the build it was made for (its updater compares that with the
        # release's build), the original key (so Android installs it over the TV's copy), and the Android TV home-screen entry
        badging = run(tool("aapt"), "dump", "badging", path)
        m = re.search(r"package: name='([^']+)' versionCode='(\d+)' versionName='([^']+)'", badging)
        if not m:
            fail("cannot read the TV app's package details")
        pkg, code, vname = m.groups()
        if pkg != TV_PACKAGE or vname != VERSION or int(code) != int(build):
            fail("the TV app is %s versionCode %s versionName %s — expected %s %s %s" % (pkg, code, vname, TV_PACKAGE, build, VERSION))
        if "leanback-launchable-activity:" not in badging:
            fail("the TV app has no Android TV home-screen entry (LEANBACK_LAUNCHER)")
        certs = run(tool("apksigner"), "verify", "--print-certs", path)
        if APK_CERT_SHA256 not in certs.replace(":", "").lower():
            fail("the TV app is not signed with the original Mind It! key — it would not install over the TV's copy")
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import tv_apk_check
        problems, info = tv_apk_check.check(path, build)
        if problems:
            fail("the TV app would not work on a TV:\n  - " + "\n  - ".join(problems[:12]))
        print("TV app: %s versionCode %s, versionName %s, original key; on a TV: named %r, opens %s" % (pkg, code, vname, info.get("label"), info.get("activity")))
    elif kind == "mac":
        r = subprocess.run(["unzip", "-tq", path], capture_output=True, text=True)
        if r.returncode != 0:
            fail(name + " is damaged: " + r.stdout[-300:])
        listing = run("unzip", "-Z1", path)
        if "Mind It!.app/Contents/MacOS/" not in listing:
            fail(name + " does not contain Mind It!.app")
    elif kind == "html":
        with open(path, "rb") as f:
            head = f.read()
        if b"<html" not in head[:4000].lower() or VERSION.encode() not in head:
            fail(name + " is not the Mind It! page")
    print("ok  %-36s %10s" % (name, mb(size)))


def cmd_validate(d, build):
    build = int(build)
    join_parts(d)
    bfile = os.path.join(d, "BUILD")
    if not os.path.exists(bfile) or open(bfile).read().strip() != str(build):
        fail("the staged files are not build %s (BUILD file says %r)" % (build, open(bfile).read().strip() if os.path.exists(bfile) else None))
    sums = os.path.join(d, SUMS)
    if not os.path.exists(sums):
        fail(SUMS + " is missing from the staged files")
    listed = {}
    for line in open(sums):
        if line.strip():
            h, n = line.split(None, 1)
            listed[n.strip().lstrip("*")] = h.lower()
    for n, h in listed.items():
        p = os.path.join(d, n)
        if not os.path.exists(p):
            fail("%s is listed in %s but not staged" % (n, SUMS))
        if sha256(p) != h:
            fail("%s does not match its fingerprint — damaged on the way; stage it again" % n)
    known = set(LABEL)
    for p in glob.glob(os.path.join(d, "*")):
        n = os.path.basename(p)
        if n in (SUMS, "BUILD", "RELEASE_NOTES.md"):
            continue
        if n not in known:
            fail("unexpected file in the staged build: " + n)
        if n not in listed:
            fail(n + " has no fingerprint in " + SUMS)
    for n, _, kind in PLATFORM:
        p = os.path.join(d, n)
        if os.path.exists(p):
            check_file(p, kind, build)
        else:
            print("--  %-36s not in this build (the previous release's file will be kept, and marked)" % n)
    for n, _, kind in OPTIONAL:
        p = os.path.join(d, n)
        if os.path.exists(p):
            check_file(p, kind, build)
        else:
            print("--  %-36s not in this build (kept from the previous release if it has one)" % n)
    if not os.path.exists(os.path.join(d, "RELEASE_NOTES.md")):
        fail("RELEASE_NOTES.md is missing")
    tag = tag_for(build)
    if any(r.get("tag_name") == tag for r in all_releases()) or remote_tag_exists(tag):
        fail("%s already exists (published or draft). Nothing was changed. Existing releases are never overwritten." % tag)
    latest = latest_release()
    if latest and (build_of(latest["tag_name"]) or 0) >= build:
        fail("build %s is not newer than the latest release (%s)" % (build, latest["tag_name"]))
    print("Build %s is ready to publish as %s." % (build, tag))


# ---------------------------------------------------------------- history
def changelog_section(build):
    p = "Reports/MIND_IT_CHANGELOG.md"
    if not os.path.exists(p):
        return ""
    text = open(p).read()
    m = re.search(r"^### Build %s\b.*?$(.*?)(?=^### |^## )" % build, text, re.S | re.M)
    if not m:
        return ""
    head = re.search(r"^### (Build %s\b.*)$" % build, text, re.M).group(1)
    return "### " + head + "\n" + m.group(1).strip() + "\n"


def cmd_history():
    hist = json.load(open("releases/history.json"))
    existing = {r.get("tag_name") for r in all_releases()}
    for e in sorted(hist["builds"], key=lambda x: x["build"]):
        tag = tag_for(e["build"])
        if tag in existing or remote_tag_exists(tag):
            print("skip %s (already published)" % tag)
            continue
        tmp = tempfile.mkdtemp()
        files, sums = [], []
        for name, f in sorted(e["files"].items()):
            out = os.path.join(tmp, name)
            with open(out, "wb") as fh:
                fh.write(subprocess.run(["git", "show", "%s:%s" % (e["commit"], f["path"])], capture_output=True, check=True).stdout)
            h = sha256(out)
            if h != f["sha256"] or os.path.getsize(out) != f["size"]:
                fail("build %s: %s from the history does not match its recorded fingerprint — not published" % (e["build"], name))
            files.append(out + "#" + LABEL.get(name, name))
            sums.append("%s  %s" % (h, name))
        with open(os.path.join(tmp, SUMS), "w") as fh:
            fh.write("\n".join(sums) + "\n")
        files.append(os.path.join(tmp, SUMS) + "#SHA-256 fingerprints")
        notes = ("**Earlier build, restored from this repository's history.** These are exactly the files published for build %s "
                 "on %s; their SHA-256 fingerprints match the build report. The newest build is always at "
                 "[Latest](https://github.com/%s/releases/latest).\n\n%s\n**SHA-256**\n```\n%s\n```\n"
                 % (e["build"], e["date"], REPO, changelog_section(e["build"]) or "", "\n".join(sums)))
        nf = os.path.join(tmp, "notes.md")
        open(nf, "w").write(notes)
        run("gh", "release", "create", tag, *files, "--repo", REPO, "--target", e["commit"],
            "--title", "Mind It! v%s — Build %s" % (VERSION, e["build"]), "--notes-file", nf, "--latest=false")
        print("published %s (earlier build, not marked latest)" % tag)
        shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------- publish
def carried_build(prev, n):
    """the build a carried-over file really comes from: the previous release's label says "(build N, unchanged)" when it
    was itself carried over"""
    a = next((a for a in prev["assets"] if a["name"] == n), {})
    m = re.search(r"\(build (\d+), unchanged\)", a.get("label") or "")
    return int(m.group(1)) if m else build_of(prev["tag_name"])


def cmd_publish(d, build):
    build = int(build)
    tag = tag_for(build)
    prev = latest_release()
    carried = {}
    for n, _, _ in PLATFORM:
        if not os.path.exists(os.path.join(d, n)):
            if not prev or not any(a["name"] == n for a in prev["assets"]):
                fail("%s is missing and no earlier release has it" % n)
            run("gh", "release", "download", prev["tag_name"], "--repo", REPO, "--pattern", n, "--dir", d)
            carried[n] = build_of(prev["tag_name"])
            print("kept %s from %s" % (n, prev["tag_name"]))
    for n, _, _ in OPTIONAL:
        if not os.path.exists(os.path.join(d, n)) and prev and any(a["name"] == n for a in prev["assets"]):
            run("gh", "release", "download", prev["tag_name"], "--repo", REPO, "--pattern", n, "--dir", d)
            carried[n] = carried_build(prev, n)
            print("kept %s from %s" % (n, prev["tag_name"]))
    names = [n for n, *_ in PLATFORM + EXTRA + OPTIONAL if os.path.exists(os.path.join(d, n))]
    sums = ["%s  %s" % (sha256(os.path.join(d, n)), n) for n in names]
    open(os.path.join(d, SUMS), "w").write("\n".join(sums) + "\n")
    notes = open(os.path.join(d, "RELEASE_NOTES.md")).read().replace("{TAG}", tag).replace("{REPO}", REPO)
    links = []
    for n in names:
        lab = LABEL[n] + (" — build %s file, unchanged in this release" % carried[n] if n in carried else "")
        links.append("- [%s](https://github.com/%s/releases/download/%s/%s) · %s" % (lab, REPO, tag, n, mb(os.path.getsize(os.path.join(d, n)))))
    notes += "\n\n## Downloads (this release)\n" + "\n".join(links)
    notes += "\n\n**SHA-256 fingerprints**\n```\n" + "\n".join(sums) + "\n```\n"
    nf = os.path.join(tempfile.mkdtemp(), "notes.md")
    open(nf, "w").write(notes)
    files = [os.path.join(d, n) + "#" + LABEL[n] + (" (build %s, unchanged)" % carried[n] if n in carried else "") for n in names]
    files.append(os.path.join(d, SUMS) + "#SHA-256 fingerprints")
    title = "Mind It! v%s — Build %s" % (VERSION, build)
    run("gh", "release", "create", tag, *files, "--repo", REPO, "--target", os.environ.get("GITHUB_SHA", "main"),
        "--title", title, "--notes-file", nf, "--draft")
    draft = next((r for r in all_releases() if r.get("draft") and r.get("tag_name") == tag), None)
    if not draft:
        fail("the draft release was not created; nothing was published")
    have = {a["name"]: a["size"] for a in draft["assets"]}
    for n in names + [SUMS]:
        if have.get(n) != os.path.getsize(os.path.join(d, n)):
            fail("draft upload of %s is incomplete — the draft '%s' was kept (not public); delete it on the Releases page, then run again" % (n, title))
    api("repos/%s/releases/%s" % (REPO, draft["id"]), "-X", "PATCH", "-F", "draft=false", "-F", "prerelease=false", "-f", "make_latest=true")
    print("published %s as the latest release" % tag)
    if prev:
        open(os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "previous_latest_id"), "w").write(str(prev["id"]))


# ---------------------------------------------------------------- verify
def cmd_verify(build):
    build = int(build)
    tag = tag_for(build)
    rel = api("repos/%s/releases/tags/%s" % (REPO, tag))
    problems = []
    latest = latest_release()
    if not latest or latest["tag_name"] != tag:
        problems.append("Latest points to %s, not %s" % (latest and latest["tag_name"], tag))
    tmp = tempfile.mkdtemp()
    run("gh", "release", "download", tag, "--repo", REPO, "--dir", tmp)
    expected = {}
    for line in open(os.path.join(tmp, SUMS)):
        if line.strip():
            h, n = line.split(None, 1)
            expected[n.strip()] = h
    for n, h in expected.items():
        p = os.path.join(tmp, n)
        if not os.path.exists(p) or sha256(p) != h:
            problems.append("%s: downloaded file does not match its fingerprint" % n)
        else:
            print("ok  %s downloads and matches %s…" % (n, h[:16]))
    for n, _, _ in PLATFORM:
        if n not in expected:
            problems.append(n + " is missing from the release")
    if problems:
        rid = rel["id"]
        api("repos/%s/releases/%s" % (REPO, rid), "-X", "PATCH", "-F", "draft=true")
        pf = os.path.join(os.environ.get("RUNNER_TEMP", "/tmp"), "previous_latest_id")
        if os.path.exists(pf):
            api("repos/%s/releases/%s" % (REPO, open(pf).read().strip()), "-X", "PATCH", "-f", "make_latest=true")
        fail("verification failed, so %s was turned back into a draft and the previous release is the latest again: %s" % (tag, "; ".join(problems)))
    # Can people without a GitHub account download? (only if the repository is public)
    url = "https://github.com/%s/releases/latest/download/%s" % (REPO, PLATFORM[0][0])
    try:
        req = urllib.request.Request(url, method="HEAD")
        code = urllib.request.urlopen(req, timeout=30).status
    except urllib.error.HTTPError as e:
        code = e.code
    except Exception as e:
        code = str(e)
    if code == 200:
        print("Anyone can download (no GitHub account needed): %s" % url)
    else:
        print("::warning::The download links need a signed-in GitHub account with access (answer %s): the repository is private. "
              "Make it public in Settings → General → Danger Zone if anyone should be able to download." % code)


# ---------------------------------------------------------------- README
def cmd_readme(build):
    build = int(build)
    tag = tag_for(build)
    rel = api("repos/%s/releases/tags/%s" % (REPO, tag))
    size = {a["name"]: a["size"] for a in rel["assets"]}
    labels = {a["name"]: a.get("label") or "" for a in rel["assets"]}
    when = datetime.strptime(rel["published_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    L = "https://github.com/%s/releases/latest/download/" % REPO

    def note(n):
        m = re.search(r"\(build (\d+), unchanged\)", labels.get(n, ""))
        return " — *build %s file, unchanged in build %s*" % (m.group(1), build) if m else ""

    def item(icon, who, text, n, kind):
        if n not in size:
            return "- %s **%s** — not in this release" % (icon, who)
        return "- %s **%s** — [%s](%s%s) (%s, %s)%s" % (icon, who, text, L, n, kind, mb(size[n]), note(n))

    guides = [(n, l.replace(" (PDF)", "")) for n, l in EXTRA if n in size and "QC" not in n]
    block = "\n".join(x for x in [
        "<!-- LATEST-START (this section is rewritten automatically each time a release is published) -->",
        "## ⬇️ Download Mind It! — Latest Version",
        "",
        "**Mind It! v%s · Build %s** · released %s" % (VERSION, build, when.strftime("%-d %B %Y")),
        "",
        item("🪟", "Windows laptop", "Download for Windows", "Mind-It-Windows.exe", ".exe"),
        item("📲", "Galaxy Tab (Android)", "Download for Android", "Mind-It-Android-Galaxy-Tab.apk", ".apk"),
        item("🍎", "Mac (Apple Silicon)", "Download for Mac", "Mind-It-Mac-Apple-Silicon.zip", ".zip"),
        item("📺", "Mi Box / Android TV (audience screen)", "Download Mind It! TV", "Mind-It-Android-TV.apk", ".apk") if "Mind-It-Android-TV.apk" in size else None,
        "- 🌐 **Web, iPhone or iPad** — [Open the web version](%s) (nothing to install)%s" % (WEB_URL, (" · [download the page](%smindit.html)" % L) if "mindit.html" in size else ""),
        ("- 📘 **Guides** — " + " · ".join("[%s](%s%s)" % (l, L, n) for n, l in guides)) if guides else "",
        "",
        "**[View All Previous Versions →](https://github.com/%s/releases)**" % REPO,
        "<!-- LATEST-END -->",
    ] if x is not None)
    block = re.sub(r"\n{3,}", "\n\n", block)
    text = open("README.md").read()
    new = re.sub(r"<!-- LATEST-START.*?<!-- LATEST-END -->", lambda m: block, text, flags=re.S)
    if new == text:
        print("README already up to date")
        return
    open("README.md", "w").write(new)
    print("README download section → build %s" % build)


# ---------------------------------------------------------------- notices
def cmd_notices():
    """releases/notices.json: {"notices": [{"builds": [129, …], "text": "…"}]}. Each listed release whose notes don't
    start with that text gets it added at the top. Files, tags, dates and the latest release are never touched; a
    release that already carries the text is skipped, so this can run on every publish."""
    p = "releases/notices.json"
    if not os.path.exists(p):
        print("no notices"); return
    spec = json.load(open(p, encoding="utf-8"))
    by_tag = {r.get("tag_name"): r for r in all_releases()}
    done = 0
    for n in spec.get("notices", []):
        text = n["text"].strip()
        for b in n["builds"]:
            r = by_tag.get(tag_for(b))
            if not r:
                print("--  %s: no such release" % tag_for(b)); continue
            body = r.get("body") or ""
            if body.startswith(text):
                print("ok  %s already carries the notice" % r["tag_name"]); continue
            new = text + "\n\n" + body
            api("repos/%s/releases/%d" % (REPO, r["id"]), "-X", "PATCH", "-f", "body=" + new)
            chk = api("repos/%s/releases/%d" % (REPO, r["id"]))
            if not (chk.get("body") or "").startswith(text) or len(chk.get("assets") or []) != len(r.get("assets") or []):
                fail("%s: the notice didn't stick" % r["tag_name"])
            print("ok  %s: notice added (files unchanged: %d)" % (r["tag_name"], len(chk.get("assets") or []))); done += 1
    print("notices added: %d" % done)


if __name__ == "__main__":
    c = sys.argv[1] if len(sys.argv) > 1 else ""
    {"validate": lambda: cmd_validate(sys.argv[2], sys.argv[3]),
     "history": cmd_history,
     "publish": lambda: cmd_publish(sys.argv[2], sys.argv[3]),
     "verify": lambda: cmd_verify(sys.argv[2]),
     "readme": lambda: cmd_readme(sys.argv[2]),
     "notices": cmd_notices}.get(c, lambda: fail("usage: see the top of this file"))()
