# Day 18: Processing Multiple Input Files (`NR == FNR`, `FILENAME`)

Welcome to **Day 18**! Today you will learn the classic `awk` technique for joining, comparing, or looking up data between two files.

---

## 1. Core Idiom: `NR == FNR`

When passing two files to `awk`: `awk '...' file1.txt file2.txt`
- `NR`: Total line count across all files.
- `FNR`: Line count inside current file.

As long as `awk` is reading `file1.txt`, `NR == FNR` is **TRUE**.
As soon as it moves to `file2.txt`, `NR` continues incrementing, so `NR == FNR` becomes **FALSE**.

### Structure
```awk
NR == FNR {
    # Actions for File 1 (building lookup table in an array)
    lookup[$1] = $2
    next
}
{
    # Actions for File 2 (using lookup table)
    print $0, lookup[$1]
}
```

---

## 📝 Day 18 Assignment & Practical Test

### Task 1: Compare Files
Compare user accounts between `data/sample_passwd.txt` and `data/employees.txt` to find matching usernames.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day18.sh
```

---
*Next up: Day 19 - Advanced Regular Expressions*
