**Mind It! v1.69 · Build 156** · 28 October 2026

Everything you asked for today — the Theme list, ⟳ Sync with its status, 🏁 End game now, 📊 Question stats and a newer engine for the laptop app — and the fixes from a full code review and QA pass.

## Fixed
- **The 🎨 Theme list on the Galaxy Tab.** On the tablet remote held upright, the list opened off the left edge of the screen, so the options were cut off (on the last screen and everywhere else); held sideways, the last few themes hid behind a scroll. All 14 themes now show in full, both ways. Every dropdown menu in the app now keeps itself on the screen.
- **A phone could peek at another team's 💡 hint.** With team codes on, a phone that knew another team's number (it's visible to every phone) could read that team's hint — the first letter and word lengths — without its code. Now a phone only gets its own team's hint, wheel and chips, with the right code. Fixed on the laptop and on the Galaxy Tab when it hosts.
- **The Volume slider now has a name for screen readers** (in Undo & resets and in Setup → Sound) — the one gap left by build 155's accessibility check.

## New
- **⟳ Sync devices.** The laptop and the Galaxy Tab now keep the same questions, players and Historic Games:
  - **after every game:** when the laptop saves a game, a connected tablet gets it a few seconds later — no reconnecting (this is why your tablet showed 2 games when the laptop had 3);
  - **⟳ Sync** on the tablet remote's top bar, any time;
  - **⟳ Sync devices** on the laptop: in Player Profiles, in the list of connected devices, and in ⋯ during a game.

  Nothing is deleted: each device keeps everything and gets what it was missing (a game you deleted on purpose stays deleted). The tablet needs this build (156) for the automatic sync and its ⟳ Sync button; a tablet still on build 155 syncs only when it connects, as before.

- **Sync status.** Beside ⟳ Sync on the laptop and on the tablet: *Last synced 2 min ago · laptop 3 games · tablet 3 games*. When the two differ, the tablet's button shows **⟳ Sync ⚠** so a 3-vs-2 like last night's shows at a glance.
- **📊 Question stats.** Every game you save now remembers which questions were got. In the Question Database each question shows its record (*✓ 2 of 3 games*, *✗ nobody got it*), and **More ▾ → 📊 Question stats** lists the questions nobody got and the ones every game got (maybe too easy), each with ✎ to edit or delete. It counts games from this build on; the stats travel with Historic Games to the tablet.
- **🏁 End game now, during the game.** In ⋯ on the laptop and on the Galaxy Tab when it hosts, and as **🏁 End Game Now** on the tablet remote (the tablet in charge). It asks first, then goes straight to the standings with the scores as they are; the game is saved to Historic Games as usual. It doesn't show once the game is already over. The remote needs this build (156).

## Under the hood
- **The laptop app's engine is up to date.** Electron 33 → 44 (the built-in Chrome 130 → 152, Node.js 20 → 24): back on a version that gets security fixes, and none of the ~45 published problems of the old one. Your games, players and settings are untouched. Checked on Linux with the laptop app's whole test half and a Windows build; not yet run on a real Windows PC — build 155's EXE stays on the downloads page in case.

## Downloads
Windows (Mind-It-Windows.exe), Galaxy Tab (Mind-It-Android-Galaxy-Tab.apk), Mind It! TV for the Mi Box (Mind-It-Android-TV.apk), the web page (mindit.html), the guides (as in build 155) and the QC report. No Mac app in this build (every 5th build — the Mac stays on build 155 until 160). Your saved games, players and settings carry over.
