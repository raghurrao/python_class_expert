# Day 3: Text Data Parsing on the CLI (`cut`, `sort`, `uniq`, `grep`, `wc`)

Before loading raw data files into database tables, data engineers inspect, clean, and profile text data on the Linux command line.

---

## 1. Tool Overview

| Tool | Description | Common Flags | Example |
| :--- | :--- | :--- | :--- |
| `cut` | Extract specific delimiter-separated columns | `-d` (delimiter), `-f` (fields) | `cut -d',' -f2,4 data.csv` |
| `sort` | Sort lines of text files | `-n` (numeric), `-r` (reverse), `-k` (column) | `sort -t',' -k3,3nr data.csv` |
| `uniq` | Filter or count adjacent duplicate lines | `-c` (count), `-d` (duplicates only) | `sort data.txt \| uniq -c` |
| `wc` | Count lines, words, or bytes | `-l` (lines) | `wc -l data.csv` |
| `grep` | Pattern matching with Regular Expressions | `-i` (ignore case), `-v` (invert match) | `grep -E "^[0-9]+" data.csv` |

---

## 2. Combining Tools into Data Profiling Pipelines

### Example: Find top 3 most common user roles in a CSV
```bash
# Skip header (tail -n +2), cut column 3 (role), sort, count unique occurrences, sort descending numerically
tail -n +2 dataset.csv | cut -d',' -f3 | sort | uniq -c | sort -nr | head -n 3
```

---

## 3. Hands-On Practical Exercise (Day 3)

Run `01_linux_basics/day3_parsing.sh` to profile a sample web server log and customer dataset!
