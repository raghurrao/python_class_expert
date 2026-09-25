"""Run one or more semicolon-terminated SQL statements from a file."""

from pathlib import Path
import sqlite3
import sys


ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "books.db"


def display_rows(cursor: sqlite3.Cursor) -> None:
    columns = [column[0] for column in cursor.description or ()]
    rows = cursor.fetchall()
    if not columns:
        print("Statement executed.")
        return
    values = [["NULL" if value is None else str(value) for value in row] for row in rows]
    widths = [max([len(columns[i])] + [len(row[i]) for row in values]) for i in range(len(columns))]
    print(" | ".join(columns[i].ljust(widths[i]) for i in range(len(columns))))
    print("-+-".join("-" * width for width in widths))
    for row in values:
        print(" | ".join(row[i].ljust(widths[i]) for i in range(len(columns))))
    print(f"({len(rows)} row{'s' if len(rows) != 1 else ''})")


def statements_from(sql: str):
    """Yield complete statements, respecting quoted strings and SQL comments."""
    buffer = ""
    for line in sql.splitlines(keepends=True):
        buffer += line
        if sqlite3.complete_statement(buffer):
            statement = buffer.strip()
            if statement:
                yield statement
            buffer = ""
    if buffer.strip():
        raise ValueError("A SQL statement is missing its final semicolon.")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python run_sql.py path\\to\\your-query.sql")
        return 2
    if not DB_PATH.exists():
        print("Database not found. Create it first with: python setup_database.py")
        return 1

    query_path = Path(sys.argv[1])
    if not query_path.is_absolute():
        query_path = ROOT / query_path
    if not query_path.exists():
        print(f"SQL file not found: {query_path}")
        return 1

    sql = query_path.read_text(encoding="utf-8")
    try:
        with sqlite3.connect(DB_PATH) as connection:
            connection.execute("PRAGMA foreign_keys = ON")
            for statement in statements_from(sql):
                cursor = connection.execute(statement)
                display_rows(cursor)
    except (sqlite3.Error, ValueError) as error:
        print(f"SQL error: {error}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
