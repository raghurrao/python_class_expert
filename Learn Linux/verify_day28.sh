#!/bin/bash
echo "=== Day 28 Assignment Test ==="
df -h | awk '
NR > 1 {
  pct = $5
  gsub(/%/, "", pct)
  if (pct >= 10) {
    printf "[WARNING ALERT] Mount: %-15s | Use: %d%%\n", $6, pct
  }
}
'
echo "============================="
