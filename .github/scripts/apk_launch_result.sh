#!/bin/bash
# Mind It! — turn the emulator launch test's result line (apk_launch_test.sh) into a message on the workflow run (build 137).
# usage: apk_launch_result.sh <result file> <label> [block [<release notes .md>]]
#   ok   → a notice (and, with release notes given, one line in them saying the app was opened on the emulator);
#   fail → an error; with "block" the step fails, so nothing after it runs (the release is not published);
#   skip, or no result → a warning: the emulator didn't run the test; the release goes ahead on the other checks.
F="$1"; L="$2"; BLOCK="${3:-}"; NOTES="${4:-}"
R=$(head -c 1500 "$F" 2>/dev/null | tr -d '\r' | tr '\n' ' ' | sed 's/ *$//')
case "$R" in
  ok*)
    echo "::notice title=$L opens on Android 15::$L — $R"
    if [ -n "$NOTES" ] && [ -f "$NOTES" ]; then
      printf '\n\n**Opened before publishing:** the tablet app was installed on an Android 15 emulator, opened from its icon, and was still open 20 seconds later with no crash.\n' >> "$NOTES"
    fi ;;
  fail*)
    echo "::error title=$L does not open on Android 15::$L — $R"
    if [ "$BLOCK" = block ]; then echo "Nothing is published: fix the APK, stage the build again."; exit 1; fi ;;
  *)
    echo "::warning title=$L — the emulator didn't run the test::$L — ${R:-no result}. The other checks decide." ;;
esac
exit 0
