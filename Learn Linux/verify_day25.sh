#!/bin/bash
echo "=== Day 25 Assignment Test ==="
MIN_RAM=10
awk -v min="$MIN_RAM" '
NR > 1 && $6 >= min {
  printf "Server: %-18s | RAM: %.1f GB (>= %d GB limit)\n", $2, $6, min
}
' data/servers.txt
echo "============================="
