**Mind It! v1.69 · Build 190** · 20 November 2026

This build fixes everything found by a full check of build 189: four reviews of the code, and a scan of every screen on the TV, the laptop, the Galaxy Tab both ways and the phones. It also brings the 5th-build refresh: a new Mac app, updated guides, and the stress test plus 60-minute soak.

## Mastermind It! wagers you type in
- **The amount box is always big enough.** On the laptop it could shrink to a sliver ("Ove…", "Amount (Hid…"). Now it keeps its width, and Save and Clear move underneath when the column is narrow.
- **Hints that fit.** Where "Amount (hidden as you type)" doesn't fit, it reads "Amount (hidden)". The sealed-code box reads "e.g. 7K2QX9M" when it's narrow.
- **Long team names in full** in the wager panel, instead of "The Magnificent Kno…".
- **Galaxy Tab upright, Online Mode:** the amount box no longer shrinks to almost nothing beside All in · Half · 0.
- **The Galaxy Tab as the laptop's remote:** an All in or Set sent just as the laptop moved on to the next wager is refused, never applied to the wrong wager.

## Fixed in the game
- **A restart while wagers were being revealed on stage** no longer leaves Mastermind It! stuck. After Resume, "Reveal wagers on stage" shows the rest.
- **Each game's Mastermind It! starts clean.** The history and achievements no longer carry the previous game's marking or "extended" flag.
- **🥔 Hot Potato:** Reset question takes the pass back as well.
- **🎡 The Wild square** appears in every game, also when you replay the same board.
- **"A Different Team Answered?" → Wrong:** the turn stays with the team whose turn it was.
- **💡 Hints:** a hint a team asked for on the previous question is not spent on the next one. The phone's hint box now uses the right words on Rewind It! and Phoenix squares.
- **🗑 Delete quiz** is not offered while an unfinished game is waiting for Resume, so the unfinished game can't be deleted by mistake. Its "Quiz deleted" message now shows.

## Level on points at the end
- **The phones follow the TV's tie-break** (most correct answers, or the sudden-death tiebreaker). The team that lost the tie no longer sees "joint lead", "=1st" or "Joint winners". Each phone says who won the tie-break.

## Screens
- **Galaxy Tab upright:** the strip of host cards is only as tall as the two cards on screen, so there's no gap above the dots. "Swipe for …" names the cards still to come, and on the last page it reads "‹ Back to …".
- **Galaxy Tab upright, 7 or more teams:** the score chips under the question put the score under the name, so names are readable.
- **Phones:**
  - the long team name shows in full before the game and in the Scoreboard;
  - the question timer sits under the team name;
  - "1st of 12 teams" (was "1st · of");
  - buttons are at least 44 px tall.
- **Season finale:** co-champions are shown together as "SEASON CHAMPIONS".
- **Night Recap:** no "0 players" when Player Profiles weren't used.
- **An open panel** (Player Profiles, Historic Games) is never covered by the undo bar.

## Safety
- **Only the Mind It! app's own windows can control the quiz.** A web page open in a browser on the same laptop or Galaxy Tab can no longer act as the Quizmaster or change your players' file.
- **Handing the quiz to another device:** another device on the Wi-Fi can no longer take over, or cancel, a hand-over that is waiting for approval.
- **Backup host:** after the laptop restarts with another game, the Galaxy Tab forgets its old backup and stops offering "Take over".

## Also
- The Galaxy Tab app, Mind It! TV app, Windows app and Mac app are build 190. The in-app update works as in build 177.
- The guides are updated for builds 186–190.
- Nothing was tried on real devices. Everything above was checked on the build machine. The 15-Minute Device Check (in the QC report) is for your own devices.

## Updating the Galaxy Tab
Android may warn that the app could be harmful. That is Google Play Protect: it warns about apps installed from outside the Play Store that can update themselves. Tap the small arrow (**More details**), then **Install anyway**. This build asks for no new permissions.
