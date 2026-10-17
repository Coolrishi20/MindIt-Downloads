**Mind It! v1.69 · Build 133** · 17 October 2026

## What's new
- **🎸 New intro theme**, as you approved it (preview "mix 5a"): new hard-rock music, a deep cinematic **"MIND IT!"**, a bigger, booming explosion on its own, then a short closing riff.
  - **Loading screen:** the new riff loops seamlessly while the quiz gets ready.
  - **Intro page:** it now stays until the closing riff has finished (about 8.7 s; it was 6.8 s).
  - **🎵 Play The Mind It! Sting** and the winner screen play the same theme (about 9.8 s).
  - Build 132's music dip under the old first line is gone: the new mix lowers the music under "MIND IT!" by itself.
- **★ About & Credits** now says *Music and announcer voice created in collaboration with ElevenLabs*.

## Unchanged
- Everything else. If you set your own sting audio in Setup, it still replaces the theme. Volume, mute and 🔊 Sound On This TV work as before.

## Compatibility
- **Laptop ↔ Galaxy Tab:** build 133 uses the same laptop and tablet server code as 132, so a 132 device and a 133 device can still move a quiz between them. Update both anyway, so the intro sounds the same everywhere.
- **Galaxy Tab:** installs over the old app (same signing key, versionCode 133) and keeps its data.
- **Windows:** the portable app. Use it in place of your old `Mind It!.exe`; your data stays.
- **Mac:** Apple Silicon only (M1–M4), macOS 11 or later. It is ad-hoc signed, so the first time you open it go to System Settings › Privacy & Security › Open Anyway.

## Known issues / not yet tried on real devices
- **Sound checks so far:** the intro was checked only on the build machine, rendered through the app's own code and sound chain. Nobody has heard it on real laptop speakers, the Galaxy Tab or a TV yet.
- **Loudness:** at the same volume setting, the new intro is about 1 dB quieter overall than build 132's. The music is about 1.7 dB quieter and the explosion louder; that is the balance you approved.
- **Licence:** ElevenLabs' music terms allow use in an app, or playing it at public events, only on its Scale and Business plans. Offline commercial use is excluded on every plan. Check your plan before a paid quiz night.

Tests: 117 suites, 2,635 of 2,637 checks passed in the full run. The 2 misses were older checks that assumed build 132: the TV-sound check waited a fixed 9 s for the sting to end (the new sting is 9.8 s), and the report check expected build 132. Both were updated and re-run: all pass. The new theme check (`fix133m`, 32/32) renders the intro through the app and compares it with the approved mix 5a. Full details: QC report (attached).
