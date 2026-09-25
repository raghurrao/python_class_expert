# Day 32 — Normalize a sales schema

**Today's goal:** Reduce duplicated facts by separating customers, order headers, and order lines into related tables.

**Suggested time:** 60–75 minutes

**Interactive routine:** Compare the current teaching table with the normalized design. Run the safe demo, then answer the design assignment and self-test.

## 1. Why normalize?

The course's `book_orders` table is intentionally simple: one row represents an order line and repeats the customer's name and date on every row. A real order may contain several books. If the order has multiple lines, repeating the customer and date can create update inconsistencies.

Normalization organizes facts so each kind of fact has a clear home:

- `day32_customers`: customer details;
- `day32_orders`: one row per order header, with customer and date;
- `day32_order_items`: one row per book line in an order;
- `books`: the existing book catalog.

The relationships are:

```text
customers 1 ─── many orders
orders    1 ─── many order_items
books     1 ─── many order_items
```

## 2. First, second, and third normal form (intuition)

- **First normal form (1NF):** Store one value per cell and avoid repeating groups of columns such as `book_1`, `book_2`, `book_3`.
- **Second normal form (2NF):** In a table with a composite key, each non-key column should depend on the whole key, not only part of it.
- **Third normal form (3NF):** Non-key facts should depend on the key, the whole key, and nothing but the key. For example, customer name belongs with the customer ID in the customer table, rather than repeating it in every order line.

These are practical design checks. Real schema design also considers access patterns, constraints, history, and business rules.

## 3. A normalized schema example

```sql
CREATE TABLE day32_customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL
);

CREATE TABLE day32_orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL REFERENCES day32_customers(customer_id),
    order_date TEXT NOT NULL
);

CREATE TABLE day32_order_items (
    order_id INTEGER NOT NULL REFERENCES day32_orders(order_id),
    line_number INTEGER NOT NULL,
    book_id INTEGER NOT NULL REFERENCES books(book_id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    PRIMARY KEY (order_id, line_number)
);
```

`day32_order_items` uses a composite primary key: line numbers are unique within each order. The same book can appear on many order lines, but one line number cannot be repeated within an order.

## 4. Query across the normalized tables

```sql
SELECT o.order_id, c.customer_name, o.order_date,
       b.title, i.quantity, b.price,
       i.quantity * b.price AS estimated_line_total
FROM day32_orders AS o
INNER JOIN day32_customers AS c
    ON o.customer_id = c.customer_id
INNER JOIN day32_order_items AS i
    ON o.order_id = i.order_id
INNER JOIN books AS b
    ON i.book_id = b.book_id
ORDER BY o.order_id, i.line_number;
```

This returns one row per order item. An order with three books produces three rows, while its customer and date are stored once in the order header.

## 5. Today's safe runnable practice

The query file creates these lesson tables inside a transaction, inserts a two-line order, displays the joined result, then rolls back. No permanent schema change is left behind.

Run it from PowerShell in the course folder:

```powershell
python run_sql.py queries/day-32.sql
```

## 6. Assignment — reason about the design

1. Which table stores a customer's name?
2. Which table stores the order date?
3. Which table stores the ordered book and its quantity?
4. Why can one order have multiple rows in `day32_order_items`?
5. What does the composite key `(order_id, line_number)` guarantee?
6. Write a query to calculate total units per order using `day32_order_items`.

## 7. Self-test — answer without notes

1. Why should a customer name usually be stored once in a customer table?
2. What is an order header?
3. What is an order line?
4. Which normal form is concerned with values being atomic and avoiding repeating columns?
5. Why is quantity in the order line rather than the book table?
6. What does a foreign key enforce?

## 8. Answer key — check after trying

### Assignment solutions

1. `day32_customers.customer_name`.
2. `day32_orders.order_date`.
3. `day32_order_items` stores `book_id` and `quantity` per line.
4. An order can contain multiple different books; each line is one item in that order.
5. It allows line numbers to repeat across orders, but not within the same order.
6. Example:

   ```sql
   SELECT order_id, SUM(quantity) AS units_in_order
   FROM day32_order_items
   GROUP BY order_id;
   ```

### Self-test solutions

1. It avoids inconsistent repeated copies and lets each order refer to the customer by ID.
2. The row representing the order as a whole, such as its customer and date.
3. One product/book and quantity within an order.
4. First normal form (1NF).
5. Quantity can differ for each order line; it is a fact about the order-book combination, not about the book itself.
6. It ensures that a referenced row exists in the parent table.

## 9. Ready for Day 33?

You’re ready when you can describe the one-to-many relationships and explain what belongs in the header versus the line table. Send me your query for total units per order and your reasoning for the composite key.
