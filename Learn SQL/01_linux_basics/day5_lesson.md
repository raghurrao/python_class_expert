# Day 5: Production Shell Scripting Patterns for Data Operations

To build reliable data pipelines, bash scripts must include proper error handling, logging, exit traps, and parameter validation.

---

## 1. Key Scripting Best Practices

### Defensive Flags:
```bash
set -e # Exit immediately if any command returns non-zero status
set -u # Treat unset variables as an error
set -o pipefail # Return value of a pipeline is the status of the last command to fail
```

### Logging & Timestamps:
```bash
log_msg() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}
```

### Cleanup Traps:
```bash
# Register automatic cleanup function on script exit or interrupt
cleanup() {
    echo "Cleaning up temporary files..."
    rm -f /tmp/temp_data_$$.csv
}
trap cleanup EXIT
```

---

## 2. Hands-On Practical Exercise (Day 5)

Run `01_linux_basics/day5_scripting.sh` to execute a production-grade Bash pipeline script with logging and error handling!
