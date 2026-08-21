#!/bin/bash
echo "=== Day 15 Assignment Test ==="
awk '
NR > 1 { dept[$4]++ }
END {
  for (d in dept) {
    printf "Department: %-15s | Count: %d\n", d, dept[d]
  }
}
' data/employees.txt
echo "============================="
