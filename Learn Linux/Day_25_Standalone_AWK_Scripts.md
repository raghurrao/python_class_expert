# Day 25: Standalone `awk` Scripts (`#!/usr/bin/awk -f`, `-v var=val`)

Welcome to **Day 25**! Today you will learn how to turn `awk` code into executable standalone scripts and pass bash variables into `awk`.

---

## 1. Passing Shell Variables with `-v`
```bash
threshold=50
awk -v limit="$threshold" '$5 > limit { print $2, $5 }' data/servers.txt
```

---

## 📝 Day 25 Assignment & Practical Test

### Task 1: Dynamic CPU Limit Script
Pass a shell variable `MIN_RAM=10` into `awk` using `-v min_ram="$MIN_RAM"` to filter servers with RAM >= MIN_RAM.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day25.sh
```

---
*Next up: Day 26 - Shell Pipeline Mastery*
