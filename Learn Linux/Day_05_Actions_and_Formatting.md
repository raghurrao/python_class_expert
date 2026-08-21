# Day 5: Actions & Formatting (`print` vs `printf`)

Welcome to **Day 5**! Today you will master output formatting using `printf` to generate perfectly aligned tabular reports.

---

## 1. Core Concepts

### `print` vs `printf`
- `print`: Simple output, automatically adds newline `\n` and inserts `OFS` between comma-separated arguments.
- `printf`: C-style formatted output. Gives full control over padding, width, alignment, and decimal precision. **Does NOT automatically add a newline** (you must append `\n`).

### Common `printf` Specifiers
- `%s` : String
- `%d` : Integer
- `%.2f` : Floating point number rounded to 2 decimal places
- `%-15s` : Left-aligned string padded to 15 characters 
- |Hello          |
- |←---- 15 ----→|
- `%10d` : Right-aligned integer padded to 10 characters

---

## 2. Examples & Commands

### Example 1: Aligned Columns with `printf`
```bash
awk 'NR > 1 { printf "%-15s %-15s %6.2f GB\n", $2, $3, $6 }' data/servers.txt
```

### Example 2: Formatted Financial Report
```bash
awk -F',' 'NR > 1 { printf "%-12s | %-12s | $%8.2f\n", $1, $3, $6 }' data/sales_data.csv
```

---

## 📝 Day 5 Assignment & Practical Test

### Task 1: Aligned Server Metrics Report
Using `data/servers.txt`, skip the header row (`NR > 1`) and print Hostname ($2), Status ($4), and CPU Usage ($5) formatted with left alignment:
`printf "%-18s %-12s %6.1f%%\n"`

### Task 2: Employee Salary Table
Using `data/employees.txt`, print Name ($2 $3), Department ($4), and Salary ($5) formatted nicely as:
`printf "%-20s %-15s $%7d\n"`

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day05.sh
```

---
*Next up: Day 6 - BEGIN and END Blocks*
