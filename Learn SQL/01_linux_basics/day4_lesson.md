# Day 4: Stream Processing with `awk` and `sed`

`awk` and `sed` are power tools in the Linux data engineer's toolkit. They allow you to transform, reformat, and perform inline calculations on text data streams before inserting into database tables.

---

## 1. `sed` (Stream Editor)

`sed` performs string substitutions, deletions, and pattern replacements.

### Basic Syntax:
`sed 's/search_pattern/replacement_pattern/g' input.txt` (`g` = global flag to replace all occurrences per line).

### Practical Uses:
```bash
# Clean CSV: replace double quotes with empty string
sed 's/"//g' raw_data.csv

# Replace NULL strings with empty values
sed 's/N\/A/NULL/g' raw_data.csv
```

---

## 2. `awk` (Text Processing Language)

`awk` treats each line as a record and each column (delimited by whitespace or custom separator) as a field (`$1`, `$2`, `$3`... `$NF`).

### Key Concepts:
- `-F','`: Sets field separator to comma `,`.
- `NR`: Current row number (Line number).
- `NF`: Number of fields (columns) in current row.
- `BEGIN { ... }`: Block executed before processing any records.
- `END { ... }`: Block executed after processing all records.

### Powerful Examples:
```bash
# Print line number, customer name ($2), and amount ($4)
awk -F',' 'NR > 1 { print "Row " NR ": " $2 " spent $" $4 }' orders.csv

# Calculate total sum of amount column ($4)
awk -F',' 'NR > 1 { sum += $4 } END { print "Total Sales: $" sum }' orders.csv
```

---

## 3. Hands-On Practical Exercise (Day 4)

Run `01_linux_basics/day4_awk_sed.sh` to run `awk` aggregation and `sed` cleaning pipelines!
