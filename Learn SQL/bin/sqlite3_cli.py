#!/usr/bin/env python3
import sys
import sqlite3
import os
import csv
import shlex

class SQLiteCLI:
    def __init__(self, db_path=":memory:"):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.headers = True
        self.mode = "column" # column, csv, line, list

    def execute_sql(self, sql):
        sql = sql.strip()
        if not sql:
            return
        if sql.startswith("."):
            self.handle_dot_command(sql)
            return

        try:
            # Split statements by semicolon while ignoring semicolons inside quotes
            statements = [s.strip() for s in sql.split(";") if s.strip()]
            for stmt in statements:
                if stmt.startswith("."):
                    self.handle_dot_command(stmt)
                    continue
                self.cursor.execute(stmt)
                if self.cursor.description:
                    cols = [desc[0] for desc in self.cursor.description]
                    rows = self.cursor.fetchall()
                    self.print_results(cols, rows)
                else:
                    self.conn.commit()
                    if self.cursor.rowcount >= 0:
                        print(f"Rows affected: {self.cursor.rowcount}")
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)

    def handle_dot_command(self, cmd_str):
        parts = shlex.split(cmd_str)
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd in (".exit", ".quit"):
            sys.exit(0)
        elif cmd == ".tables":
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;")
            tables = [r[0] for r in self.cursor.fetchall()]
            print("  ".join(tables))
        elif cmd == ".schema":
            if args:
                self.cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name=?;", (args[0],))
            else:
                self.cursor.execute("SELECT sql FROM sqlite_master WHERE sql IS NOT NULL ORDER BY type, name;")
            for r in self.cursor.fetchall():
                if r[0]:
                    print(f"{r[0]};")
        elif cmd == ".headers":
            if args and args[0].lower() in ("on", "1", "yes"):
                self.headers = True
            elif args and args[0].lower() in ("off", "0", "no"):
                self.headers = False
            print(f"Headers: {'on' if self.headers else 'off'}")
        elif cmd == ".mode":
            if args and args[0] in ("column", "csv", "line", "list"):
                self.mode = args[0]
                print(f"Mode set to: {self.mode}")
            else:
                print("Usage: .mode [column|csv|line|list]")
        elif cmd == ".import":
            if len(args) < 2:
                print("Usage: .import FILE TABLE")
                return
            csv_file, table_name = args[0], args[1]
            if not os.path.exists(csv_file):
                print(f"Error: file not found '{csv_file}'")
                return
            with open(csv_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader, None)
                if not header:
                    print("Error: empty CSV file")
                    return
                cols_def = ", ".join([f'"{col}" TEXT' for col in header])
                self.cursor.execute(f'CREATE TABLE IF NOT EXISTS "{table_name}" ({cols_def});')
                placeholders = ", ".join(["?"] * len(header))
                self.cursor.executemany(f'INSERT INTO "{table_name}" VALUES ({placeholders});', reader)
                self.conn.commit()
                print(f"Imported data into '{table_name}'.")
        elif cmd == ".help":
            print("""Available dot commands:
  .tables             List names of tables
  .schema [TABLE]     Show the CREATE statements
  .headers on|off     Turn display of headers on or off
  .mode MODE          Set output mode (column, csv, line, list)
  .import FILE TABLE  Import data from FILE into TABLE
  .dump               Dump database in SQL text format
  .exit / .quit       Exit this program""")
        elif cmd == ".dump":
            for line in self.conn.iterdump():
                print(line)
        else:
            print(f"Unknown dot command '{cmd}'. Type .help for available commands.")

    def print_results(self, cols, rows):
        if not rows and not self.headers:
            return

        if self.mode == "csv":
            writer = csv.writer(sys.stdout)
            if self.headers:
                writer.writerow(cols)
            for row in rows:
                writer.writerow(row)

        elif self.mode == "line":
            for row in rows:
                for col, val in zip(cols, row):
                    print(f"{col:>15} = {val}")
                print()

        elif self.mode == "list":
            if self.headers:
                print("|".join(cols))
            for row in rows:
                print("|".join(str(v) if v is not None else "" for v in row))

        else: # column (default)
            col_widths = [len(c) for c in cols]
            for row in rows:
                for i, val in enumerate(row):
                    val_str = str(val) if val is not None else "NULL"
                    if len(val_str) > col_widths[i]:
                        col_widths[i] = len(val_str)

            if self.headers:
                header_line = " | ".join(f"{cols[i]:<{col_widths[i]}}" for i in range(len(cols)))
                print(header_line)
                print("-" * len(header_line))

            for row in rows:
                row_str = " | ".join(f"{(str(row[i]) if row[i] is not None else 'NULL'):<{col_widths[i]}}" for i in range(len(cols)))
                print(row_str)

def main():
    db_file = ":memory:"
    sql_to_run = None

    args = sys.argv[1:]
    if args:
        if args[0].startswith("-"):
            pass
        else:
            db_file = args[0]
            args = args[1:]

    if args:
        sql_to_run = " ".join(args)

    cli = SQLiteCLI(db_file)

    if sql_to_run:
        cli.execute_sql(sql_to_run)
        return

    # Check if stdin has data (piped input)
    if not sys.stdin.isatty():
        content = sys.stdin.read()
        cli.execute_sql(content)
        return

    # Interactive REPL
    print(f"SQLite version 3 (Python CLI Wrapper)")
    print(f"Connected to '{db_file}'")
    print("Enter \".help\" for usage hints.")
    print("Enter SQL statements terminated with a \";\".\n")

    buffer = ""
    while True:
        try:
            prompt = "sqlite> " if not buffer else "   ...> "
            line = input(prompt)
        except (EOFError, KeyboardInterrupt):
            print()
            break

        line_str = line.strip()
        if not buffer and line_str.startswith("."):
            cli.handle_dot_command(line_str)
            continue

        buffer += line + "\n"
        if ";" in line:
            cli.execute_sql(buffer)
            buffer = ""

if __name__ == "__main__":
    main()
