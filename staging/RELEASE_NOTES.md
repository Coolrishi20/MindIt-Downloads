**Mind It! v1.69 · Build 187** · 16 November 2026

## A permanent check of the team cards
- Every build is now tested on the score cards that sit beside the board during play. The check plays every team count from 2 to 12 on the TV, the laptop and the Galaxy Tab. It uses long and short team names and the busiest cards possible: the last-place team playing while also the returning 👑 champion and on a 🔥 streak. It measures every part of every card (picture, name, score, place, the Now Playing band, the cat, 👑 and 🔥) and fails if anything leaves its card or covers another part. It covers all 14 themes too.
- Run on build 186, it found the faults below. All are fixed in this build.

## Team cards, fixed
- **A team on a 🔥 streak:** with 8 or more teams, the Rascala! cat jumped outside the card and the team's name was squeezed onto its score. With fewer teams the cat dropped to the bottom of the card. The cat now stays in its place on every card.
- **A team on a 🔥 streak that isn't playing:** the "🔥 On Fire" badge covered the team's place ("3rd"). The cat, 👑 and 🔥 now sit together in a small row at the card's top-left, so the place stays visible. When more than one is there they are short ("👑 ×3", "🔥 6"), as they already are with 8 or more teams.
- **The last-place team playing while champion and on a streak (2–4 teams):** "Now Playing" broke over two lines under the cat. The cat is now the first thing in the band and everything fits on one line.
- **The Gaming Theme, 8–12 teams:** its wider place pill touched the cat. The cat now keeps clear of the pill in every theme.
- Which team gets the cat, the crown or the flames is unchanged.

## Also in this release
- The rules that place the Rascala! cat are now written once, in one place, instead of across three builds. A lone cat on a card is where it was, except with 10 or 12 teams on the laptop: about 1 pixel further left, where the "10th" pill needed the room.
- Behind the scenes, the test run now checks its own test servers before it starts, and no longer rewrites its timing file every time.
- Galaxy Tab and Mind It! TV apps are build 187; the in-app update works as in build 177.
- The Mac app and the guides are build 185's (unchanged). The next build with a new Mac app and guides is 190.
- Not tried on real devices: everything above was checked on the build machine only. The 15-Minute Device Check (in the QC report) is for your own devices.

## Updating the Galaxy Tab
Android may warn that the app could be harmful. That is Google Play Protect: it warns about apps installed from outside the Play Store that can update themselves. Tap the small arrow (**More details**), then **Install anyway**. This build asks for no new permissions.
