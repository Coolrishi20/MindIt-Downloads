**Mind It! v1.69 · Build 151** · 24 October 2026

## New
- **Rewind It! from the team's phone.** In Buzzer Mode the team that gets Rewind It! spins the cowboy-hat wheel on its own phone and taps STOP; the TV shows "spin it on your phone" / "tap STOP!". In every other mode the Quizmaster keeps the wheel (the laptop can still spin or stop for the team).
- **The Galaxy Tab looks premium** ("Studio Glass": deep navy, soft gold light, glass cards, pill buttons) and works better in portrait:
  - Rewind It!: 🤠 Spin The Wheel, then Show The Question, is the big button (it used to offer Correct / Wrong first), and the remote says REWIND IT! (it said BLIND IT!);
  - the winner gets a card with The Rascala!, Champions Card and Continue;
  - the pinned buttons never cover the scores; each team's wager is one row with big boxes; Correct / Wrong in Mastermind It! are big;
  - the home screen puts Start New Game and Connect To Laptop side by side near the top; all text is at least 14 px.
- **The trailer's own takes** for the right answer, buzz, pass, score pop, Triple Gamble, Phoenix and the crowd cheer.

## Better
- **The UI/UX audit, all 13 changes:**
  - Rewind It!'s payout reads as a gain or a loss at a glance (green +, red −);
  - the question card no longer repeats REWIND IT! / BLIND IT! six times;
  - Blind It!'s wager key and QR caption are easier to read on bright themes;
  - a team that can't wager on Mastermind It! says why;
  - one Spin button on the laptop;
  - the winner's "What's next" has four clear tiles;
  - "Lock wager & show question" sits at the top;
  - the tablet's update card says which build;
  - notices no longer cover open dialogs;
  - lighter Special Question icons;
  - "The Rascala! — team name";
  - the tablet's Settings sheet clears Android's buttons.
- **Animations:**
  - the winner's confetti falls again (a theme's own animation had hidden it);
  - the phone's BUZZ IN gently glows when it's live;
  - a small dotted "thinking" orb beside long waits (phones connecting, "Waiting for the next question…", the tablet's link, the TV's start screen, sealed wagers), never beside a failure;
  - the wager screens' glows are lighter on slow TVs and phones.
  
  Nothing moves with Reduce Motion or Motion Off.
- **Wi-Fi TVs on a slow link no longer drop out while a big picture is loading.** Before, a TV still downloading a picture question could miss the laptop's check-in, be closed, reconnect, get the whole picture again and repeat: "Reconnecting to the Quizmaster…" on a working Wi-Fi. Fixed on the laptop and on the tablet.
- **Team codes are always on** (an Excel template that said "No" only hid them from your Phones card while the phones still had to type them).
- **Wrong PINs and team codes:** each lockout from the same device doubles (5, 10, 20, 40, then 60 minutes).
- **Setup is lighter:** the twelve live theme samples only move while you can see them.
- The score-adjustment pop-up appears centred again.
- With Reduce Motion or Motion Off, the Rewind It! wheel stands still while it waits for the phone.
- **The guides:** the Complete Idiot's Guide (185 pages) and the Quick Start are updated to build 151, with new pictures of the tablet and phone wager screens; the other three keep their content. The features one-pager and the mobile players' guide use the new names.
- A code clean-up: unused code removed (the page is 12 KB smaller); nothing you use changed.

## Unchanged
- **Rules, timers, wagers, scores, saved games and connections.** **Version:** still v1.69.

## Compatibility
- **Data:** the same saved data and backup files as build 150.
- **Galaxy Tab:** installs over build 150 (versionCode 151, original key). The tablet's own **App Update** (Settings) can install this build.

## Checks
The full programme, all on the final files:
- **173 test suites, 4,019 checks — all passed** (104 in the browser, 2,750; 69 on the laptop app, 1,269). New suites for this build: the phone's Rewind It! wheel (fix151, fix151j, fix151d), the audit changes (fix151u 33), the Galaxy Tab (fix151t 50), the animations (fix151a 32), the scoring rules over whole ranges (fix151p 12), the PIN lockouts (fix151s 9) and the code audit (fix151c, fix151cd, fix151cj).
- **The Audience View audit:** all 306 TV screens clean.
- **Stress — all six phases** 24/24 (idle, network, load, lock, rapid taps, health check) and the **60-minute soak** 14/14 (3 whole games with 8 teams, Final wagers from the phones, a sudden-death tiebreaker from the tablet, 66 questions, 10 phones, no false disconnects).
- The Windows joiner test 4/4; the EXE carries the same page, laptop app and tablet app.

## Not yet tried for real
- Tested in the sandbox only (browsers and the laptop app under Linux; the tablet app on GitHub's Android emulator). Nothing was run on your real Windows PC, Galaxy Tab, phones or TVs; the new look on the tablet, the phone's wheel and the animations need a look on the real devices. The sounds were checked for playing, timing and level, not listened to.
