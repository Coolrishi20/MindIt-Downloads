**Mind It! v1.69 · Build 153** · 26 October 2026

## New
- **Mind It! TV connects even when the Wi-Fi hides the quiz.** Some routers stop the Mi Box from finding the laptop or tablet by itself. Mind It! TV now has two fallbacks:
  - it searches its own network for the quiz;
  - it shows a **4-digit code**: on the laptop or the Galaxy Tab, open 📺 Connect Audience Screen → **Add a TV** and type the code. After 5 wrong tries the TV shows a new code.
- **Mind It! TV updates from the laptop.** The laptop app carries the TV app of the same build. Mind It! TV takes the newer of the laptop's copy and GitHub's (the laptop's when the box is offline). It still installs only when you press ⬆ App Update, after the usual checks that the file is genuine and signed with your key.
- **A new Mind It! TV start screen** in the studio look: large quiz cards you pick with the remote, the pairing code, and App Update with a progress bar.
- **📹 Video Call (Teams, Zoom, Meet)** replaces Teams Presentation Mode (same switch, same saved setting). It also:
  - sizes the Audience View window to 16:9 for sharing;
  - keeps the laptop's own picture calm (no confetti, particles or rays; loops play once) with the question and answer about 12 % bigger;
  - shows sharing steps for Teams, Zoom and Google Meet.

  Wi-Fi TVs and Mind It! TV keep the normal full picture.
- **Online Mode picks the graphics for you:**
  - it turns on Video Call and sets Motion to **Subtle** on this laptop;
  - a notice says what changed, with **Keep Full motion** and **Keep Phone Buzzer**;
  - leaving Online Mode puts your old Motion setting back.
- **Up to 10 teams** (was 8): Quick Setup, + Add Team, Random Teams, Add Past Game and Excel team lists. 9 and 10 teams get a compact side score column on the TV.
- **🏁 End Quiz on the laptop** on the final standings, awards and winner screens. It asks first (Cancel is the default), records the game once, then goes back to Setup.
- **Podium finishes instead of win %** on the player page, Team Settings, both leaderboards and the player editor. The Excel export keeps both columns.

## Better
- **Speed on the laptop**, after your 8-team game with the Audience View window and a Teams call:
  - while the Audience View window is open, the Quizmaster page doesn't draw its TV preview twice. A card says "Showing in the Audience View window", and the preview comes back when the window closes;
  - the timer ring moves with one smooth animation instead of restarting ten times a second;
  - Wi-Fi TVs get a new picture at most twice a second when only the timer changed.

  Measured in the sandbox: a timed question is about 40 % less work, and the slowest moments (Blind It!, the winner) run up to about 60 % smoother.
- **End screens are never cut off:** Achievements, Game Highlights and Fun Stats fit every team, and the Night Recap lists every team (it stopped at 8).
- **The tablet remote in portrait** shows the answer under the question, as in landscape.
- **Setup:**
  - the side rail shows each section's name (it was icons only, a guess on the tablet);
  - Quick Setup has an **Answering** step (out loud or 📱 Phone Buzzers);
  - a jump row on Rounds & Questions (the Mastermind It! question is one tap away);
  - Advanced game rules move to Gameplay & Rules as "More Rules", with one export button;
  - text is at least 14 px, and touch buttons are 48 px on the tablet;
  - "Host: — (optional)" no longer reads like an error.
- **A more premium look:** the laptop host's cards, top bar and TV preview frame; the phones' keys and cards; the TV's score cards and podium; the tablet's home tiles. Buttons press gently (not with Reduce Motion or Motion Off).
- **Layout:**
  - Historic Games' podiums show the team pictures and fit a phone;
  - a past game's page marks 1st, 2nd and 3rd in gold, silver and bronze;
  - Player Profiles have bigger photos, and the leaderboard marks its top three and reads well on a phone;
  - the Question Database's top row and the Add / Edit Question form fit better, with Save always in view;
  - the saved pictures (Champions card, standings, Night Recap) keep every team's players at 9 and 10 teams. The Champions card adds 2nd and 3rd;
  - the page fits the iPhone and iPad screen edges.

## Unchanged
- **Rules, timers, wagers, scores, saved games and connections.** **Version:** still v1.69.

## Compatibility
- **Data:** the same saved data and backup files as build 152.
- **Galaxy Tab:** installs over build 152 (versionCode 153, original key). If the tablet has build 152, its App Update can install this build. On an older build, install it by hand once.
- **Windows:** build 152 can update itself (Setup → Advanced → ⬆ App Update). On an older build, replace the EXE by hand once.
- **Mi Box S:** Mind It! TV 152 updates itself with ⬆ App Update. It needs "Android System WebView" 105 or newer.

## Checks
The full programme, all on the final files:
- **189 test suites, 4,625 checks: all passed** (117 in the browser, 3,304; 72 on the laptop app, 1,321).
  - New suites for this build: Mind It! TV's network search and pairing (fix153 20, fix153tv 33, fix153j 14, fix153d 10), Video Call (fix153v 21), the premium pass (fix153p 91, fix153c 34), speed, Online Mode, podiums and End Quiz (fix153z 63), the layout upgrades (fix153l 90) and the TV updating from the laptop (fix153u 21).
  - The full run found three older laptop-app suites that didn't match this build. All three were tests, not the app: one counted Quick Setup's steps (Answering is new), and two read the laptop's TV preview while Online Mode had the Audience View window open (the preview now rests then, on purpose). Each was updated and run again (31/31). The app didn't change, so the rest wasn't re-run.
- **The Audience View audit:** all 405 TV screens clean, now including 8, 9 and 10 teams, with and without Video Call.
- **Stress, all six phases:** 24/24.
- **The 60-minute soak:** 14/14. Three whole games with 8 teams, Final wagers from the phones, a tiebreaker from the tablet, 67 questions, 10 phones, no false disconnects.
- **The files:** the Windows joiner test passed 4/4. The EXE carries the same page, laptop app, tablet app and TV app. Both Android apps are signed with your original key.

## Not yet tried for real
- Tested in the sandbox only. Nothing was run on your real Mi Box S, Galaxy Tab, Windows PC, phones or TV. In particular:
  - the Mi Box's network search and pairing code on your Wi-Fi;
  - the Mi Box updating from the laptop;
  - a real Teams, Zoom or Meet share with Online Mode;
  - the speed gains on your laptop during a call (the numbers come from a slowed-down browser, not from Teams).
- The new Mind It! TV start screen was checked as code and as mock-up pictures, not on a TV.
