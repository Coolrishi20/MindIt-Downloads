# Mind It! v1.69 — Changelog

**Version 1.69 is frozen**; each Windows/Android build gets a build number (the Android versionCode). This file starts with the release notes for the builds since the last full release check, then the complete development history.

## Release notes — builds 116 → 135 (12–18 October 2026)

### Build 135 — the tablet app fixed, no more false "Storage Full", drawn backdrops (18 October)
- **The Galaxy Tab app is fixed:** builds 129–134 installed as "application" and closed at once (a packaging fault). Build 135 fixes it: it is called **Mind It!** and installs over it keeping your data (not yet opened on a real tablet — please check). Every APK is now checked the way the tablet reads it.
- **No more false "Storage Full" with an iPhone:** the iPhone/iPad remote no longer copies the laptop's whole player database; the webpage keeps a large database in the browser's own database; the laptop's file is read before anything is saved; messages say what really happened, and nothing is lost when a save fails (Try Again · Save Backup File).
- **Drawn TV backdrops** for Christmas, Halloween, Ramadan / Eid, Diwali, Summer, Comic Book, Gaming and Movies (original drawings).
- **The remote warns about mixed builds** too.

### Build 134 — Intermission music, the build number, a mixed-build warning, a castle for the wizards (17 October)
- **☕ Intermission music:** the theme's background loop plays quietly during the Intermission countdown and fades out when you resume.
- **★ About & Credits** (and Setup → About) shows the build: *Version 1.69 · Build 134*.
- **Connected Devices** warns (**⚠ Different Builds**) when a connected remote, such as the Galaxy Tab, runs another build.
- **Wizard / Magical School theme:** a castle at night on the TV, with owls, a dragon, a phoenix and bats flying past behind the quiz (an original drawing).
- **Not in this build:** the Comic Book backdrop — your image didn't come through.

### Build 133 — the new intro theme (17 October)
- **New intro theme**, the preview you approved (mix 5a): new hard-rock music, a deep cinematic **"MIND IT!"**, a bigger, booming explosion on its own, then a short closing riff.
  - It plays in the intro, the 🎵 Mind It! sting and on the winner screen, in the Windows, Mac and Android apps, the webpage and the web link.
  - The loading screen loops the new riff seamlessly.
  - The intro page stays until the closing riff has finished: about 8.7 s, instead of 6.8 s.
- **★ About & Credits** says *Music and announcer voice created in collaboration with ElevenLabs*.
- **Build 132's dip under the old first line is off:** the new mix lowers the music under "MIND IT!" by itself.
- A 132 laptop and a 133 Galaxy Tab (or the other way round) can still move a quiz between them.

### Build 132 — sound on a Wi-Fi TV, a clearer intro line, the Rehearsal Report, the quiz back to the tablet (17 October)
- **🔊 Sound on a Wi-Fi TV:** in 📡 Connect Audience Screen, **🔊 Sound On This TV** sends the quiz's sound to that TV's own speakers. Press **OK** on the TV remote once (TV browsers need a button press before they play sound). The laptop or tablet then goes quiet, so there's no echo, and question videos play with sound on that TV. If the TV drops off, the sound comes back to the laptop within about a second. One TV at a time. 🟡 Not yet heard on a real TV.
- **The intro's first line is easier to hear:** the music dips slightly (5 dB) under the first line, then comes back for "MIND IT!" and the explosion. Nothing else in the intro changed. The same applies to the 🎵 sting.
- **📋 Rehearsal Report** (📲 Connect ▾, or 🧪 Test Hosting): a file to send after a rehearsal. It covers this device, the app file's fingerprint, Test Hosting, each TV, the remotes, the team phones, sound and errors. It never contains codes, PINs or keys.
- **Shorter TV address from the laptop:** type just `192.168.1.20/tv` — no `http://`, no `:8765`. The longer form still works and is shown underneath.
- **🔒 Lock is a small icon** on the remote, so the top bar takes less room (on an iPhone the quiz name no longer wraps).
- **📲 Hand Quiz to the Galaxy Tab:** the laptop offers a running quiz to a Galaxy Tab that's connected as a remote. The tablet accepts, and takes everything over the same safe way as *Take Over Tablet Quiz*, the other way round; the laptop becomes the Quizmaster remote. 🟡 Not yet tried with a real Galaxy Tab.
- **Fixed:**
  - A Galaxy Tab whose quiz had moved to the laptop could never host again (builds 130–131): every later quiz page on it turned into the laptop's remote, and its phones were sent to the laptop. Now it hosts again when you start a quiz there (or the next day), and when the quiz comes back.
  - While the Galaxy Tab hosted, a trusted remote that wasn't connected made the tablet cut off the next remote and its own remote link, again and again (builds 130–131).
  - The optional theme music now also plays on the TV when the TV has the sound.
- **Both devices need build 132 to move a quiz** between them (the laptop and the Galaxy Tab say so politely otherwise).

### Build 131 — the intro's new voice (17 October)
- **New intro voice:** your new recording (*Dark Villain, Cinematic*) replaces the old voice in the intro, the 🎵 Mind It! sting, the sound-test buttons and the winner screen, in the Windows, Mac and Android apps, the webpage and the web link. The music, the loading screen, the explosion and the ending are exactly as before (checked sample for sample).
- To fit the old timing, only two things changed. The silent pause in the middle of the clip is shorter (1.2 s → 0.3 s), and the voice starts at the music's build, about 1 s earlier than the old voice. "IT!" now ends right on the explosion. The clip's level was raised to match the old voice.

### Build 130 — TVs over the Wi-Fi, moving a tablet quiz to the laptop, five smaller upgrades (16 October)
- **📡 Audience Screens:** any TV or computer with a web browser on the same Wi-Fi shows the audience screen — no cable, no app, no casting. 📺 Audience View ▾ → 📡 Connect Audience Screen shows the address (`…/tv`). Several screens at once; rename them, set a safe margin, test, refresh or disconnect them. Works from the laptop and the Galaxy Tab. Only the audience picture is sent: your controls, answers before they're revealed, wagers, PINs and players never leave your device. 🟡 Not yet tried on a real smart-TV browser.
- **💻 Take Over Tablet Quiz:** a quiz running on the Galaxy Tab moves to the laptop while it runs — scores, question, Daily Doubles and wagers, chips, the countdown, the Final — after the tablet's Quizmaster approves. Phones keep their team (no code to type), remotes and TVs follow, and the tablet becomes the Quizmaster remote. Only one device ever hosts. 🟡 Not yet tried with a real Galaxy Tab.
- **🧪 Test Hosting** (Connect Device → Run Test), a **🔋 battery warning** while hosting, **🔒 lock the remote** (press and hold to unlock), a **▂▄▆ signal** for every remote in Connected Devices, and the Windows joiner now checks the file's **fingerprint** (SHA-256).

