#!/bin/bash
echo "=== Day 27 Assignment Test ==="
awk '
NR > 1 {
  bars = int($5 / 10)
  bar_str = ""
  for (i=1; i<=10; i++) {
    if (i <= bars) bar_str = bar_str "#"
    else bar_str = bar_str "-"
  }
  printf "%-18s [%-10s] %5.1f%%\n", $2, bar_str, $5
}
' data/servers.txt
echo "============================="
