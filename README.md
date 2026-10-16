# Mind It! v1.69 — downloads

**Current build: 130** (16 October 2026). Each new build replaces the files below, so this page always holds the latest version.

## Which file do I need?

| Device | File | Size | Check (first 16 of SHA-256) |
|---|---|---|---|
| Windows laptop | [`Windows/Mind It!.exe`](Windows/) | 69 MB | `03cbf028753c207e` |
| Galaxy Tab (Android) | [`Android/Mind It! for Android (Galaxy Tab).apk`](Android/) | 1.7 MB | `729633a4746dc7f1` |
| Mac (Apple Silicon only) | [`Mac/Mind It! for Mac (Apple Silicon).zip`](Mac/), then follow `Mac/How to install on a Mac.txt` | 100 MB | `c053a8e034759edf` |
| Any computer's web browser (no install) | [`Web/mindit.html`](Web/): the webpage version | 2.7 MB | `0159f9aade1aeb28` |
| Guides (PDF) | [`Guides/`](Guides/): Complete Idiot's Guide, Players' Guide, Quick Start, Quizmaster Cheat Sheet, Rehearsal Checklist | | |
| Reports | [`Reports/`](Reports/): QC report, changelog, rollback guide | | |

**To download a file:** open it on GitHub and click the **Download raw file** button (⤓, top right of the file view). Every file is complete; there are no parts to join.

- **Windows:** this is the portable app. Replace your old `Mind It!.exe` with this one; your data stays.
- **Galaxy Tab:** open the APK on the tablet and tap **Update**. It is signed with the original key (versionCode 130), so it installs over the old app and keeps its data.
- **Mac:** see `Mac/How to install on a Mac.txt`. Not yet tried on a real Mac. Test it at home before a quiz night.
- **Webpage (`mindit.html`):** double-click it on a Windows PC or Mac and it opens in Chrome, Edge or Safari. It is the whole quiz, but **without phones or the tablet** (a webpage can't host them), and it keeps its own players and history in that browser. Use backup files to move data between it and the laptop app. It doesn't work as a downloaded file on an iPhone or iPad. Complete Idiot's Guide 4.1c.
- **iPhone / iPad:** there is no app file to install.
  - **To play the quiz on the iPhone or iPad itself:** open **https://coolrishi20.github.io/MindIt-Web/** in Safari, then **Share → Add to Home Screen**. Once opened with internet it also works with **no internet** (since build 129).
  - **As the remote for a laptop quiz:** on the laptop open **📲 Connect ▾ → Connect Device** and scan the **iPad / iPhone** code with the Camera (Complete Idiot's Guide, Setup B2).
  - **As a team phone:** join from the laptop as usual (Complete Idiot's Guide 8.6).

## New in build 130

- **📡 TVs without a cable:** any TV, projector or computer with a web browser on the same Wi-Fi can show the audience screen. On the laptop (or the hosting Galaxy Tab): **📺 Audience View ▾ → Connect Audience Screen**, then type the address it shows (ending in `/tv`) into the TV's browser. You can connect several screens and name, test or disconnect each one. Only the audience picture is sent; your controls, answers, wagers and PINs never leave your device. 🟡 Not yet tried on a real smart TV.
- **💻 Take Over Tablet Quiz:** a quiz running on the Galaxy Tab moves to the laptop while it runs, after the tablet approves. Scores, question, wagers, chips and the countdown all move. Phones keep their team without a new code, remotes and TVs follow, and the tablet becomes the remote. 🟡 Not yet tried with a real Galaxy Tab, so rehearse at home first.
- **🧪 Test Hosting** (Connect Device → Run Test), a **🔋 battery warning** while hosting, **🔒 Lock** on the remote, and a **signal** for each remote in Connected Devices.

Build 129 added device names, Add Phone Remote always available, background hosting on the tablet and the offline webpage.

Full history: `Reports/MIND_IT_CHANGELOG.md`. Test results: `Reports/MIND_IT_QC_REPORT.pdf` (build 130: 2,495 / 2,495 checks passed; iPhone and iPad checks used phone- and tablet-sized browsers, not real Safari; the Galaxy Tab's server and the TVs were tested on the build machine; a real Galaxy Tab and real smart TVs were not used).

## Older builds

Builds since 125 stay in this repository's history: **Commits** → pick a build → **Browse files**. The last known-good build before this series (build 119) is described in `Reports/MIND_IT_ROLLBACK_GUIDE.md`.

The source code lives in the separate private repository `MindIt-`. It is never copied here.
