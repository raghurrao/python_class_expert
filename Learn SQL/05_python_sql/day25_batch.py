#!/usr/bin/env python3
import sqlite3
import time

def main():
    db_path = "/home/raghurao/Learnings/Learn SQL/05_python_sql/benchmark.db"
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS metrics_log;")
    cursor.execute("""
        CREATE TABLE metrics_log (
            metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            reading REAL,
            logged_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
    """)

    print("==================================================")
    print("    DAY 25: HIGH-PERFORMANCE BATCH INSERTIONS     ")
    print("==================================================")

    # Generate 10,000 synthetic metric rows
    batch_data = [(f"sensor_{i % 50}", 20.0 + (i * 0.05)) for i in range(10000)]

    start_time = time.time()
    with conn:
        cursor.executemany("INSERT INTO metrics_log (device_id, reading) VALUES (?, ?);", batch_data)
    elapsed = time.time() - start_time

    cursor.execute("SELECT COUNT(*) FROM metrics_log;")
    total_count = cursor.fetchone()[0]

    print(f"[1] Bulk Inserted {total_count:,} records using executemany().")
    print(f"    Total Time Elapsed: {elapsed:.4f} seconds ({total_count / elapsed:,.0f} rows/sec)")

    conn.close()
    print("--------------------------------------------------")
    print("✅ DAY 25 EXERCISE COMPLETED SUCCESSFULLY!")
    print("==================================================")

if __name__ == "__main__":
    main()
