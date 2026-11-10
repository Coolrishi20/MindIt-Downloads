**Mind It! v1.69 · Build 179** · 10 November 2026

Fixes from a full audit of everything older than build 176: scores, turns, saves, syncing between devices, the laptop app and the Android apps.

## Scores and turns
- **A score changed on the final standings** (Adjust score, Undo) now also changes the saved game in Historic Games, player stats and the winner.
- **Phone Buzzer Mode:** a team that buzzes just before the clock runs out keeps its turn for your verdict (it used to be passed, and CORRECT / WRONG ANSWER then scored the next team). If nobody buzzes, nothing is passed: Reopen Buzzers or No One Answered, as you choose.
- **Holding a key** (W, S, X, Space…) counts once. It used to mark every team in turn.
- **Phone Remote:** a second tap made before the phone has caught up is ignored instead of hitting the next team.
- **Undo after a question has closed** corrects the score without handing the turn back to the wrong team.
- **Setup and back** during a question: the clock carries on from where it was. In Mastermind It!, answers that closed when time ran out stay closed (also after a restart).
- **Reset question** gives Phoenix, Bottoms Up and Triple Gamble back, as Undo does.
- **🏹 Robin Hood's gift** no longer counts as a correct answer in tie-breaks. A double-click on WRONG ANSWER no longer adds a second wrong answer to the night's facts.
- **A phone wager** that arrives as you close wagers counts, instead of the minimum.
- **A new Mastermind It! question** (Rematch, Random from the Question Database) no longer keeps the old one's choices, picture, note or accepted answers.

## Saves and syncing
- **A big unfinished game** (photos, music) is no longer lost if the app restarts twice before you press Resume.
- **A damaged game file** is repaired as it loads instead of leaving a blank page.
- **Laptop ⇄ Galaxy Tab sync:** merging the same duplicate player on both devices no longer deletes the player; questions with the same wording but different answers, and questions in other scripts (Arabic, Hindi…) or with symbols (7 × 8, 7 + 8), are no longer merged away.
- **Loading an older backup** keeps corrections made later in Historic Games.
- **A crash during a Rehearsal**, then Start fresh: the quiz you prepared comes back.
- **When nothing can be saved** (storage full), the app says so instead of "Autosaved".
- Lowering **Categories / Clues per category** asks before removing questions. **+ Add Team** is locked while a game is paused. Question pictures: iPhone (HEIC) photos are converted, very large pictures made smaller, other files refused. A question with the word "constructor" no longer hides the Duplicates tab.

## Laptop app, Galaxy Tab and Mind It! TV
- The laptop app can't be stopped by a bad message from another device on the Wi-Fi, or by a Wi-Fi drop. A file dropped outside a drop zone can't replace the quiz page. Phones show "The quiz is moving…" again during a hand-back to the Galaxy Tab. Electron updated to 44.10.2.
- After a hand-over, only paired devices get the pass that skips the PIN. A take-over request from a device that isn't paired is marked on your screen.
- **Galaxy Tab:** only the app's own pages can use its saved games; attaching a keyboard cover or clicker no longer reloads the quiz; Back on the quiz page asks for a second press; one device can no longer overload the tablet's server.
- **Mind It! TV** only follows another address when the quiz it shows has stopped answering.

## Also in this release
- No rule, score or wager changed except as above. Old saves and backups open as before.
- The Mac app (build 175), the guides (build 175) and the Quiz Night Run-Sheet (build 177) are unchanged.
- Not tried on real devices: everything above was checked on the build machine only.

## Updating the Galaxy Tab
Android may warn that the app could be harmful. That is Google Play Protect: it warns about apps installed from outside the Play Store that can update themselves. Tap the small arrow (**More details**), then **Install anyway**. This build asks for no new permissions.
