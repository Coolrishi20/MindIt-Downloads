# Mind It!

<!-- LATEST-START (this section is rewritten automatically each time a release is published) -->
## ⬇️ Download Mind It! — Latest Version

**Mind It! v1.69 · Build 152** · released 24 October 2026

- 🪟 **Windows laptop** — [Download for Windows](https://github.com/Coolrishi20/MindIt-Downloads/releases/latest/download/Mind-It-Windows.exe) (.exe, 72.6 MB)
- 📲 **Galaxy Tab (Android)** — [Download for Android](https://github.com/Coolrishi20/MindIt-Downloads/releases/latest/download/Mind-It-Android-Galaxy-Tab.apk) (.apk, 2.7 MB)
- 🍎 **Mac (Apple Silicon)** — [Download for Mac](https://github.com/Coolrishi20/MindIt-Downloads/releases/latest/download/Mind-It-Mac-Apple-Silicon.zip) (.zip, 103.9 MB) — *build 150 file, unchanged in build 152*
- 📺 **Mi Box / Android TV (audience screen)** — [Download Mind It! TV](https://github.com/Coolrishi20/MindIt-Downloads/releases/latest/download/Mind-It-Android-TV.apk) (.apk, 211 KB)
- 🌐 **Web, iPhone or iPad** — [Open the web version](https://coolrishi20.github.io/MindIt-Web/) (nothing to install) · [download the page](https://github.com/Coolrishi20/MindIt-Downloads/releases/latest/download/mindit.html)
- 📘 **Guides** — [The Complete Idiot's Guide](https://github.com/Coolrishi20/MindIt-Downloads/releases/latest/download/Mind-It-Complete-Idiots-Guide.pdf) · [Quick Start](https://github.com/Coolrishi20/MindIt-Downloads/releases/latest/download/Mind-It-Quick-Start.pdf) · [Quizmaster Cheat Sheet](https://github.com/Coolrishi20/MindIt-Downloads/releases/latest/download/Mind-It-Quizmaster-Cheat-Sheet.pdf) · [Rehearsal Checklist](https://github.com/Coolrishi20/MindIt-Downloads/releases/latest/download/Mind-It-Rehearsal-Checklist.pdf) · [Players' Guide](https://github.com/Coolrishi20/MindIt-Downloads/releases/latest/download/Mind-It-Players-Guide.pdf)

**[View All Previous Versions →](https://github.com/Coolrishi20/MindIt-Downloads/releases)**
<!-- LATEST-END -->

---

## Which one do I need?

- **Windows laptop:** the portable app — no installer. Put it where your old `Mind It!.exe` was and use it instead; your players, history and saved game stay. Windows may ask once to allow it on the network: allow it (phones, the tablet and TVs need it).
- **Galaxy Tab:** open the APK on the tablet and tap **Update**. It's signed with the original Mind It! key, so it installs over the old app and keeps its data. **The tablet app from builds 129–134 doesn't work** (it shows the name "application" and closes at once): use build 135 or newer — it installs over it with **Update**.
- **Mac (Apple Silicon — M1, M2, M3, M4):** double-click the zip, drag **Mind It!.app** into Applications, then the first time: Apple menu › System Settings › Privacy & Security › **Open Anyway**. Allow "find devices on your local network". Not yet tried on a real Mac — test it at home first. (Intel Macs aren't supported.)
- **Web version:** opens in any browser with nothing to install — the whole quiz, but **without phones or the tablet** (a webpage can't host them), and with its own players and history in that browser. On an **iPhone or iPad**: open it in Safari, then **Share › Add to Home Screen**; once opened with internet it also works offline.
- **iPhone / iPad as the remote for a laptop quiz:** on the laptop open **📲 Connect ▾ › Connect Device** and scan the **iPad / iPhone** code with the Camera.
- **Both the laptop and the Galaxy Tab:** keep them on the **same build** — moving a running quiz between them needs it.

Full instructions: **The Complete Idiot's Guide** (chapter 4).

## Checking a download (optional)

Every release lists the **SHA-256 fingerprint** of each file (and has a `SHA256SUMS.txt`). On Windows: `certutil -hashfile "Mind-It-Windows.exe" SHA256` · on a Mac: `shasum -a 256 <file>`. The fingerprint must match the release page.

## Previous versions

**[All releases](https://github.com/Coolrishi20/MindIt-Downloads/releases)** — every published build with its own files, notes and fingerprints. Builds 125–131 are there too (their original files, checked against the build reports). The newest build is always marked **Latest**. The Galaxy Tab APKs of builds 129–134 are kept there as history but don't open on a tablet; don't install them.

Apps and PDFs are published only as releases. This repository holds the download page, the text reports — [changelog](Reports/MIND_IT_CHANGELOG.md) · [rollback guide](Reports/MIND_IT_ROLLBACK_GUIDE.md) — and the release tools ([RELEASING.md](RELEASING.md)). Up to build 131 the app and PDF files were also kept in the repository (`Windows/`, `Android/`, `Mac/`, `Web/`, `Guides/`, `Reports/`); they were taken out of the current files in build 134 and are still in the repository's history and in the build-131 release.

The source code lives in the separate private repository `MindIt-`. It is never copied here.
