# Day 1: Shell Navigation, Directory Setup & Environment Variables

Welcome to **Day 1** of your 30-Day SQL & Data Engineering journey!

Before we query databases with SQL, we must master the **Linux Command Line Environment**. Data engineers and database administrators interact with SQL databases, servers, ETL pipelines, and configuration files via the Linux terminal every day.

---

## 1. Core Navigation Commands

| Command | Purpose | Example |
| :--- | :--- | :--- |
| `pwd` | Print Working Directory (where am I?) | `pwd` |
| `ls` | List directory contents | `ls -la` (long format, show hidden files) |
| `cd` | Change Directory | `cd 01_linux_basics` or `cd ..` |
| `mkdir` | Make Directory | `mkdir -p data/raw` |
| `touch` | Create an empty file | `touch config.env` |
| `rm` | Remove files/directories | `rm temp.txt` or `rm -rf old_data` |

---

## 2. File Permissions (`chmod`)

Linux is a multi-user system. Every file has 3 permission levels:
1. **User (u)**: Owner of the file
2. **Group (g)**: Group members
3. **Others (o)**: Everyone else

Permission types:
- `r` (read = 4)
- `w` (write = 2)
- `x` (execute = 1)

### Command Syntax:
```bash
# Give execute permissions to user/owner
chmod +x my_script.sh

# Numeric permission (755 = rwxr-xr-x)
chmod 755 my_script.sh
```

---

## 3. Environment Variables (`export`, `ENV`)

Environment variables pass configurations (like DB connection strings, passwords, paths) to scripts and binaries without hardcoding them.

### Setting & Reading Environment Variables:
```bash
# Define a variable for current shell session
export DB_NAME="sql_learning"
export DB_PORT=5432

# Print variable
echo $DB_NAME
echo "Connecting to DB: $DB_NAME on port $DB_PORT"

# List all exported environment variables
env | grep DB_
```

---

## 4. Hands-On Practical Exercise (Day 1)

Run the automated script `01_linux_basics/day1_env.sh` to test your environment and verify your setup!

### Instructions:
```bash
cd "/home/raghurao/Learnings/Learn SQL"
./01_linux_basics/day1_env.sh
```
