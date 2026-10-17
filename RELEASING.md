# Publishing a Mind It! build

From build 132 on, every build is published as a **GitHub Release** of this repository instead of being committed as files.
The README's "Download Mind It! — Latest Version" links (`…/releases/latest/download/<file>`) always lead to the newest
published release, so they never need editing; the workflow also rewrites that section's version, date and sizes.

## How a build is published (automatic since build 133)

**Since build 133 (owner, 17 Oct 2026: "automatic") there's nothing to click:** staging a build starts the workflow below by
itself, and the release appears on its own (usually within a few minutes). The checks are the same — if any fails, nothing is
published and you see a red ✗ in the **Actions** tab. You can still start it by hand (step 2) — for example to re-run it.

1. **The build machine stages the tested build** (Claude does this after the tests pass):

   ```
   python3 tools/stage_release.py 133 release_notes_133.md \
     "Mind It!.exe=Mind-It-Windows.exe" \
     "Mind It! for Android (Galaxy Tab).apk=Mind-It-Android-Galaxy-Tab.apk" \
     "Mind It! for Mac (Apple Silicon).zip=Mind-It-Mac-Apple-Silicon.zip" \
     "mindit.html=mindit.html" \
     "MIND_IT_COMPLETE_IDIOTS_GUIDE.pdf=Mind-It-Complete-Idiots-Guide.pdf" … (the other guides and the QC report)
   ```

   This pushes one commit to the temporary branch **`release-staging`** — nothing else. Files over 90 MB are stored in pieces
   (GitHub refuses files over 100 MB in git). The commit also carries a copy of `.github/workflows/publish-release.yml`:
   GitHub runs a workflow started by a push from the pushed branch, so that copy is what makes the push start the release.
   The checks and the publishing code always come from `main`.

2. **The workflow publishes it** — by itself after step 1. To start it by hand instead (a re-run, or if it didn't start):
   **Actions** tab → **Publish a Mind It! release** → **Run workflow** → type the build number → **Run workflow**.

   The workflow, in order:
   - **checks** the staged files: every SHA-256 fingerprint; the EXE is a Windows program; the APK is `com.mindit.app`, versionName 1.69,
     versionCode = the build number, and signed with the original key (so it updates the installed app); the Mac zip is intact and
     contains `Mind It!.app`; the page is Mind It! 1.69; the tag doesn't exist yet; the build is newer than the latest release.
     **If anything fails, nothing is published.**
   - (started by hand with the box ticked) publishes the earlier builds 125–131 from this repository's history, oldest first, never as "latest";
     each file is checked against the fingerprint recorded when it was built (`releases/history.json`).
   - creates the release **as a draft**, checks every upload, then publishes it as **Latest** — tag `v1.69-build<N>`,
     title **Mind It! v1.69 — Build N**, with the notes, a download link per file and the fingerprints.
   - downloads every file of the new release again and compares fingerprints. If anything is wrong, the release goes back to
     draft and the previous release is the latest again.
   - rewrites the README's download section and deletes `release-staging` (always after an automatic run; by hand, if you left
     that box ticked).

## Rules the workflow keeps

- An existing release or tag is never changed, replaced or deleted. Running it twice for the same build stops with "already exists".
- Drafts and prereleases are never the latest; an older build is never made the latest.
- A platform with no new file in a build keeps the previous release's file, labelled with its own build number.
- Nothing is deleted except the temporary `release-staging` branch, and only after a verified publish.

## Storage

- **The repository (git):** from build 132 on, it only grows by text (README, reports). Its history up to build 131 stays as it is
  (no history rewriting); the build-131 app and PDF files were taken out of the current files in build 134 (owner: "Remove the old
  build-131 app files"), so they're only in the history and in the releases. The staged build lives on `release-staging` until it's published; GitHub cleans up the deleted
  branch's data on its own schedule.
- **Release files:** stored by GitHub with the release, outside the repository's git history; up to 2 GB per file.
- **Actions artifacts:** not used.

## If something goes wrong

- *"already exists"*: that build is already published (or a draft of it is waiting on the Releases page — publish or delete it there).
- *"not newer than the latest release"*: stage the newer build.
- *A check failed*: nothing was published; fix the build, stage it again (delete `release-staging` on GitHub first) and run again.
- *Changing a staged file after it was published*: not possible — a published release is never changed. Stage the next build number.
