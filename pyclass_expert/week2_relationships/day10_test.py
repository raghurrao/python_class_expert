# Day 10 Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python day10_test.py
# It will verify if your assignment code is correct!

import sys
import os

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week2_relationships.day10_assignment as assignment
except ImportError as e:
    print(f"[FAIL] Could not import day10_assignment.py. Error: {e}")
    sys.exit(1)

passed_tests = 0
total_tests = 0

def run_test(test_name, test_fn):
    global passed_tests, total_tests
    total_tests += 1
    try:
        test_fn()
        print(f"[PASS] {test_name}")
        passed_tests += 1
    except AssertionError as e:
        print(f"[FAIL] {test_name}")
        print(f"   AssertionError: {e}\n")
    except Exception as e:
        print(f"[FAIL] {test_name}")
        print(f"   Unexpected Error: {type(e).__name__}: {e}\n")

print("Starting Day 10 Tests...\n")

# 1. Salary Component Tests
def test_salary():
    assert hasattr(assignment, 'Salary'), "Salary class missing"
    sal = assignment.Salary(5000.0, 10000.0)
    # 5000 * 12 + 10000 = 60000 + 10000 = 70000.0
    assert abs(sal.get_annual_compensation() - 70000.0) < 0.001

run_test("Salary component calculations", test_salary)

# 2. Employee Composes Salary Tests
def test_employee_composition():
    assert hasattr(assignment, 'Employee'), "Employee class missing"
    
    sal = assignment.Salary(4000.0, 5000.0)
    emp = assignment.Employee("Alice", sal)
    
    assert emp.name == "Alice"
    assert emp.salary is sal, "Employee does not reference the correct Salary object"
    # 4000 * 12 + 5000 = 53000.0
    assert abs(emp.get_total_salary() - 53000.0) < 0.001

run_test("Employee composition delegates correctly", test_employee_composition)

# 3. Company Composes Employees Tests
def test_company_payroll():
    assert hasattr(assignment, 'Company'), "Company class missing"
    
    comp = assignment.Company("TechCorp")
    assert comp.name == "TechCorp"
    assert comp.employees == []
    
    emp1 = assignment.Employee("Alice", assignment.Salary(4000.0, 5000.0)) # 53000
    emp2 = assignment.Employee("Bob", assignment.Salary(6000.0, 8000.0))   # 80000
    
    comp.add_employee(emp1)
    comp.add_employee(emp2)
    
    assert len(comp.employees) == 2
    assert comp.employees[0] is emp1
    
    # 53000 + 80000 = 133000.0
    payroll = comp.get_payroll_cost()
    assert abs(payroll - 133000.0) < 0.001, f"Expected 133000.0 payroll, got {payroll}"

run_test("Company payroll aggregation (Multi-composition)", test_company_payroll)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed Day 10 assignments.")
    print(f"Proceed to the Week 2 Challenge when you are ready!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in day10_assignment.py")
