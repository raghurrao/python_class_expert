# Day 17: Multi-Dimensional Arrays & Dynamic `split()`

Welcome to **Day 17**! Today you will learn multi-key indexing (`arr[key1, key2]`) to aggregate data by multiple dimensions.

---

## 1. Core Concepts

In `awk`, multidimensional arrays are simulated using composite keys:
```awk
sales[region, category] += amount
```

---

## 2. Examples & Commands

### Example 1: Sales by Region AND Category
```bash
awk -F',' '
NR > 1 { sales[$2, $3] += $6 }
END {
  for (combined in sales) {
    split(combined, keys, SUBSEP)
    printf "Region: %-8s | Category: %-12s | Total: $%.2f\n", keys[1], keys[2], sales[combined]
  }
}
' data/sales_data.csv
```

---

## 📝 Day 17 Assignment & Practical Test

### Task 1: Department Payroll by Location
Using `data/employees.txt`, aggregate total salary by Department ($4) AND Location ($5) using composite keys `arr[$4, $5]`.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day17.sh
```

---
*Next up: Day 18 - Multi-File Processing (`FILENAME`, `NR == FNR`)*
