**Mind It! v1.69 · Build 146** · 22 October 2026

## New
- **A premium look on every theme:** glossy board tiles, category headers rimmed in the theme's accent colour, deeper score cards, a soft glow on the question and the answer, framed pictures and a spotlight for the Daily Double — all in each theme's own colours. Comic Book, Gaming and Wizard keep their own style. The laptop, tablet remote and phones get the same depth.
- **🎨 Theme ▾ in your top bar** (next to Sound): pick any of the 12 themes and the whole game changes look at once — the laptop, the TV window and the Wi-Fi TVs — without leaving the question. Setup → 5 · Audio & Presentation still has the theme previews.
- **🎲 Fun team names:** **🎲 Fun Names** in Quick Setup names every team at once; in Setup → 2 · Teams a 🎲 beside each name gives that team a new one (your QuizBiz-style favourites first: Question Tarantino, Quiztiano Ronaldo, The Quiztice League…).
- **Easier to read on the TV:** a question's picture now fits its frame (on a 16:9 TV the bottom was cut off), team names, the turn line ("Next to Pick:") and the revealed answer are bigger, and the Final wager screen just says "Category".
- **Phones:** one team card (name, place and score), **"Your Turn to Pick!"** in words when it's your team's turn, your score and place under the buzzer, a tidier wager pad — and they now follow your **Motion** setting (Full / Subtle / Off).
- **Wi-Fi Audience Screens** (a TV opening the laptop's address) now play the animations too. New motion: the answer rises with a line sweeping under it, the turn banner slides in, a picture rises into its frame.
- **Laptop:** Correct and Wrong are the same size; Setup's right-hand column scrolls above the Go-Live bar. **Tablet remote:** +30 Sec only shows with a question open.
- **A new theme picker** (Setup → 5 · Audio & Presentation): larger, cleaner previews of each theme on the TV, **In Use** on the current one.
- **Back to the board after 3 seconds** (was 7), on by default — switched on once on every device with this update; you can still turn it off.
- **Google Drive backups, lighter and steadier:** made a few seconds after the screen appears (the standings and winner share one upload), skipped once a day when nothing changed, more time for big backups on slow internet, patient retries that never start during a question, and the size and time shown. Backups need nothing changed in your Google script.
- **☁️ Restore from Drive** (Setup → 6 · Advanced → Google Drive Backup): your newest backups in Drive, newest first; ↺ Restore asks first and keeps a Safety Backup, like Choose Backup File. **Needs the new Google script** (MindIt_GoogleDrive_Backup.gs, version 2) — a 2-minute update; until then the app shows the steps and backups keep going up as before.
- **🎨 Theme on the tablet remote:** in the remote's top bar, the same 12 themes; one tap changes the laptop, the TV window and the Wi-Fi TVs.
- **No One Answered closes after 3 seconds** (was 7), like Back to the Board.
- **A slow Wi-Fi TV lightens itself:** a Wi-Fi Audience Screen that can't keep up switches to gentle motion and drops the heavy glows; the laptop tells you which TV. Reload the TV's page to try full motion again.
- **🏆 Champions card:** on the winner screen, a Champions Card tile puts the winning team on the TV with its players' pictures and stats; **💾 Save Champions Picture** saves it to share.

## Checked
- The 10-second blip from build 145's stress test didn't come back in eight repeat runs; the stress test now watches for it. In the stress run's idle phase the monitors saw no stall at all.
- A slow TV (4× slower): the TV kept 36–65 frames a second through the moments and 57–60 at rest (the winner's falling dots 17–25, up from 8 in 145); the Quizmaster page's longest pause stayed about 1 second, as in 145.

## Guide
- The Complete Idiot's Guide (174 pages), Quick Start, cheat sheet and checklist are updated for build 146, with three new real screenshots.

## Unchanged
- **The rules, timers and scores.**
- **Versions:** still v1.69.

## Compatibility
- **Data:** the same kind of saved data and backup files as build 145.
- **Galaxy Tab:** installs over build 145 (versionCode 146, original key); a tablet on 143–145 offers the update itself when it connects to a laptop on 146. Update the laptop and the tablet together so phones get the new data from either one (and the tablet's 🎨 Theme needs the laptop on 146).

## Checks (a major change, so all of them)
- 158 suites, 3,549/3,549 checks (three tests updated and run again); the Audience View audit; the stress phases and the 60-minute soak (details in the QC report).

## Not yet tried for real
- Tested in the sandbox only (browsers and the laptop app under Linux). Nothing was run on your real Windows PC, Galaxy Tab, phones or TVs; how the new look and motion run depends on each screen.
- **Restore from Drive** was tested against a stand-in for your Google script on this computer, not against Google itself; the slow-TV switch was tested on the sandbox's own slow TVs and by simulating it, not on a real TV.
