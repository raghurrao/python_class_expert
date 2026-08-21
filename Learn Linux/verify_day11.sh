#!/bin/bash
echo "=== Day 11 Assignment Test ==="
awk '
NR > 1 {
  split($3, ip, ".")
  printf "%-18s Subnet: %s.%s.%s\n", $2, ip[1], ip[2], ip[3]
}
' data/servers.txt
echo "============================="
