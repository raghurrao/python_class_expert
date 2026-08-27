-- Day 30: Data Warehouse Analytics Query Suite

-- 1. Regional Sales Revenue Summary
SELECT 
    c.region,
    COUNT(f.sale_id) AS total_orders,
    SUM(f.quantity) AS total_items_sold,
    ROUND(SUM(f.total_amount), 2) AS total_revenue
FROM fact_sales f
JOIN dim_customers c ON f.customer_key = c.customer_key
GROUP BY c.region
ORDER BY total_revenue DESC;

-- 2. Product Category Performance
SELECT 
    p.category,
    p.product_name,
    SUM(f.quantity) AS total_units,
    ROUND(SUM(f.total_amount), 2) AS category_revenue
FROM fact_sales f
JOIN dim_products p ON f.product_key = p.product_key
GROUP BY p.category, p.product_name
ORDER BY category_revenue DESC;

-- 3. Customer Revenue Ranking using Window Functions
SELECT 
    c.customer_name,
    c.region,
    ROUND(SUM(f.total_amount), 2) AS customer_spend,
    DENSE_RANK() OVER (ORDER BY SUM(f.total_amount) DESC) AS spend_rank
FROM fact_sales f
JOIN dim_customers c ON f.customer_key = c.customer_key
GROUP BY c.customer_name, c.region;
