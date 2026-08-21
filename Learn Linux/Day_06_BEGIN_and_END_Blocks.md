# Day 6: BEGIN & END Special Blocks

Welcome to **Day 6**! Today you will learn about the special `BEGIN` and `END` blocks in `awk`.

---

## 1. Core Concepts

`awk` execution follows 3 phases:

1. **`BEGIN { ... }`**: Code executed **BEFORE** any input records are read. Use it for initialization (headers, variables, setting `FS` / `OFS`).
2. **`pattern { action }`**: Main loop executed **FOR EACH LINE** in input.
3. **`END { ... }`**: Code executed **AFTER** all input lines have been processed. Use it for summaries, totals, averages, and footers.

---

## 2. Examples & Commands

### Example 1: Header, Data, and Footer Summary
```bash
awk -F',' '
BEGIN { print "=== SALES REPORT HEADER ===" }
NR > 1 { printf "%-12s | $%8.2f\n", $2, $6 }
END { print "=== END OF REPORT ===" }
' data/sales_data.csv
```

### Example 2: Counting Records with `END`
```bash
awk '
BEGIN { count = 0 }
$4 == "Active" { count++ }
END { print "Total Active Servers:", count }
' data/servers.txt
```

---

## 📝 Day 6 Assignment & Practical Test

### Task 1: Complete User Account Report
Write an `awk` program using `data/sample_passwd.txt` that:
1. `BEGIN`: Prints header `"=== SYSTEM USERS ==="`
2. Main: Prints Username ($1) and UID ($3) for users with UID >= 1000
3. `END`: Prints footer `"=== END OF LIST ==="`

### Task 2: Count Active Web Servers
Write an `awk` script that counts how many servers in `data/servers.txt` have Hostname starting with `web` AND Status `"Active"`, printing the total in `END`.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day06.sh
```

---
*Next up: Day 7 - Week 1 Review & Practical Capstone Challenge*
