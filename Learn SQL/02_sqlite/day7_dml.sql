-- Day 7: Data Manipulation Queries

-- Insert Departments
INSERT INTO departments (dept_name, location) VALUES
('Engineering', 'Building A'),
('Data Science', 'Building B'),
('Sales', 'Building C'),
('Marketing', 'Building D');

-- Insert Employees
INSERT INTO employees (first_name, last_name, email, salary, dept_id) VALUES
('Alice', 'Smith', 'alice@company.com', 95000, 1),
('Bob', 'Jones', 'bob@company.com', 88000, 1),
('Charlie', 'Brown', 'charlie@company.com', 72000, 2),
('Diana', 'Prince', 'diana@company.com', 105000, 2),
('Evan', 'Wright', 'evan@company.com', 65000, 3),
('Fiona', 'Gallagher', 'fiona@company.com', 120000, 1),
('George', 'Martin', 'george@company.com', 55000, NULL);

-- UPSERT Example: Update location if dept_name conflicts
INSERT INTO departments (dept_name, location) VALUES
('Engineering', 'Building A - Tech Hub')
ON CONFLICT(dept_name) DO UPDATE SET location = excluded.location;

-- UPDATE 10% raise for Data Science dept (dept_id = 2)
UPDATE employees SET salary = salary * 1.10 WHERE dept_id = 2;
