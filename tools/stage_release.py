#!/usr/bin/env python3
"""Put a finished, tested Mind It! build on the temporary `release-staging` branch, ready for the owner to publish
(Actions → "Publish a Mind It! release" → Run workflow). Run on the build machine from a clone of MindIt-Downloads:

  python3 tools/stage_release.py <build> <release notes .md> <file>=<asset name> [<file>=<asset name> …]

Asset names (fixed, so the "latest" download links never change):
  Mind-It-Windows.exe · Mind-It-Android-Galaxy-Tab.apk · Mind-It-Mac-Apple-Silicon.zip · mindit.html ·
  Mind-It-Complete-Idiots-Guide.pdf · Mind-It-Quick-Start.pdf · Mind-It-Quizmaster-Cheat-Sheet.pdf ·
  Mind-It-Rehearsal-Checklist.pdf · Mind-It-Players-Guide.pdf · Mind-It-QC-Report.pdf
A platform file left out is carried over from the previous release (and marked as such).

The branch is an orphan (it shares no history with main) and holds only this build. Files over 90 MB are stored in
90 MB pieces (GitHub refuses files over 100 MB in git); the workflow joins them and checks every fingerprint.
After a verified publish the workflow deletes the branch. Only that branch is pushed (never forced) — never main, tags or releases.
"""
import hashlib, os, shutil, subprocess, sys, tempfile

PIECE = 90 * 1000 * 1000


def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    build, notes, pairs = sys.argv[1], sys.argv[2], sys.argv[3:]
    assert build.isdigit(), "build must be a number"
    repo = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True, check=True).stdout.strip()
    url = subprocess.run(["git", "-C", repo, "remote", "get-url", "origin"], capture_output=True, text=True, check=True).stdout.strip()
    work = tempfile.mkdtemp(prefix="mindit-stage-")
    subprocess.run(["git", "init", "-q", "-b", "release-staging", work], check=True)
    d = os.path.join(work, "staging")
    os.makedirs(d)
    sums = []
    for pair in pairs:
        src, name = pair.rsplit("=", 1)
        sums.append("%s  %s" % (sha256(src), name))
        size = os.path.getsize(src)
        if size <= PIECE:
            shutil.copyfile(src, os.path.join(d, name))
        else:
            with open(src, "rb") as f:
                i = 0
                while True:
                    chunk = f.read(PIECE)
                    if not chunk:
                        break
                    with open(os.path.join(d, "%s.%03d" % (name, i)), "wb") as out:
                        out.write(chunk)
                    i += 1
        print("staged %-36s %12d bytes  %s" % (name, size, sums[-1][:16]))
    open(os.path.join(d, "SHA256SUMS.txt"), "w").write("\n".join(sums) + "\n")
    open(os.path.join(d, "BUILD"), "w").write(build + "\n")
    shutil.copyfile(notes, os.path.join(d, "RELEASE_NOTES.md"))
    g = ["git", "-C", work]
    subprocess.run(g + ["add", "-f", "staging"], check=True)
    msg = "Build %s staged for release (temporary branch — removed by the release workflow after publishing)" % build
    subprocess.run(g + ["-c", "user.name=Claude", "-c", "user.email=noreply@anthropic.com", "commit", "-q", "-m",
                        msg + "\n\nCo-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01CyZjp4agWKeQDDj6PzGMVH"], check=True)
    r = subprocess.run(g + ["push", url, "release-staging:release-staging"])   # a normal push of the staging branch only — never forced
    if r.returncode != 0:
        sys.exit("Not staged: a build is probably already waiting on release-staging. Publish it (or delete that branch on GitHub) first.")
    print("Build %s is waiting on release-staging. Publish it: Actions → Publish a Mind It! release → Run workflow → %s" % (build, build))
    shutil.rmtree(work, ignore_errors=True)


if __name__ == "__main__":
    main()
