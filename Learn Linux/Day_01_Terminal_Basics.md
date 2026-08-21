# Day 1: Terminal Navigation & Path Mechanics

Welcome to **Day 1** of your 30-Day Linux Mastery course! Today, you will master the fundamental commands used to navigate the Linux directory tree and understand paths.

---

## 1. Core Concepts

### What is the Shell?
The Shell is a command interpreter that acts as an interface between you and the Linux kernel. When you type commands into the terminal, the shell executes them.

### The Linux Directory Structure (The Root `/`)
Unlike Windows (which uses drive letters like `C:\` or `D:\`), Linux organizes everything into a single inverted tree hierarchy starting at the **Root Directory (`/`)**.

Common top-level directories:
- `/` - Root directory (top of the file system).
- `/home` - Contains personal user directories (e.g., `/home/raghurao`).
- `/etc` - System-wide configuration files.
- `/var` - Variable data (logs, databases, spools).
- `/bin` & `/usr/bin` - Essential user command binaries (like `ls`, `ps`, `cat`).
- `/proc` - Virtual filesystem providing process and kernel information.

---

## 2. Essential Commands

### Command 1: `pwd` (Print Working Directory)
Shows where you currently are in the directory structure.
```bash
pwd
```
*Output Example:* `/home/raghurao/Learnings/Learn Linux`

### Command 2: `ls` (List Directory Contents)
Lists files and folders in your current location or specified path.

Useful flags:
- `ls` : Basic list.
- `ls -l` : Long listing format (shows permissions, owner, file size, modification date).
- `ls -a` : List all files, including hidden files (files starting with `.`).
- `ls -lh` : Human-readable file sizes (e.g., `4K`, `25M`, `1G` instead of raw bytes).
- `ls -la` / `ls -lah` : Combine flags (long format, hidden files, human-readable).

### Command 3: `cd` (Change Directory)
Moves your terminal location to a target directory.

Special Directory Shortcuts:
- `.` : Current directory.
- `..` : Parent directory (one level up).
- `~` : Your home directory (`/home/raghurao`).
- `-` : Previous directory you were in (toggle back).

Examples:
```bash
cd /var/log      # Navigate using absolute path
cd ..            # Move up one directory
cd ~             # Jump to home directory
cd -             # Jump back to previous directory
```

---

## 3. Absolute vs Relative Paths

- **Absolute Path**: Starts from the root directory (`/`). It always points to the exact same location regardless of where you currently are.
  - *Example:* `/home/raghurao/Learnings/Learn Linux`
- **Relative Path**: Starts relative to your current working directory.
  - *Example:* If you are in `/home/raghurao`, the relative path to `Learn Linux` is `Learnings/Learn Linux`.

---

## 4. Day 1 Practical Exercises

Try these commands right now in your terminal to practice:

1. Print your current directory:
   ```bash
   pwd
   ```
2. Navigate to the root directory `/`:
   ```bash
   cd /
   pwd
   ```
3. List all contents in long format including hidden files:
   ```bash
   ls -lah
   ```
4. Navigate to `/var/log` using an absolute path and list the files:
   ```bash
   cd /var/log
   ls -lh
   ```
5. Return to your home directory using the shortcut:
   ```bash
   cd ~
   pwd
   ```
6. Return to your learning directory:
   ```bash
   cd "/home/raghurao/Learnings/Learn Linux"
   pwd
   ```

---

## 💡 Quick Self-Check Questions
1. What command tells you your current location in the Linux file system?
2. What is the difference between `ls -l` and `ls -la`?
3. What shortcut directory represents one level up?

---
*Next up: Day 2 - File & Directory Operations (`mkdir`, `touch`, `cp`, `mv`, `rm`)*
