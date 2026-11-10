**Mind It! v1.69 · Build 180** · 10 November 2026

Fixes from an audit of build 179 (26 items), and the every-fifth-build extras: a new Mac app, refreshed guides, and the stress and 60-minute soak tests.

## Put right from build 179
- **Question history after a sync:** a laptop ⇄ Galaxy Tab sync could save the questions' internal keys wrongly, so "already played" marks and question stats stopped matching after a restart. Keys saved that way are repaired automatically.
- **Questions with accents or symbols** (é, ñ, $, £, +, ×…) match their history, stats and Fix Later flags from older builds again.
- **Mastermind It!:** Start timer after the clock ran out reopens answers on the phones again; closed answers stay closed while you're in Setup; Setup and back keeps the clock.
- **Historic Games:** a correction made while that game's end screen is still showing is kept.
- **Question pictures** are only made smaller when over 3 MB, and then to 2560 px (build 179 shrank them to 800 px).
- **Files can be dropped** onto the "Choose files" boxes in Setup again.
- **Restoring a backup** brings back a game record deleted in Historic Games.
- **While a Resume offer is waiting,** Setup now says its changes aren't saved until you choose Resume or Start fresh.
- **"+ Add Team"** works again in Add Past Game while a game is paused (Setup's own stays locked).
- **Undo of a score adjustment** keeps the turn where it is.

## Also fixed
- **💡 Hint + Phoenix** pays half the Phoenix amount, as the screens say, and its WRONG ANSWER button now shows that a wrong answer costs nothing. **💡 Hint on a Rewind It! question** shows the right amounts.
- **Phone Buzzer Mode:** after a take-over, hand-over or restart mid-question the buzzers work again by themselves; a team that already answered can't buzz again after switching modes; a buzz from another question is never taken.
- **Backup tablet:** keeps its copy while you're in paused Setup; a take-over at Time's up stays at Time's up.
- **Hand-over to the Galaxy Tab:** the laptop's keyboard shortcuts can't score while scoring is paused.
- **Phone Remote:** after the quiz moved to the Galaxy Tab, an unpaired phone goes there to pair; a tap ignored because the screen had changed now says so on the phone.
- **Reset question** while Bottoms Up waits for "Finished / Not finished" works.
- **Laptop app:** guessing the PIN after a hand-over is limited like everywhere else.

## Galaxy Tab and Mind It! TV updates
- The in-app update works exactly as it did in build 177 (build 179's extra check is gone).
- **One-time note:** updating *from* build 179 still runs build 179's update code. If the Galaxy Tab stays on "Handing it to Android…", install build 180 once from this download page; from then on in-app updates work as before.

## Also in this release
- New **Mac app** (build 180), **refreshed guides**, and the stress and 60-minute soak tests were run.
- No rule, score or wager changed except as above. Old saves and backups open as before.
- Not tried on real devices: everything above was checked on the build machine only.

## Updating the Galaxy Tab
Android may warn that the app could be harmful. That is Google Play Protect: it warns about apps installed from outside the Play Store that can update themselves. Tap the small arrow (**More details**), then **Install anyway**. This build asks for no new permissions.