### Build 129 — device names, Add Phone Remote, the tablet keeps hosting, offline webpage (16 October)
- **Rename devices** in Connected Devices (📲 Connect ▾ → Connect Device), on the laptop or a hosting Galaxy Tab — e.g. *Quiz Desk* or *Backstage phone*. Names are kept after reconnects and restarts.
- **📱 Add Phone Remote is always there** on the remote in control, also after it reconnected without the PIN.
- **The Galaxy Tab keeps hosting** when its screen goes off or another app is opened; a notification says *Mind It! is hosting a quiz*. 🟡 Not yet tried on a real tablet.
- **Other Galaxy Tabs find the tablet's game:** their start screen shows **Tablet Game Found → Connect**. 🟡 Not yet tried on real tablets.
- **The webpage works with no internet** once opened (https://coolrishi20.github.io/MindIt-Web/); with internet it loads the newest build first.

### Build 128 — trusted devices, one controller, the tablet as the server (16 October)
- **Trusted devices:** a remote (Galaxy Tab, iPad, iPhone or the 📱 Phone Remote) connects once with the PIN and is remembered — after a Wi-Fi drop or a restart of the laptop or the device it reconnects by itself, without the PIN.
- **One remote at a time:** a second device never takes over by itself. It waits, and the laptop shows a small card — **Allow & Switch**, **Reject** or **Ignore** (the request expires after 2 minutes). The quiz carries on unchanged when control moves.
- **Connected Devices** (📲 Connect ▾ → Connect Device): who's in control, who's waiting, your trusted devices and when they last connected — Give Control, Disconnect, Forget. **New PIN** forgets every device.
- **Galaxy Tab as the server:** with no laptop, team phones (wagers, chips, buzzers, Final answers) and a phone remote join the tablet. 🟡 Not yet tried on a real Galaxy Tab — rehearse at home first.
- Team phones and the Audience View are not affected by any of this.

### Build 127 — an iPad or iPhone as the full remote (16 October)
- 📲 **Connect Tablet is now called Connect Device** (in the Connect ▾ menu, Setup → 6 · Advanced and the Devices window) and shows two codes: **Galaxy Tab** (as before) and **iPad / iPhone**. Scan the second one with the Camera and Safari opens the same full Quizmaster remote the Galaxy Tab uses — no app to install (Complete Guide, Setup B2).
- Add it to the home screen for a **Mind It!** icon; it keeps working after the laptop app is restarted (same Wi-Fi, same PIN).
- On an iPhone the remote's board now fits the screen — all six columns, nothing cut off.
- The webpage version is also online for iPhones and iPads: **https://coolrishi20.github.io/MindIt-Web/** (it runs the quiz on its own; it can't be a remote for the laptop).

### Build 126 — Mind It! on the home screen (13 October)
- 📲 **Add to Home Screen** on an iPhone or iPad (Safari → Share → Add to Home Screen) now gives a proper **Mind It!** icon — the gold M logo — that opens the team-phone page or the 📱 Phone Remote **full-screen**, without Safari's address bar (Complete Guide 8.6). Android phones get the same icon (Chrome opens it as a normal tab).
- **Downloads on GitHub:** your private **MindIt-Downloads** page holds each build as single complete files (no parts), including the new **webpage version** `mindit.html` (Complete Guide 4.1c).
- Nothing else changes: game screens, rules and saved data are the same as build 125.

### Build 125 — five improvements (13 October)
- 🗑 **Recently Deleted**: bring a deleted player back — profile, picture and statistics — for 30 days.
- 🛟 **Safety backups**: made automatically just before a backup is restored, players or a game record are deleted, or you Start fresh; the last 10 are listed in Backups & Restore.
- ☑ **Select** several players to archive or delete them together.
- The **tablet keeps what you're typing** (Adjust Score and other boxes) when the laptop changes the scores.
- 🖼 **Results Picture** for any game in Historic Games.

### Build 124 — delete a player (13 October)
- 🗑 **Delete a player** from Player Profiles (on the player's page, next to Archive). It asks first; their past games keep their name and nobody else's statistics change; not possible while they're playing; a sync never brings them back; restoring a backup made before does.
- The Mac app is now for **Apple Silicon Macs only**.

### Build 123 — restore asks first, Mac app (13 October)
- Restoring a backup or loading a game file now **always asks first** (Restore Backup / Load File / Cancel), even when no game is running, so a quiz you're still setting up can't be replaced by accident. Player-profile files still just add players.
- **Mind It! for Mac** — the laptop app for Apple Silicon and Intel Macs (macOS 11+). Not yet tried on a real Mac.
- Team photos stay inside the saved game (your decision).

### Build 122 — Returning Champion rule (13 October)
- 👑 The crown goes to a team only if **every player of last game's winning team** is on it tonight (new players alongside are fine). If last game's winner was one person, the new team that person is on is crowned. If the winners are split across teams, or one of them isn't playing, nobody is crowned.
- “N wins in a row” follows the same rule; the rule's note in Setup → Gameplay & Rules says it too.

### Build 121 — QC fixes
No rule, layout or save-format changes. Every fix was measured before and after (see `MIND_IT_QC_REPORT.pdf`).
- **Connection Health:** phones that check in normally no longer flicker between *Connected* and *Unstable*; a phone that really drops out still turns amber, then red.
- **Quizmaster tablet:** no longer redraws its whole screen every second (numbers being typed stay put; taps no longer land on a button that is being replaced). Its Connection Health shows round trips in bands (“under 100 ms”) and “just now”; the laptop still shows exact numbers.
- **Phone Buzzer Mode:** the BUZZ IN button is no longer rebuilt ~6 times a second — every tap now counts (30/30, was 14/30). The fast buzzer check pauses while the phone is locked.
- **Phones during a question:** the screen is no longer rebuilt at every check-in; the countdown still follows the laptop (+time, stop).
- **Laptop:** the Phones card (Join link & QR code), wager card and live-setup card are only redrawn when something changes — open sections stay open.
- **📱 Phone remote:** one background check, however many buttons are pressed; the seconds update in place.
- **Saved game:** an unfinished game is no longer lost when Mind It! is opened and closed again without choosing *Resume saved game* or *Start fresh* (this also affected build 119). It is offered at every start until you choose.

### Build 120
Setup tidy-up (Board & Flow placement, one Export History button, no leftover step numbers, Speed Bonus box); **Random Team Generator:** tap to select, tap another team's player to swap, **+** to move, ↶ Undo Last Change, ⟲ Reset to Generated Teams, ✓ Confirm Teams.

### Builds 116–119
Tablet “Waiting For A Buzz…” and clearer buzzer wording; settings carried across a port change; layout tweaks (pop-ups beside the host panel, board panel, one Begin Game, Correct/Wrong size, portrait tablet header, chip names in full, phone footer, game record rows).

---

# Complete development history

This is a condensed history of the original development chat (676 turns, late Sep → 9 Oct 2026). Turn numbers `[tNNN]` point into that chat.

| Mark | Meaning |
|---|---|
| ✅ | Implemented and shipped (confirmed by the build reports and the current code) |
| ◐ | Partly done |
| ↩ | Implemented, then replaced or removed |
| 💬 | Discussed or offered only — **never implemented** |

**Version scheme:**
- The visible version went 1.0 → 1.1.0 → 1.2.0 … 1.94, then was **reset to 1.69** at Android build 18 and **frozen**.
- The user's 1.69 spec said: "DO NOT change the version number again after this update… Keep the version at 1.69 for all future work until I explicitly instruct you to change it."
- Since then only the internal Android versionCode rises, one per APK: **18 → 128**.

---

## Phase 1 — Web artifact (claude.ai), before the desktop app

### Origin and naming
- ✅ **Origin:** the user asked to modify "Akram's Spellbound!", a Jeopardy-style builder owned by another organisation. It was rebuilt as a new artifact, **TRIVIZZLE**: a dark-blue TV studio stage, a marquee-bulb logo, value tiles, a podium scoreboard, a countdown ring, host and audience views, an Excel/CSV template, autosave, 4-letter team codes and private wagers [t0–t5].
- ✅ **Renamed Mind It!** at the same link (https://claude.ai/artifact/2iL2v91yVkXTkRycp7E7h5). The starter template became 4 rounds + Final [t12–t13].
- ✅ Touch-first tablet/phone UI; a QR code on the Final page; automatic team sequencing ("NOW PLAYING"); End Round Early fixed (an in-app confirm, since browser pop-ups are blocked); away teams; "Wrong, no penalty" [t6–t7].
- ✅ Excel starter template (later reduced to two sheets: "Start Here" + "Questions", laid out like the user's own sheet); a Number of Rounds setting [t8–t9, t20–t23].
- ✅ The user's ground rules: verbal answers; phones only for private input; the TV must never show host controls or private wagers; free and local, with no paid services [t10–t11].

### Rules and wager flow
- ✅ **DD minimum wager = clue value**; maximum = score or the low-score cap [t16–t17].
- ✅ **UAE Dirham sign** everywhere (bundled glyph font) [t18–t19].
- ↩ Multiple-choice questions and the values/DD/notes columns removed from the sheet [t22–t23].
- ✅ Full-game check, 6 fixes [t24–t25].
- ✅ **Adjust score** with a TV banner; a TV display help panel; **Final minimum wager 0** (teams on exactly 0 may play) [t26–t27].
- ✅ **Random DDs only on each category's top two values**, fixed for the round [t28–t29].
- ✅ DDs: 1 in Round 1, then 2 per round [t33]. Later Round 4 went to 3.
- **Wager-entry saga** [t30–t55]:
  - sealed codes, then the DD wager told to the QM, then QR direct submit via a Bun "Mind It! Live" app (Windows/Mac ZIPs);
  - then team-code entry; then ZIP removal requested; then Claude-account sharing, which failed for personal accounts;
  - then **sealed codes restored** (dash optional);
  - then the shared link made **players-only** to prevent hijacking.
  - ↩ The Live ZIPs and Python kit were dropped from the flow; the desktop EXE later replaced them.

### Hosting, scoring and the sting
- ✅ **QUIZMASTER MODE** on phones/tablets (password gate; only a hash is stored) [t62–t63].
- ✅ **Turn order:** the next question goes to the team after the question's owner (user correction) [t64–t65].
- ✅ **CORRECT / WRONG ANSWER / PASS:** wrong deducts and passes; the pass-on bonus only for explicit passes; TV banners [t66–t67].
- ✅ 13 of 35 review suggestions [t70–t71]:
  - Final timer (60 s), one wager key per game, sound on/off and volume, turn strip, score count-up, round-summary movers, How to Play slide, winner confetti.
- ✅ Final quality pass and a "Mind It!" sting [t74–t75].
- **"Mind It! Ver 1.0"** patch notes [t76–t77].
- ↩ Synthetic-voice sting replaced by the **user's own recording** (deeper, 20% quieter, 15% slower), with a cinematic explosion [t78–t87].
- ✅ Ties first shown as joint champions [t89].

### Defaults, look and the first desktop apps
- ✅ **"Final changes":** timer 30 → **45 s** with auto-start; rock-style intro music; regression [t112–t113].
- ✅ **Pass-On Bonus ON (25%)**; **Round 4 DDs = 3**; Final timer; **pass timer = min(30 + left, 45)**; loading ≈6 s [t116–t119].
- ✅ Icon library (Twemoji, later replaced); Title Case; consistency pass [t122–t127].
- ✅ **Zoned TV layout**; **Host Cam**; **Teams Presentation Mode** [t128–t139].
- 💬 Quick Quiz Generator (J! Archive): copying refused, never built [t134–t135].
- ✅ **Windows EXE** (Electron portable, port 8765, data in `%APPDATA%\Mind It!`), first built **27 Sep 2026** [t142–t143].
- ✅ Built-in fonts, Save Standings picture, **Player Profiles**, permanent player images [t152–t155].
- ✅ Setup split into sections (**APP_VERSION 1.1.0**); editable stats (Edit Score, Add Past Game) [t156–t161].
- ✅ Mac zips (Apple Silicon + Intel), unsigned and untested [t164–t165]. ↩ Dropped later.
- ✅ **Batch build [t168–t169]:**
  - **ties broken by most correct answers**;
  - **Final answers typed on phones** (desktop);
  - phone remote with PIN;
  - 11 badges; leaderboard;
  - Turn Order / DD cap moved to Advanced.

## Phase 2 — Desktop + Android, versions 1.2.0 → 1.94 (28 Sep → ≈1 Oct)

| Version / build | Main changes |
|---|---|
| (pre-1.2.0) | ✅ Historic Games crash fix (records repaired / set aside); **game-icons.net badge set** (106 at first; 135 today incl. Women) [t171]; ✅ picture editor [t173]; ✅ fixed QM password kept at the user's wish [t175]; ✅ **Speed Bonus** +100 [t179] → **50% of the round's lowest value** [t181]; ✅ **Theme system, 12 themes** [t183]; ✅ **Android app** (WebView, Quizmaster Remote + standalone, `com.mindit.app`, versionCode 1, "1.2.0") [t185]; ✅ **Bollywood + Sports** themes (14 themes); Himesh likeness/name and the "Harry Potter" name declined [t187] |
| **1.2.0** (28 Sep) | Patch notes (full and short) [t189–t191] |
| **1.2.5** / build 2 | ✅ Theme Intensity default **Full** [t193]; ✅ "dont make for mac intel" [t195]; ✅ new app icon [t199] |
| — | ✅ **Questions Library by category** + Add To Round [t203]; data locations explained [t207]; ✅ **Google Drive backup** via the user's Apps Script (tested only with a stand-in) [t211] |
| **1.2.6** / build 3 | ✅ Default-theme preview fix; ✅ APK rebuilt for API 35 / minSdk 24 (Galaxy Tab A9+ install issue); ✅ **Fantasy and Music themes removed** (12 left); ◐ theme polish; ✅ Final questions from one-question categories; ✅ new games filled with **random library questions** [t213] |
| **1.2.7** / build 4 | ✅ **Wi-Fi library sync** laptop ↔ tablet [t217] |
| **1.2.8** / build 5 | ✅ Players and history sync, Possible Duplicates / Review & Merge (never automatic) [t221] |
| **1.2.9** / builds 6–7 | ✅ Logo exploration → **"Hex Labyrinth · Icon Cut"** official logo (without "SINCE 2026"); bigger symbol + Android adaptive icon [t223–t237] |
| **1.3.0** / build 8 | ✅ **Final answer checking** (advisory; accepted alternates) [t239] |
| **1.50** / build 9 | ✅ **Achievements & Fun Stats** (20 + 15), play-by-play log; full QC [t241]. 💬 **Google Cast** spec: user declined, "too ambitious" [t242–t248] |
| **1.70** / build 10 | ✅ Animated hex logo on loading/intro/TV; Large Text On TV + Colour-Blind-Safe; 🔁 Duplicates tab; keep laptop awake; **Play Again (New Questions)** [t253] |
| **1.80** / 11 | ✅ Tablet home redesign (Continue Game card, Laptop Game Found, status chips…) [t259] |
| **1.81** / 12 | ✅ Gold "MIND IT!" wordmark everywhere [t263] |
| **1.90** / 13 | ◐ Landscape alignment + **theme-adaptive logos**, TV-safe margins (targeted fixes, not a full redesign) [t265] |
| **1.91–1.94** / 14–17 | ✅ Final-only question upload; ✅ "⬆ Import Template" to the library; ✅ tablet picture sync fix; ✅ **iPhone HEIC** photos [t267–t277] |

## Phase 3 — Version frozen at 1.69 (Android builds 18 → 128)

| Builds | Main changes |
|---|---|
| **18** (≈1 Oct) | ✅ **Version set to 1.69 everywhere**; **EXE + APK only, no Mac** (user spec); UI clean-up; **Credits** (Claude, ChatGPT, Rishi, Jeopardy, The Thirst for Random Knowledge); top bar 📺 · 📲 · Sound · ⋯ · Setup [t278–t279]. ✅ Web link kept updated with each build [t280–t281] |
| 19–21 | ✅ Voice line "Stadium Boom" with stutter (the user's own recording) [t287]; ↩ Bollywood-only music made from the user's clip, then **removed** ("not good enough… I'll record a new one later") [t288–t291] |
| 22–30 | ✅ **Rehearsal mode**, fresher random rounds, phone tidy-ups [t295]; ✅ **Random Team Generator** + 27-rule achievements [t297]; ✅ career achievements + **streak flames** [t301]; ✅ library keeps media [t305]; ✅ **auto-add questions to the library** on game finish and template load [t309–t311]; ✅ library tabs (Round / ⭐ Final) [t311]; ✅ **Switch Final Question**, edits by ID, **frozen Historic Game snapshots** [t313]; ✅ library Excel export [t317]; ✅ **+30 Sec Extend** (manual, repeatable, logged) [t319] |
| 31–37 | ✅ **👁 Preview** (isolated) [t321]; ✅ **True Daily Double** moment + Ran The Category [t325]; ✅ 24 more achievements (49 rules) [t329]; ✅ **Phone Buzzer Mode** (off by default) + **Host Stats** [t331]; ✅ past games credited to Rishi as host [t333]; ✅ **Host ≠ Player, one role per match**, Rishi default [t335]; ✅ Longest Game baseline 2 h, real play time [t337] |
| 38–45 | ✅ Logo "M" in **Montserrat Black, embossed**, wordmark in Montserrat [t343]; dark-navy M border [t345]; ✅ **early-buzz lockout**, reaction times, **Returning Champion** [t349]; ✅ **Triple Gamble chip**, and **Daily Doubles can never be passed** [t351]; ✅ TG reveal + summary + phone scoreboard [t355]; ✅ **Game Rules panel + presets** (Classic / Full Show / Family Night), **Quizmaster Guide PDF**, sections renamed "2 · Teams & Players" / "3 · Gameplay & Rules" [t359]; ✅ QC fixes [t363]; ✅ **board fill animation** (Dramatic R3–4), loading 6 → **4.8 s** [t371] |
| 46 | 💬 Evading Play Protect declined [t373]; ↩ a new release key was made, then **reverted to the original key** at the user's request [t375–t377] |
| 47–50 | ✅ **29 "Women" team badges**, layout refresh; ✅ Game Rules portrait fixes; ✅ tablet remote 2×2 pad, DD/Final/phone layouts; ✅ more layouts (Now picking card, profile tabs incl. Head-to-head, Historic Games cards) [t383–t397] |
| 51–57 | ✅ Teams & Players cards, Rounds at a glance + Fill Empty Slots, grouped Advanced, **TV winner podium** [t399]; ✅ app-wide QC/consistency ("Question Database", "Historic Games" naming; **Risky Quizzness part not executed** at the user's request) [t401]; ✅ layout rounds 5–6: DD screen (gold, **not pink**, QR kept), category reveal, round summary, notifications, phone wager pad, leaderboard, player grid, import steps, Devices panel, Quick Setup cards, Host Cam corners/sizes, Tonight's Teams walk-on [t409–t421] |
| 58–63 | ✅ How to Play cards, **Intermission**, phone timer, loading "TONIGHT · … · Your Quizmaster: Rishi", Random Teams cards [t425–t431]; ✅ **tablet PIN on a number pad** [t433]; ✅ re-check + **Rehearsal Checklist PDF** [t437]; ✅ layout code merged [t441]; ✅ long-session test, About & Credits, **Backups & Restore**, tablet settings, size 3.28 → 2.37 MB [t445–t447] |
| 64–70 | ✅ **"Underdog" chip** + chip logos [t455–t457] → ✅ phoenix logo **F4 Black & Gold**, matching TG logo [t469] → ✅ renamed **Phoenix** [t471]; ✅ guide, checklist, Phoenix achievements [t475]; ✅ Phoenix right answer **double + 20% of the gap** [t481] |
| 71–76 | ✅ Phoenix: **wrong = no loss**, **once per game** [t483]; ✅ **no Phoenix in the Final**, second-lowest fallback if more than 2,000 behind [t485]; ✅ "THE PHOENIX IS LIVE" announcement + ember + phoenix cry [t487]; ✅ cry **option C (eagle screech)** + **casino sting** for TG + tight build (2.27 MB) [t492–t496]; ✅ **host can change wagers** (teams can't) [t503–t504]; ✅ QC fixes (DD "Half" within range, Title Case after bullets) [t508] |
| 77–90 | ✅ compact **Your chips** row [t510]; ✅ **Quizmaster chip override** ("Use for…" / "Switch off") [t514]; ✅ Board & flow: back to board after a correct answer, hide finished categories (both off at first) [t518]; ✅ Quick Setup layout, all pages standardised, 3 dialog sizes [t528–t530]; ✅ **live TV preview**, **setup icon rail**, **one-handed tablet mode** [t536]; ✅ **Bottoms Up** chip (off by default, Round 1) [t546] → drink wording changed twice → **designated player** [t548–t554]; ✅ **every team needs a Player Database player** [t556]; ✅ tablet-sized team screen, used chips hidden [t560]; ✅ **Phoenix capped at the leader, only if more than 2,000 behind** [t564]; ✅ QC + size (EXE 75.6 → **68.9 MB**, English-only locales) [t568]. 💬 Claude Code migration prompt written [t570], then the user said **"ah leave it"** [t573] |
| 91–94 | ✅ **Side-column TV scoreboard** for 7–8 teams [t582]; ✅ Board & flow switch fixes, gold volume slider, **back-to-board ON by default**, **💓 heartbeat** (on), **who-got-it line**, Import Template to Database, **newest-first random rounds** [t584–t588]; ✅ new **clue list editor** (mock-up C) + **Replace Round from Database** [t592]; ✅ **TV shrink-to-fit** + **Replace Category** [t594] |
| 95–100 (7 Oct) | ✅ Add-Questions card first [t598]; clean-up [t600]; ✅ **portrait recap card** [t608]; ✅ **Bottoms Up ON by default (Full Show)** + Windows zip [t614]; 💬 code-signing priced (~US$110–300/yr), not bought [t616]; ✅ gold rail icons [t620]; ✅ guide refresh + ~55 host line icons [t626]; 💬 gold icons on TV/phones previewed, declined ("na its fine") [t628–t630] |
| 101–104 (7–8 Oct) | ✅ Question Database button at the top [t636]; ✅ icons centred (user: "only send .exe and apk files unless i ask for anything else") [t638–t640]; ✅ **Phosphor Light** icons replace "childish" ones [t644]. From here the EXE is delivered as 3 parts + a joiner (30 MiB send limit). 💬 Go + WebView2 single-file rewrite started, then **stopped at the user's request**; Electron kept [t648–t651]. 💬 One-file zip download page: impossible (artifacts refuse zip) [t655]. ✅ Joiner `.bat` fixed to find renamed "(1)" parts by size [t661] |
| **105** (9 Oct) | ✅ Tablet **"device storage is full"** fix: profiles kept in a file via the Android bridge (WebView storage ≈10 MB) [t665] |
| **106** | ✅ Tablet **↩ Back to Board**, **🔐 Team Codes** on laptop and tablet, **↕ Reorder** within a category [t667] |
| **107** | ✅ Tablet **big next-step button**; **phone status in Team Codes** (items 1 and 4) [t672] |
| **108** | ✅ **Category replacement with chosen questions** (exact-5 rule), round-tab memory, performance, **Audience View QC** at 9 screen sizes, tablet More row restored, phones stay signed in across a laptop reload, "👑 Champion ×N" crown text. 74 suites, 1,657 / 1,657; 234 / 234 AV screenshots. Report doc A–G [t673–t675] |
| — | 📄 **Handover documentation** (this file set), no code changes [t676] |
| **109** (9 Oct, new chat) | ✅ Bug-fix build, no rule changes: **B1** a wrong Triple Gamble now closes the tile and the next pick goes to the team after the owner; **B2** Phoenix and Bottoms Up chip flags, state and logs reset at every new game (the logs were also leaking last game's chip achievements into the next game); **B19** Returning Champion worked out again on Play Again / Reset / Start a new game; **B20** "any drink counts" wording replaced. New module `app97`, new suite `fix109` (31 checks, 13/31 on build 108). 75 suites, 1,691 / 1,691 |
| **110** (10 Oct) | ✅ After a live quiz with repeated TV "Reconnecting" covers: **root cause** = the Quizmaster window was throttled by Chromium when minimised/covered (timers ~1/min) → fixed with `backgroundThrottling:false`. ✅ Compact connection lines (TV/tablet/phones, never full screen once connected; TV timer dimmed while unverified). ✅ Phones: one poll at a time, backoff, asleep beacon, instant wake check, round-trip reporting. ✅ Tablet: one socket, 0.5→8 s backoff, unstable state. ✅ Server: WebSocket heartbeat, health endpoint. ✅ Timeouts passed through three old wrappers (were cut to 3 s). ✅ **Check Connections** + **TEST ALL CONNECTIONS** (setup, 📶 chip on laptop and tablet). ✅ **END GAME** on the tablet (save once, confirm, thanks, Main Menu; retry-safe; rehearsal; standalone). Suites `conn110`, `endgame110`; `stress110` phases incl. a 60-minute real-time run. 77 suites, 1,742 / 1,742 checks passed in one full run (39 min); conn110 needed one retry there because of a test-harness page-selection flake, fixed and re-run alone 35/35. Look approved by the user ("ok") from screenshots. |
| **111** (10 Oct) | ✅ build 111 (10 Oct): lighter saves from the user's backup diagnostics — the “↩ Undo replace” round copy is dropped once play starts; the autosave stores a question picture as a pointer when the identical picture is in the picture store (rehydrated on load; the store never drops a picture the game uses; backup files stay complete); new photo originals capped at 800 px (cropped 512 px unchanged; existing photos untouched); one-time repair of impossible playing times (under 1 min for a game over 20 min → start-to-finish length, marked estimated). Module `app99`, suite `lighter111` (20 checks). 78 suites, 1,777 / 1,777. |
| **112** (11 Oct) | ✅ build 112 (11 Oct, `app100.js`): 📶 Devices → “Phone Join QR (for Teams)” shows the players’ join code (it opened the Quizmaster Phone Remote with its PIN); phones say “Thanks For Playing!” after END GAME and after the laptop’s “Back to setup” even when the Final was played on phones; no Speed Bonus countdown on Triple Gamble questions (TV, preview, tablet); Undo gives a chip back (Triple Gamble / Phoenix / Bottoms Up, open or closed question); final standings, Final reveal list and winner screen break a points tie by most correct answers (user decision); minimum 2 teams in the detailed setup + Begin Game guard; no Phoenix in Phone Buzzer Mode (user decision); phone join QR on the pre-game TV (setup + Tonight’s Teams; top-right with many teams; setting, on by default); a one-player team takes its player’s name (and picture, as before), restoring its own name when a second player joins. User decisions: Phoenix speed bonus after the cap — keep; Daily Double stays in place on reorder — keep. Suite `fix112` (38); `qcx`, `conn110` updated for one-player team names. Full run 1,754/1,759 → the 5 were the expected name/position checks, fixed and re-run green. |
| **113** (11 Oct) | ✅ build 113 (11 Oct, `app101.js`, user: “do them all”, no mock-ups needed): TV score cards show each team's place (1st in gold; top-right of the card, in the Now Playing strip, or beside the score in the side column; hidden while all level); a long team name in the Now Playing bar shrinks to fit; the laptop's Correct button shows the speed bonus while it can be earned (⚡ +100); correct answers on the final standings / winner podium and the phones' scoreboard (`desktop/main.js` passes `cor`); a hand-edited clue value switches to own values so Begin Game keeps it (§25-D); the Phoenix “Comeback Kid” is now 🚀 “Phoenix Climber” (duplicate id); Setup phone card wording. Suite `fix113`; `achphx` expectation updated; `zones` screenshot retry. |
| **114** (11 Oct) | ✅ build 114 (11 Oct, `app102.js`, user: “Do all of them and also update the browser only web link too”): the Final question locks once the Final starts; typed Final answers close 2 s after time's up (`desktop/main.js` `time_up`); 48 px Setup touch targets on the tablet; Replace Round warns about questions already in tonight's quiz (`app88`); Phone Buzzer Mode TV fixes (no Now Playing team while anyone can buzz, “BUZZERS REOPEN”, no turn strip, speed chip only for the picker); About → Licences (qrcode-generator, jsQR, fonts); phones vibrate on their pick / wager (Android). Guides updated; web link republished. Suite `fix114`. |
| **115** (11 Oct) | ✅ build 115 (11 Oct, `app103.js`, user: “do all 6”): Phone Buzzer Mode — no Correct/Wrong (laptop buttons, C/W/X keys, tablet) until a team buzzes; no Phoenix without the phone server (browser-only, tablet-only); the saved game survives a port change (`desktop/main.js` saved-game copy); `laptop_app.sh` sandbox guard; accepted alternates editable during the Final again (114 lock regression); old Quizmaster Guide PDF retired. Suite `fix115`. No web link this build (every alternate build: 116 next). |
| **116** (12 Oct) | ✅ build 116 (12 Oct, `app104.js`, user: “do 1-5”): the tablet shows “🔔 Waiting For A Buzz…” in Phone Buzzer Mode until a team buzzes (status lines say any team can buzz; a late tap gets “Nobody has buzzed yet”); theme, sound, house rules and camera settings survive a port change (`settings-copy.json`); README corrected (B17); unreachable Live-kit/old-room code removed (B16); the TV audit waits for the dice (B23). Web link republished. |
| **117** (12 Oct) | ✅ build 117 (12 Oct, `app105.js`, user: “do them all”): Phone Buzzer Mode — the tablet drops the turn-order line, the laptop hint names who buzzed first and says a wrong answer reopens the buzzers, then “Picks next”; the old Live-kit preload start-up branch removed; `conn110` test steadied; new 2-page Rehearsal Checklist (build 117). Web link not republished (every alternate build — next 118). |
| **118** (12 Oct) | ✅ build 118 (12 Oct, `app106.js` + `style.css`, user: “do them all”, layout only): pop-up messages beside the laptop's right-hand panel instead of over it; the board panel shows “questions left” once (separate card merged); the hidden second Begin Game on Setup removed; Correct / Wrong the same size; slimmer Setup header. Web link republished. |
| **119** (12 Oct) | ✅ build 119 (12 Oct, `app107.js` + `style.css`, user: “do them all”, layout only, before/after shown first): portrait tablet header (name on top, buttons below); tablet chip names in full; phone “Connected” + “Change Team Code” on one line under the scoreboard; game record page score beside each team name; Random Team Generator team counts on one row. Web link not republished (next 120). |
| **120** (12 Oct) | ✅ build 120 (12 Oct, `app108.js` + `style.css`, user: “do them all”, layout only, before/after shown first): Board & Flow card above the Audio & Presentation Back / Next buttons; Export History To Excel once in Backups & Data; leftover step numbers hidden; Speed Bonus Points as a normal box. **Random Team Generator** (user spec “Interactive team swapping”, `app109.js`): select → swap, select → + move (refuses to empty a team), same-team tap re-selects, ✕ Cancel Selection, ↶ Undo Last Change, ⟲ Reset to Generated Teams, scroll kept, slide-in. Returning Champion **reviewed only** (no change; findings and a proposed rule await approval). Web link republished. |
| **121** (12 Oct) | ✅ build 121 (12 Oct, `app110.js`, full-QC phase of the user's “continue current task first, then complete full QC…” request; fixes only, no rule or layout changes): Connection Health no longer flickers a normally-polling phone to Unstable (the laptop added its own 3 s refresh gap to the phone's age); the tablet's copy of Connection Health shows round trips in bands and “just now”, so the laptop stops re-sending the whole game to the tablet every second (the tablet redrew its whole screen each time — typed Adjust Score numbers and taps on the next-step button could be lost); team phones rebuild the screen only when something changes — in Phone Buzzer Mode the BUZZ IN button was rebuilt ~6.5×/s and 14 of 30 ordinary taps were lost (now 30/30), and during a question every check-in rebuilt the screen because the seconds left were part of the change test; the fast buzzer check pauses while the phone is locked; the laptop's Phones / wager / live-setup cards are only replaced when their content changes (Join link & QR code no longer snaps shut twice a second); the 📱 phone remote keeps one check loop (each button press used to add another) and updates the seconds in place; **an unfinished game is no longer lost when Mind It! is opened and closed again without choosing** Resume / Start fresh (found by the QC restart test, also in build 119; a spare copy `mindit.resume.pending` is kept until a choice is made). `fix121` 39/39. |
| **122** (13 Oct) | ✅ build 122 (13 Oct, `app111.js`, user: “do it like returning champion only if the full team is there, if the team was just one person then the new team with that person is crowned returning champion”): 👑 Returning Champion only when every player of last game's winning team is on one team tonight (extra players allowed; one-player winner → the team that player is on; split or missing winners → no crown; deleted players not counted; teams without players matched by name; joint winners → first qualifying team; the win streak follows the same rule); the rule's note in Gameplay & Rules updated. `champ122` 15/15. |
| **123** (13 Oct) | ✅ build 123 (13 Oct, `app112.js`, user chose 2B and “leave it” for team photos; asked for the EXE, APK, “the apple installation file” and the guides in one release): restoring a backup or loading a game file **always asks first** (Restore Backup / Load File / Cancel), even with no game running; player-profile files still merge without asking. ✅ **Mac laptop app** on the user's explicit request (Apple Silicon + Intel zip, ad-hoc signed, not run on a real Mac). Team photos stay in the save (B37, as decided). `fix123` 13/13. |
| **124** (13 Oct) | ✅ build 124 (13 Oct, `app113.js`, user: “I want the ability to delete players from the database … next time onwards the mac should only be for apple silicon”): 🗑 **Delete a player** from Player Profiles (asks first; past games keep the name; not while playing; sync keeps it deleted; a backup restore brings them back). Mac app now Apple Silicon only. Before/after shown (laptop, tablet landscape and portrait). `fix124` 19/19. |
| **125** (13 Oct) | ✅ build 125 (13 Oct, `app114.js` + `app113.js`/`app112.js` updates + CSS, user: “do them all and show the before and after”): 🗑 **Recently Deleted** (restore a deleted player — profile, picture, stats — for 30 days; then only the name stays); 🛟 **Safety backups** (IndexedDB, last 10, made before a restore / file load, player or record deletion, Start fresh / New quiz; Restore or Save File from Backups & Restore); ☑ **Select** several players → Archive / Delete; the **tablet keeps what you type** (Adjust Score and other boxes) through a redraw; 🖼 **Results Picture** for any Historic Game (the existing recap card, drawn from the record). Before/after images shown. `fix125` 27/27, `fix125d` 9/9. |
| **126** (13 Oct) | ✅ build 126 (13 Oct, `build.py` head + `vendor/touch-icon-180.png`/`-192.png`, user: “ok do both, include the webpage as a download option in github”): **📲 home-screen support** — `apple-mobile-web-app-capable`, black status bar, title “Mind It!”, theme colour `#03051c`, the gold M logo as a full-bleed 180×180 `apple-touch-icon` (and a 192×192 `icon`), so Safari **Share → Add to Home Screen** on an iPhone/iPad gives a proper icon that opens the team-phone page or the 📱 Phone Remote full-screen (Guide 8.6). No game-screen changes. **Downloads on GitHub:** the private repo `MindIt-Downloads` holds each build as single files (EXE, APK, Mac zip, guides, reports) plus **`Web/mindit.html`** — the webpage version (Guide 4.1c). Web link republished (alternate builds). Tests `fix126` 8/8, `fix126d` 13/13 (Chromium with iPhone emulation, not real Safari). |
| **127** (16 Oct) | ✅ build 127 (16 Oct, `app115.js` + `style.css` + desktop `main.js` route, user asked whether the iPhone webpage could be a remote for the laptop quiz, then “do it”; then “change connect tablet into connect device”): **📲 Connect Tablet renamed Connect Device** everywhere (dialog, Connect ▾ menu, Setup → 6 · Advanced card + button, Devices panel button, *Show Device QR / PIN*); it shows two codes — **Galaxy Tab** (unchanged `MINDIT1|…`) and **iPad / iPhone**, a web address `http://<laptop>/tablet?remote=…&s=…&t=<PIN>` the Camera opens in Safari; the laptop app serves the page at **`/tablet`**; there the remote asks `/api/link/info` for the current game number before each (re)connect, so a home-screen icon survives a laptop restart (PIN still required; New PIN still disconnects); under 600 px the remote board uses `minmax(0,1fr)` columns and smaller tiles so all columns fit an iPhone. The GitHub-hosted webpage (`MindIt-Web`, https) can't reach the laptop (mixed content) — explained to the user. Test `fix127d` 19/19 (Chromium iPhone/iPad emulation). Also new: public repo `Coolrishi20/MindIt-Web` hosts the webpage via GitHub Pages (https://coolrishi20.github.io/MindIt-Web/). |
| **128** (16 Oct) | ✅/🟡 build 128 (16 Oct, `app116.js` + `style.css` + desktop `main.js` link/remote rewrite + Android `MindItHost.java`/`Json.java` + `MainActivity` bridge; owner's specs “Trusted Device Reconnection & Host-Controlled Device Management” and “Multi-Device Remote Control Hierarchy”, decisions: Phone Remote counts, phone joins the laptop directly, 2-minute requests, then “i need the tablet to be the server”): **trusted devices** (PIN once → per-device secret, sha-256 stored in `trusted-devices.json`, survives restarts; New PIN / Forget revoke); **one control slot** shared by tablets, iPad/iPhone and the 📱 Phone Remote, kept by its owner across drops and restarts; a second device waits — the host gets an Allow & Switch / Reject / Ignore card (right-hand panel, never on the TV or in Present mode), requests expire after 2 min; only the controller receives the game state; **Connected Devices** panel (in control · waiting · trusted with last-connected, Give Control / Disconnect / Forget); the remote's waiting card (Ask For Control); **📱 Add Phone Remote** on a laptop-connected tablet sends a phone straight to the laptop; **Galaxy Tab as the server**: the APK runs a Java port of the laptop's server (HTTP + WebSocket: team phones, chips, buzzers, Final answers, Phone Remote, /tablet, link, health) and the page uses it at http://127.0.0.1:<port>. Tests `fix128d` 33, `fix128e` 18, `fix128t` 22 (tablet server on the JVM; not a real Galaxy Tab). |

---

## Discussion-only items (💬 never implemented)

- **Casting / TV:** native Google Cast receiver and Android TV app (declined); a second TV via a second casting device; Samsung Smart View advised against (it mirrors the host controls).
- **Fast Track, Evil Round, True/False, Sequence questions, "Risky Quizzness" theme:** appear only in pasted QC/redesign specs; **never part of Mind It!**
- **Quick Quiz Generator** (J! Archive or Claude-written questions).
- **Result sharing extras:** recap as a TV slide, "Save recap" in Historic Games, recap styles, certificates, printable team cards.
- **Rules and modes:**
  - **New rounds:** sudden-death tiebreaker, Lightning Round, Joker Round, Specialist Subject, Hot Streak bonus, Line Bonus, Jackpot Pot, Hot Tiles, Spotlight Player, Ask the Room.
  - **Question styles:** picture rounds and Name That Tune, lifelines, Coryat score, Judges' review, "Answer in the form of a question", "I'll take … for 400" banner, "Time for one more clue".
  - **Final rules:** Final for positive scores only.
  - **Party Mode:** Sip Penalty, Hand Out Sips and others.
- **Chips:** Shield, Steal, Hot Seat, Time Boost, Hint, Extra Turn, Head Start, Freeze, Side Bet, Copycat, Jackpot, Mystery Box, Category Expert, Double Trouble, Lucky Dip, Boomerang, Taxman, Alliance, Wildcard, Double Down, Insurance, Wheel of Fortune, Bounty, Category Lock, Clock Stopper. Also chips or Phoenix in Buzzer Mode, Final-Round Phoenix, Phoenix Fury ×3, Phoenix help options A/C/D.
- **Hosting:** Undo pop-up toast, confirm early reveal, in-app pre-show checklist, read questions aloud, "⚑ Fix later" flag, big-button bar, jump to Round 2 / Final, value presets, "Classic"/"Current" value presets, timer lights. Also Undo for "No one got it", "No one got it" on the tablet at any time, one-tap Easy→Hard sort and moving categories (t670 items 2, 3, 5).
- **Questions:** convert the user's PowerPoint quiz (`Jeopardy_14Aug26.pptm`, 60 questions + Final "FIFA World Cup"); difficulty-balanced rounds; real difficulty from results; category colours; syncing "Not Duplicates" decisions; trimming stored game size.
- **Long term:** league/season mode, team profiles, saved line-ups, team-name generator, head-to-head beyond profiles, audience vote/polls, Bonus Wheel.
- **Platform:** changeable QM password (the user said keep it), code signing / Microsoft Store, auto-updates, an installer (the NSIS config exists but is unused), a lighter ~10 MB Windows shell, a Claude Code production migration, **version 1.70** (overruled: "You asked to keep 1.69").
- **Visual:** team-logo styles 1–16 and the Tabler-based women logos (not chosen); logo "M" options other than Montserrat Embossed; setup icon styles B–E; Lucide/Tabler/Heroicons/Iconoir; recap layouts 2–9; mock-ups A/B for the clue editor; the round editor as a draggable board.

## Removed or replaced (↩)

| Was | Now |
|---|---|
| Castle background and intro video | Removed early |
| Multiple-choice questions | Removed (old files still load) |
| Synthetic speech sting | The user's own recording |
| Mind It! Live Bun ZIPs, Python kit in the flow | Desktop EXE server; `mindit_live.py` generated as legacy until build 115, removed in build 116 |
| Twemoji / emoji team icons | game-icons.net badges (135) |
| Fantasy and Music themes | Removed (fall back to Default) |
| Marquee "MIND IT!" logo | Hex Labyrinth logo |
| Custom gold line icons | Phosphor Light |
| "Underdog" puppy chip | Phoenix (F4 logo) |
| Old Phoenix/TG fanfares, cry v1 | Eagle screech (C), casino sting |
| New Android release key | Original key restored (`MindIt_Android_Signing_Key.zip` unused) |
| Bottoms Up "any drink" / religion wording / "Someone else" | Designated player. The last leftover "any drink counts" sentence (QM override dialog, `app79`) was fixed in build 109. |
| Bollywood-only music | Removed, awaiting the user's recording |
| Mac builds | Dropped |
| Go + WebView2 port | Stopped, never shipped |
