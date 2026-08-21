#!/bin/bash
echo "=== Week 2 Capstone Test ==="
awk -F',' '
NR > 1 {
  units += $4
  total += $6
  count++
  if ($6 > max) max = $6
}
END {
  printf "=== SALES SUMMARY ===\n"
  printf "Total Transactions : %d\n", count
  printf "Total Units Sold   : %d\n", units
  printf "Total Revenue      : $%.2f\n", total
  printf "Average Sale Value : $%.2f\n", total/count
  printf "Max Single Sale    : $%.2f\n", max
}
' data/sales_data.csv
echo "============================="
