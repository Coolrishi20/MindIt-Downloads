**Mind It! v1.69 · Build 141** · 20 October 2026

## New — four things you'll see
You asked for "any upgrades or improvements?", answered "do them all" to the nine suggested, and approved the before/after pictures of the five you can see ("ok all five").
- **✅ Pre-show checklist on Setup.** A card on the right of Setup ticks itself every few seconds:
  - **TV / Audience View** — the Audience window is open, or a TV is connected over Wi-Fi. **Open Audience View** opens it.
  - **Team phones** (laptop app) — how many teams have joined. Only needed for phone buzzers; otherwise optional. **🔐 Team Codes** shows the codes.
  - **Tablet remote** (laptop app) — connected or not (optional).
  - **Sound** — **▶ Test Sound** plays the reveal sound so you can hear it in the room.
  - **Questions** — every question of the rounds you're playing, and the Final, is filled in. **📚 Question Database** opens it.
  - **Backup file** — whether you've made one today. **⬇ Back Up Now** makes one.
  - **Storage** — where the game is kept (see below).
  - The top says "N of M ready" for the lines that matter; optional ones show a dash. Nothing stops you from starting without them.
- **⚑ Fix Later.** When a question or its answer is wrong or badly worded, tap **⚑ Fix Later** (or press **F**) while it is on screen — on the laptop or on a remote (tablet or phone). Also in the Final.
  - A small note confirms it. Tap again (**⚑ Flagged — Remove Flag**) to take the flag off.
  - The **Question Database** gets a **⚑ Fix Later** tab while anything is flagged: the question, the answer, which quiz, round and category, and when you flagged it. **✎ Edit** opens it in the database (or **➕ Add To Question Database** if it isn't there yet). **✓ Fixed** takes it off the list.
  - At the end of the game, the laptop shows "⚑ N questions flagged to fix" with **⚑ Open Fix Later List**.
  - Up to 300 flags are kept, with your players and Question Database.
- **Reveal asks first when nobody has answered yet.** When teams take turns (the question passes to the next team), or on a Daily Double, **Reveal Answer** (button or R key) now asks "Reveal the answer now?" — **Keep It Hidden** or **Reveal Answer** — if no team has answered yet, so a mis-tap can't spoil the question.
  - Once any team has answered, passed or buzzed in, Reveal works straight away as before.
  - In Classic turns (reveal first, then score) nothing changes.
  - The tablet remote asks on its own screen; the laptop then doesn't ask again. The phone remote reveals at once, as before.
- **📊 Night Recap on the TV.** On the winner screen, the final standings and the awards screen, **📊 Night Recap** (laptop, tablet or phone remote) puts one slide on the TV: "Tonight's Recap" with the quiz title, date and host, the champion (or joint champions) with their score and players, the standings, four numbers (questions played, Daily Doubles, the biggest swing, game time) and up to four highlights (a tiebreaker, Triple Gamble / Phoenix / Bottoms Up, achievements).
  - From there: **🏆 Winner Screen**, **Back to standings**, **💾 Save Standings Picture** or **🎲 Play Again (New Questions)**.
  - It fits upright (portrait) TVs and up to 8 teams. On an upright screen with many teams the champion and the whole table always show; a highlight that doesn't fit whole is left out.

## Safer saving
- **Backups & Restore says where your game is kept.** Two new lines: **Complete copy (pictures, videos, music)** — when it was last saved — and **Storage**:
  - laptop app: "Kept in the Mind It! folder on this computer";
  - Galaxy Tab: "Kept in the tablet app's own files";
  - a browser: the page now asks the browser once to keep its storage. If it agrees: "Protected — the browser keeps it". If not: "Not protected — the browser may clear it if space runs low, so back up regularly".
- **The complete copy stores Question Database pictures once.** A game picture that is also in your Question Database is saved as a pointer to it, not a second copy, so the complete copy is smaller and quicker to write. After a crash the picture comes back from the database, as the quick save has done since build 111.

## Checks before every release
- **The tablet app keeps a saved game.** The release check on an Android emulator now also starts a game in the tablet app, lets it save its complete copy into the app's files, closes the app completely, reopens it and checks the game is found. If that fails, nothing is published; the result is added at the end of these notes.
- **The 60-minute soak plays a tiebreaker and the Night Recap.** Game 2 is forced into a tie for first place and the tiebreaker is played from the tablet; game 1 shows the Night Recap on the TV.
- **Two unused old functions removed** (an early version of the phone remote's start-up and an old logo drawing). They were replaced long ago and never ran. The code checker now reports no issues at all.

## Guide
- 7 new pictures (the Pre-show checklist, the ⚑ Fix Later button and Question Database tab, the early-reveal question, the Night Recap on the TV, the winner screen's What's Next card with the Night Recap and the Fix Later card, the Backups & Restore storage lines); new text in Step 12, 6.4, 15.3, 15.10, 15.12, 19.1 and Chapter 22; a “New in build 141” list at the front; the cheat sheet gains ⚑ Fix Later (F) and 📊 Night Recap; the Complete Idiot's Guide is now 168 pages

## Unchanged
- **The rules:** scoring, turns and every rule are as before.
- **Versions:** still v1.69.
- **Laptop app and Galaxy Tab:** no change to `main.js` or the tablet's Java code (versionCode 141 only). The hand-over between laptop and tablet is unchanged (protocol 132).

## Compatibility
- **Data:** nothing is deleted and no IDs change. A game saved in 140 opens in 141, and a game saved in 141 opens in 140.
- **Flags:** build 140 keeps them but doesn't show them.
- **On the Night Recap:** build 140 has no recap slide. If you go back to 140, leave the recap (🏆 Winner Screen) before closing, or the TV would be empty there.
- **Galaxy Tab:** installs over build 140 (versionCode 141, original key).

## Not yet tried for real
- The new screens were tested in the laptop app, the webpage and the tablet remote page on the build machine, not on a real Windows PC, Mac, Galaxy Tab or TV. The release check opens the APK on an Android emulator and saves and reopens a game there.

Tests: 146 suites, 3,264/3,264 checks. Full details: QC report (attached).
