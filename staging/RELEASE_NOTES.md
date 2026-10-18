**Mind It! v1.69 · Build 136** · 18 October 2026

## New
- **🌐 Online Mode replaces Family Night**, for a quiz on a **Teams call** (Setup → 3 · Gameplay & Rules, and Quick Setup step 3).
  - **On:** Speed Bonus, Streak Flames, Returning Champion, Board Fill Animation, Pass-On Bonus (25%) and the Final Round.
  - **Off:** the Phoenix Chip. Its switch is hidden while Online Mode is selected, so it can't be switched on by accident.
  - **As Family Night had them:** everything else (no Triple Gamble, no Bottoms Up, no early-buzz lockout, Daily Double wagers shown).
  - **When you pick it:** 2 question rounds + the Final Round (Round 1 200–1,000, Round 2 400–2,000) and Standard answering. You can still change the rounds and any setting afterwards.
  - **Wagers without phones** (players at home can't reach the laptop's Wi-Fi):
    - for the Final Round the TV shows **📩 Send your wager to the Quizmaster · private chat message** instead of a QR code;
    - for a Daily Double the TV asks the team to tell you their wager;
    - there's no "Scan to join" code;
    - on the laptop the wager card puts the cursor in the first box, ready for you to type.
  - Classic and Full Show are unchanged.
- **Backups about a third smaller.** A backup file kept each question picture twice: once with your players' pictures and once inside the quiz. Now it's kept once, and the quiz points to it.
  - Measured on your 10 October backup: a build-135 backup of that data is 10.5 million characters; build 136 makes it 7.1 million.
  - The same goes for Safety Backups and Google Drive backups.
  - Build 119 (the rollback build) and builds 132–136 restore the new backups with every picture back in the quiz (tested). Older backups still restore as before.
- **See where your data is.** Backups & Restore → **Right now** has two new lines:
  - **Player Data:** where the players, pictures, history and Question Database are saved (this laptop's file, the tablet's file, this browser's database or this browser), how big they are and when they were last saved.
  - **Pictures:** how many there are and how big they are together.
- **🗜 Make photos smaller** (only when you tap it). Each player photo keeps a larger original so you can re-crop it later. Since build 111 new ones are kept at 800 px, but older ones can be up to 1,600 px.
  - The button checks first, tells you how many photos and how much smaller, and asks.
  - It makes a safety backup, then makes those originals 800 px.
  - Every player keeps their picture. The photos on screens, question pictures, animated GIFs and see-through pictures don't change.
  - On your 10 October backup: 13 originals, 2.5 MB → 1.2 MB. With the smaller backups above, a backup of that data goes from 10.5 to 5.7 million characters.
- **Warnings on the old releases.** The release notes of builds 129–134 now start with "Don't install this release's Galaxy Tab app". Their files are unchanged.

## Compatibility
- **Data:** nothing is deleted, and no player or picture IDs change.
- **Rules:** if Family Night was what you last used, your switches stay exactly as they were (shown as Custom). Tap **Online Mode** to switch.
- **Backups:** build 119 (the rollback build) and builds 132–136 restore build-136 backups. Build-135 and older backups restore in 136.
- **Galaxy Tab:** installs over build 135 (versionCode 136, original key). Builds 129–134 of the tablet app don't open; install this one over them with **Update**.
- **Windows:** the portable app, as before.
- **Mac:** Apple Silicon, ad-hoc signed. The first time you open it: System Settings › Privacy & Security › **Open Anyway**.

## Not yet tried on real devices
- **Make photos smaller and the new lines** were tested in Chromium and in the laptop app, not on an iPhone or the Galaxy Tab.
- **Online Mode** was tested in Chromium and in the laptop app, not on a real Teams call.
- **The tablet app:** you confirmed build 135 opens and works on your Galaxy Tab. Build 136 packages it the same way and passes the same check (name "Mind It!", opening screen in the app, original key), but hasn't been opened on the tablet yet.

Tests: 127 suites, all 2,813 checks passed on the first try, on this build's page with Online Mode. New checks: `fix136o` (26/26) and `fix136od` (6/6) Online Mode in the browser and the laptop app; `fix136` (27/27) lighter backups — restored in build 119 (the rollback build) and builds 132–136 — and Make Photos Smaller; `fix136d` (7/7) the same in the laptop app. The tablet app passed `apk_check.py` (name "Mind It!", opening screen in the app) and Google's `aapt2` reads the same. Full details: QC report (attached).
