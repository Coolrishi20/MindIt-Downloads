**Mind It! v1.69 · Build 188** · 17 November 2026

## Steadier test runs
- Three of the build checks sometimes failed when the full test run kept the machine busy, then passed when run alone. Each had its own cause, and each is fixed:
  - **The TV lobby countdown check** set the start time 10 minutes ahead, rounded to the minute. If the check began in the last seconds of a minute, the countdown could read 08:59 by the time it looked. It now uses 11 minutes and allows for that.
  - **The laptop ⇄ Galaxy Tab hand-back check** expected to see the request "approved". On a busy machine the laptop page sometimes moved straight on to preparing the quiz, which is what it should do, before the check looked. Both steps now count.
  - **The 14-theme check** sometimes ran past its fixed 20-minute limit. Every check's limit is now at least 2½ times its usual time. A check that does run over now says so, instead of giving no result.
- **Found along the way:** on a busy player's phone, a Setup-only helper (the 🎲 fun team names) sometimes looked for the game before the phone had one. That left a note in the app's hidden error list. Nobody saw anything, and it now checks first.

## A release process that won't move under us
- The release workflow (which publishes each build and opens the tablet app on an Android emulator first) now names the Ubuntu version it runs on, 26.04, the one builds 186 and 187 were published on. GitHub can't swap it out without us seeing. Its GitHub tools are on their current versions, which also ends the warning about an old Node.js.
- It was tried before this release: the emulator opened builds 187 and 186 on the updated workflow.

## Also
- Galaxy Tab and Mind It! TV apps are build 188; the in-app update works as in build 177.
- The Mac app and the guides are build 185's (unchanged). The next build with a new Mac app and guides is 190.
- Not tried on real devices: everything above was checked on the build machine only. The 15-Minute Device Check (in the QC report) is for your own devices.

## Updating the Galaxy Tab
Android may warn that the app could be harmful. That is Google Play Protect: it warns about apps installed from outside the Play Store that can update themselves. Tap the small arrow (**More details**), then **Install anyway**. This build asks for no new permissions.
