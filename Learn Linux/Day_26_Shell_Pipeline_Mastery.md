# Day 26: Shell Pipeline Mastery (`awk` + `grep` + `sort` + `uniq`)

Welcome to **Day 26**! Today you will learn how `awk` interacts with core Linux CLI utilities (`grep`, `sed`, `sort -k`, `uniq -c`, `head`).

---

## 📝 Day 26 Assignment & Practical Test

### Task 1: Top IP Address Extractor Pipeline
Combine `awk '{ print $1 }' data/web_access.log | sort | uniq -c | sort -nr | head -n 3` to find top 3 visiting IPs.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day26.sh
```

---
*Next up: Day 27 - Custom Text Dashboards & Reporting*
