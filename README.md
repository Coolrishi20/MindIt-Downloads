# Mind It! v1.69 — downloads

**Current build: 126** (13 October 2026). Each new build replaces the files below, so this page always holds the latest version.

## Which file do I need?

| Device | File | Size | Check (first 16 of SHA-256) |
|---|---|---|---|
| Windows laptop | [`Windows/Mind It!.exe`](Windows/) | 69 MB | `6cd8baecb68cc8cb` |
| Galaxy Tab (Android) | [`Android/Mind It! for Android (Galaxy Tab).apk`](Android/) | 1.6 MB | `c18ac5de3743017a` |
| Mac (Apple Silicon only) | [`Mac/Mind It! for Mac (Apple Silicon).zip`](Mac/), then follow `Mac/How to install on a Mac.txt` | 100 MB | `c04447c1fc64ee60` |
| Any computer's web browser (no install) | [`Web/mindit.html`](Web/): the webpage version | 2.6 MB | `b3e16cb9c68e70ac` |
| Guides (PDF) | [`Guides/`](Guides/): Complete Idiot's Guide, Players' Guide, Quick Start, Quizmaster Cheat Sheet, Rehearsal Checklist | | |
| Reports | [`Reports/`](Reports/): QC report, changelog, rollback guide | | |

**To download a file:** open it on GitHub and click the **Download raw file** button (⤓, top right of the file view). Every file is complete; there are no parts to join.

- **Windows:** this is the portable app. Replace your old `Mind It!.exe` with this one; your data stays.
- **Galaxy Tab:** open the APK on the tablet and tap **Update**. It is signed with the original key (versionCode 126), so it installs over the old app and keeps its data.
- **Mac:** see `Mac/How to install on a Mac.txt`. Not yet tried on a real Mac. Test it at home before a quiz night.
- **Webpage (`mindit.html`):** double-click it on a Windows PC or Mac and it opens in Chrome, Edge or Safari. It is the whole quiz, but **without phones or the tablet** (a webpage can't host them), and it keeps its own players and history in that browser. Use backup files to move data between it and the laptop app. It doesn't work as a downloaded file on an iPhone or iPad. Complete Idiot's Guide 4.1c.
- **iPhone / iPad:** there is no app file to install. Join from the laptop as usual, then in Safari tap **Share → Add to Home Screen** to get a full-screen **Mind It!** icon (Complete Idiot's Guide 8.6).

## New in build 126

- 📲 **Mind It! on the home screen:** on an iPhone or iPad, **Share → Add to Home Screen** now gives the gold **M** icon named **Mind It!**, which opens the team-phone page or the 📱 Phone Remote full-screen, with no Safari address bar.
- The **webpage version** is now offered here (`Web/mindit.html`).
- Game screens, rules and saved data are the same as build 125.

Full history: `Reports/MIND_IT_CHANGELOG.md`. Test results: `Reports/MIND_IT_QC_REPORT.pdf` (build 126: 2,169 / 2,169 checks passed; the iPhone checks used a phone-sized browser, not a real iPhone).

## Older builds

Builds since 125 stay in this repository's history: **Commits** → pick a build → **Browse files**. The last known-good build before this series (build 119) is described in `Reports/MIND_IT_ROLLBACK_GUIDE.md`.

The source code lives in the separate private repository `MindIt-`. It is never copied here.
