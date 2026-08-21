# Day 12: String Manipulation Part 2 (`sub`, `gsub`, `match`, `tolower`, `toupper`)

Welcome to **Day 12**! Today you will learn search and replace functions (`sub`, `gsub`) and case conversion in `awk`.

---

## 1. Core Functions

- `sub(regex, repl, target)`: Replaces FIRST occurrence of `regex` with `repl` in `target` (defaults to `$0`).
- `gsub(regex, repl, target)`: Replaces ALL occurrences of `regex` with `repl` in `target` (global replace).
- `tolower(str)`: Converts string to lowercase.
- `toupper(str)`: Converts string to uppercase.
- `match(str, regex)`: Returns starting index of `regex` match in `str`.

---

## 2. Examples & Commands

### Example 1: Global Substitution with `gsub()`
Replace all colons `:` with spaces:
```bash
awk -F':' '{ gsub(/:/, " | "); print $0 }' data/sample_passwd.txt
```

### Example 2: Uppercase Conversion
```bash
awk '{ print toupper($2), $3 }' data/servers.txt
```

---

## 📝 Day 12 Assignment & Practical Test

### Task 1: Clean Log Timestamp Brackets
Using `data/web_access.log`, use `gsub(/\[|\]/, "")` to strip the brackets `[` and `]` from the timestamp field ($4).

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day12.sh
```

---
*Next up: Day 13 - Math & Numeric Functions*
