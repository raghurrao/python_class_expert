# Day 11: String & Datetime Processing

Today we learn string operations and parsing datetimes, which are vital for time-series and log files.

## Core Concepts
* **String accessors:** `df['col'].str.lower()`, `df['col'].str.contains()`, `df['col'].str.extract()`.
* **Datetime conversions:** `pd.to_datetime()`.
* **Datetime accessors:** `df['date_col'].dt.year`, `df['date_col'].dt.month`, `df['date_col'].dt.day`.
