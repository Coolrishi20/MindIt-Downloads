**Mind It! v1.69 · Build 137** · 18 October 2026

## New — Online Mode for Teams calls
- **Teams Presentation Mode switches on with Online Mode.** Picking Online Mode (Setup → 3 · Gameplay & Rules, or Quick Setup step 3) also opens the Audience View window and its **Presentation Check**: share that window in Teams with **Include computer sound** on. If you pick it during a game, this happens once you tap **Apply**. (Not in the Galaxy Tab app: it has no second window, so Teams calls are hosted from the laptop.)
- **How to Play on the TV explains a call:** "Unmute and answer out loud on the call before the timer runs out", and for the Final Round "Everyone sends a wager, then their answer, to the Quizmaster in a private chat message". This fixes build 136, whose Final Round card still said "answers on their phone".
- **Final Round answers by private chat:**
  - the TV's Final question says **📩 Send your answer to the Quizmaster in a private chat message**;
  - when the time is up, the **Mark Each Team** card has a box for each team: type the answer they sent and press **Enter** (or Save), and the cursor moves to the next team;
  - each answer gets the usual suggestion (Likely Correct / Review / Likely Incorrect); you still decide;
  - the reveal on the TV shows the answer they sent, then Correct or Wrong, and the game record keeps it;
  - changing an answer after you marked it clears the mark, so you mark it again.
- **Wagers from the chat:**
  - **All in · Half · 0** next to each team's wager box; on a Daily Double, **Half** joins Minimum and Maximum;
  - in Online Mode the phone-only parts are gone: the sealed-code boxes, the wager key, the private booth button and "phones connected";
  - the cursor starts in the first amount box. This fixes build 136's webpage version, where it started in a sealed-code box.
- **📋 Copy picture for the chat** at the end of the game, next to Save picture. The results picture goes on the clipboard: click the Teams message box and press **Ctrl+V** (⌘V on a Mac). If the browser or tablet can't copy, the picture is saved as a file instead.
- **Speed Bonus window: 15 seconds in Online Mode** (10 in Classic and Full Show), because an answer takes a moment longer to reach you on a call. You can still change it (Answer Within (Seconds)). Picking another preset puts 10 back, unless you changed it yourself.
- **Unchanged:** Classic and Full Show, and every Online Mode switch from build 136.

## Releases
- **The tablet app is now opened on an Android emulator before a release is published.** The release workflow installs the APK on Android 15, taps its icon, and checks 20 seconds later that the app is open and hasn't crashed. If it isn't, nothing is published.
  - Tried on the published apps: build 134's closes at once, as it did on your tablet; build 136's opens.
  - When the app opens, the line "Opened before publishing" is added at the end of these notes.

## Compatibility
- **Data:** nothing is deleted, and no IDs change. Answers typed from the chat are saved with the game.
- **Galaxy Tab:** installs over build 136 (versionCode 137, original key).
- **Windows and Mac laptop app:** it may now put a picture on the clipboard (for Copy picture). It still never reads the clipboard.
- **Laptop and tablet together:** keep both on the same build, as before.

## Not yet tried for real
- **A Teams call:** Online Mode was tested in Chromium and in the laptop app, not on a real Teams call.
- **Pasting into Teams:** Copy picture was tested by reading the clipboard back, in Chromium and in the laptop app (the picture is there, 1,080 × 1,350), not by pasting into Teams.
- **The Galaxy Tab:** Copy picture there should fall back to saving the file. That fallback was tested in Chromium, not on the tablet.
- **The tablet app:** you confirmed build 135 works on your Galaxy Tab. Build 137 is packaged the same way and passes the same checks, but hasn't been opened on the tablet.

Tests: 129 suites, all 2,837 checks passed on the first try, on this build's page. New checks: `fix137` (31/31) Online Mode for Teams calls in the browser and `fix137d` (10/10) in the laptop app (the copied picture read back from the laptop's clipboard); `fix136o` now checks what the TV and the wager card actually show (it fails on the published build-136 page, 25/27, and passes here). The tablet app passed `apk_check.py` (name "Mind It!", opening screen in the app) and Google's `aapt2` reads the same. Full details: QC report (attached).
