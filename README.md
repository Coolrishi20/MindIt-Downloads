# Mind It! v1.69 — downloads

**Current build: 129** (16 October 2026). Each new build replaces the files below, so this page always holds the latest version.

## Which file do I need?

| Device | File | Size | Check (first 16 of SHA-256) |
|---|---|---|---|
| Windows laptop | [`Windows/Mind It!.exe`](Windows/) | 69 MB | `5d23dc2b3492b6fc` |
| Galaxy Tab (Android) | [`Android/Mind It! for Android (Galaxy Tab).apk`](Android/) | 1.6 MB | `6b26e0b354c48199` |
| Mac (Apple Silicon only) | [`Mac/Mind It! for Mac (Apple Silicon).zip`](Mac/), then follow `Mac/How to install on a Mac.txt` | 100 MB | `1e78e68dd9c6f290` |
| Any computer's web browser (no install) | [`Web/mindit.html`](Web/): the webpage version | 2.6 MB | `947701b38193bb1f` |
| Guides (PDF) | [`Guides/`](Guides/): Complete Idiot's Guide, Players' Guide, Quick Start, Quizmaster Cheat Sheet, Rehearsal Checklist | | |
| Reports | [`Reports/`](Reports/): QC report, changelog, rollback guide | | |

**To download a file:** open it on GitHub and click the **Download raw file** button (⤓, top right of the file view). Every file is complete; there are no parts to join.

- **Windows:** this is the portable app. Replace your old `Mind It!.exe` with this one; your data stays.
- **Galaxy Tab:** open the APK on the tablet and tap **Update**. It is signed with the original key (versionCode 129), so it installs over the old app and keeps its data.
- **Mac:** see `Mac/How to install on a Mac.txt`. Not yet tried on a real Mac. Test it at home before a quiz night.
- **Webpage (`mindit.html`):** double-click it on a Windows PC or Mac and it opens in Chrome, Edge or Safari. It is the whole quiz, but **without phones or the tablet** (a webpage can't host them), and it keeps its own players and history in that browser. Use backup files to move data between it and the laptop app. It doesn't work as a downloaded file on an iPhone or iPad. Complete Idiot's Guide 4.1c.
- **iPhone / iPad:** there is no app file to install.
  - **To play the quiz on the iPhone or iPad itself:** open **https://coolrishi20.github.io/MindIt-Web/** in Safari, then **Share → Add to Home Screen**. Once opened with internet it also works with **no internet** (since build 129).
  - **As the remote for a laptop quiz:** on the laptop open **📲 Connect ▾ → Connect Device** and scan the **iPad / iPhone** code with the Camera (Complete Idiot's Guide, Setup B2).
  - **As a team phone:** join from the laptop as usual (Complete Idiot's Guide 8.6).

## New in build 129

- **Rename devices** in Connected Devices (📲 Connect ▾ → Connect Device), on the laptop or a hosting Galaxy Tab. Names are kept after reconnects and restarts.
- **📱 Add Phone Remote is always there** on the remote in control, also after it reconnected without the PIN.
- **The Galaxy Tab keeps hosting** when its screen goes off or another app is opened (notification *Mind It! is hosting a quiz*), and **other Galaxy Tabs find its game** (*Tablet Game Found*). 🟡 Not yet tried on a real tablet, so rehearse at home first.
- **The webpage works with no internet** once it has been opened (https://coolrishi20.github.io/MindIt-Web/).

Build 128 added trusted devices, one remote at a time with your approval, Connected Devices and the Galaxy Tab as the server.

Full history: `Reports/MIND_IT_CHANGELOG.md`. Test results: `Reports/MIND_IT_QC_REPORT.pdf` (build 129: 2,316 / 2,316 checks passed; iPhone and iPad checks used phone- and tablet-sized browsers, not real Safari; the Galaxy Tab as the server was tested on the build machine, and its background hosting and *Tablet Game Found* not at all, as they need a real tablet).

## Older builds

Builds since 125 stay in this repository's history: **Commits** → pick a build → **Browse files**. The last known-good build before this series (build 119) is described in `Reports/MIND_IT_ROLLBACK_GUIDE.md`.

The source code lives in the separate private repository `MindIt-`. It is never copied here.
