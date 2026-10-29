**Mind It! v1.69 · Build 160** · 29 October 2026

Big libraries stay fast, the theme colours reach the host controls on older tablets too, the bots' answers on the TV keep out of the way, and every guide is updated — plus the Mac app.

## Faster with a big library
Tried with 5,000 questions, 50 players and 100 past games of 120 questions each — every main screen and action timed, and the slow ones fixed:

| | Build 159 | Build 160 |
|---|---|---|
| Question Database → All Questions | 0.58 s | 0.15 s |
| Question Database → Mastermind It! tab | 0.54 s | 0.08 s |
| Setup redraw | 0.49 s | 0.14 s |
| Setup → Rounds tab | 0.72 s | 0.20 s |
| Setup → Teams tab | 0.71 s | 0.16 s |

- The 👁 Preview button and the 📎 picture mark on each Question Database row looked their question up by searching the whole library, row by row. Now one lookup per screen. Same buttons, same marks.
- The duplicate check is now done quietly a few seconds after start-up, so even the first time you open the Question Database it opens at once.
- The scenery clock and Setup's live TV preview now wait for the next screen refresh. Before, they made the browser lay out the whole screen two extra times on every redraw.

## Fixed
- **The theme colours on the Galaxy Tab remote with an older Android System WebView.** Build 159's theme colours use a colour-mixing feature that older web views don't have. There, some host-control backgrounds came out see-through instead of the theme's colour. Build 159's notes said they would "keep the navy". That was wrong, sorry. Build 160 adds plain theme colours underneath for those web views.
- **A bot's answer on the TV** now sits on the edge of the question card, clear of a long question (with 7 or more teams), the ⚡ Speed Bonus countdown and the score cards. In build 159 it could cover a long question.

## Guides
All five guides are updated for build 160:
- **Quick Start:** practise with bots, Question Database shortcuts, ⟳ Sync devices, the back button and Close, 🏁 End game now, theme colours on your host screens, and restoring a backup on the Galaxy Tab.
- **The Complete Idiot's Guide (Online Mode):** "New in builds 156–160", practise alone with bots, one-tap add, and the laptop's 🏆 Season tab, with new pictures.
- **Quizmaster Cheat Sheet and Rehearsal Checklist:** updated, with NEW tags for what to try.
- **Players' Guide:** unchanged, because nothing players see changed.

## Downloads
- Windows (Mind-It-Windows.exe)
- **Mac (Apple Silicon)**, new in this build. The Mac app is made every 5th build.
- Galaxy Tab (Mind-It-Android-Galaxy-Tab.apk)
- Mind It! TV for the Mi Box (Mind-It-Android-TV.apk)
- The web page (mindit.html)
- The five guides and the QC report

Your saved games, players and settings carry over.
