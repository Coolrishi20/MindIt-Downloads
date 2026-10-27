**Mind It! v1.69 · Build 154** · 27 October 2026

## Fixed first
- **The laptop's clue board while the Audience View window is open (a build-153 bug).** Build 153 rests the laptop's TV preview while the Audience View window is open, to save effort, but that preview was the only board you could click on a laptop. **Pick a clue** now shows at the top of the host panel whenever the preview rests: click a value and the TV follows.

## New
- **A main menu on the laptop.** Mind It! opens on a title screen:
  - ▶ **Prepare tonight's quiz** (or press Enter);
  - ⏯ **Continue last game** (only when there's a saved game);
  - Question Database, Players & History, Rehearsal and Settings;
  - last night's champions on a podium, with last night's Rascala!;
  - which screens are ready, and the backup status.

  It fits the laptop's screen without scrolling. The Galaxy Tab and phones keep their own start screens.
- **Prepare tonight's quiz** (laptop, Galaxy Tab, phone, web):
  - three ways to start: 🔁 **Same as last time** (last game's teams, players, rules, answering, theme and special question in one tap), 🎯 **New quiz, step by step**, or ⚡ **Quick game** (4 teams, 2 rounds, random questions from your Question Database);
  - four short steps: Questions → Teams → How you play → Check;
  - "How are you playing tonight?": **In the room**, **Phone Buzzers** or **Online call** sets the rules, the answering and the screen together;
  - the Check ticks what's ready and has a **Fix** button for anything missing, then a big **Begin game**.

  The Galaxy Tab's Start New Game opens it. All the settings are still one tap away.
- **Sound clues.** MP3, M4A and WAV files work wherever clue pictures and videos do: the upload box, the clue editor, the Question Database and Excel templates by file name. The TV shows a gold sound wave while a clip plays, and the host has **▶ Play / ↺ Replay / ■ Stop** for sound and video clues on the laptop and the Galaxy Tab. A Question Database **media link** now plays on the TV (picture, video or sound).
- **The Rascala! badge, live:** the cowboy cat sits on the last-place team's TV score card during play (teams level in last all get it; nobody while everyone is level).
- **The Rascala! voice:** "…heh heh… Naughty Pussy." as the cowboy cat appears at The Rascala! reveal, in the Mind It! announcer's voice.
- **Online Mode:**
  - **🎲 Random turn order** (on by default; a switch in the rules): when the game begins the turn order is drawn at random, and Tonight's teams on the TV shows the draw, so everyone on the call can see the Quizmaster didn't choose it;
  - **Nicknames:** a player with a nickname in Player Profiles is shown by it during an Online Mode game. Player Profiles, Historic Games, saved games and the Excel exports keep real names.
- **12 new achievements:**
  - Rewind It!: 🤠 Jackpot Spin, 🌪️ Wheel Of Misfortune, 🎡 Rewind Royalty, 😎 Lucky Lasso;
  - Blind It!: 🕶️ Blind Luck, 👓 Seeing Clearly;
  - The Rascala!: 🏃 Escaped The Rascala!, 😼 Rascala Repeat, 🐾 Nine Lives;
  - and 🎵 Name That Tune, 🧠 Stumped The Room, 💬 Fastest Fingers.

  Your old games get 😼 Rascala Repeat and 👓 Seeing Clearly when the app opens (the only two their saved details allow); nothing else in them changes. From now on each game also saves a short question-by-question record, so future achievements can count it too.
- **Question stats:** each Question Database question remembers how often it was answered right, wrong or not at all, so you can spot the easy ones.

## Better
- **The category names before each round** stay on screen for 3 seconds each (were 1.45), long enough to read out.
- **Setup → Rounds & Questions** is split into **Rounds**, **Questions** and **⭐ Mastermind It!** sub-tabs (it was one very long page).
- **The laptop host with the Audience View window open** uses the whole screen: the controls spread across two columns (three on big screens) instead of one narrow column, so there is much less scrolling.
- **Mastermind It! wagers:** one help line for the sealed codes instead of the same sentence under every team, and each team's boxes side by side.
- **Speed:** redraws are about 18 % lighter on the laptop with the Audience View window open, and about 19 % on the Galaxy Tab when it hosts (measured in the sandbox).

## Unchanged
- **Rules, timers, wagers, scores and connections.** Saved games and backups load as before. **Version:** still v1.69. **The theme music** is unchanged.

## Compatibility
- **Data:** the same saved data and backup files as build 153; new details are added alongside.
- **Galaxy Tab:** installs over build 153 (versionCode 154, original key); its App Update can install it.
- **Windows:** build 152 and later update themselves (Setup → Advanced → ⬆ App Update).
- **Mi Box S:** Mind It! TV 154 updates itself, from the laptop or the internet.
- **Mac and the guides:** not rebuilt in this build. The Mac download is still build 150's app, and the guides are still build 152's; both are refreshed in build 155.

## Checks
- **Full run on the final files: 192 suites, 4,847 checks, all passed** — browser 120 suites 3,526/3,526; laptop app 72 suites 1,321/1,321. New: fix154 24, fix154r 60 (sound clues, stats, achievements), fix154p 117 (main menu, Prepare tonight's quiz, sub-tabs).
- **Audience View audit:** 406/406, no issues.
- **Stress, all six phases:** 24/24 (idle 2, network 6, load 4, lock 2, rapid taps 4, health 6).
- **Found and fixed on the way:** a direct Wi-Fi TV picture outside a capture threw once The Rascala! badge was on the score cards (fixed; every file rebuilt, the whole programme re-run); two sound tests updated for The Rascala! voice (16 sounds by design).
- **Signed with your original key** (Galaxy Tab and Mind It! TV, versionCode 154); the Windows EXE carries the same page, the build-154 tablet app and the build-154 TV app.

## Not yet tried for real
- Tested in the sandbox only. Nothing was run on your real laptop, Galaxy Tab, Mi Box S, phones or TV. In particular:
  - the main menu inside the laptop app window;
  - sound clues heard through a TV;
  - Prepare tonight's quiz on the tablet;
  - the Online Mode draw on a real call.
- **No 60-minute soak in this build**, as agreed; it runs in build 155.
