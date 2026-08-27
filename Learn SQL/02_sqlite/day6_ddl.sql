-- Day 6: Schema Definition for Company Database

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;

CREATE TABLE departments (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT NOT NULL UNIQUE,
    location TEXT DEFAULT 'Headquarters'
);

CREATE TABLE employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    salary REAL CHECK (salary > 0),
    hire_date DATE DEFAULT (DATE('now')),
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id) ON DELETE SET NULL
);
