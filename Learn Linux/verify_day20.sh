#!/bin/bash
echo "=== Day 20 Assignment Test ==="
awk '
function human_bytes(b) {
  if (b >= 1048576) return sprintf("%.2f MB", b/1048576)
  if (b >= 1024) return sprintf("%.2f KB", b/1024)
  return sprintf("%d Bytes", b)
}
{
  printf "File: %-18s | Size: %s\n", $2, human_bytes($10)
}
' data/web_access.log
echo "============================="
