#!/usr/bin/env python3
import sqlite3
import json
import csv
import os
from datetime import datetime

class ETLPipeline:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.raw_dir = os.path.join(base_dir, "raw_data")
        self.db_path = os.path.join(base_dir, "warehouse.db")
        self.sql_file = os.path.join(base_dir, "star_schema.sql")

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_schema(self):
        print("[1] Initializing Warehouse Star Schema...")
        with self.get_connection() as conn:
            with open(self.sql_file, 'r') as f:
                conn.executescript(f.read())

    def extract(self):
        print("[2] Extracting Raw Datasets...")
        # Extract Customers JSON
        with open(os.path.join(self.raw_dir, "raw_customers.json")) as f:
            customers = json.load(f)

        # Extract Products CSV
        products = []
        with open(os.path.join(self.raw_dir, "raw_products.csv")) as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "product_name": row["product_name"],
                    "category": row["category"],
                    "unit_price": float(row["unit_price"])
                })

        # Extract Orders CSV
        orders = []
        with open(os.path.join(self.raw_dir, "raw_orders_2026.csv")) as f:
            reader = csv.DictReader(f)
            for row in reader:
                orders.append({
                    "order_id": int(row["order_id"]),
                    "customer_id": int(row["customer_id"]),
                    "product_id": int(row["product_id"]),
                    "date": row["date"],
                    "qty": int(row["qty"])
                })

        return customers, products, orders

    def transform_and_load(self, customers, products, orders):
        print("[3] Transforming & Loading Dimension Tables...")
        conn = self.get_connection()
        cursor = conn.cursor()

        # Load dim_customers
        cust_map = {}
        for c in customers:
            cursor.execute(
                "INSERT INTO dim_customers (customer_id, customer_name, region) VALUES (?, ?, ?);",
                (c["id"], c["name"], c["region"])
            )
            cust_map[c["id"]] = cursor.lastrowid

        # Load dim_products
        prod_map = {}
        prod_price_map = {}
        for p in products:
            cursor.execute(
                "INSERT INTO dim_products (product_id, product_name, category, unit_price) VALUES (?, ?, ?, ?);",
                (p["id"], p["product_name"], p["category"], p["unit_price"])
            )
            prod_map[p["id"]] = cursor.lastrowid
            prod_price_map[p["id"]] = p["unit_price"]

        # Load dim_date
        dates = set(o["date"] for o in orders)
        for dt_str in dates:
            dt = datetime.strptime(dt_str, "%Y-%m-%d")
            date_key = int(dt.strftime("%Y%m%d"))
            cursor.execute(
                "INSERT OR IGNORE INTO dim_date (date_key, full_date, year, quarter, month, day_name) VALUES (?, ?, ?, ?, ?, ?);",
                (date_key, dt_str, dt.year, (dt.month-1)//3 + 1, dt.month, dt.strftime("%A"))
            )

        print("[4] Transforming & Loading Fact Sales Table...")
        for o in orders:
            dt = datetime.strptime(o["date"], "%Y-%m-%d")
            date_key = int(dt.strftime("%Y%m%d"))
            cust_key = cust_map[o["customer_id"]]
            prod_key = prod_map[o["product_id"]]
            total_amt = o["qty"] * prod_price_map[o["product_id"]]

            cursor.execute(
                "INSERT INTO fact_sales (customer_key, product_key, date_key, quantity, total_amount) VALUES (?, ?, ?, ?, ?);",
                (cust_key, prod_key, date_key, o["qty"], total_amt)
            )

        conn.commit()

    def validate_data_quality(self):
        print("[5] Executing Data Quality Assertions...")
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) FROM fact_sales;")
        fact_count = cursor.fetchone()[0]
        assert fact_count > 0, "Data Quality Error: fact_sales is empty!"

        cursor.execute("SELECT COUNT(*) FROM fact_sales WHERE total_amount IS NULL OR total_amount <= 0;")
        invalid_sales = cursor.fetchone()[0]
        assert invalid_sales == 0, "Data Quality Error: Invalid sales amounts detected!"

        print("    ✅ All Data Quality checks passed cleanly!")
        conn.close()

    def run(self):
        print("==================================================")
        print("    DAY 29: AUTOMATED DATA ENGINEERING ETL RUNNER ")
        print("==================================================")
        self.init_schema()
        customers, products, orders = self.extract()
        self.transform_and_load(customers, products, orders)
        self.validate_data_quality()
        print("--------------------------------------------------")
        print("✅ DAY 29 ETL PIPELINE COMPLETED SUCCESSFULLY!")
        print("==================================================")

if __name__ == "__main__":
    base_dir = "/home/raghurao/Learnings/Learn SQL/06_data_engineering_capstone"
    pipeline = ETLPipeline(base_dir)
    pipeline.run()
