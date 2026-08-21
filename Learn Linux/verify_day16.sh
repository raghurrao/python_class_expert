#!/bin/bash
echo "=== Day 16 Assignment Test ==="
awk '
NR > 1 { payroll[$5] += $4 }
END {
  for (loc in payroll) {
    printf "Location: %-12s | Total Salary: $%d\n", loc, payroll[loc]
  }
}
' data/employees.txt
echo "============================="
