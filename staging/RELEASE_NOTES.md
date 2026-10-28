**Mind It! v1.69 · Build 157** · 28 October 2026

The fixes you asked for this afternoon — above all, syncing between the laptop and the Galaxy Tab now works with your real data.

## Fixed
- **⟳ Sync didn't do anything.** A sync starts with the tablet sending its copy — questions, players, Historic Games and the players' photos — to the laptop. Since build 139 the laptop takes at most 2 MB in one message from a device on the Wi-Fi (a safety limit), and with photos your copy is about 9 MB, so the laptop refused it and the tablet waited for ever. That's why ⟳ Sync on the tablet and ⟳ Sync devices on the laptop changed nothing (and why the game saved at the end of the night didn't arrive). The tablet now sends a big copy in pieces under the limit and the laptop puts them back together; the limit itself stays for everything else. If a sync ever gets no answer, the tablet now says so after 90 seconds instead of waiting. **Update both the laptop app and the Galaxy Tab to 157.**
- **The Ready to Play card on the main menu** lines up: the TV, tablet and phone chips sit in even columns at one height, with 📺 Connect a TV and ⟳ Sync devices as full buttons below them.

## New
- **⟳ Sync devices on the main menu** (Ready to Play), with *Last synced … · this laptop N games · tablet N games* under it.
- **Restore from a backup file on the Galaxy Tab:** tablet home → Settings → Backup → **⬆ Restore From Backup File**. It opens Backups & Restore; pick a MindIt_Backup file. It asks first, keeps a safety copy of what is on the tablet, and adds the players and Historic Games in the file (nothing is deleted).
- **Backup files ending in .txt or .json** both restore — on the tablet and on the laptop (e-mail and chat apps sometimes rename them).

## Downloads
Windows (Mind-It-Windows.exe), Galaxy Tab (Mind-It-Android-Galaxy-Tab.apk), Mind It! TV for the Mi Box (Mind-It-Android-TV.apk), the web page (mindit.html), the guides (as in build 155) and the QC report. No Mac app in this build (the Mac stays on build 155 until 160). Your saved games, players and settings carry over.
