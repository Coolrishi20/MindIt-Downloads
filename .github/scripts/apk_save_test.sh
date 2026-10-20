#!/bin/bash
# Mind It! — the tablet app's own save files, checked on an Android emulator (build 141; owner: "do them all").
# Run right after apk_launch_test.sh, with the app installed. It opens the quiz page in the app (Start New Game on the home
# screen), lets the page save its complete copy of the game into the app's files (MainActivity.gameWrite), closes the app,
# opens it again and checks the page finds that copy in the files (MainActivity.gameRead).
# The page reports through its console, which the Android WebView writes to logcat (since build 141, Android only, once each):
#   "MINDIT_FS page android build N"                 the quiz page opened
#   "MINDIT_FS saved android state+media … chars"    the complete copy went into the tablet's files
#   "MINDIT_FS failed android …"                     writing them failed
#   "MINDIT_FS found android state … chars, media …" at start-up the page read a copy back from the files
# usage: apk_save_test.sh <result file> [<screenshot.png>]
# The result file gets one line: "ok: …", "fail: …" (the page opened but the files didn't work), or "skip: …" (the emulator
# couldn't open the quiz page, or the APK is from before build 141 — the app was not judged on this).
OUT="$1"; SHOT="${2:-}"; PKG=com.mindit.app
: > "$OUT"
cat > /tmp/mindit-find.py <<'PY'
import re, sys
x = open('/tmp/mindit-ui.xml', encoding='utf-8', errors='replace').read()
for m in re.finditer(r'<node [^>]*>', x):
    n = m.group(0); t = re.search(r' text="([^"]*)"', n); d = re.search(r' content-desc="([^"]*)"', n)
    tx = (t.group(1) if t else '') + ' ' + (d.group(1) if d else '')
    if (tx.strip() == sys.argv[1]) if len(sys.argv) > 2 else (sys.argv[1] in tx):   # "exact": the whole text, not part of it
        b = re.search(r'bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', n)
        if b:
            x1, y1, x2, y2 = map(int, b.groups()); print((x1 + x2) // 2, (y1 + y2) // 2); break
PY
tap_text(){   # tap the on-screen element whose text contains $1 (the page in the WebView is in the accessibility tree)
  for i in $(seq 1 12); do
    adb shell uiautomator dump /sdcard/mindit-ui.xml >/dev/null 2>&1
    adb shell cat /sdcard/mindit-ui.xml > /tmp/mindit-ui.xml 2>/dev/null
    [ -n "$OUT" ] && cp /tmp/mindit-ui.xml "$OUT.xml" 2>/dev/null   # kept with the results, to see what the screen held
    # a slow emulator sometimes shows "Process system isn't responding" over everything: answer Wait and look again
    W=$(python3 /tmp/mindit-find.py "Wait"); if [ -n "$W" ] && grep -q "responding" /tmp/mindit-ui.xml; then adb shell input tap $W; sleep 3; continue; fi
    # the app runs full screen: Android's one-time "Viewing full screen — Got it" note covers it at first
    G=$(python3 /tmp/mindit-find.py "Got it"); if [ -n "$G" ] && grep -q "full screen" /tmp/mindit-ui.xml; then adb shell input tap $G; sleep 2; continue; fi
    # Android 13+ may ask "Allow Mind It! to send you notifications?" over the quiz page: answer Allow
    N=$(python3 /tmp/mindit-find.py "Allow" exact); if [ -n "$N" ] && grep -q "send you notifications" /tmp/mindit-ui.xml; then adb shell input tap $N; sleep 2; continue; fi
    XY=$(python3 /tmp/mindit-find.py "$1")
    if [ -n "$XY" ]; then adb shell input tap $XY; return 0; fi
    sleep 4
  done
  return 1
}
home_gone(){   # true once the app's home screen ("Run the whole quiz on this tablet") has left the screen
  adb shell uiautomator dump /sdcard/mindit-ui.xml >/dev/null 2>&1; adb shell cat /sdcard/mindit-ui.xml > /tmp/mindit-ui.xml 2>/dev/null
  [ -s /tmp/mindit-ui.xml ] && ! grep -q "Run the whole quiz on this tablet" /tmp/mindit-ui.xml; }
open_quiz(){   # open the app and tap Start New Game; check the quiz page really replaced the home screen (up to 3 taps)
  adb shell monkey -p "$PKG" -c android.intent.category.LAUNCHER 1 >/dev/null 2>&1; sleep 8
  for t in 1 2 3; do tap_text "Start New Game" || return 1; sleep 6; home_gone && { OPENED="the quiz page opened (tap $t)"; return 0; }; done
  OPENED="Start New Game was tapped 3 times but the home screen stayed"; return 1; }
shot(){ [ -n "$SHOT" ] && adb exec-out screencap -p > "$SHOT" 2>/dev/null; return 0; }
log(){ adb logcat -d 2>/dev/null | grep -o "MINDIT_FS $1[^\"]*" | head -1; }
crash(){ adb logcat -d -b crash 2>/dev/null | grep -A3 "FATAL EXCEPTION" | grep -m3 -E "Process: $PKG|Exception|Error" | tr '\n' ' ' | cut -c1-300; }

adb shell settings put secure immersive_mode_confirmations confirmed >/dev/null 2>&1 || true   # no "Viewing full screen" note
adb shell pm grant "$PKG" android.permission.POST_NOTIFICATIONS >/dev/null 2>&1 || true   # no "Allow notifications?" question (Android 13+)
adb shell am force-stop "$PKG" >/dev/null 2>&1; adb logcat -c; adb logcat -b crash -c 2>/dev/null || true
OPENED=""
if ! open_quiz; then shot; echo "skip: ${OPENED:-could not find Start New Game on the home screen} (the emulator's screen reader view; see the .xml next to this result)" > "$OUT"; cat "$OUT"; exit 0; fi
for i in $(seq 1 20); do [ -n "$(log saved)$(log failed)" ] && break; sleep 2; done
PAGE=$(log page); SAVED=$(log saved); FAILED=$(log failed); C1=$(crash)
if [ -z "$PAGE" ]; then
  shot; [ -n "$C1" ] && { echo "fail: the quiz page crashed the app — $C1" > "$OUT"; cat "$OUT"; exit 0; }
  echo "skip: $OPENED but didn't report (an APK from before build 141)" > "$OUT"; cat "$OUT"; exit 0; fi
if [ -z "$SAVED" ]; then shot; echo "fail: the quiz page opened ($PAGE) but the complete copy wasn't saved in the tablet's files — ${FAILED:-no save reported in 40 s}${C1:+; crash: $C1}" > "$OUT"; cat "$OUT"; exit 0; fi
# close the app completely and open it again: the copy must come back from the files
adb shell am force-stop "$PKG"; sleep 2; adb logcat -c
if ! open_quiz; then shot; echo "skip: saved ($SAVED) but couldn't open the quiz page again — $OPENED" > "$OUT"; cat "$OUT"; exit 0; fi
for i in $(seq 1 15); do [ -n "$(log found)" ] && break; sleep 2; done
FOUND=$(log found); C2=$(crash)
shot
if [ -n "$FOUND" ] && [ "${FOUND#*nothing}" = "$FOUND" ] && [ -z "$C2" ]; then
  echo "ok: $SAVED; after closing and reopening the app: $FOUND" > "$OUT"
else
  echo "fail: $SAVED, but after reopening the app: ${FOUND:-the page did not read the files}${C2:+; crash: $C2}" > "$OUT"
fi
cat "$OUT"
