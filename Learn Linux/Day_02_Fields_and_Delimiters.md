# Day 2: Fields & Custom Delimiters (`-F`, `FS`, `OFS`)

Welcome to **Day 2**! Today you will learn how `awk` breaks text into fields and how to process non-standard formats (like CSV files or colon-separated Linux files like `/etc/passwd`).

---

## 1. Core Concepts

### Field Separator (`FS` / `-F`)
By default, `awk` uses contiguous whitespace (spaces or tabs) to split lines into fields (`$1`, `$2`, etc.).
If your file uses a different delimiter (like `:`, `,`, or `|`), you must tell `awk` using either:
1. Command line flag: `awk -F':' '{ print $1 }' file`
2. Built-in variable inside `BEGIN`: `awk 'BEGIN { FS=":" } { print $1 }' file`

### Output Field Separator (`OFS`)
When you print multiple fields separated by commas in `awk`:
```bash
awk '{ print $1, $2 }' file
```
`awk` inserts the **Output Field Separator (`OFS`)** between them. By default, `OFS` is a single space. You can change `OFS` to a comma, colon, or tab!

---

## 2. Examples & Commands

### Example 1: Parsing `/etc/passwd` (Colon Delimited)
`/etc/passwd` uses colons `:` as field separators:
`username:password:UID:GID:comment:homedir:shell`

Extract Username ($1) and Shell ($7):
```bash
awk -F':' '{ print $1, $7 }' data/sample_passwd.txt
```

### Example 2: Parsing CSV Files (`-F','`)
`sales_data.csv` uses commas `,` as field separators:

Extract Date ($1), Region ($2), and TotalSales ($6):
```bash
awk -F',' '{ print $1, $2, $6 }' data/sales_data.csv
```

### Example 3: Changing Output Field Separator (`OFS`)
Format output as a TSV (Tab Separated Values) or custom separator:
```bash
awk -F':' 'BEGIN { OFS=" ---> " } { print $1, $6, $7 }' data/sample_passwd.txt
```

---

## 📝 Day 2 Assignment & Practical Test

Complete these 4 tasks in your terminal:

### Task 1: Extract Bash Users
**Goal:** Using `data/sample_passwd.txt`, print Username ($1) and Home Directory ($6) for all users who use `/bin/bash` as their shell ($7).
- *Hint:* `-F':'` and `$7 == "/bin/bash"`

### Task 2: CSV Electronics Sales Filter
**Goal:** Using `data/sales_data.csv`, extract Date ($1), Region ($2), and TotalSales ($6) for rows where Category ($3) is `"Electronics"`.
- *Hint:* `-F','` and `$3 == "Electronics"`

### Task 3: Custom Formatted User Output
**Goal:** Print all users from `data/sample_passwd.txt` formatted as: `User: <username> | UID: <uid>` using `OFS=" | "`.

### Task 4: Extracting System Users with UID < 10
**Goal:** Using `data/sample_passwd.txt`, extract Username ($1) and UID ($3) for all accounts with UID < 10.

---

### 🧪 Automated Assignment Verifier
Test your answers:
```bash
bash ./verify_day02.sh
```

---
*Next up: Day 3 - Built-in Variables (`NR`, `FNR`, `NF`, `FS`, `OFS`, `RS`, `ORS`)*
