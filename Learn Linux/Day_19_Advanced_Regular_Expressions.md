# Day 19: Advanced Regular Expressions in `awk`

Welcome to **Day 19**! Today you will learn advanced regex patterns, capture techniques, and using `match()` with `RSTART` and `RLENGTH`.

---

## 1. Special Match Variables

When `match(string, regex)` succeeds:
- `RSTART`: Character index where match started.
- `RLENGTH`: Length of matched substring.

`substr(string, RSTART, RLENGTH)` extracts the exact matched string!

---

## 📝 Day 19 Assignment & Practical Test

### Task 1: Extract User Agent with `match()`
Using `data/web_access.log`, extract the User-Agent string enclosed in quotes.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day19.sh
```

---
*Next up: Day 20 - User-Defined Functions*
