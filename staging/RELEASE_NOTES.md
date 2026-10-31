**Mind It! v1.69 · Build 163** · 30 October 2026

The TV no longer goes blank for a moment during a question. Nothing else changes.

## The TV picture
Until now, on every TV, in every question:
- the question disappeared about 2.3 seconds after it opened, and came back about half a second later;
- after ✓ Correct, the TV was empty for about 1.7 seconds;
- after going back to the board, the whole board disappeared for about 1.5 seconds.

The Audience View window on the laptop never had this; only the TVs (the Mind It! TV app, or a TV's browser) did. It started with the theme moments in build 150.

What happened: when a question opens, the TV plays the theme's moment itself, with layers in front of and behind the question. Each layer removes itself when the moment ends. When the laptop took its own copies of those layers away, the TV mixed one of its layers up with the question, and when that layer removed itself, the question went with it. Now a layer is only ever matched with a layer.

- The theme moments still play on the TV as before.
- Only how the TV draws changed: no change to timers, scores, turns, saves or phones.
- The fix is in the page the laptop (or the Galaxy Tab) gives your TVs. A TV picks it up the next time it loads that page: after updating the laptop app, press ↻ Refresh All Screens in 📺 Connect Audience Screen (or restart the TV app). The Mind It! TV app is rebuilt as build 163 too, with no change of its own.

## Tests
- A new test plays questions, correct answers and returns to the board on the laptop app, with one TV in today's Chrome and one in the older engine the Mind It! TV app supports. Each TV checks itself every 25 milliseconds. On build 162 it finds the blank moments every time; on build 163 there are none.
- One test sometimes opened a Daily Double square by chance (they are placed at random) where it expected a question. It now clears them first. The app is unchanged.

## Downloads
- Windows (Mind-It-Windows.exe)
- Galaxy Tab (Mind-It-Android-Galaxy-Tab.apk)
- Mind It! TV for the Mi Box (Mind-It-Android-TV.apk)
- The web page (mindit.html)
- The five guides (as in build 160)
- The QC report

There is no Mac app in this build: the Mac stays on build 160 until 165. Your saved games, players and settings carry over.
