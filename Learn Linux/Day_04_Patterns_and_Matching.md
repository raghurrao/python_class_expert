# Day 4: Patterns & Matching (`~`, `!~`, `&&`, `||`)

Welcome to **Day 4**! Today you will learn advanced pattern filtering using regular expression matching (`~` matches, `!~` does not match) and combining conditions with logical AND (`&&`) / OR (`||`).

---

## 1. Core Concepts

### Regex Operators
- `$N ~ /pattern/` : True if field N matches regular expression `pattern`.
- `$N !~ /pattern/` : True if field N DOES NOT match regular expression `pattern`.

### Logical Operators
- `&&` (AND): Both conditions must be true.
- `||` (OR): At least one condition must be true.
- `!` (NOT): Negates condition.

---

## 2. Examples & Commands

### Example 1: Regex Matching on Specific Field (`~`)
Find servers whose hostname ($2) starts with `"web"`:
```bash
awk '$2 ~ /^web/ { print $1, $2, $3 }' data/servers.txt
```

### Example 2: Negative Regex Match (`!~`)
Find web access logs where the HTTP status code ($9) is NOT 200:
```bash
awk '$9 !~ /^200$/ { print $1, $6, $7, $9 }' data/web_access.log
```

### Example 3: Combining Conditions with `&&`
Find active servers with CPU usage ($5) > 50%:
```bash
awk '$4 == "Active" && $5 > 50 { print $2, "CPU:", $5 }' data/servers.txt
```

---

## 📝 Day 4 Assignment & Practical Test

### Task 1: Web & DB Server Search
Find all servers in `data/servers.txt` where Hostname ($2) matches either `web` OR `db`.

### Task 2: Active High RAM Servers
Extract Hostname ($2) and RAM ($6) for active servers (`$4 == "Active"`) using **more than 8 GB of RAM** (`$6 > 8`).

### Task 3: HTTP Error Log Extractor
Using `data/web_access.log`, extract IP ($1) and Status Code ($9) for requests where status code is 400 or higher (`$9 >= 400`).

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day04.sh
```

---
*Next up: Day 5 - Actions & Formatting (`print` vs `printf`, column alignment)*
