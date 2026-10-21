#!/bin/bash
# Mind It! — open the Galaxy Tab app on an Android emulator the way a person does (tap the icon), and check it really opens.
# Since build 137 (owner: "do them all" — the launch test from the build-136 list). Builds 129–134 passed every file check
# but closed at once on the tablet; this test runs the app.
# usage: apk_launch_test.sh <apk> <result file> [<screenshot.png>]
# The result file gets one line:
#   "ok: …"   the app opened and is still open 20 seconds later, with no crash;
#   "fail: …" the APK doesn't install (a fault in the APK) or the app doesn't open / closes / crashes;
#   "skip: …" the emulator had a problem of its own (no device, no space) — the APK was not judged.
# No line at all also means the emulator itself didn't run the test.
APK="$1"; OUT="$2"; SHOT="${3:-}"; PKG=com.mindit.app
# A crash counts only when Android's crash log names this app's own process ("Process: com.mindit.app, PID: …").
# Since build 145: the emulator's screen reader tool (uiautomator, which the save check runs to find buttons) can itself crash
# as it closes ("FATAL EXCEPTION: UiAutomation … Bad file descriptor", a shell process with no "Process:" line); the build 145
# release run stopped on that line although the app kept running and found its saved game. Other processes' crashes are only noted.
crash(){ adb logcat -d -b crash 2>/dev/null | awk -v P="$PKG" '/FATAL EXCEPTION/{b=1;m=0;n=0;x="";next} b{n++; if(index($0,"Process: " P ",")||index($0,"Process: " P ":")){m=1;p=$0} else if(m&&x==""&&$0~/(Exception|Error)/)x=$0; if(n>=3){ if(m){print p" "x; exit} b=0 }}' | tr -s ' ' | cut -c1-300; }
others(){ adb logcat -d -b crash 2>/dev/null | awk -v P="$PKG" '/FATAL EXCEPTION/{t=$0; sub(/.*FATAL EXCEPTION: */,"",t); getline q; if(index(q,"Process: " P ",")||index(q,"Process: " P ":")) next; sub(/.*Process: */,"",q); if(q~/AndroidRuntime/) q=""; o=o (o?", ":"") t (q?" in "q:"")} END{print o}' | cut -c1-200; }
: > "$OUT"
if ! timeout 120 adb wait-for-device; then echo "skip: no emulator answered (adb wait-for-device)" > "$OUT"; cat "$OUT"; exit 0; fi
adb uninstall "$PKG" >/dev/null 2>&1 || true
if ! timeout 180 adb install -r "$APK" > /tmp/install.txt 2>&1; then
  MSG=$(tr '\n' ' ' < /tmp/install.txt | cut -c1-300)
  if grep -q "INSTALL_FAILED_INSUFFICIENT_STORAGE" /tmp/install.txt || ! grep -q "INSTALL_" /tmp/install.txt; then
    echo "skip: the emulator couldn't install it (not a fault in the APK) — $MSG" > "$OUT"
  else
    echo "fail: the APK doesn't install — $MSG" > "$OUT"
  fi
  cat "$OUT"; exit 0
fi
COMP=$(adb shell cmd package resolve-activity --brief -c android.intent.category.LAUNCHER "$PKG" 2>/dev/null | tail -1 | tr -d '\r')
adb logcat -c; adb logcat -b crash -c 2>/dev/null || true
adb shell monkey -p "$PKG" -c android.intent.category.LAUNCHER 1 > /tmp/monkey.txt 2>&1      # = tapping the app's icon
sleep 20
PID=$(adb shell pidof "$PKG" 2>/dev/null | tr -d '\r')
TOP=$(adb shell dumpsys activity activities 2>/dev/null | grep -E "topResumedActivity|mResumedActivity" | head -1 | tr -d '\r' | sed 's/^ *//')
ONS=$(echo "$TOP" | grep -oE "[A-Za-z0-9_.]+/[A-Za-z0-9_.\$]+" | head -1)
CRASH=$(crash); OTHER=$(others)
WV=$(adb logcat -d 2>/dev/null | grep -c -i "chromium\|webview" || true)
[ -n "$SHOT" ] && adb exec-out screencap -p > "$SHOT" 2>/dev/null
if [ -n "$PID" ] && [ "${ONS%%/*}" = "$PKG" ] && [ -z "$CRASH" ]; then
  echo "ok: opened and still open after 20 s (icon → $COMP; on screen: $ONS; process $PID; WebView log lines $WV)${OTHER:+ (not the app: the emulator crash log also has $OTHER)}" > "$OUT"
else
  echo "fail: icon → ${COMP:-nothing}; on screen: ${ONS:-${TOP:-nothing}}; process: ${PID:-not running}; crash: ${CRASH:-none}" > "$OUT"
fi
cat "$OUT"
