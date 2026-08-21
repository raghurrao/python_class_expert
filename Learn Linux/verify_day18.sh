#!/bin/bash
echo "=== Day 18 Assignment Test ==="
awk -F':' '
NR == FNR {
  users[$1] = $6
  next
}
{
  username = tolower($2)
  if (username in users) {
    print "Found match:", username, "Home:", users[username]
  }
}
' data/sample_passwd.txt data/employees.txt
echo "============================="
