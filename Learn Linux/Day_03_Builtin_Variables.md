# Day 3: Built-in Variables (`NR`, `FNR`, `NF`, `FS`, `OFS`, `RS`, `ORS`)

Welcome to **Day 3**! Today you will learn the essential built-in variables that give `awk` its power and state awareness.

---

## 1. Core Built-in Variables

| Variable | Description |
| :--- | :--- |
| `NR` | **Number of Records**: Total line number processed so far across all input files. |
| `FNR` | **File Record Number**: Line number relative to current file being read. |
| `NF` | **Number of Fields**: Count of columns on the current line. |
| `FS` | **Field Separator**: Input delimiter (default: whitespace). |
| `OFS` | **Output Field Separator**: Output delimiter (default: space). |
| `RS` | **Record Separator**: Input record delimiter (default: newline `\n`). |
| `ORS` | **Output Record Separator**: Output record delimiter (default: newline `\n`). |

---

## 2. Examples & Use Cases

### Example 1: Printing Line Numbers with `NR`
```bash
awk '{ print NR, $0 }' data/servers.txt
```

### Example 2: Skipping CSV Header Row (`NR > 1`)
When processing CSV files, `NR > 1` skips the header row:
```bash
awk -F',' 'NR > 1 { print $1, $3, $6 }' data/sales_data.csv
```

### Example 3: Filtering by Field Count (`NF`)
Print lines that have more than 5 columns:
```bash
awk 'NF >= 6 { print "Line", NR, "has", NF, "fields" }' data/servers.txt
```

---

## 📝 Day 3 Assignment & Practical Test

### Task 1: Print CSV Data without Header
Using `data/sales_data.csv`, print line number (`NR`), Region ($2), and TotalSales ($6) for all rows **except the header row**.

### Task 2: Count Columns per Line
Print the `ServerID` ($1) and the total number of fields (`NF`) for each row in `data/servers.txt`.

### Task 3: Display First 3 Rows Only
Write an `awk` command that prints only the first 3 lines of `data/sample_passwd.txt` using `NR`.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day03.sh
```

---
*Next up: Day 4 - Patterns & Matching (Regex `~`, `!~`, logical operators `&&`, `||`)*
