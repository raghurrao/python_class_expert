#!/bin/bash
echo "=== Day 23 Assignment Test ==="
ps aux | awk '
NR > 1 && $4 > 0.0 {
  printf "PID: %-6s | MEM: %5.1f%% | USER: %-10s | CMD: %s\n", $2, $4, $1, $11
}
' | head -n 5
echo "============================="
