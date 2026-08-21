#!/bin/bash
echo "=== Day 19 Assignment Test ==="
awk '{
  if (match($0, /"([^"]+)"$/, m)) {
    print $1, "User-Agent:", substr($0, RSTART, RLENGTH)
  }
}' data/web_access.log | head -n 5
echo "============================="
