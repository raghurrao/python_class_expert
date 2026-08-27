-- Day 27: Star Schema DDL for Data Warehouse

DROP TABLE IF EXISTS fact_sales;
DROP TABLE IF EXISTS dim_customers;
DROP TABLE IF EXISTS dim_products;
DROP TABLE IF EXISTS dim_date;

CREATE TABLE dim_customers (
    customer_key INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER UNIQUE,
    customer_name TEXT NOT NULL,
    region TEXT NOT NULL
);

CREATE TABLE dim_products (
    product_key INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER UNIQUE,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    unit_price REAL NOT NULL
);

CREATE TABLE dim_date (
    date_key INTEGER PRIMARY KEY, -- e.g. 20260827
    full_date DATE UNIQUE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    day_name TEXT
);

CREATE TABLE fact_sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_key INTEGER,
    product_key INTEGER,
    date_key INTEGER,
    quantity INTEGER,
    total_amount REAL,
    FOREIGN KEY (customer_key) REFERENCES dim_customers(customer_key),
    FOREIGN KEY (product_key) REFERENCES dim_products(product_key),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);
