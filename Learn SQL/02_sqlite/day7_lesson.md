# Day 7: Data Manipulation Language (DML) & CSV Import

DML queries modify database rows: `INSERT`, `UPDATE`, `DELETE`, and conflict-handling `UPSERT` (`ON CONFLICT`).

---

## 1. Key DML Syntax

### Multi-row Insertion:
```sql
INSERT INTO departments (dept_name, location) VALUES
('Engineering', 'Building A'),
('Data Science', 'Building B'),
('Sales', 'Building C');
```

### Conflict Handling (UPSERT):
```sql
INSERT INTO departments (dept_id, dept_name, location) VALUES
(1, 'Engineering', 'Building A - Renovated')
ON CONFLICT(dept_id) DO UPDATE SET
location = excluded.location;
```

### Update & Delete:
```sql
UPDATE employees SET salary = salary * 1.10 WHERE dept_id = 1;
DELETE FROM employees WHERE salary < 50000;
```

---

## 2. Bulk CSV Import via CLI

```sql
.mode csv
.import raw_data.csv target_table
```

---

## 3. Hands-On Practical Exercise (Day 7)

Run `02_sqlite/day7_run.sh` to insert sample data and populate `company.db`!
