#!/bin/bash
# Open every APK in a folder on the running emulator, one after another (build 137). usage: apk_launch_many.sh <apk dir> <results dir>
mkdir -p "$2"
for a in "$1"/*.apk; do t=$(basename "$a" .apk); bash "$(dirname "$0")/apk_launch_test.sh" "$a" "$2/$t.txt" "$2/$t.png"; done
