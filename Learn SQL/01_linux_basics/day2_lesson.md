# Day 2: Linux I/O Redirection & Pipes for Data Processing

In Data Engineering and Database Operations, data flows continuously between commands, files, scripts, and database engines. Master **I/O Redirection** and **Piping** to manipulate data streams efficiently.

---

## 1. The Standard Data Streams

Linux processes communicate via 3 standard channels:
1. `stdin` (Standard Input - `0`): Input data stream (keyboard or file).
2. `stdout` (Standard Output - `1`): Normal command output stream.
3. `stderr` (Standard Error - `2`): Error log stream.

---

## 2. Redirection Operators

| Operator | Action | Example |
| :--- | :--- | :--- |
| `>` | Redirect `stdout` to a file (overwrites) | `echo "id,name" > users.csv` |
| `>>` | Redirect `stdout` to a file (appends) | `echo "1,Alice" >> users.csv` |
| `2>` | Redirect `stderr` (errors) to a file | `ls nonexistent 2> error.log` |
| `2>&1` | Combine `stderr` with `stdout` | `command > output.log 2>&1` |
| `<` | Redirect file into `stdin` | `sqlite3 my.db < query.sql` |

---

## 3. The Power of Pipes (`|`)

The pipe operator `|` passes the `stdout` of one command directly into the `stdin` of the next command.

```bash
# Example: Inspect top 5 lines of log file containing "ERROR"
cat server.log | grep "ERROR" | head -n 5
```

---

## 4. Viewing File Contents (`head`, `tail`, `cat`)

```bash
# View entire file
cat users.csv

# View first 10 lines
head -n 10 dataset.csv

# View last 10 lines (great for monitoring log files)
tail -n 10 server.log

# Continuously stream new log entries (follow mode)
tail -f server.log
```

---

## 5. Hands-On Practical Exercise (Day 2)

Run `01_linux_basics/day2_pipes.sh` to see redirection and pipes in action with a sample dataset!
