# 30-Day Mastery Plan: SQL and SQLAlchemy

This 30-day plan is designed to take you from a basic understanding to an expert level in SQL and SQLAlchemy (both Core and ORM) in Python. The plan requires approximately 1-2 hours of dedicated study and coding per day.

## Week 1: SQL Fundamentals & Relational Database Concepts
*Goal: Build a rock-solid foundation in pure SQL before abstracting it with Python.*

*   **Day 1-2: Data Definition Language (DDL)**
    *   Learn: `CREATE TABLE`, `ALTER TABLE`, `DROP TABLE`, Data types, Primary Keys, Foreign Keys, Constraints (`NOT NULL`, `UNIQUE`, `CHECK`).
    *   Practice: Design a schema for a simple blog (Users, Posts, Comments).
*   **Day 3-4: Data Manipulation Language (DML) - CRUD**
    *   Learn: `INSERT`, `SELECT` (including `WHERE`, `ORDER BY`, `LIMIT`, `OFFSET`), `UPDATE`, `DELETE`.
    *   Practice: Populate your blog database with mock data and query specific users or posts.
*   **Day 5: Advanced Querying & Aggregations**
    *   Learn: `GROUP BY`, `HAVING`, Aggregation functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`).
    *   Practice: Find the number of posts per user, average comments per post.
*   **Day 6: Joins (The Heart of Relational Databases)**
    *   Learn: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL OUTER JOIN`, Self Joins.
    *   Practice: Write queries to fetch a post along with its author's details and all associated comments.
*   **Day 7: Subqueries & Common Table Expressions (CTEs)**
    *   Learn: Nested queries, `EXISTS`, `IN`, `WITH` clause (CTEs) for readable complex queries.
    *   Practice: Refactor complex join queries into CTEs.

## Week 2: Introduction to SQLAlchemy & SQLAlchemy Core
*Goal: Connect to databases using Python and execute SQL programmatically using SQLAlchemy Core (the SQL Expression Language).*

*   **Day 8: Setup, Engines, and Connections**
    *   Learn: Installing SQLAlchemy, creating an `Engine`, connection strings (SQLite for local, PostgreSQL for production), connection pooling basics.
    *   Practice: Set up an SQLite database and write a script to connect and test the connection.
*   **Day 9: Metadata and Table Reflection**
    *   Learn: The `MetaData` object, defining tables programmatically using `Table`, `Column`, `Integer`, `String`, etc. Reflecting existing databases.
    *   Practice: Recreate Week 1's blog schema using SQLAlchemy Core `Table` constructs.
*   **Day 10: Executing Core Inserts and Selects**
    *   Learn: `insert()`, `select()`, executing statements with `connection.execute()`, fetching results (`fetchone`, `fetchall`).
    *   Practice: Insert mock data into your Core tables and retrieve it.
*   **Day 11: Core Filtering, Ordering, and Updates/Deletes**
    *   Learn: `where()`, operators (`==`, `!=`, `like()`, `in_()`), `order_by()`, `update()`, `delete()`.
    *   Practice: Build Python functions that update user emails or delete old posts.
*   **Day 12: Core Joins and Aliases**
    *   Learn: Using `.join()`, `.select_from()`, table aliases (`alias()`).
    *   Practice: Execute the complex join queries from Week 1 using SQLAlchemy Core expressions.
*   **Day 13: Transactions and Connection Management**
    *   Learn: Context managers (`with engine.connect()`, `with engine.begin()`), committing, rolling back.
    *   Practice: Write a script that inserts a User and a Post in a single transaction; test failure scenarios to ensure rollback works.
*   **Day 14: Week 2 Mini-Project**
    *   Task: Build a command-line interface (CLI) application for a library system (Books, Authors, Loans) using strictly SQLAlchemy Core.

## Week 3: SQLAlchemy Object-Relational Mapper (ORM)
*Goal: Transition to the ORM approach, mapping database tables to Python classes.*

*   **Day 15: ORM Basics: Declarative Mapping & Sessions**
    *   Learn: `declarative_base()` (or the new 2.0 `DeclarativeBase`), mapping classes to tables, creating a `Session`.
    *   Practice: Map the blog schema to Python classes (`User`, `Post`, `Comment`).
