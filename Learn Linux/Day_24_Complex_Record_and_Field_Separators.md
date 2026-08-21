# Day 24: Complex Record & Field Separators (`RS=""`, Multi-line Records)

Welcome to **Day 24**! Today you will learn how to process multi-line records separated by blank lines using `RS=""`.

---

## 1. Multi-line Records (`RS=""`)
Setting `RS=""` (empty record separator) tells `awk` that **paragraphs / multi-line blocks separated by blank lines** are single records!
`FS="\n"` sets each line in the block as a field (`$1`, `$2`, `$3`).

---

## 📝 Day 24 Assignment & Practical Test

### Task 1: Parse Multi-line Contact Cards
Using `data/multiline_contacts.txt`, set `BEGIN { RS=""; FS="\n" }` and print Name ($1) and Email ($2) on a single line.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day24.sh
```

---
*Next up: Day 25 - Standalone `awk` Scripts (`#!/usr/bin/awk -f`, `-v`)*
