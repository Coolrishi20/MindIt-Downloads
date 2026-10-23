**Mind It! v1.69 · Build 150** · 23 October 2026

## New
- **The game sounds like the trailer.** Every moment now uses the same sound, at the same balance, as your 45-second trailer's cue sheet:
  - a **right answer** rings the ding, then the score “pops” a moment later;
  - a phone's **BUZZ IN** plays the trailer's buzz (before: two beeps);
  - a **whoosh** carries the TV to a new board, the round summary, the standings, the recap, the awards and the match-up (never into or back from a question);
  - the **standings** tick as the leaderboard moves;
  - the **winner** lands with the big impact, then the crowd cheers;
  - changing the **theme** gives a short sparkle;
  - Blind It!, Mastermind It! and the sudden-death tiebreaker keep the impact; Triple Gamble, Phoenix and Bottoms Up keep their sounds.
  
  The sounds also sit at the trailer's levels now, so none of them is louder than it should be against the others. A theme with its own sounds keeps them (Theme Sounds On).
- **The guides are up to date** (all five): the new names (Blind It!, Mastermind It!, Never Mind It!), **Rewind It!** with its payout table, **The Rascala!**, the tagline, the tablet's own **App Update**, the sound pack and this build's sounds, with new pictures from build 150. The Complete Idiot's Guide is now 183 pages; the Quick Start, cheat sheet, checklist and players' guide keep their length. The worked example in Chapters 16–17 keeps its pictures from a real game played before build 148 (it says so), and the tablet and phone pictures of the wagers are still the older ones.

## Better
- The Mac app is back in the release (build 150, Apple Silicon): it has everything since build 147.

## Unchanged
- **Rules, timers, wagers, scores, saved games and connections.** **Version:** still v1.69.

## Compatibility
- **Data:** the same saved data and backup files as build 149.
- **Galaxy Tab:** installs over build 149 (versionCode 150, original key). The tablet's own **App Update** (Settings) can install this build.

## Checks
The full set, as every 5th build — all on the final files:
- **162 test suites, 3,792 checks** passed (95 in the browser, 67 on the laptop app; the new sound suite fix150 37/37). Two laptop-app suites first needed attention; both were test measurements, not the app (details in the QC report), and pass 44/44 after the fix.
- **The Audience View audit:** all 306 TV screens clean.
- **A slow TV:** smooth on the default theme (29–72 frames a second) and on Comic Book (23–42), no stall longer than a third of a second.
- **Stress — all six phases** 24/24 (idle, network, load, lock, rapid taps, health check) and the **60-minute soak** 14/14 (3 whole games, a tiebreaker, 10 phones, no false disconnects).
- The Windows joiner test 4/4; the Mac app carries the same page and tablet app.
- The **QC report** for builds 149 and 150 is in this release.

## Not yet tried for real
- Tested in the sandbox only (browsers and the laptop app under Linux; the tablet app on GitHub's Android emulator; the Mac app was built and signed here but not opened on a Mac). Nothing was run on your real Windows PC, Mac, Galaxy Tab, phones or TVs; the sounds were checked for playing, timing and level, not listened to.