*   **Day 16: CRUD with the ORM**
    *   Learn: Adding objects (`session.add()`), querying (`session.query()` or 2.0 style `session.execute(select())`), updating object attributes, deleting objects.
    *   Practice: Perform all basic CRUD operations using ORM objects.
*   **Day 17: Relationships (One-to-Many & Many-to-One)**
    *   Learn: `relationship()`, `ForeignKey()`, `back_populates`.
    *   Practice: Link `User` to `Post` (One-to-Many) and `Post` to `Comment`. Traverse these relationships in Python (e.g., `user.posts`).
*   **Day 18: Many-to-Many Relationships**
    *   Learn: Association tables, linking tables using `relationship(secondary=...)`.
    *   Practice: Add a `Tag` model to the blog and create a Many-to-Many relationship between `Post` and `Tag`.
*   **Day 19: Advanced Querying with ORM**
    *   Learn: Filtering by relationships (e.g., `has()`, `any()`), joining in ORM, eager loading vs. lazy loading (`joinedload`, `selectinload`).
    *   Practice: Write efficient queries to fetch all posts with their tags and authors without triggering N+1 query problems.
*   **Day 20: Migrations with Alembic (Crucial Tool)**
    *   Learn: Setting up Alembic (`alembic init`), creating revisions (`alembic revision --autogenerate`), applying migrations (`alembic upgrade head`).
    *   Practice: Initialize Alembic in your project, add a new column to the `User` table, and migrate the database.
*   **Day 21: Week 3 Mini-Project**
    *   Task: Convert the Week 2 library CLI application to use SQLAlchemy ORM and add Alembic for database migrations.

## Week 4: Advanced Topics, Performance, & Integration
*Goal: Master production-level SQLAlchemy, optimization, and real-world integration.*

*   **Day 22: The N+1 Problem & Query Optimization**
    *   Learn: Profiling SQL queries (setting `echo=True`), understanding lazy loading pitfalls, mastering relationship loading strategies.
    *   Practice: Deliberately create an N+1 problem in your blog app and fix it using `selectinload()`.
*   **Day 23: SQLAlchemy 2.0 Syntax Deep Dive**
    *   Learn: The shift from 1.4 to 2.0. `Session.execute(select(...))` vs `Session.query(...)`. Async SQLAlchemy (`AsyncEngine`, `AsyncSession`).
    *   Practice: Refactor your queries to strictly use 2.0 syntax. (Bonus: Try setting up an async connection).
*   **Day 24: Event Listeners & Hooks**
    *   Learn: `sqlalchemy.event`, `before_insert`, `before_update`.
    *   Practice: Add an event listener to automatically generate a slug for a `Post` based on its title before insertion, or update an `updated_at` timestamp.
*   **Day 25: Bulk Operations & Performance**
    *   Learn: `insert().values()`, `update()`, `session.bulk_save_objects()`, `session.execute(insert(), [list of dicts])`.
    *   Practice: Benchmark inserting 10,000 records using standard ORM `add()` vs bulk operations.
*   **Day 26: Hybrid Attributes and SQL Expressions**
    *   Learn: `@hybrid_property`, `@hybrid_method`.
    *   Practice: Add a hybrid property to `User` that calculates their full name or total post count directly on the database side.
*   **Day 27: Integrating with Web Frameworks**
    *   Learn: Flask-SQLAlchemy (for Flask) or integrating pure SQLAlchemy with FastAPI/Django. Dependency injection for sessions.
    *   Practice: Build a simple REST API (e.g., FastAPI) exposing your blog models.
*   **Day 28-30: Final Project - E-commerce Backend**
    *   Task: Build a complete database backend for an e-commerce store.
    *   Requirements:
        *   Models: User, Product, Category, Order, OrderItem.
        *   Relationships: Many-to-Many (Products & Categories), One-to-Many (Order & OrderItem).
        *   Migrations: Fully managed by Alembic.
        *   Optimized Queries: No N+1 problems.
        *   Logic: Transactions to handle inventory deduction during order placement.

---
### Next Steps for Today:
1. Review the plan above.
2. Let me know if you want to adjust the pacing or focus more on a specific area (like web framework integration vs data engineering).
3. When you are ready, we will start with **Day 1: Data Definition Language (DDL)**. I will provide explanations and coding exercises!
