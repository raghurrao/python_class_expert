#!/bin/bash
echo "=== Day 24 Assignment Test ==="
awk '
BEGIN { RS=""; FS="\n" }
{
  print "Contact " NR ": " $1 " | " $2
}
' data/multiline_contacts.txt
echo "============================="
