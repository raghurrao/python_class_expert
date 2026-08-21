# Day 11: String Manipulation Part 1 (`length`, `substr`, `index`, `split`)

Welcome to **Day 11**! Today you will learn built-in string functions to inspect, slice, and split string data in `awk`.

---

## 1. Core Built-in String Functions

| Function | Description | Example |
| :--- | :--- | :--- |
| `length(str)` | Returns character count of `str`. | `length($2)` |
| `substr(str, pos, len)` | Extracts substring starting at 1-indexed `pos`. | `substr($1, 1, 10)` |
| `index(str, target)` | Returns 1-indexed position of `target` in `str` (or 0 if not found). | `index($0, "GET")` |
| `split(str, arr, delim)` | Splits `str` into array `arr` using `delim`. Returns field count. | `split($4, a, "/")` |

---

## 2. Examples & Commands

### Example 1: Extract Date Parts using `split()`
```bash
awk -F',' 'NR > 1 { split($1, date, "-"); print "Year:", date[1], "Month:", date[2], "Day:", date[3] }' data/sales_data.csv
```

### Example 2: Length of User Names
```bash
awk -F':' '{ print $1, "Length:", length($1) }' data/sample_passwd.txt
```

---

## 📝 Day 11 Assignment & Practical Test

### Task 1: Extract Substring IP Subnet
Using `data/servers.txt`, extract the first 3 octets of IP ($3) using `split(IP, octets, ".")` and print `octets[1]"."octets[2]"."octets[3]`.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day11.sh
```

---
*Next up: Day 12 - String Manipulation Part 2 (`sub`, `gsub`, `match`, `tolower`, `toupper`)*
