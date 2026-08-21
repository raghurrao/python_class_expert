# Day 13: Math & Numeric Functions (`int`, `sqrt`, `rand`, `srand`, `exp`, `log`)

Welcome to **Day 13**! Today you will learn built-in mathematical functions in `awk`.

---

## 1. Core Functions

- `int(x)`: Truncates `x` to an integer.
- `sqrt(x)`: Square root of `x`.
- `rand()`: Generates random floating point number between `0.0` and `1.0`.
- `srand(seed)`: Seeds random number generator (usually seeded with time).
- `log(x)`: Natural logarithm of `x`.
- `exp(x)`: Exponential `e^x`.

---

## 2. Examples & Commands

### Example 1: Truncating Decimals with `int()`
```bash
awk 'NR > 1 { printf "%-18s Integer CPU: %d%%\n", $2, int($5) }' data/servers.txt
```

### Example 2: Generating Random Data
```bash
awk 'BEGIN { srand(); for(i=1; i<=5; i++) print "Random:", int(rand()*100) }'
```

---

## 📝 Day 13 Assignment & Practical Test

### Task 1: Truncated Sales Amount
Using `data/sales_data.csv`, skip header (`NR > 1`) and print TotalSales ($6) truncated to integer using `int()`.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day13.sh
```

---
*Next up: Day 14 - Week 2 Review & Challenge*
