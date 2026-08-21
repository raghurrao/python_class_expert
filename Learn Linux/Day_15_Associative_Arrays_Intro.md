# Day 15: Introduction to Associative Arrays

Welcome to **Day 15**! Today you will learn one of `awk`'s most powerful features: **Associative Arrays** (key-value maps).

---

## 1. Core Concepts

Unlike arrays in languages like C/Java that use numeric indices `0, 1, 2`, `awk` arrays are **associative**. Indices can be **strings**!

### Syntax
```awk
count["192.168.1.10"]++
total["Electronics"] += 3000
```

---

## 2. Examples & Commands

### Example 1: Count Frequency of IP Addresses in Web Logs
```bash
awk '{ ip[$1]++ } END { for (i in ip) print i, "Requests:", ip[i] }' data/web_access.log
```

### Example 2: Total Revenue by Category
```bash
awk -F',' 'NR > 1 { revenue[$3] += $6 } END { for (cat in revenue) printf "%-15s : $%.2f\n", cat, revenue[cat] }' data/sales_data.csv
```

---

## 📝 Day 15 Assignment & Practical Test

### Task 1: Count Employees per Department
Using `data/employees.txt`, skip header (`NR > 1`) and count the number of employees in each **Department** ($4) using associative arrays. Print in `END`.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day15.sh
```

---
*Next up: Day 16 - Array Operations & Iteration*
