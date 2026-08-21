# Day 20: User-Defined Functions

Welcome to **Day 20**! Today you will learn how to define your own reusable functions in `awk`.

---

## 1. Syntax

```awk
function format_currency(val) {
    return sprintf("$%.2f", val)
}
```

---

## 📝 Day 20 Assignment & Practical Test

### Task 1: Custom Bytes-to-Human Formatter
Write a custom `awk` function `human_bytes(b)` that converts raw byte values into KB or MB.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day20.sh
```

---
*Next up: Day 21 - Week 3 Review & Challenge*
