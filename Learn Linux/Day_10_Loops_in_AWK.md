# Day 10: Loops in `awk` (`for`, `while`, `do-while`, `next`)

Welcome to **Day 10**! Today you will learn how to loop over fields and lines in `awk`.

---

## 1. Core Syntax

### `for` Loop
```awk
for (i = 1; i <= NF; i++) {
    print $i
}
```

### `while` Loop
```awk
i = 1
while (i <= NF) {
    print $i
    i++
}
```

### Flow Control Keywords
- `next`: Immediately stops processing the current record and skips to the NEXT line in the input file.
- `break`: Exits current loop.
- `continue`: Skips to next iteration of loop.

---

## 2. Examples & Commands

### Example 1: Print Each Field on a New Line
```bash
awk '{ for (i=1; i<=NF; i++) print "Field", i, ":", $i }' data/multiline_contacts.txt
```

---

## 📝 Day 10 Assignment & Practical Test

### Task 1: Reverse Column Order Output
Using `data/servers.txt`, write a loop that prints the fields of each line in **reverse order** (from `$NF` down to `$1`).

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day10.sh
```

---
*Next up: Day 11 - Built-in String Functions Part 1*
