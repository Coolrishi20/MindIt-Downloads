**Mind It! v1.69 · Build 191** · 20 November 2026

This build moves the laptop app to a newer engine (Electron 45) and makes the automated checks steadier. Making them steadier turned up two real faults on a busy laptop, both fixed: a double-click could count twice, and a restarted laptop could offer a quiz the Galaxy Tab had taken over.

## Fixed in the game
- **A double-click counts once, even on a busy laptop.** When the laptop was slow to redraw the screen, a quick double-click on **WRONG ANSWER** took points off the answering team and then off the next team too. A double-click on **PASS** could skip a team. The app now looks at when you actually pressed, not only when it got round to it. Two presses made more than about a third of a second apart still both count, as before. The same goes for the keyboard shortcuts and every other host button that already ignored a double press.
- **After the Galaxy Tab takes over, a restarted laptop never offers that quiz for Resume.** When the laptop app starts again it asks whether the Galaxy Tab took the quiz over. On a busy or slow laptop, reading the saved quiz could take longer than that check waited, so the check gave up: the laptop could then offer the quiz for Resume while the tablet was running it, and a phone that woke up late wasn't sent to the tablet. The check now runs as soon as the saved quiz has been read, however long that takes.

## Laptop app
- **Electron 45.4.1** (was 44.10.2), with Chromium 156 and the latest security fixes. Nothing in how the app looks or works changes.
- From now on the laptop app moves to each new Electron version in the next build.

## Checks
- Six checks that sometimes failed only because the build machine was busy now wait for the right moment instead of a fixed time. A few others still needed a second try in the full run (all passed); they are next, in build 192.

## Also
- The Galaxy Tab app and Mind It! TV app are build 191. The in-app update works as in build 177.
- The Mac app and the guides are build 190's (the next new Mac app and guides: build 195).
- Nothing was tried on real devices. Everything above was checked on the build machine. The 15-Minute Device Check (in the QC report) is for your own devices.

## Updating the Galaxy Tab
Android may warn that the app could be harmful. That is Google Play Protect: it warns about apps installed from outside the Play Store that can update themselves. Tap the small arrow (**More details**), then **Install anyway**. This build asks for no new permissions.
