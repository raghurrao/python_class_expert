#!/bin/bash
echo "=== Day 17 Assignment Test ==="
awk '
NR > 1 { payroll[$4, $5] += $4 }
END {
  for (k in payroll) {
    split(k, keys, SUBSEP)
    printf "Dept: %-12s | Location: %-10s | Payroll: $%d\n", keys[1], keys[2], payroll[k]
  }
}
' data/employees.txt
echo "============================="
