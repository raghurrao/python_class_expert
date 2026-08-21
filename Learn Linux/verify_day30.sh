#!/bin/bash
echo "========================================================="
echo "   🎓 30-DAY AWK MASTERY FINAL GRADUATION TEST 🎓"
echo "========================================================="
echo ""

awk '
BEGIN {
  print "========================================================="
  print "          SYSTEM HEALTH & WEB ANALYTICS REPORT           "
  print "========================================================="
}

# Process File 1: servers.txt
FILENAME ~ /servers/ {
  if (NR > 1) {
    if ($4 == "Active") active++
    else inactive++
    total_ram += $6
    if ($5 > max_cpu) { max_cpu = $5; peak_host = $2 }
  }
}

# Process File 2: web_access.log
FILENAME ~ /web_access/ {
  reqs++
  bytes += $10
  if ($9 >= 400) errors++
  ip_cnt[$1]++
}

END {
  print "\n[1] SERVER FLEET AUDIT"
  printf "    Active Servers   : %d\n", active
  printf "    Inactive Servers : %d\n", inactive
  printf "    Total RAM Pool   : %.2f GB\n", total_ram
  printf "    Peak CPU Host    : %s (%.1f%%)\n", peak_host, max_cpu

  print "\n[2] WEB TRAFFIC AUDIT"
  printf "    Total Requests   : %d\n", reqs
  printf "    Total Bandwidth  : %.2f KB\n", bytes/1024
  printf "    HTTP Errors      : %d\n", errors

  print "\n[3] TOP VISITING IPS"
  for (ip in ip_cnt) {
    printf "    %-18s : %d requests\n", ip, ip_cnt[ip]
  }

  print "\n========================================================="
  print " 🎉 CONGRATULATIONS! YOU HAVE GRADUATED AWK MASTERY! 🎉"
  print "========================================================="
}
' data/servers.txt data/web_access.log

echo ""
