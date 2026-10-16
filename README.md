# Mind It! v1.69 — downloads

**Current build: 128** (16 October 2026). Each new build replaces the files below, so this page always holds the latest version.

## Which file do I need?

| Device | File | Size | Check (first 16 of SHA-256) |
|---|---|---|---|
| Windows laptop | [`Windows/Mind It!.exe`](Windows/) | 69 MB | `1f38f139dac1baee` |
| Galaxy Tab (Android) | [`Android/Mind It! for Android (Galaxy Tab).apk`](Android/) | 1.6 MB | `20ed7e1d8f676891` |
| Mac (Apple Silicon only) | [`Mac/Mind It! for Mac (Apple Silicon).zip`](Mac/), then follow `Mac/How to install on a Mac.txt` | 100 MB | `69f902de39ed72c0` |
| Any computer's web browser (no install) | [`Web/mindit.html`](Web/): the webpage version | 2.6 MB | `510fe51dbb236a2c` |
| Guides (PDF) | [`Guides/`](Guides/): Complete Idiot's Guide, Players' Guide, Quick Start, Quizmaster Cheat Sheet, Rehearsal Checklist | | |
| Reports | [`Reports/`](Reports/): QC report, changelog, rollback guide | | |

**To download a file:** open it on GitHub and click the **Download raw file** button (⤓, top right of the file view). Every file is complete; there are no parts to join.

- **Windows:** this is the portable app. Replace your old `Mind It!.exe` with this one; your data stays.
- **Galaxy Tab:** open the APK on the tablet and tap **Update**. It is signed with the original key (versionCode 128), so it installs over the old app and keeps its data.
- **Mac:** see `Mac/How to install on a Mac.txt`. Not yet tried on a real Mac. Test it at home before a quiz night.
- **Webpage (`mindit.html`):** double-click it on a Windows PC or Mac and it opens in Chrome, Edge or Safari. It is the whole quiz, but **without phones or the tablet** (a webpage can't host them), and it keeps its own players and history in that browser. Use backup files to move data between it and the laptop app. It doesn't work as a downloaded file on an iPhone or iPad. Complete Idiot's Guide 4.1c.
- **iPhone / iPad:** there is no app file to install.
  - **To play the quiz on the iPhone or iPad itself:** open **https://coolrishi20.github.io/MindIt-Web/** in Safari, then **Share → Add to Home Screen**.
  - **As the remote for a laptop quiz:** on the laptop open **📲 Connect ▾ → Connect Device** and scan the **iPad / iPhone** code with the Camera (Complete Idiot's Guide, Setup B2).
  - **As a team phone:** join from the laptop as usual (Complete Idiot's Guide 8.6).

## New in build 128

- **Trusted devices:** a remote (Galaxy Tab, iPad, iPhone or the 📱 Phone Remote) connects once with the PIN and then reconnects by itself, including after a restart.
- **One remote at a time:** a second device waits. On the laptop you choose **Allow & Switch**, **Reject** or **Ignore**; the quiz carries on unchanged when control moves.
- **Connected Devices** (📲 Connect ▾ → Connect Device) shows who is in control, who is waiting and your trusted devices.
- **The Galaxy Tab can be the server:** with no laptop, team phones and a phone remote join the tablet. 🟡 Not yet tried on a real Galaxy Tab, so rehearse at home first.

Full history: `Reports/MIND_IT_CHANGELOG.md`. Test results: `Reports/MIND_IT_QC_REPORT.pdf` (build 128: 2,269 / 2,269 checks passed; iPhone and iPad checks used phone- and tablet-sized browsers, not real Safari; the Galaxy Tab as the server was tested on the build machine, not on a real tablet).

## Older builds

Builds since 125 stay in this repository's history: **Commits** → pick a build → **Browse files**. The last known-good build before this series (build 119) is described in `Reports/MIND_IT_ROLLBACK_GUIDE.md`.

The source code lives in the separate private repository `MindIt-`. It is never copied here.
