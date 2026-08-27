# Day 29: Building the End-to-End Automated ETL Pipeline

The ETL pipeline orchestrates:
1. **Extract**: Ingestion of raw JSON and CSV files from landing zone.
2. **Transform**: Normalization, date key generation, foreign key lookups, quality validation checks.
3. **Load**: High-performance batch insertion into Star Schema Data Warehouse (`warehouse.db`).

---

## Hands-On Practical Exercise (Day 29)

Run `python3 06_data_engineering_capstone/etl_pipeline.py` to trigger the automated Data Pipeline!
