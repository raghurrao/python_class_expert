#!/bin/bash
echo "=== Day 22 Assignment Test ==="
awk '
{ status[$9]++ }
END {
  printf "=== HTTP STATUS CODE BREAKDOWN ===\n"
  for (s in status) {
    printf "Status %s : %d occurrences\n", s, status[s]
  }
}
' data/web_access.log
echo "============================="
