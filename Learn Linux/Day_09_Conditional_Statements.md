# Day 9: Conditional Statements (`if`, `else if`, `else`)

Welcome to **Day 9**! Today you will learn how to write complex decision logic inside `awk` actions using `if`, `else if`, `else`, and ternary operators (`? :`).

---

## 1. Core Syntax

```awk
if (condition1) {
    # action 1
} else if (condition2) {
    # action 2
} else {
    # fallback action
}
```

### Ternary Operator
`variable = (condition) ? true_val : false_val`

---

## 2. Examples & Commands

### Example 1: Categorizing Server CPU Usage
```bash
awk '
NR > 1 {
  if ($5 >= 80) {
    status = "CRITICAL"
  } else if ($5 >= 50) {
    status = "WARNING"
  } else {
    status = "OK"
  }
  printf "%-18s | CPU: %5.1f%% | Status: %s\n", $2, $5, status
}
' data/servers.txt
```

---

## 📝 Day 9 Assignment & Practical Test

### Task 1: Salary Grade Classification
Using `data/employees.txt`, skip header (`NR > 1`) and classify employees based on Salary ($5):
- Salary >= 80000: `"Senior Tier"`
- Salary >= 65000: `"Mid Tier"`
- Otherwise: `"Junior Tier"`
Print Name ($2 $3), Salary ($5), and Grade.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day09.sh
```

---
*Next up: Day 10 - Loops in `awk` (`for`, `while`)*
