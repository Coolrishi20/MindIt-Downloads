**Mind It! v1.69 · Build 162** · 30 October 2026

Setup and the Question Database are quicker on the Galaxy Tab. Nothing you see on them has changed.

## Setup on the Galaxy Tab
I tested on a tablet-sized screen slowed down to tablet speed, with a library the size of yours.

- Redrawing all seven Setup tabs once each takes 3.8 s in total (build 161: 6.3 s). For example, Quick Setup takes 0.36 s (was 0.73 s) and Gameplay & Rules 0.42 s (was 0.93 s).
- Setup still builds every tab but leaves out the work for the tabs you can't see:
  - each button's line icon is put in once (one redraw used to do the same 584 buttons 3,091 times);
  - the question editor is drawn only on Rounds & Questions;
  - Player Management is drawn only on Teams;
  - the phone-remote QR code is worked out once per address.
- Each tab looks exactly as in build 161, on laptop, tablet and phone screens.
- A correction to build 161's notes: Setup took 0.6–1.3 s per redraw on the tablet (depending on the tab), not 1.5 s. The 1.5 s was measured with a test setting that shows all seven tabs at once.

## Question Database
- All Questions opens in about 1.7 s on the tablet (build 161: about 4.8 s).
- The list shows its first 100 questions at once. The next 50 appear as you scroll near the end, usually before you reach them.
- The same applies to a large category, Recently Added and search results. Lists of 100 or fewer are unchanged.
- Select All Available still selects the whole list. Scrolled to the end, the list is the same as in build 161.
- With a keyboard, pressing Tab through the list shows the next 50 as you reach the end of what's shown.
- One difference: the browser's own Find (Ctrl+F) only finds questions already shown. The Question Database's search box searches them all, as before.

## Checked before release
- A code review found no serious problems. Three small points were fixed: the list stops watching your scrolling once it's closed; the keyboard can reach every question (above); and if Setup ever fails to sort its cards into tabs, the question editor and Player Management are still drawn.
- A layout review compared every Setup tab, the Question Database and the game board with build 161 on laptop, tablet (both ways round) and phone screens: they're the same, pixel for pixel.

## Tests
- Some tests waited a fixed time for something to happen and sometimes failed when the computer was busy. They now wait for the event itself. One of them could accept the previous quiz's save as the current one.
- The phone tests now wait until the laptop has the new teams before the phones join.
- Two tests were wrong in rare cases: one expected the question screen when the cell it opened was a wager cell, and one checked a Setup card that redraws itself every 3 seconds in between. Both now allow for it. The app is unchanged.

## Downloads
- Windows (Mind-It-Windows.exe)
- Galaxy Tab (Mind-It-Android-Galaxy-Tab.apk)
- Mind It! TV for the Mi Box (Mind-It-Android-TV.apk)
- The web page (mindit.html)
- The five guides (as in build 160)
- The QC report

There is no Mac app in this build: the Mac stays on build 160 until 165. Your saved games, players and settings carry over.
