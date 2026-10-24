**Mind It! v1.69 · Build 152** · 24 October 2026

## New
- **Mind It! TV, an app for the Mi Box (Android TV).** It turns the box into the audience screen:
  - it finds the quiz on the Wi-Fi by itself, whether the laptop or the Galaxy Tab is hosting;
  - it shows the TV picture full-screen and keeps the screen on;
  - it remembers the quiz and reconnects on its own;
  - it's run entirely with the remote, and the game stays on the laptop or tablet.
  
  New download: **Mind-It-Android-TV.apk** (install once from a USB stick or "Send Files to TV"; see the guide in the release). It updates itself: **⬆ App Update** on its start screen, plus a quiet daily check, never while it's showing the quiz.
- **The laptop app updates itself.**
  - Setup → Advanced → **⬆ App Update** (a quiet check about once a day, too).
  - On Windows it downloads the new build beside the current one, checks the file is genuine, then **Restart into build N**. Never during a game.
  - On a Mac it opens the download page.
- **The Galaxy Tab's update no longer goes through the browser** (the download used to stop at 2.65 MB / 2.65 MB). Mind It! downloads the update itself, checks it's genuine and signed with your key, then shows Android's install screen. The first time, Android asks you to allow Mind It! to install apps.
- **⬇ Excel ▾ in the Question Database's top row:**
  - the Quiz Template;
  - the Mastermind It! Template;
  - the whole Question Database (edit it in Excel and ⬆ Import it back).
  
  More ▾ now shows how many 🔁 Duplicates it has found.

## Better
- **Host controls:**
  - **"Are you sure?" boxes start on Cancel.** A stray Space or Enter after E or U can no longer end the round or undo a score.
  - **End round early is now Shift+E**; E alone does nothing.
  - **T after a pause resumes** from the seconds left (it used to restart from full).
  - **One set of timer words:** Pause, Resume, End.
  - **Mastermind It! results:** "Mark each team" comes first.
  - **The Timer card** sits under the TV preview on the laptop and the tablet in landscape.
  - **The reset buttons** are in their own "Danger zone" row, away from Undo.
  - **The Rewind It! and Mastermind It! panels** are about half as tall.
  - **⌨ Keyboard Shortcuts** in ⋯, or press **?**.
  - **Click a team's score** to adjust it.
  - **The top bar's text is larger.**
- **The Galaxy Tab hosting in portrait:** the TV preview folds away behind "📺 Show TV preview", so the clue picker and teams come first.
- **A phone used as the remote:** the board's category names are readable (10–12 px, were 9) and no word is cut in two.
- **Layout:**
  - the Undo pop-up after a score is centred again (it sat to the right, and off the edge on a portrait tablet);
  - the CORRECT / WRONG buttons show the amount the same way;
  - on wide screens, Undo & resets moves under the TV preview on the wager screens (about a third less scrolling);
  - the host panel's small print is at least 14 px;
  - notices on a portrait tablet no longer cover the top bar's buttons;
  - after a Resume, the timer ring carries on from where it paused instead of jumping back to full.
- **The guides** describe this build's changes (Shift+E, Resume, the Excel menu, the updates, Mind It! TV).

## Unchanged
- **Rules, timers, wagers, scores, saved games and connections.** **Version:** still v1.69.

## Compatibility
- **Data:** the same saved data and backup files as build 151.
- **Galaxy Tab:** installs over build 151 (versionCode 152, original key). Because the browser problem is fixed inside this build, install 152 by hand once (open the APK from Downloads); later updates are one tap.
- **Windows:** replace the EXE by hand this once; build 152 and later update themselves.
- **Mi Box S:** needs "Android System WebView" 105 or newer (update it in Google Play on the box if the app shows a red notice).

## Checks
The full programme, all on the final files:
- **179 test suites, 4,221 checks: all passed** (109 in the browser, 2,931; 70 on the laptop app, 1,290).
  - New suites for this build: the Question Database menu and tablet and phone layout (fix152 29), host controls (fix152h 39), the layout pass (fix152l 49), Mind It! TV (fix152tv 26), the tablet's in-app update (fix152tab 47) and the laptop's self-update (fix152u 21).
  - The first full run found four older suites that didn't match this build. Three were tests looking for things that moved on purpose. One was a small real layout slip: Correct grew to three lines with the speed bonus on. It's fixed, and the whole programme was run again from the start.
- **The Audience View audit:** all 306 TV screens clean.
- **Stress, all six phases:** 24/24.
- **The 60-minute soak:** 11/11. Two whole games with 8 teams, Final wagers from the phones, a sudden-death tiebreaker from the tablet, Night Recap on the TV, 59 questions, 10 phones, no false disconnects.
- **The files:** the Windows joiner test passed 4/4. The EXE carries the same page, laptop app and tablet app. Both Android apps are signed with your original key.

## Not yet tried for real
- Tested in the sandbox only. The Mi Box app, the tablet's and the laptop's self-updates, and the new host controls have not been tried on your real Mi Box S, Galaxy Tab, Windows PC, phones or TV. In particular: the Android install screens, Windows SmartScreen or antivirus on a freshly downloaded EXE, and the Mi Box finding the quiz on your Wi-Fi.
