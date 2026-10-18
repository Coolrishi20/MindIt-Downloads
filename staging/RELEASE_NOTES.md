**Mind It! v1.69 · Build 139** · 19 October 2026

## New
- **The "now playing" light is now a white spotlight.** The team whose turn it is gets a white ring and a soft white glow that breathes slowly. Before, it was gold, which looked a lot like a team that is 🔥 On Fire. You chose this from three options.
  - The gold **Now Playing** tag above the team stays.
  - A team that is **Now Playing and On Fire** shows the white ring round the orange one. Before, the flames hid the Now Playing glow completely.
  - A Returning Champion who is playing shows the white ring round its gold one.
  - The same in all 12 themes, on the TV and on the laptop's preview.
- **The Final Round timer is 45 seconds by default** (was 60).
  - A saved game still on the old 60 seconds moves to 45 once.
  - Any other time you set is kept, and you can still choose anything from 10 to 600 seconds in Setup → Final Round seconds.
  - A Final that is already running keeps its time.

## Fixed — layouts with many teams and players
Checked with 8 teams (the most a game can have) and 8 players a team, on 9 TV and screen sizes, the laptop at 1900×975 and 1366×768, the tablet remote and team phones. These were wrong and are fixed:
- **Final Round reveal (6–8 teams):** the standings list covered the answer cards. Now the standings sit in two columns and the cards stay on one row. With 2–5 teams it looks the same as before.
- **Intro, Returning Champion:** with several players the champion card grew over the MIND IT! logo. Now the players have their own smaller line (up to two lines), and a long team name is a little smaller.
- **TV with 7–8 teams (scoreboard down the side):** the Now Playing glow sat about 47 pixels to the right of its team. It now sits exactly on it.
- **Phone Buzzer Mode, 7–8 teams:** "*Team* Buzzed In!" was cut off at both ends with a long team name. It now fits.
- **💾 Recap card picture, 7–8 teams:** the stats ran into the footer and off the bottom of the card. The boxes above them now stop where they fit.
- **💾 Standings picture:** a champion with more than 6 players showed 6 of them off-centre. Now they are centred, with "+2" (and so on) for the rest.
- **Galaxy Tab remote, marking the Final with 8 teams:** the rows were ragged and Correct / Wrong were small. They now line up on every row and are 48 pixels tall.
- **Laptop at 1366×768 with 7–8 teams:** the team statuses on the Question On Screen card pushed the buttons out of view. They now use two columns.

## Fixed — reliability on the Wi-Fi
- **One bad message no longer stops the Windows and Mac app.** In build 138, a single message over 32 KB from a TV, or a broken WebSocket message from any device on the Wi-Fi, made the laptop app stop responding (Electron's error box). We reproduced it on 138. Now that one connection is closed and the quiz carries on.
- **TVs on weak Wi-Fi:** a slow TV now gets the newest picture as soon as it catches up, and the ones in between are skipped. Before, it got every picture, fell further and further behind, and the backlog filled memory. Laptop and Galaxy Tab.
- **A device that stops taking data can't hold up the others.** On the Galaxy Tab, each phone, remote and TV now has its own sending queue. Before, one stuck device could freeze the whole tablet server. A device that makes no progress for 20 seconds, or has more than 96 MB waiting, is disconnected and reconnects by itself. On the laptop, a device with over 1 MB waiting that doesn't go down is disconnected the same way.
- **Big pictures and videos when the Galaxy Tab hosts:** files for the Wi-Fi TVs are kept within 120 MB in all, and each can be up to about 30 MB (40 MB of data). Older ones the TVs aren't showing are let go first.
  - A file that is too big, or that can't fit next to what is on screen, isn't sent: the TVs show the screen without it.
  - You get one note on the tablet saying so. The file isn't asked for again, so it can't send the tablet round in circles.
- **Team-code guessing limit:** after 20 *different* wrong team codes from one phone in 10 minutes, that phone waits 5 minutes and is told "Too many wrong team codes from this phone. Wait 5 minutes, then try again." A phone that keeps checking in with the same mistyped code counts once, and other phones aren't affected. Laptop and Galaxy Tab.
- **Message size from other devices:**
  - **Laptop app:** requests from other devices may be 2 MB (was 30 MB) and are refused at once when they say they are bigger; link messages from remotes are limited to 2 MB (was 64 MB).
  - **Galaxy Tab:** link messages from remotes are limited to 2 MB (requests were already limited in build 138).
  - **Unchanged:** the quiz page on the same computer or tablet keeps its large limits, and the Galaxy Tab hand-over keeps 30 MB.
- **Screens that have left are forgotten.** The 📺 list of Audience Screens forgets an offline screen after 7 days away and keeps at most 12 unnamed offline screens. Some TV browsers arrive as a new screen every time, so the list used to grow without end. Screens you named, blocked or chose for the sound stay.

## Unchanged
- How the game plays: scoring, turns, one go per team (build 138), rules and presets. Only the Final timer's default changed.
- Versions and data: still v1.69. Saves and backups open in 138 and 139 alike.

## Compatibility
- **Data:** nothing is deleted and no IDs change. A game saved in 138 opens in 139 (its 60-second Final timer becomes 45 once), and the other way round.
- **Galaxy Tab:** installs over build 138 (versionCode 139, original key).
- **Laptop and tablet together:** keep both on the same build, as before.

## Not yet tried for real
- **On a real Galaxy Tab:** the tablet server's changes were tested with its server code run on a computer, and the release check opens the app on an Android emulator.
- **On real Windows and Mac machines:** the laptop-app changes were tested in the laptop app on the build machine (the same app shell, on Linux).
- **Real weak Wi-Fi and real smart TVs:** slow and stuck TVs were simulated with test programs that read slowly or not at all.

Tests: 139 suites and 3,053 checks, all passing on this build's page: 136 suites first time, and three out-of-date tests (not the app) corrected and passed (`fix130c`, `desk`, `fix139j`). New: `fix139` (20/20) and `fix139l` (16/16) on the webpage, `fix139j` (26/26) on the tablet's server code, `fix139t` (9/9) on the tablet's quiz page, `fix139d` (23/23) in the laptop app. Connection stress tests 24/24 and the 60-minute soak 2/2 (0 false disconnects). Layout audit: 234 screens with 0 issues, and again 0 with 8 teams × 8 players. The tablet app passed `apk_check.py`. Full details: QC report (attached).
