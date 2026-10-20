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
    if sys.argv[1] in ((t.group(1) if t else '') + ' ' + (d.group(1) if d else '')):
        b = re.search(r'bounds="\[(\d+),(\d+)\]\[(\d+),(\d+)\]"', n)
        if b:
            x1, y1, x2, y2 = map(int, b.groups()); print((x1 + x2) // 2, (y1 + y2) // 2); break
PY
tap_text(){   # tap the on-screen element whose text contains $1 (the page in the WebView is in the accessibility tree)
  for i in 1 2 3 4 5 6; do
    adb shell uiautomator dump /sdcard/mindit-ui.xml >/dev/null 2>&1
    adb shell cat /sdcard/mindit-ui.xml > /tmp/mindit-ui.xml 2>/dev/null
    XY=$(python3 /tmp/mindit-find.py "$1")
    if [ -n "$XY" ]; then adb shell input tap $XY; return 0; fi
    sleep 3
  done
  return 1
}
open_quiz(){ adb shell monkey -p "$PKG" -c android.intent.category.LAUNCHER 1 >/dev/null 2>&1; sleep 8; tap_text "Start New Game"; }
log(){ adb logcat -d 2>/dev/null | grep -o "MINDIT_FS $1[^\"]*" | head -1; }
crash(){ adb logcat -d -b crash 2>/dev/null | grep -A3 "FATAL EXCEPTION" | grep -m3 -E "Process: $PKG|Exception|Error" | tr '\n' ' ' | cut -c1-300; }

adb shell am force-stop "$PKG" >/dev/null 2>&1; adb logcat -c; adb logcat -b crash -c 2>/dev/null || true
if ! open_quiz; then echo "skip: couldn't find Start New Game on the app's home screen (the emulator's screen reader view)" > "$OUT"; cat "$OUT"; exit 0; fi
for i in $(seq 1 20); do [ -n "$(log saved)$(log failed)" ] && break; sleep 2; done
PAGE=$(log page); SAVED=$(log saved); FAILED=$(log failed); C1=$(crash)
if [ -z "$PAGE" ]; then
  [ -n "$C1" ] && { echo "fail: the quiz page crashed the app — $C1" > "$OUT"; cat "$OUT"; exit 0; }
  echo "skip: the quiz page didn't report (an APK from before build 141, or the page didn't open)" > "$OUT"; cat "$OUT"; exit 0; fi
if [ -z "$SAVED" ]; then echo "fail: the quiz page opened ($PAGE) but the complete copy wasn't saved in the tablet's files — ${FAILED:-no save reported in 40 s}${C1:+; crash: $C1}" > "$OUT"; cat "$OUT"; exit 0; fi
# close the app completely and open it again: the copy must come back from the files
adb shell am force-stop "$PKG"; sleep 2; adb logcat -c
if ! open_quiz; then echo "skip: saved ($SAVED) but couldn't open the quiz page again" > "$OUT"; cat "$OUT"; exit 0; fi
for i in $(seq 1 15); do [ -n "$(log found)" ] && break; sleep 2; done
FOUND=$(log found); C2=$(crash)
[ -n "$SHOT" ] && adb exec-out screencap -p > "$SHOT" 2>/dev/null
if [ -n "$FOUND" ] && [ "${FOUND#*nothing}" = "$FOUND" ] && [ -z "$C2" ]; then
  echo "ok: $SAVED; after closing and reopening the app: $FOUND" > "$OUT"
else
  echo "fail: $SAVED, but after reopening the app: ${FOUND:-the page did not read the files}${C2:+; crash: $C2}" > "$OUT"
fi
cat "$OUT"
