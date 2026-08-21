# Day 8: Arithmetic & Aggregations (Sums, Averages, Min/Max)

Welcome to **Day 8**! Today you will learn how to perform calculations, compute totals, calculate averages, and find min/max values across columns in `awk`.

---

## 1. Core Concepts

### Math Operators
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Modulo (Remainder): `%`
- Exponentiation: `^`

### Accumulators
You can accumulate values across lines using variables in `awk`:
```bash
total += $6
count++
```

---

## 2. Examples & Commands

### Example 1: Summing a Column (Total RAM)
```bash
awk 'NR > 1 { sum += $6 } END { printf "Total RAM Used: %.2f GB\n", sum }' data/servers.txt
```

### Example 2: Calculating Column Average (Average Salary)
```bash
awk '
NR > 1 { sum += $5; count++ }
END { printf "Average Salary: $%.2f (Count: %d)\n", sum/count, count }
' data/employees.txt
```

### Example 3: Finding Maximum Value (Peak CPU)
```bash
awk '
NR > 1 { if ($5 > max) { max = $5; max_host = $2 } }
END { printf "Peak CPU Host: %s (%.1f%%)\n", max_host, max }
' data/servers.txt
```

---

## 📝 Day 8 Assignment & Practical Test

### Task 1: Calculate Total Revenue
Using `data/sales_data.csv`, sum TotalSales ($6) for all sales rows (skip header `NR > 1`) and print the total revenue formatted as `$%.2f`.

### Task 2: Average RAM Usage of Active Servers
Using `data/servers.txt`, calculate and print the **average RAM usage** (`$6`) across **Active servers only** (`$4 == "Active"`).

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day08.sh
```

---
*Next up: Day 9 - Conditional Statements (`if`, `else if`, `else`)*
