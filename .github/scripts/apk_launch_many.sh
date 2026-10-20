#!/bin/bash
# Open every APK in a folder on the running emulator, one after another (build 137). usage: apk_launch_many.sh <apk dir> <results dir>
mkdir -p "$2"
for a in "$1"/*.apk; do t=$(basename "$a" .apk); bash "$(dirname "$0")/apk_launch_test.sh" "$a" "$2/$t.txt" "$2/$t.png"
  bash "$(dirname "$0")/apk_save_test.sh" "$2/$t.save" "$2/$t-save.png"; done   # build 141: save and reopen a game (results *.save)
