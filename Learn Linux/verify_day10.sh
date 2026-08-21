#!/bin/bash
echo "=== Day 10 Assignment Test ==="
awk '
NR <= 3 {
  for (i = NF; i >= 1; i--) {
    printf "%s ", $i
  }
  print ""
}
' data/servers.txt
echo "============================="
