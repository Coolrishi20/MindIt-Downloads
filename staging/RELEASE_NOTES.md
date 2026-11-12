**Mind It! v1.69 · Build 183** · 12 November 2026

## Galaxy Tab: player profiles survive a damaged save file
- If the Galaxy Tab switches off in the middle of saving the player file, the cut-short file is now skipped and its backup copy is read instead. Build 182 passed the damaged file to the quiz page, which could not read it.
- If the backup copy is missing too, but build 182's small save (the profiles without photos) is there, the tablet now opens **all your players, their stats and games** from it, just without their photos, instead of none at all. The next save writes a new, whole player file. The tablet remembers which photo belongs to which player, so the laptop keeps every photo and the next **⟳ Sync devices** puts them back on the tablet.
- When the file is fine, or when nothing whole is left, the tablet behaves exactly as in build 182.

## Also in this release
- Quicker, clearer test runs before each release: a check that fails only because four test groups ran at once is now run again on its own automatically and reported as "passed when re-run alone". The two laptop-app checks for the tablet app inside the laptop app now pass in the first run.
- Galaxy Tab and Mind It! TV apps are build 183; the in-app update works as in build 177.
- The Mac app and the guides are build 180's (unchanged). The next build with a new Mac app and guides is 185.
- Not tried on real devices: everything above was checked on the build machine only. The 15-Minute Device Check (in the QC report) is for your own devices.

## Updating the Galaxy Tab
Android may warn that the app could be harmful. That is Google Play Protect: it warns about apps installed from outside the Play Store that can update themselves. Tap the small arrow (**More details**), then **Install anyway**. This build asks for no new permissions.
