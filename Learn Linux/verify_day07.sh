#!/bin/bash
echo "=== Week 1 Capstone Test ==="
awk '
BEGIN {
  printf "=== SERVER FLEET AUDIT REPORT ===\n"
  printf "%-18s %-15s %-8s %-8s\n", "HOSTNAME", "IP", "CPU%", "RAM(GB)"
  printf "--------------------------------------------------------\n"
  active=0; inactive=0
}
NR > 1 {
  if ($4 == "Active") {
    printf "%-18s %-15s %-8.1f %-8.1f\n", $2, $3, $5, $6
    active++
  } else {
    inactive++
  }
}
END {
  printf "--------------------------------------------------------\n"
  printf "Active Servers: %d | Non-Active Servers: %d\n", active, inactive
}
' data/servers.txt
echo "============================="
