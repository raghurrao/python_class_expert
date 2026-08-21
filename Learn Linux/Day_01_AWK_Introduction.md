# Day 1: Introduction to `awk` & Syntax Fundamentals

Welcome to **Day 1** of your 30-Day `awk` Mastery Course! Today, you will learn what `awk` is, how its basic execution syntax works, and how to write your first `awk` one-liners.

---

## 1. Core Concepts

### What is `awk`?
`awk` is a domain-specific programming language designed for **text processing, data extraction, and report generation**. It is standard on virtually all Unix/Linux systems (Aho, Weinberger, and Kernighan created it in 1977; hence the name **A-W-K**).

Unlike simple text utilities like `cat` or `grep`, `awk` treats input data as a collection of **records** (lines by default) and **fields** (words/columns separated by whitespace by default).

### Basic Syntax Structure
The fundamental pattern of an `awk` program is:

```bash
awk 'pattern { action }' filename
```

- **`pattern`**: A condition or regular expression that determines *which* lines to process. If omitted, `awk` executes the action on **every line**.
- **`action`**: Code inside curly braces `{ ... }` that determines *what to do* when a pattern matches. If omitted, `awk` prints the entire matching line by default.

---

## 2. Basic One-Liners & Field Identifiers

### Printing the Entire Line (`$0`)
In `awk`, `$0` represents the complete current line (record).

```bash
awk '{ print $0 }' data/servers.txt
```
*Result:* Prints every line in `data/servers.txt` (similar to `cat`).

### Printing Specific Columns / Fields (`$1`, `$2`, `$3`...)
`awk` automatically splits each line into space-delimited columns:
- `$1` = First field (column 1)
- `$2` = Second field (column 2)
- `$3` = Third field (column 3)
- `$NF` = Last field (NF = Number of Fields)

#### Example 1: Extract Hostname ($2) and IP Address ($3)
```bash
awk '{ print $2, $3 }' data/servers.txt
```

#### Example 2: Extract Hostname ($2) and Status ($4)
```bash
awk '{ print $2, $4 }' data/servers.txt
```

#### Example 3: Extract ServerID ($1) and the Last Column ($NF)
```bash
awk '{ print $1, $NF }' data/servers.txt
```

---

## 3. Filtering Input with Patterns

You can prefix actions with a pattern to only process matching rows.

### Pattern Matching with Strings
Print only rows where the line contains the word `"Active"`:
```bash
awk '/Active/ { print $2, $3, $4 }' data/servers.txt
```

### Pattern Matching with Logical Comparisons
Print servers where CPU Usage ($5) is greater than 50%:
```bash
awk '$5 > 50 { print $2, "High CPU:", $5 }' data/servers.txt
```

Print servers where Status ($4) is NOT equal to `"Active"`:
```bash
awk '$4 != "Active" { print $2, $4 }' data/servers.txt
```

---

## 4. Input via Pipes (`|`)

`awk` works seamlessly in shell pipelines:

```bash
ps aux | awk '{ print $1, $2, $3, $11 }' | head -n 10
```
This pipes the output of `ps aux` into `awk`, extracting User ($1), PID ($2), CPU% ($3), and Command ($11).

---

## 5. Day 1 Practical Exercises

Run these commands in your terminal inside `/home/raghurao/Learnings/Learn Linux`:

1. Change directory to your learning workspace:
   ```bash
   cd "/home/raghurao/Learnings/Learn Linux"
   ```
2. Print only the `Hostname` ($2) and `RAM_Usage_GB` ($6) of all servers:
   ```bash
   awk '{ print $2, $6 }' data/servers.txt
   ```
3. Find all servers whose status ($4) is `"Active"` and print their ID ($1) and Hostname ($2):
   ```bash
   awk '$4 == "Active" { print $1, $2 }' data/servers.txt
   ```
4. Find all servers using more than 10 GB of RAM ($6 > 10):
   ```bash
   awk '$6 > 10 { print $2, "RAM:", $6 }' data/servers.txt
   ```
5. Use `ps aux` and `awk` to print the Process ID ($2) and Command ($11) of the top 5 running processes:
   ```bash
   ps aux | awk '{ print $2, $11 }' | head -n 6
   ```

---

## 💡 Self-Check Quiz
1. What does `$0` represent in `awk`?
2. How do you refer to the last field of a line regardless of how many columns it has?
3. What happens if you omit the `pattern` in `awk 'pattern { action }'`?

---

## 📝 Day 1 Assignment & Practical Test

Test your understanding of Day 1 concepts by completing these **4 Assignment Tasks** using `data/servers.txt` or system outputs. Write down or run your `awk` commands in the terminal!

### Task 1: High CPU Server Alert
**Goal:** Write an `awk` command to inspect `data/servers.txt` and print the `ServerID` ($1) and `Hostname` ($2) of all servers where CPU usage ($5) is **greater than 70%**.
- *Expected Output:* Should output `102 web-prod-02` and `103 db-prod-01`.

### Task 2: Maintenance & Inactive Audit
**Goal:** Write an `awk` command to list the `Hostname` ($2) and `IPAddress` ($3) of all servers whose `Status` ($4) is **NOT** equal to `"Active"`.
- *Expected Output:* Should output servers `db-prod-02` and `backup-node-01`.

### Task 3: Extracting Disk Usage
**Goal:** Use the Linux `df -h` command piped into `awk` to print the **Filesystem** ($1) and **Use%** ($5) of all mounted file systems.
- *Hint:* `df -h | awk '...'`

### Task 4: Extracting User Account Names
**Goal:** Run `awk` on `data/servers.txt` to print the `Hostname` ($2) and the **last column** ($NF) of every row.

---

### 🧪 Automated Assignment Verifier
You can verify your answers automatically by running the Day 1 verification test script:
```bash
bash ./verify_day01.sh
```

---
*Next up: Day 2 - Fields & Delimiters (`$0`..`$NF`, custom field separators `-F`, `FS`)*

