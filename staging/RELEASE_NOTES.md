**Mind It! v1.69 · Build 135** · 18 October 2026

## Fixed
- **The Galaxy Tab app is fixed.** Builds 129–134 installed under the name "application" and closed straight away ("application closed because this app has a bug").
  - **Cause:** a fault in the step that packages the Android app. The tablet read every text in the app's settings one place out: the name became "application", and the screen to open became "activity", which doesn't exist. Earlier checks read the file a different way, so they didn't catch it.
  - **Now:** the app is called **Mind It!** and its opening screen is where Android looks for it. Install it over the broken one with **Update**: same app and signing key, so the tablet keeps its data. Every APK is now checked the way the tablet reads it before it can be released.
- **No more false "Storage Full" with an iPhone.**
  - **Cause:** an iPhone or iPad opened as the remote (📲 Connect Device → iPad / iPhone) copied the laptop's whole player database, photos included, into Safari each time it connected. Safari allows each website only about 5 MB, however much space the phone has. The remote never even used that copy.
  - **On the remote:** it no longer copies the database.
  - **On the webpage:** a large database is kept in the browser's own database (IndexedDB), each picture stored once under its existing ID. It is checked by reading it back before the old copy is removed.
  - **On the laptop:** its player file is read before anything is saved, so an old quick copy can never overwrite it, and each save is confirmed. The laptop no longer shows a false "storage full" once its database grows large.
  - **The messages now say what actually happened:** the browser's limit, storage blocked (Private Browsing), another tab holding the storage, or the laptop/tablet file not written. Nothing is lost when a save fails: changes stay on screen and a bar offers **Try Again** and **⬇ Save Backup File**.
  - **Fewer writes:** a save with nothing changed writes nothing, and the Galaxy Tab app re-syncs on reconnect at most every 10 minutes.
  - **New photos:** on an iPhone a photo is saved as a JPEG within a size budget, unless it really has see-through parts. Existing pictures and IDs are untouched.

## New
- **Drawn TV backdrops for eight themes:** Christmas, Halloween, Ramadan / Eid, Diwali, Summer, Comic Book, Gaming and Movies. Each is an original picture behind the quiz with a few things moving in it, like the Wizard castle in build 134.
  - With **Subtle** intensity, or a device set to reduce motion, they stay still.
  - The Comic Book backdrop is an original drawing with made-up heroes; your picture wasn't used because it shows Marvel and DC characters.
- **The remote warns about mixed builds too:** "⚠ Different Builds — This device runs build 135, the laptop runs build 134."

## Compatibility
- **Data:** nothing is reset or deleted, and player and picture IDs don't change.
- **Moving a quiz:** builds 132–135 can still move a quiz between the laptop and the Galaxy Tab.
- **Galaxy Tab:** installs over builds 129–134 (versionCode 135, original key).
- **Windows:** the portable app, as before.
- **Mac:** Apple Silicon, ad-hoc signed (first open: System Settings › Privacy & Security › Open Anyway).

## Not yet tried on real devices
- **The tablet app hasn't been opened on a real tablet yet.** No Android device or emulator is available on the build machine. The APK was checked the way Android reads it, and it passed: name Mind It!, the opening screen exists in the app's code, all permissions correct, original key.
  - **Please:** install it on the Galaxy Tab and confirm it's called Mind It! and opens.
- **The iPhone fix was tested in Chromium,** with Safari's 5 MB limit simulated, not in real Safari.
- **The backdrops** were checked at 1920×1080 in Chromium, not on a real TV browser.

Tests: 123 suites, all 2,732 checks passed in the full run on this build's page. One older suite (`fix128d`, the 📱 Add Phone Remote code) passed on its automatic retry; the QR reader in the check missed the code once; the check now reads it more carefully and passed five times in a row. New checks: `fix135` (27/27) the backdrops and the remote warning; `storq` (17/17) the webpage with Safari's 5 MB limit simulated; `fix135d` (7/7) and `fix135s` (9/9) the laptop app with a large database and an iPhone remote. The tablet app passed `apk_check.py` (name "Mind It!", opening screen in the app) and Google's `aapt2` reads the same. Full details: QC report (attached).
