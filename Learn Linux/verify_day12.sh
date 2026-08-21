#!/bin/bash
echo "=== Day 12 Assignment Test ==="
awk '{
  time = $4
  gsub(/\[|\]/, "", time)
  print $1, "Time:", time
}' data/web_access.log | head -n 5
echo "============================="
