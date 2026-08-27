# Day 12: PostgreSQL Architecture, Schemas & `psql` CLI

Welcome to **Module 3: PostgreSQL & Advanced SQL Features**!

PostgreSQL is an enterprise-class, open-source Object-Relational Database Management System (ORDBMS) designed for high concurrency, ACID compliance, and extensible data types.

---

## 1. PostgreSQL Architecture & Objects

```
PostgreSQL Instance (Cluster)
 ├── Databases (e.g. postgres, analytics_db)
 │    ├── Schemas (e.g. public, staging, warehouse)
 │    │    ├── Tables & Views
 │    │    ├── Indexes (B-Tree, GIN, GiST)
 │    │    └── Functions & Triggers
 └── Roles & Permissions (Users / Groups)
```

---

## 2. PostgreSQL `psql` CLI Commands

| Command | Action |
| :--- | :--- |
| `psql -h localhost -U postgres -d mydb` | Connect to database |
| `\l` | List databases |
| `\dn` | List schemas |
| `\dt` | List tables in current schema |
| `\d table_name` | Describe table structure & indexes |
| `\q` | Quit `psql` |

---

## 3. Hands-On Practical Exercise (Day 12)

Run `03_postgres/day12_run.sh` to construct multi-schema database objects!
