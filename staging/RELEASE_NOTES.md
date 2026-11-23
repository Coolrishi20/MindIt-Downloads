**Mind It! v1.69 · Build 192** · 23 November 2026

This build makes the laptop app use less memory, so Mind It! sits more comfortably next to another app on the same laptop. Nothing on screen changes.

## Less memory
- **The app's own code is stored more compactly.** The app's code contains a few thousand emoji and symbols (✓, ●, ▾ …). Because of them, the browser inside the laptop app kept the whole 4 MB of code and the whole stylesheet at two bytes per letter, in the Quizmaster window, again in the Audience window, and in the laptop app's own copy. Those characters are now written as short codes that mean the same thing, so everything is kept at one byte per letter. The same characters show on screen as before. The Galaxy Tab and TV apps load the same page, so they get the same saving.
- **A save no longer leaves full copies of your library in memory.** After each save the app kept its last complete text of the Player Profiles (twice: with and without photos), and every photo's text twice between saves. It now keeps only what the next save needs. Saving is as quick as before, and the saved file is exactly the same.
- **A save no longer briefly doubles the laptop app's memory.** With a big library, each save used to read the whole old file back in before writing the new one. It now skips that when the file is the one it wrote last.

## How much
Measured inside the laptop app with the TV, the Galaxy Tab and 10 phones connected, and a big library (5,000 questions, 50 players, 100 past games):

| Moment | Build 191 | Build 192 |
|---|---|---|
| Setup screen, library loaded | about 539 MB | about 513 MB |
| Mid-game | about 572 MB | about 557 MB |
| Peak while saving a 3.5 MB library | 189 MB | 148 MB (the app's main process) |

That's a modest saving of about 3–5% of the total, more with a big library or many photos. An empty window of the laptop app's engine (Electron) already takes about 290 MB on its own, whatever Mind It! does. If you need much more room for the other app, hosting from the Galaxy Tab takes Mind It! off the laptop almost entirely.

## Checks
- A new check (fix192, 11 checks) covers all of the above. It passes 11 of 11 on build 192 and 6 of 11 on build 191.
- The full test run (249 suites, both laptop-app groups included) passed 6,223 of 6,228 checks. The ten suites that needed a look all pass when run alone, some after a small change to the check itself.
- The build machine was rebuilt since build 191, with a newer test browser. Five older checks needed a small change to work with it or with the page's new compact text. These were test changes, not app changes.

## Also
- The Galaxy Tab app and Mind It! TV app are build 192. The in-app update works as in build 177.
- The laptop app stays on Electron 45.4.1, which is still the newest version.
- The Mac app and the guides are build 190's (the next new Mac app and guides: build 195).
- Nothing was tried on real devices. Everything above was checked on the build machine, which draws in software, so the memory figures on your Windows laptop will differ. The 15-Minute Device Check (in the QC report) is for your own devices.

## Updating the Galaxy Tab
Android may warn that the app could be harmful. That is Google Play Protect: it warns about apps installed from outside the Play Store that can update themselves. Tap the small arrow (**More details**), then **Install anyway**. This build asks for no new permissions.
