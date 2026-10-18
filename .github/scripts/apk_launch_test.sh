#!/bin/bash
# Mind It! — open the Galaxy Tab app on an Android emulator the way a person does (tap the icon), and check it really opens.
# Since build 137 (owner: "do them all" — the launch test from the build-136 list). Builds 129–134 passed every file check
# but closed at once on the tablet; this test runs the app.
# usage: apk_launch_test.sh <apk> <result file> [<screenshot.png>]
# The result file gets one line: "ok …" or "fail …". No line at all means the emulator itself didn't run the test.
APK="$1"; OUT="$2"; SHOT="${3:-}"; PKG=com.mindit.app
note(){ echo "$*"; }
adb wait-for-device
adb uninstall "$PKG" >/dev/null 2>&1 || true
if ! adb install -r "$APK" > /tmp/install.txt 2>&1; then echo "fail: the APK didn't install — $(tr '\n' ' ' < /tmp/install.txt | cut -c1-300)" > "$OUT"; exit 0; fi
COMP=$(adb shell cmd package resolve-activity --brief -c android.intent.category.LAUNCHER "$PKG" 2>/dev/null | tail -1 | tr -d '\r')
adb logcat -c; adb logcat -b crash -c 2>/dev/null || true
adb shell monkey -p "$PKG" -c android.intent.category.LAUNCHER 1 > /tmp/monkey.txt 2>&1      # = tapping the app's icon
sleep 20
PID=$(adb shell pidof "$PKG" 2>/dev/null | tr -d '\r')
TOP=$(adb shell dumpsys activity activities 2>/dev/null | grep -E "topResumedActivity|mResumedActivity" | head -1 | tr -d '\r' | sed 's/^ *//')
CRASH=$(adb logcat -d -b crash 2>/dev/null | grep -A3 "FATAL EXCEPTION" | grep -m3 -E "Process: $PKG|Exception|Error" | tr '\n' ' ' | cut -c1-300)
WV=$(adb logcat -d 2>/dev/null | grep -c -i "chromium\|webview" || true)
[ -n "$SHOT" ] && adb exec-out screencap -p > "$SHOT" 2>/dev/null
if [ -n "$PID" ] && echo "$TOP" | grep -q "$PKG/.MainActivity\|$PKG/$PKG.MainActivity" && [ -z "$CRASH" ]; then
  echo "ok: opened and still running after 20 s (launcher → $COMP; on screen: ${TOP##* }; process $PID; WebView log lines $WV)" > "$OUT"
else
  echo "fail: launcher → ${COMP:-none}; on screen: ${TOP:-nothing}; process: ${PID:-not running}; crash: ${CRASH:-none}" > "$OUT"
fi
note "$(cat "$OUT")"
