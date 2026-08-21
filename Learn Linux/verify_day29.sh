#!/bin/bash
echo "=== Day 29 Assignment Test ==="
awk '
BEGIN { print "[" }
NR > 1 {
  printf "  {\"id\": %d, \"hostname\": \"%s\", \"ip\": \"%s\", \"status\": \"%s\"}%s\n", $1, $2, $3, $4, (NR < 8 ? "," : "")
}
END { print "]" }
' data/servers.txt
echo "============================="
