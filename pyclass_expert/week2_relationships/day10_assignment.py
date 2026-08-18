# Day 10 Assignment: Composition vs. Inheritance
# ----------------------------------------------------------------------
# Instructions: Build the classes using composition.
# Run 'python day10_test.py' to verify your solutions.

# ======================================================================
# Exercise 1: Salary Component
# ======================================================================
class Salary:
    """
    Requirements:
    1. Constructor should take 'monthly_pay' (float) and 'annual_bonus' (float).
    2. Implement 'get_annual_compensation(self)' returning: (monthly_pay * 12) + annual_bonus.
    """
    # TODO: Implement Salary class


# ======================================================================
# Exercise 2: Employee Class (Composes Salary)
# ======================================================================
class Employee:
    """
    Requirements:
    1. Constructor should take 'name' (str) and 'salary' (an instance of Salary).
    2. Store them in 'self.name' and 'self.salary'.
    3. Implement 'get_total_salary(self)' which delegates to the Salary object's
       get_annual_compensation method and returns the float result.
    """
    # TODO: Implement Employee class


# ======================================================================
# Exercise 3: Company Class (Composes Employee list)
# ======================================================================
class Company:
    """
    Requirements:
    1. Constructor should take 'name' (str).
    2. Initialize an instance list attribute 'employees' to an empty list.
    3. Implement 'add_employee(self, employee)' to append an Employee to the list.
    4. Implement 'get_payroll_cost(self)' that calculates the sum of
       get_total_salary() for all employees in the company.
    """
    # TODO: Implement Company class
