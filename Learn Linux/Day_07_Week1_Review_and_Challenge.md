# Day 7: Week 1 Review & Practical Capstone Challenge

Congratulations on completing **Week 1**! Today you will put everything you learned together in a comprehensive practical test.

---

## Week 1 Concept Recap
- **Day 1:** Syntax `awk 'pattern { action }'`, `$0`..`$NF`, running one-liners.
- **Day 2:** Custom field separators (`-F`, `FS`, `OFS`) for CSV and `/etc/passwd`.
- **Day 3:** Built-in variables (`NR`, `FNR`, `NF`, `FS`, `OFS`, `RS`, `ORS`).
- **Day 4:** Regex matching (`~`, `!~`), logic (`&&`, `||`).
- **Day 5:** Formatting outputs (`printf`, column alignment).
- **Day 6:** Execution workflow (`BEGIN`, main, `END` blocks).

---

## 📝 Week 1 Capstone Challenge

### Challenge 1: Server Fleet Health Audit
Using `data/servers.txt`, write an `awk` program that outputs a clean report:
1. `BEGIN`: Print title `"=== SERVER FLEET AUDIT REPORT ==="` and column headers `HOSTNAME`, `IP`, `CPU%`, `RAM(GB)`.
2. Body: For all **Active** servers (`$4 == "Active"`), print Hostname, IP, CPU Usage, and RAM Usage formatted with `printf`.
3. `END`: Print total count of active servers and total count of inactive/maintenance servers.

---

### 🧪 Automated Assignment Verifier
```bash
bash ./verify_day07.sh
```

---
*Next up: Week 2 - Day 8 Arithmetic & Aggregations*
