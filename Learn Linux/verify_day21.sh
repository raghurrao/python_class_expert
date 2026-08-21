#!/bin/bash
echo "=== Week 3 Capstone Test ==="
awk '
{
  reqs[$1]++
  bytes[$1] += $10
  total_bytes += $10
}
END {
  printf "=== WEB TRAFFIC AUDIT ===\n"
  printf "%-16s | %-8s | %-12s | %-8s\n", "IP ADDRESS", "REQUESTS", "BANDWIDTH", "TRAFFIC%"
  printf "--------------------------------------------------------\n"
  for (ip in reqs) {
    pct = (total_bytes > 0) ? (bytes[ip]/total_bytes)*100 : 0
    printf "%-16s | %-8d | %8d B | %6.1f%%\n", ip, reqs[ip], bytes[ip], pct
  }
}
' data/web_access.log
echo "============================="
