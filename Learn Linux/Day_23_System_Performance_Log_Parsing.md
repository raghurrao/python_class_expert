# Day 23: System Performance Log Parsing (`ps aux`, `df -h`)

Welcome to **Day 23**! Today you will parse live system monitoring commands (`ps aux`, `df -h`, `free`) with `awk`.

---

## 📝 Day 23 Assignment & Practical Test

### Task 1: Find Top Memory Consuming Processes from `ps aux`
Pipe `ps aux` to `awk` to find processes consuming **more than 0.5% memory** (`$4 > 0.5`).

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day23.sh
```

---
*Next up: Day 24 - Complex Record & Field Separators (`RS=""`)*
