# Day 16: Array Operations & Iteration (`for (k in arr)`, `in`, `delete`)

Welcome to **Day 16**! Today you will learn advanced array manipulations: testing key existence with `in`, deleting keys, and sorting array outputs.

---

## 1. Core Syntax

### Testing Key Existence
```awk
if (key in array) {
    print "Key exists!"
}
```

### Deleting Keys
```awk
delete array[key]
```

---

## 2. Examples & Commands

### Example 1: Count HTTP Status Codes
```bash
awk '{ status[$9]++ } END { for (s in status) printf "HTTP Status %s : %d requests\n", s, status[s] }' data/web_access.log
```

---

## 📝 Day 16 Assignment & Practical Test

### Task 1: Department Total Payroll
Using `data/employees.txt`, calculate total payroll per Location ($5) and print location totals.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day16.sh
```

---
*Next up: Day 17 - Multi-Dimensional Arrays & `split()`*
