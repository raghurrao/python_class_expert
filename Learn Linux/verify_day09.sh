#!/bin/bash
echo "=== Day 9 Assignment Test ==="
awk '
NR > 1 {
  if ($5 >= 80000) grade = "Senior Tier"
  else if ($5 >= 65000) grade = "Mid Tier"
  else grade = "Junior Tier"
  printf "%-18s | $%6d | Tier: %s\n", $2" "$3, $5, grade
}
' data/employees.txt
echo "============================="
