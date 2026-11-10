**Mind It! v1.69 · Build 178** · 10 November 2026

Five small fixes from a code audit of builds 176–177.

## What's fixed
- **Pass-on bonus after a time-out.** When a team's time ran out and you later scored it Correct from "A different team answered?", it could also collect a pass-on bonus for a pass another team made *after* its turn. It now gets the bonus only for passes made before its own turn.
- **The last team's time runs out.** The question closes as "No One Answered", and for those 7 seconds the question card now offers **"⏰ Team A's time ran out — answered in time after all?" → Give Team A its answer back**. It cancels the close and brings CORRECT / WRONG ANSWER back for that team.
- **🔊 Sound Check** stops when you leave Setup (it used to play on over the opening screens), and keeps its "Playing 2 of 6…" line if Setup redraws.
- **Tablet newer than the laptop.** A Galaxy Tab on build 177 connected to a laptop on an older build kept re-sending its error list every second or two. It now stops after the laptop says no, and tries once more the next time it connects.
- **Present mode's toolbar** keeps finger-sized buttons (44 px) on touch screens. With a mouse it stays the slim line of build 177.

## Also in this release
- No other rule, score, timer or wager changed. Old saves and backups open as before.
- The Mac app (build 175), the guides (build 175) and the Quiz Night Run-Sheet (build 177) are unchanged.

## Updating the Galaxy Tab
Android may warn that the app could be harmful. That is Google Play Protect: it warns about apps installed from outside the Play Store that can update themselves. Tap the small arrow (**More details**), then **Install anyway**. This build asks for no new permissions.
