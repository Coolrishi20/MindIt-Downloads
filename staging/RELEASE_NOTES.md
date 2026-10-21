**Mind It! v1.69 · Build 143** · 21 October 2026

## New
You picked "7" from the list after build 142 and approved the before/after picture.
- **📲 The tablet offers its own update.** When the Galaxy Tab finds or connects to a laptop that carries a newer tablet app (the laptop app has carried one since build 142), it says so:
  - **On the Main Menu:** an **Update Available** card under the laptop it found ("Galaxy Tab app build N is on <laptop> · This tablet has build M") with **Update**.
  - **While connected:** a banner at the top with **Update** and **Later**. It takes the place of the old "⚠ Different builds — update the older one from the download page" line, which said the same thing but couldn't do anything.
  - **Update** opens the laptop's download page in Chrome on the tablet (over your Wi-Fi). Then **Download** → open the file → **Update**, as with the code on the laptop. If Chrome warns about the file, tap **Download anyway**.
  - **Later** hides the offer until the tablet app is opened again.
  - Only the Galaxy Tab app shows it. An iPad or iPhone remote, the laptop, the TV and the phones show nothing new.
- **Once only:** this arrives with build 143, so the move from 142 to 143 is the last one that needs the code (📲 Connect Device → Update the Tablet App on the laptop, or the APK).

## Guide
- 2 new pictures (the Update Available card on the tablet's Main Menu, the banner on the tablet remote); new text in 4.2 and 22.7; “New in build 143” at the front; the Quick Start, Rehearsal Checklist and cheat sheet say build 143; the Complete Idiot's Guide is still 171 pages

## Unchanged
- **The rules and the game screens:** nothing changes.
- **Versions:** still v1.69.
- **Laptop app:** unchanged apart from the page and the tablet app it carries (build 143).
- **Galaxy Tab:** the Main Menu's Update card, the remote's banner, and two small additions to the app's own code: `appBuild()` (its build number) and `openTabletAppPage()` (opens the laptop's download page in the browser — it accepts only a local Wi-Fi address and the fixed `/tablet-app` page). versionCode 143.

## Compatibility
- **Data:** nothing changes in what is saved.
- **Galaxy Tab:** installs over build 142 (versionCode 143, original key). A laptop on build 141 or older carries no tablet app, so the tablet offers nothing there.

## Not yet tried for real
- Tested with the real laptop app and a tablet-sized browser with a stand-in for the tablet app's bridge; the new app code was compiled into the APK and its address rule checked, but opening Chrome from the app hasn't been tried on a real Galaxy Tab. The release check opens the APK on an Android emulator and saves and reopens a game there.

Tests: 149 suites, 3,288/3,288 checks. Full details: QC report (attached).
