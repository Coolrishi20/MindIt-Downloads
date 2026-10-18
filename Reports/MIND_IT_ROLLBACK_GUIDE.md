# Mind It! v1.69 — Rollback Guide

**What this is for:** if the new build (125) misbehaves on the night, go back to the last working build (119) quickly, without losing your players, history, Question Database or saved game.

**The rollback copy:** `MIND_IT_v1.69_PREVIOUS_WORKING_RELEASE.zip` — the files actually delivered as **build 119**, preserved before any of the build 120–125 work (not rebuilt). Its `MANIFEST.md` lists every file and `CHECKSUMS.sha256` has a SHA-256 for each of its 390 files.

| Rollback item | Where in the zip | Check |
|---|---|---|
| Windows app, build 119 | `windows/Mind It!.exe.part1–3` + `Join Mind It - build 119.bat` | joins to `Mind It!.exe`, 68,957,397 bytes, SHA-256 `49517ba1281f58ca5370a22e2214f5efd6f0c45a56d0eaf9828f76ab340b2bbb` |
| Android app, build 119 | `android/Mind It! for Android (Galaxy Tab).apk` | versionCode 119, SHA-256 `7a25704df3937c3d0cdcf45497696ff10af2f31607d6da6babdad0ebeff7ca0f`, original signing key |
| The app page itself | `source/mindit_built_build119.html` | identical to the page inside the build-119 EXE and APK |
| Source code | `source/` (git commit `2eefd72`, tag `checkpoint-build119`) | — |
| Guides and project notes as of build 119 | `docs/` | — |

**Not in the zip:** your signing keystore (keep your private `MindIt_Android_Keystore_PRIVATE.zip`), your app data (it lives on your laptop and tablet), and `node_modules`.
**Keep the zip private:** `source/android/build.sh` contains the keystore passwords in plain text.

---

## Before you roll anything back — make a backup (2 minutes)

Do this on **every device you will touch**, while the current build is still installed:

1. Open Mind It! → **⋯ ▾ → 💾 Backups & Restore → ⬇ Back Up Now**. Keep the `MindIt_Backup_….json` file somewhere safe (a USB stick, your Google Drive). It holds the current game, players, pictures, Historic Games and the Question Database.
2. Optional extra copy of the players: **Player Profiles → Export Player Profiles**.

**Can build 119 read what build 125 saved?** Don't assume it — so it was checked: the code that writes saves, profiles and backups did not change between builds 119 and 125 (build 121 only adds a spare copy that older builds ignore) (same keys `trivizzle.save.v2` and `mindit.profiles.v1`, chip keys `ud` / `bu` / `tg`, no new saved fields), and a rollback test was run (see *Rollback test* at the end). Even so, keep the backup from step 1 until you are happy.

---

## Windows laptop — back to build 119 (keeps your data)

The Windows app is a single portable EXE; your data is kept separately in your Windows user profile, not inside the EXE. Swapping the EXE does **not** touch your data.

