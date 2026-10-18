**Mind It! v1.69 · Build 138** · 18 October 2026

## New — one go per team, and the board comes back by itself
- **Each team gets one go per question**, in every turn mode including Classic. A wrong answer (with or without penalty) or a pass uses that team's go.
  - A team that has had its go can't get the same question again: not through Pass, Make Active, the host override, a remote or a key.
  - This used to be possible, mainly from the Galaxy Tab / iPad / iPhone remote: it kept showing Correct, Wrong and Pass after every team had had a go, so a question could go round again and again.
- **Passes and wrong answers go to the next team in the usual order that still has its go.**
- **When every team has had its go, the question ends by itself.**
  - The answer appears on the laptop and the TV, with **NO ONE ANSWERED** below it.
  - **7 seconds later** the board comes back, with the next team in the turn order highlighted (Classic: the same team picks, as before).
  - The question is marked as played. No points are given; points already taken off stay.
- **No One Answered** closes a question before every team has had a go. It asks first; on the tablet and phone remote, they ask.
- **Back to the board by itself after every decided question.** After a correct answer, a Daily Double or Triple Gamble, or No One Answered:
  - the answer stays up for **7 seconds**, then the board comes back with the right team highlighted, and you don't press anything;
  - until now this happened only after a correct answer, after 3½ seconds;
  - the setting is still in Setup → 5 · Audio & Presentation, now called "Back to the board automatically after each answer", with **Stay here** to stop it. No One Answered always returns;
  - **Next Question** before then goes at once, and the countdown is cancelled (no second jump);
  - **Undo** during the 7 seconds cancels it too: undoing the last wrong answer gives that team its go back.
- **Who has had a go** shows on the laptop's Scoring card and on the tablet remote: Answering Now · Passed · Wrong Answer · Not Attempted. When none are left: "All teams have attempted or passed on this question."
- **Phone Buzzer Mode:** Reopen Buzzers reopens only for teams that haven't had their go.
- **Unchanged:**
  - scoring, pass-on bonus, speed bonus, Streak Flames, Returning Champion and manual adjustments;
  - Daily Double and Triple Gamble (no pass; a wrong answer ends them);
  - the Final Round.
  - A **Reveal Answer** you press yourself while teams still have their go doesn't start the 7 seconds.

## Fixed (found in a code check of the whole app)
- **Six buttons now work in the Windows and Mac app.** These did nothing there, because the app can't show the browser's own input box:
  - **+ New Category**, **Move To Category**, **Rename** and **Delete Category** in the Question Database;
  - **⇄**, which moves a question to another round;
  - **✎ Edit Answer** on Mark Each Team.

  They now open a small box of their own: type, then **Enter** or **OK**; **Escape** or **Cancel** leaves things as they were. (The browser version and the Galaxy Tab were fine.)
- **✎ Edit Answer stays.** With team phones connected to the laptop, a corrected Final answer was replaced by the phone's answer within a second. Now the correction stays: the suggestion, the reveal on the TV and the game record use it, and the phone's answer is kept as the original. Saving an empty box now leaves the answer as it was.
- **Accents and emoji in large saves (Windows and Mac app).** A save over 64 KB could turn a letter like é, or an emoji, into "��" where it fell between two pieces of the data. Every character now arrives as typed. Your 10 October backup has no damaged characters.
- **📶 Devices** said "Tablet not connected" even when the tablet was connected. It now shows "● Connected". A phone remote doesn't count as the tablet.
- **Galaxy Tab hosting: Wi-Fi TVs stay connected.** A TV showing 📺 Audience Screen in its browser was disconnected every 15 seconds and reconnected. It now stays connected.
- **Safer with bad data.**
  - The tablet app refuses oversized or malformed messages instead of closing.
  - The laptop app ignores them instead of showing an error box.
  - After 20 wrong remote PINs, that device has to wait 5 minutes.
- **Smaller laptop-app fixes:**
  - only one "isn't responding" box at a time, and it closes by itself when the app answers again;
  - handing the quiz to the tablet stops when you press Cancel;
  - the hand-over goes ahead if the tablet confirms after the 2-minute wait.

## Lighter and faster
- **The "now playing" glow** uses much less computer power. With the Audience View open, the CPU used went from about 60 to 3.5 ms per second in Chrome (about 819 to 224 ms per second for the whole laptop app on the build machine, which has no graphics chip in the laptop app).
  - It looks the same at its calmest and brightest moments.
  - Halfway through, the amber ring fades out, where before it melted into the glow.
  - The before-and-after pictures are in the QC report.
- **Phones, TVs and tablets load the quiz page compressed:** about 1.8 MB instead of 3.6 MB. A reload checks for changes instead of downloading the page again.
- **Fewer file writes:** the laptop and tablet save the trusted-devices list once a minute, not every time a phone remote checks in (twice a second).

## Unchanged
- Everything else about how the game plays: presets, scoring and settings in Classic, Full Show and Online Mode. Only the one-go and 7-second changes above are new.

## Compatibility
- **Data:** nothing is deleted and no IDs change. Games and backups from build 137 open in 138, and the other way round.
- **Galaxy Tab:** installs over build 137 (versionCode 138, original key).
- **Laptop and tablet together:** keep both on the same build, as before.

## Not yet tried for real
- **On a real Galaxy Tab:** the Wi-Fi TV fix and the safety limits were tested with the tablet's server code run on a computer, and the release check opens the app on an Android emulator.
- **On real Windows and Mac machines:** the laptop-app fixes were tested in the laptop app on the build machine (the same app shell, on Linux).

Tests: 134 suites, all 2,953 checks passed (one older check, `fix127d`, on its automatic retry — a 4.5-second reconnection check that passed first time in the earlier run and again 22/22 on its own), on this build's page. New checks: one go per team and the automatic returns, `fix138p` (30/30, the spec's 12 scenarios and more) on the webpage and `fix138pd` (9/9, with a real tablet remote) in the laptop app; the code-check fixes, `fix138` (32/32) on the webpage, `fix138d` (22/22) in the laptop app and `fix138j` (13/13) on the tablet's server code. The tablet app passed `apk_check.py`, and Google's `aapt2` reads it the same. Full details: QC report (attached).
