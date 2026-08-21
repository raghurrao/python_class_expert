#!/bin/bash
echo "=== Day 26 Assignment Test ==="
awk '{ print $1 }' data/web_access.log | sort | uniq -c | sort -nr | head -n 3
echo "============================="
