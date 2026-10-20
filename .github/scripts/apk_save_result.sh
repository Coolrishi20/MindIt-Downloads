#!/bin/bash
# Mind It! — turn the emulator save check's result line (apk_save_test.sh, build 141) into a message on the workflow run.
# usage: apk_save_result.sh <result file> <label> [block [<release notes .md>]]
#   ok   → a notice (and, with release notes given, one line in them);
#   fail → an error; with "block" the step fails, so nothing after it runs (the release is not published);
#   skip, or no result → a warning: the emulator couldn't run this check; the release goes ahead on the other checks.
F="$1"; L="$2"; BLOCK="${3:-}"; NOTES="${4:-}"
R=$(head -c 1500 "$F" 2>/dev/null | tr -d '\r' | tr '\n' ' ' | sed 's/ *$//')
case "$R" in
  ok*)
    echo "::notice title=$L keeps a saved game::$L — $R"
    if [ -n "$NOTES" ] && [ -f "$NOTES" ]; then
      printf '\n**Saved and reopened before publishing:** on the same emulator the quiz page saved its complete copy of the game into the tablet app'"'"'s own files, and found it again after the app was closed and reopened.\n' >> "$NOTES"
    fi ;;
  fail*)
    echo "::error title=$L doesn't keep a saved game::$L — $R"
    if [ "$BLOCK" = block ]; then echo "Nothing is published: fix the APK, stage the build again."; exit 1; fi ;;
  *)
    echo "::warning title=$L — the emulator didn't run the save check::$L — ${R:-no result}. The other checks decide." ;;
esac
exit 0