1. **Close the new build safely:** if a game is running, finish the question you are on (the game autosaves after every change), make the backup above, then close Mind It! with the window's ✕ — Audience View closes with it. Wait a few seconds before starting the old EXE so the local server (port 8765) is free.
2. Unzip `MIND_IT_v1.69_PREVIOUS_WORKING_RELEASE.zip`, open the `windows` folder.
3. Keep the three `.part` files and `Join Mind It - build 119.bat` in the same folder and double-click the `.bat`. It joins them into `Mind It!.exe` and checks the result.
4. Move the build-125 `Mind It!.exe` out of the way (rename it to `Mind It! build 125.exe` or move it to another folder) — don't delete it until you are sure.
5. Run the build-119 `Mind It!.exe`. Windows SmartScreen may warn (the app isn't code-signed): **More info → Run anyway**.
6. Check: your players and Historic Games are there; the saved game offers **Resume**. If anything is missing, restore your backup: **⋯ ▾ → Backups & Restore → ⬆ Choose Backup File…**.

**To return to build 125:** close Mind It! and run the build-125 EXE again. Same data.

---

## Android tablet — read this first

⚠️ **Android does not let you install an older build over a newer one.** The tablet has build 125 (versionCode 125); build 119 has versionCode 119. Android refuses this "downgrade".

⚠️ **Uninstalling the app deletes everything Mind It! keeps on the tablet** — players, pictures, Historic Games, Question Database, the saved game and the pairing with the laptop. There is no undo.

You have three choices, safest first:

| Option | Data on the tablet | What it takes |
|---|---|---|
| **A. Keep build 125 on the tablet** and roll back only the laptop | Kept | Nothing. The tablet is a remote for the laptop; builds 119–125 speak the same link protocol, so a build-125 tablet works with a build-119 laptop. Try this first. |
| **B. Ask for a "rollback build"**: build 119's code re-packaged with a **higher** versionCode (e.g. 122), signed with your original key | Kept (installs over the top like any update) | A new APK has to be built — ask Claude for it. |
| **C. Uninstall, then install the build-119 APK** | **Deleted** — restore from your backup afterwards | 10 minutes. Only if A and B aren't possible. |

**Option C step by step (data will be deleted):**

1. On the tablet: Mind It! → **⋯ ▾ → Backups & Restore → ⬇ Back Up Now**, and save the file somewhere **off the tablet** (Google Drive, or copy it to the laptop with a cable). Check the file is really there.
2. Settings → Apps → Mind It! → **Uninstall**. (This is the step that deletes the tablet's Mind It! data.)
3. Copy `android/Mind It! for Android (Galaxy Tab).apk` from the rollback zip to the tablet and open it (allow "install unknown apps" for your file manager if asked).
4. Open Mind It! → **⋯ ▾ → Backups & Restore → ⬆ Choose Backup File…** → pick the backup from step 1.
5. Pair with the laptop again (**Connect To Laptop** → PIN).

---

## Reconnect the devices

1. Start the laptop app first and open the game (Resume, or Setup).
2. **Tablet:** Mind It! → **Connect To Laptop** → tap the laptop → enter the PIN if asked (after an uninstall it always asks).
3. **Phones:** players reload the join page (or scan the join QR code again). Phones remember their team; if a team code changed, they get the new one from 🔐 Team Codes.
4. **Audience View:** 📺 Audience View → choose the TV screen.

## Check that the rollback worked

- [ ] ⋯ ▾ → ★ About & Credits says **1.69**; the laptop runs the build you meant to run (build 119 has no ↶ Undo / ⟲ Reset buttons in the Random Team Generator — those arrived in build 120).
- [ ] Player Profiles, Historic Games and the Question Database are all there (compare a few names and counts with what you expect).
- [ ] The saved game offers **Resume**, and the scores are right.
- [ ] 📶 Connection Health: laptop, tablet and every phone show **Connected**.
- [ ] Play one question to the end (score it, then Undo it) — the TV, tablet and phones all follow.

## The web link (browser-only version)

The web link was last republished at build 124 (alternate builds: 116, 118, 120, 122, 124 — the next is 126). The link keeps a history of published versions; if you need the build-119 page there, ask Claude to republish `source/mindit_built_build119.html` to the same link.

---

## Older builds on GitHub (since build 126)

Your private **MindIt-Downloads** page keeps every build since 125 in its history (build 119, the rollback build, is not there — use the files described above): open **Commits**, pick the build (each commit says its build number), press **Browse files**, and download from there. The rollback steps above are the same whichever way you get the older files.

## Trusted devices and rollback (build 128)

Build 128 remembers trusted remotes in a small file next to your data (`trusted-devices.json`). An older build ignores it, so after rolling back each remote simply connects with the PIN again. Going forward again, the remembered devices are still there.

Build 129 adds device names to the same file. Build 128 ignores the names (the devices stay trusted and show their own names again); going forward to 129 the names come back. The Galaxy Tab APK of build 128 installs over 129 only after uninstalling (Android refuses a lower versionCode), which deletes the tablet's data — make a backup file on the tablet first (Chapter 22).

## Audience screens, transfers and rollback (build 130)

Build 130 keeps two more small files next to your data: `audience-displays.json` (names and margins of your Wi-Fi TV screens) and, on the laptop, `transfer-incoming.json` / `transfer-last.json` (the last quiz taken over from the tablet); the tablet keeps `xfer-state.json` / `xfer-final.json`. Older builds ignore them. A quiz that moved from the tablet to the laptop is in the laptop's saved game and Safety Backups; going back to build 129 on the laptop keeps it (open it with Resume). On the tablet, a quiz that moved away is not offered as a game to resume — it's in its Safety Backups. Going back to an older APK still needs an uninstall (lower versionCode), which deletes the tablet's data — back up first.

## The intro voice (build 131)

Build 131 changes only the intro's voice; it stores nothing new. Going back to build 130 brings back the old voice and keeps all your data. Builds 130 and 131 can still hand a tablet quiz over to each other (*Take Over Tablet Quiz*), because the hand-over code is the same.

## Build 132 — TV sound, report, hand-back

Build 132 keeps one more small file on the laptop, `handback-state.json` (and `handback-last.json` / `handback-final.json` for the last quiz handed to the tablet); on the tablet, `transfer-incoming.json` (a quiz coming back from the laptop) and `xfer-last.json` (the record of an earlier move, kept as history). Older builds ignore them. Rehearsal Report files are ordinary files in your Downloads (or wherever you saved them); delete them whenever you like.

- **Going back to build 131 on the laptop:** your data is unchanged. A quiz that was handed to the tablet is in the laptop's Safety Backups and the tablet's saved game. You lose TV sound, the short TV address, the report and the hand-back.
- **Going back to build 131 on the tablet:** an older APK needs an uninstall first (lower versionCode), which deletes the tablet's data — make a backup file on the tablet first (Chapter 22). Build 131 on the tablet still has the two problems fixed in 132 (it can't host again after a quiz moved to the laptop; a switched-off trusted remote cuts off others).
- **Mixed builds:** the laptop and the tablet must be on the same build to move a quiz between them (132 refuses 131 politely). Everything else — remotes, phones, TVs — works across 131 and 132.

## Build 136 — Online Mode, lighter backups, Make Photos Smaller

- **Online Mode:** going back to 135 shows Family Night again; the switches you had stay as they were (135 ignores the Online Mode setting).
- **Backup files made by 136** restore with every picture in build 119 — the rollback build in `MIND_IT_v1.69_PREVIOUS_WORKING_RELEASE.zip` — and in builds 132–135 (tested). Builds older than 111 can't read them (none of those is in use).
- **After Make Photos Smaller:** going back keeps the smaller originals (same picture IDs, any build shows them). To get the larger ones back: Backups & Restore → 🛟 Safety backups → **Before Make Photos Smaller** → ↺ Restore.
- **Galaxy Tab:** going back to 135 needs an uninstall (lower versionCode) — make a backup file first. Never 129–134.

## Build 135 — the tablet app fixed, storage fix, drawn backdrops

- **Galaxy Tab:** don't go back to builds 129–134 — those APKs close at once on the tablet. Older than 129 needs an uninstall (lower versionCode): make a backup file first.
- **Laptop:** going back to 134 works: the player file is the same format. With a large database, 135 keeps no quick copy in browser storage, so 134 shows no players for about 1.5 s after opening until it has read the file. **Save a backup file first** (Backups & Restore → Back Up Now) and don't change anything in those first seconds.
- **Webpage on an iPhone/iPad with a large database:** build 135 keeps it in the browser's own database (IndexedDB), which 134 can't read. **Before going back, save a backup file** (Backups & Restore → Back Up Now) and restore it in 134. Small databases stay in localStorage and need nothing.
- **Moving a quiz:** builds 132–135 can move a quiz between the laptop and the Galaxy Tab.

## Build 134 — Intermission music, build number, wizarding backdrop

Build 134 stores nothing new.
- **Going back to build 133** keeps all your data: Intermission is silent again, About & Credits shows only the version, and the wizard theme has its candles and crest back.
- **Moving a quiz:** builds 132, 133 and 134 can move a quiz between the laptop and the Galaxy Tab.
- **On the tablet:** going back needs an uninstall first (lower versionCode), so make a backup file first.

## Build 133 — the new intro theme

Build 133 changes only the intro's sound and adds one line to ★ About & Credits; it stores nothing new.
- **Going back to build 132** brings back the old intro and keeps all your data.
- **Moving a quiz:** builds 132 and 133 can still move a quiz between the laptop and the Galaxy Tab (same laptop and tablet server code).
- **On the tablet:** going back to 132 needs an uninstall first (lower versionCode), which deletes the tablet's data — make a backup file on the tablet first (Chapter 22).

## Source code

- Build 119: tag `checkpoint-build119` (commit `2eefd72`); build 120: tag `checkpoint-build120` (`da1753e`); build 121: tag `checkpoint-build121` (`c926b63`); build 122: tag `checkpoint-build122` (`e02d349`); build 123: tag `checkpoint-build123` (`9b2c15b`); build 124: tag `checkpoint-build124` (`ed2cc27`); build 125: tag `checkpoint-build125`.
- To rebuild an old build exactly: check out its tag, then follow `MIND_IT_BUILD_INSTRUCTIONS.md`.
- No history is rewritten for a rollback — going back means checking out an older tag, never deleting newer commits.

---

## Rollback test

*Run with build 121 (12 Oct). Build 122 changes only who gets the champion's crown at Begin Game — nothing that is saved — so the result applies to it too.*

Run on 12 Oct 2026 in the build machine's sandbox with the **real Windows laptop app** (Electron, same app shell as the EXE; Linux + virtual screen) — not on your laptop, and not on a tablet:

1. Build 121 on a fresh profile: 5 players, 1 finished game in Historic Games, a second game left unfinished on the board (600 / −200), and a backup file made.
2. The app was closed, the build-119 page put in its place, and the app started again **on the same profile**.
3. Results — **10/10 checks passed:** build 119 was really running; players (5) and Historic Games (1) kept; the finished game's scores intact; the unfinished game offered → **Resume saved game** → back on the board with 600 / −200; and the build-121 backup file restored in build 119 through ⋯ → Backups & Restore (players 5, Historic Games 1, the game from the backup).

**Not tested:** the Android rollback (no tablet here — Android's downgrade rule above is how Android works, not something seen on your tablet), and the web link.

⚠️ **One thing to know about build 119:** if you open build 119 and close it again *without* pressing **Resume saved game** or **Start fresh**, the unfinished game is not offered the next time (found during this QC, fixed in build 121). On build 119, **press Resume saved game the first time it is offered.** If it's gone, restore your backup file.

## After a rollback

Tell Claude what went wrong (what you pressed, what you saw, which device). The problem is fixed in a new build on top of 125 — rollback is the safety net, not the fix.


**Note on the Returning Champion:** build 119 still uses the old rule (any one shared player, first team in order). Rolling back changes who gets the crown, not any saved data.

**Mac:** the Mac app started at build 123 (Apple Silicon only from 124); there is no older Mac build to go back to. If the Mac app gives trouble, use the Windows laptop (restore a backup file made on the Mac — same format). Restoring a backup in build 119 doesn't ask first; build 123 does.

**Deleted players:** build 119 doesn't know about deleted players. After a rollback, a player you deleted in build 124 stays deleted on that device (the profile is gone), but past games show their name only in build 124 — build 119 shows “(removed player)” or “?” there.

**Safety backups and Recently Deleted (build 125)** live inside the app on that device; build 119 doesn't show them. Before rolling back, use **Back Up Now** (a file you keep) — and if you need a player you deleted, restore them first in build 125.
