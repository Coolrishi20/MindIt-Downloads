# Mind It! v1.69 — downloads

**Current build: 131** (17 October 2026). Each new build replaces the files below, so this page always holds the latest version.

## Which file do I need?

| Device | File | Size | Check (first 16 of SHA-256) |
|---|---|---|---|
| Windows laptop | [`Windows/Mind It!.exe`](Windows/) | 69 MB | `b4719d0b6a1d9d91` |
| Galaxy Tab (Android) | [`Android/Mind It! for Android (Galaxy Tab).apk`](Android/) | 1.7 MB | `99e32a902c462ba8` |
| Mac (Apple Silicon only) | [`Mac/Mind It! for Mac (Apple Silicon).zip`](Mac/), then follow `Mac/How to install on a Mac.txt` | 100 MB | `e66db8ceda7374e0` |
| Any computer's web browser (no install) | [`Web/mindit.html`](Web/): the webpage version | 2.7 MB | `75208b7fa73f71c3` |
| Guides (PDF) | [`Guides/`](Guides/): Complete Idiot's Guide, Players' Guide, Quick Start, Quizmaster Cheat Sheet, Rehearsal Checklist | | |
| Reports | [`Reports/`](Reports/): QC report, changelog, rollback guide | | |

**To download a file:** open it on GitHub and click the **Download raw file** button (⤓, top right of the file view). Every file is complete; there are no parts to join.

- **Windows:** this is the portable app. Replace your old `Mind It!.exe` with this one; your data stays.
- **Galaxy Tab:** open the APK on the tablet and tap **Update**. It is signed with the original key (versionCode 131), so it installs over the old app and keeps its data.
- **Mac:** see `Mac/How to install on a Mac.txt`. Not yet tried on a real Mac. Test it at home before a quiz night.
- **Webpage (`mindit.html`):** double-click it on a Windows PC or Mac and it opens in Chrome, Edge or Safari. It is the whole quiz, but **without phones or the tablet** (a webpage can't host them), and it keeps its own players and history in that browser. Use backup files to move data between it and the laptop app. It doesn't work as a downloaded file on an iPhone or iPad. Complete Idiot's Guide 4.1c.
- **iPhone / iPad:** there is no app file to install.
  - **To play the quiz on the iPhone or iPad itself:** open **https://coolrishi20.github.io/MindIt-Web/** in Safari, then **Share → Add to Home Screen**. Once opened with internet it also works with **no internet** (since build 129).
  - **As the remote for a laptop quiz:** on the laptop open **📲 Connect ▾ → Connect Device** and scan the **iPad / iPhone** code with the Camera (Complete Idiot's Guide, Setup B2).
  - **As a team phone:** join from the laptop as usual (Complete Idiot's Guide 8.6).

## New in build 131

- **A new voice for the intro:** your new recording plays in the intro, the 🎵 Mind It! sting and the winner screen, on every device. The music, the loading screen, the explosion and the ending are unchanged. To fit the old timing, the pause in the middle of the clip is shorter and the voice starts at the music's build.

Build 130 added TVs over the Wi-Fi (Audience Screens), Take Over Tablet Quiz, Test Hosting, a battery warning, the remote lock and a connection signal for each remote.

Full history: `Reports/MIND_IT_CHANGELOG.md`. Test results: `Reports/MIND_IT_QC_REPORT.pdf` (build 131: 2,526 of 2,527 checks passed — the one miss was a test step, since fixed and re-run; iPhone and iPad checks used phone- and tablet-sized browsers, not real Safari; the Galaxy Tab's server and the TVs were tested on the build machine; a real Galaxy Tab and real smart TVs were not used).

## Older builds

Builds since 125 stay in this repository's history: **Commits** → pick a build → **Browse files**. The last known-good build before this series (build 119) is described in `Reports/MIND_IT_ROLLBACK_GUIDE.md`.

The source code lives in the separate private repository `MindIt-`. It is never copied here.
