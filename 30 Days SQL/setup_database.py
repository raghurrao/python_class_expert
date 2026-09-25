"""Create or reset the local SQL course database from setup.sql."""

from pathlib import Path
import sqlite3


ROOT = Path(__file__).resolve().parent
DB_PATH = ROOT / "books.db"
SETUP_PATH = ROOT / "setup.sql"


def main() -> None:
    sql = SETUP_PATH.read_text(encoding="utf-8")
    with sqlite3.connect(DB_PATH) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.executescript(sql)
    print(f"Database ready: {DB_PATH}")
    print("It contains the books, book_reviews, and book_orders practice tables.")


if __name__ == "__main__":
    main()
