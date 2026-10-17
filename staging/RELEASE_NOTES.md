**Mind It! v1.69 · Build 134** · 17 October 2026

## What's new
- **☕ Intermission music:** while the Intermission countdown is on, the theme's background loop (the 19-second Quiz Room Riff you approved) plays quietly. It plays well under the intro music: about −25 LUFS at the default volume, against about −19 for the intro music. It fades in over 2 s and fades out when you press ▶ Resume Game.
  - It plays where the quiz's sounds play: the laptop, or the Galaxy Tab when it hosts. A TV that has 🔊 Sound On This TV plays it too.
  - The volume slider and Sound Off apply to it.
  - It stays quiet while your own theme music is playing.
- **The build number** in ★ About & Credits ("Version 1.69 · Build 134") and in Setup → About. The 📋 Rehearsal Report shows it too.
- **Connected Devices warns about mixed builds:** a yellow **⚠ Different Builds** note appears when a connected remote, such as the Galaxy Tab, runs another build.
- **Wizard / Magical School theme:** a new TV backdrop. It's an original drawing of a castle at night on a cliff above a lake, with lit windows and a moon; owls, a dragon, a phoenix and bats fly past behind the quiz. With Subtle intensity, or a device set to reduce motion, they stay still.
- **The 🎵 sting** stays as in build 133 (your choice).

## Compatibility
- **Moving a quiz:** the laptop and tablet servers now also pass on each remote's build. The code that moves a quiz between the laptop and the Galaxy Tab is unchanged, so builds 132, 133 and 134 can still move a quiz between each other.
- **Galaxy Tab:** installs over the old app (same signing key, versionCode 134) and keeps its data.
- **Windows:** the portable app. Use it in place of your old `Mind It!.exe`; your data stays.
- **Mac:** Apple Silicon only (M1–M4), macOS 11 or later. It is ad-hoc signed, so the first time you open it go to System Settings › Privacy & Security › Open Anyway.

## Known issues / not yet tried on real devices
- **Sound and the new backdrop:** both were checked only on the build machine. The Intermission music was rendered through the app's own sound chain, and the wizarding backdrop was checked at 1920×1080. Neither has been tried on real speakers or a real TV yet.
- **Comic Book theme backdrop:** not in this build; it waits for your image.

Tests: 119 suites, all 2,678 checks passed in the full run. Two older suites (question import and Excel import) passed on their automatic retry, then passed twice more afterwards. The new checks: `fix134` (24/24) covers the Intermission music, the build number, the wizarding backdrop and the tablet server passing on builds; `fix134d` (8/8) covers the laptop app's server and the warning. Full details: QC report (attached).
