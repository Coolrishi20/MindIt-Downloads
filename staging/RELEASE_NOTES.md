**Mind It! v1.69 · Build 140** · 19 October 2026

## New — four buttons for the end of a round and the end of the game
You approved these from before/after pictures, with your four answers for the tiebreaker.
- **↩ Undo pop-up.** After every score, the laptop shows what was scored at the bottom of the screen, with an **↩ Undo** button, for 8 seconds.
  - One tap undoes it straight away, with no question asked.
  - The next score replaces it.
  - It never shows on the TV and is hidden in Present mode.
  - **Undo last score** and the tablet's **↶ Undo** are unchanged.
- **⏱ One More Question.** On the board, or in Undo & resets ("Make This the Last Question" while a question is on screen). It makes the next question the last one of the round.
  - The TV shows **"LAST QUESTION OF THE ROUND"** under the team in play.
  - After that question (scored, or No One Answered), the round summary comes up by itself and says "That was the last question".
  - It turns into **✕ Cancel Last Question** until then.
- **⭐ Go to the Final.** On the board and in Undo & resets, when the game has a Final and rounds are still to come. It ends the round now (like End round early) and skips the rounds still to come. After the round summary ("Straight to the Final Round"), the Final starts.
  - Scores are kept.
  - It asks first and names the rounds it skips. The tablet asks on the tablet.
  - The Final is numbered after the last round played, so after Round 2 it is "Round 3 · Final Round".
  - **Resume** on the round summary cancels it.
- **⚡ Sudden-death tiebreaker (Quizmaster's choice).** When teams finish level on points for first place, **⚡ Play Tiebreaker** appears next to **Show final standings**. It comes up when the Final reveal is done, or on the last round summary if there is no Final.
  - **The question:** one text question picked at random from your Question Database. It is never one used in this game, and it is one never used before while any are left. Only you see the answer (on the tablet, behind a tap). **🔁 Another Question** swaps it before you show it.
  - **The answers:** teams answer out loud. You mark the first team: **Correct** wins the game. **Wrong** puts that team out. If every team is wrong, you get a **New Question** and every team is back in.
  - **Points don't change.** The winner simply ranks first among the teams level with it.
  - **Where it shows:** the standings, the winner screen, the 💾 standings picture and Historic Games all say "won the sudden-death tiebreaker". The questions shown count as used.
  - **Undo Last Mark** takes back a mark. **Cancel Tiebreaker** asks first, then goes back: most correct answers decides, as before.
  - **No question left in the Database?** You ask one of your own and mark the teams the same way.
  - **Show final standings** skips it, and most correct answers decides, exactly as before.

## Fixed
- **Final reveal on an upright (portrait) TV with 6–8 teams.** The answer cards were squeezed into one row, the standings sat small at the very bottom, and the middle of the screen was empty. Now the cards go in rows of four, larger, with the standings straight under them (6 teams: two rows of three). Landscape screens are unchanged.

## Safer saving, building and codes (the code audit you approved on 19 Oct, 12:50)
All four are part of this same build 140 — no separate version or release.
- **1 · Pictures, videos and music survive a crash.** Before, a quiz with lots of pictures, videos, music, an intro video or team photos was too big for the autosave. It saved everything except those, so after a crash or a forced restart the game came back without them. Now a **complete copy** is also kept:
  - **Windows/Mac app:** two files in the Mind It! data folder. They are found even if Mind It! opens on a different network port after a restart.
  - **Galaxy Tab:** two files in the app's own storage.
  - **Any browser:** the browser's database, which has far more room than its autosave space.
  - After a restart, **Resume saved game** brings the game back with every picture and sound. A game already resumed without them gets them put back.
  - Each copy is written to a new file first and then swapped in, so a crash mid-save keeps the previous copy. A damaged copy is skipped.
  - **You'll rarely see anything new.** Undo & resets gets one line: "✓ Complete copy saved at …". Only if there is no room anywhere for the complete copy does a **red card** appear under Now Picking, with **💾 Save Backup File** and **Try Saving Again**. A one-time message says the same.
  - **Start fresh** still makes its Safety Backup first, now with the pictures included.
  - Players, history, the Question Database and settings are saved exactly as before.
- **2 · The app can be rebuilt exactly from GitHub.**
  - The page, the Windows/Mac app and the Galaxy Tab app all build from a fresh copy of the private repository, with the tool versions locked.
  - Today's page rebuilt from GitHub is byte-for-byte the page that was tested.
  - The tablet build script only signs with your original key, and takes the passwords from the computer, never from a file.
- **3 · Team codes, the remote PIN, game keys and IDs** now come from the browser's secure random generator. The codes look exactly the same as before: 4 letters, 4 digits, 2 digits.
- **4 · Code map and checker.** A new tool lists every place where one part of the program changes another, and flags conflicts before a release. On today's code it found no problems. It found two old functions that were rewritten twice; the earlier versions are unused and harmless, and they were left alone.

## Guide and tests
- **Complete Idiot's Guide pictures refreshed:** 22 pictures refreshed and 7 new (5 for the four new buttons, 2 for the complete save: the new line in Undo & resets and the red card); section 22.1 explains the complete save; the Complete Idiot's Guide is now 165 pages. The four new buttons are explained in Chapters 15 and 18.3, with new pictures.
- **The 60-minute soak now plays whole games** to the winner screen. Teams send their Final wagers from their phones, every Final answer is marked, and a tiebreaker is played if one comes up. Each finished game is checked: the winner on the TV, the game in Historic Games and in the laptop's player file, and the recap card, history recap and standings pictures. To fit the hour, game 1 uses ⏱ One More Question late in Round 2 and game 2 uses ⭐ Go to the Final.

## Unchanged
- **The rules:** scoring, turns and every rule are as before. Ties are still decided by most correct answers unless you play the tiebreaker.
- **Versions:** still v1.69.
- **Laptop app and Galaxy Tab:** the only change is where the complete copy is stored: the laptop app's `main.js` and the tablet app's `MainActivity` each gained it. The tablet's server and the hand-over between laptop and tablet are unchanged (still protocol 132), so laptop and tablet on build 140 hand over as before.

## Compatibility
- **Data:** nothing is deleted and no IDs change. A game saved in 139 opens in 140, and a game saved in 140 opens in 139 (139 simply ignores the complete copy).
- **Saved in the middle of a tiebreaker:** the game opens on the tiebreaker in 140. Build 139 has no tiebreaker screen, so it would show an empty screen. Keep the laptop and the tablet on the same build, as before.
- **Galaxy Tab:** installs over build 139 (versionCode 140, original key).

## Not yet tried for real
- The new buttons were tested in the laptop app, the webpage and the tablet remote page on the build machine, not on a real Windows PC, Mac or Galaxy Tab. The release check opens the APK on an Android emulator.

Tests: 144 suites, 3,188/3,188 checks Full details: QC report (attached).
