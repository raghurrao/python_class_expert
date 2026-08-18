# Python Expertise Curriculum: 1-Month Day-by-Day Learning Plan

This curriculum provides a structured, day-by-day learning plan to elevate you to a Python expert in one month. Each day contains a concise **Concept Guide** (`.md` file), an **Assignment Template** with inline exercises (`.py` file), and a **Test Runner** (`_test.py` file) to automatically verify your solutions. We will begin with setting up your development environment.

All learning materials, exercises, and projects will be structured under the workspace directory [g:/30 days Leaarning/30_Days_Python](file:///g:/30%20days%20Leaarning/30_Days_Python).

---

## User Review Required

Please review the proposed breakdown of topics and files. 
> [!IMPORTANT]
> - **Initial Setup (Day 1)**: We will install Python 3.11+ and VS Code, then install the Python extensions and configure the editor.
> - **Structure**: The study schedule is planned for 5 days of core content and exercises per week, with a weekend challenge to synthesize what you learned. This allows 4 weeks of structured learning.

---

## Open Questions

> [!NOTE]
> 1. **Python Version**: Do you have a preferred Python version? We recommend Python 3.11 or 3.12 for modern syntax.
> 2. **Operating System**: Since you are on Windows, we will configure the environment using standard Windows installers and PowerShell. Let me know if you prefer WSL (Windows Subsystem for Linux) or standard Windows.

---

## Proposed Changes

We will organize the project in the workspace [g:/30 days Leaarning/30_Days_Python](file:///g:/30%20days%20Leaarning/30_Days_Python).

### Directory Structure
```
30_Days_Python/
├── week1_basics/
│   ├── day1_concepts.md        # VS Code & Python installation, configuration, and first execution
│   ├── day1_assignment.py      # Basic print syntax and path validation
│   ├── day1_test.py            # Verifies setup works
│   ├── day2_...
│   └── week1_challenge.py      # Weekend challenge: Command-line Calculator & Text Analyzer
├── week2_functions_io/
│   ├── day6_...
│   └── week2_challenge.py      # Weekend challenge: JSON-based Task Manager
├── week3_oop/
│   ├── day11_...
│   └── week3_challenge.py      # Weekend challenge: Library/Inventory Management System
└── week4_advanced/
    ├── day16_...
    └── week4_challenge.py      # Capstone Challenge: Expense Tracker CLI with external APIs
```

---

### Day-by-Day Breakdown

#### **Week 1: Environment Setup & Python Basics**
*   **Day 1: VS Code & Python Setup**
    *   *Concept*: Download & install Python, check environment variables (PATH), install VS Code, install Python Extension Pack, and learn how to run Python code.
    *   *Assignment*: Write your first Python script verifying environment configuration.
    *   *Test*: Test file checks output text and interpreter version info.
*   **Day 2: Variables, Operators & Basic Data Types**
    *   *Concept*: Python data types (`int`, `float`, `str`, `bool`), type casting, basic operations, and format strings (f-strings).
    *   *Assignment*: Implement basic calculation formulas (e.g. Fahrenheit to Celsius, compound interest).
*   **Day 3: Control Flow (Conditions & Loops)**
    *   *Concept*: `if-elif-else` branches, logical operators (`and`, `or`, `not`), `for` and `while` loops, and control statements (`break`, `continue`, `pass`).
    *   *Assignment*: Write prime number checks, number guessing game logic, and fizzbuzz.
*   **Day 4: Sequences (Lists & Tuples)**
    *   *Concept*: Lists vs. Tuples, indexing, slicing, common list methods, unpacking, and list modifications.
    *   *Assignment*: Implement shopping list manipulation functions.
*   **Day 5: Dictionaries & Sets**
    *   *Concept*: Hash maps (dicts) and unique collections (sets). Key-value lookups, dictionary iteration, set operations (union, intersection, difference).
    *   *Assignment*: Write a word counter and set duplicate remover.
*   **Week 1 Challenge: CLI Text Analyzer & Calculator**
    *   *Task*: Create a script that takes user input text, analyzes word frequency, character counts, and handles arithmetic operations using what was learned in Week 1.

---

#### **Week 2: Functions, File I/O, & Modules**
*   **Day 6: Functions & Arguments**
    *   *Concept*: Defining functions, parameters, return values, default arguments, keyword arguments, and parameter unpacking (`*args`, `**kwargs`).
    *   *Concept File*: `week2_functions_io/day6_concepts.md`
*   **Day 7: Scope & Functional Helpers**
    *   *Concept*: Local vs. Global scope, variable shadowing, lambda functions, and helpers: `map()`, `filter()`, `zip()`, and `enumerate()`.
    *   *Concept File*: `week2_functions_io/day7_concepts.md`
*   **Day 8: File Handling & Serialization**
    *   *Concept*: Reading and writing text files using the context manager (`with open`), file paths, and parsing JSON data.
    *   *Concept File*: `week2_functions_io/day8_concepts.md`
*   **Day 9: Error & Exception Handling**
    *   *Concept*: Python's exception hierarchy, handling exceptions with `try-except-else-finally`, raising exceptions, and defining custom exception classes.
    *   *Concept File*: `week2_functions_io/day9_concepts.md`
*   **Day 10: Modules, Packages, and `pip`**
    *   *Concept*: Standard library (`math`, `datetime`, `random`), importing modules, creating custom modules, the role of `__name__ == '__main__'`, and installing third-party libraries using `pip`.
    *   *Concept File*: `week2_functions_io/day10_concepts.md`
*   **Week 2 Challenge: JSON-based CLI Task Manager**
    *   *Task*: Create a command-line task manager application that lets users add, delete, toggle, and view tasks, persistent to a `tasks.json` file.

---

#### **Week 3: Object-Oriented Programming (OOP)**
*   **Day 11: Classes & Object Basics**
    *   *Concept*: Blueprint vs. instance, constructor (`__init__`), instance attributes, and the role of `self`.
    *   *Concept File*: `week3_oop/day11_concepts.md`
*   **Day 12: Encapsulation & Class/Static Methods**
    *   *Concept*: Access modifiers (`_private`, `__mangled`), property getters/setters (`@property`), `@classmethod`, and `@staticmethod`.
    *   *Concept File*: `week3_oop/day12_concepts.md`
*   **Day 13: Inheritance & Polymorphism**
    *   *Concept*: Subclasses, method overriding, inheritance chains, `super()`, multiple inheritance, and polymorphism (Duck Typing).
    *   *Concept File*: `week3_oop/day13_concepts.md`
*   **Day 14: Special (Dunder) Methods**
    *   *Concept*: Customizing object representations (`__str__`, `__repr__`), mathematical operators (`__add__`, `__sub__`), and equality checks (`__eq__`, `__hash__`).
    *   *Concept File*: `week3_oop/day14_concepts.md`
*   **Day 15: Abstract Base Classes (ABCs)**
    *   *Concept*: Enforcing interfaces using Python's `abc` module and `@abstractmethod`.
    *   *Concept File*: `week3_oop/day15_concepts.md`
*   **Week 3 Challenge: Inventory & Order Management System**
    *   *Task*: Build an inventory system using class inheritance for products (e.g. Digital vs. Physical), encapsulated attributes for prices, and properties for validation.

---

#### **Week 4: Advanced Python Concepts & Capstone**
*   **Day 16: List Comprehensions & Advanced Iterators**
    *   *Concept*: List, set, and dict comprehensions, nested comprehensions, generator expressions, and building custom iterators with `__iter__` and `__next__`.
    *   *Concept File*: `week4_advanced/day16_concepts.md`
*   **Day 17: Generators & Context Managers**
    *   *Concept*: Memory efficiency using generator functions with `yield`, and writing custom resource managers using `__enter__` and `__exit__` or the `@contextmanager` decorator.
    *   *Concept File*: `week4_advanced/day17_concepts.md`
*   **Day 18: Decorators**
    *   *Concept*: First-class functions, closures, custom decorators, decorators accepting arguments, and preserving metadata with `functools.wraps`.
    *   *Concept File*: `week4_advanced/day18_concepts.md`
*   **Day 19: Working with Web APIs**
    *   *Concept*: Understanding HTTP requests, using the `requests` library, handling status codes, query parameters, and parsing JSON API responses.
    *   *Concept File*: `week4_advanced/day19_concepts.md`
*   **Day 20: Unit Testing & Best Practices**
    *   *Concept*: Writing clean, testable code, using the standard library `unittest` module, test suites, assert methods, and mock objects.
    *   *Concept File*: `week4_advanced/day20_concepts.md`
*   **Week 4 Challenge / Capstone Project: Personal Finance Tracker CLI**
    *   *Task*: A complete CLI utility that fetches exchange rates from a public API, parses input files of transactions, validates records using property classes, logs operations, and includes unit tests verifying functionality.

---

## Verification Plan

### Automated Tests
For each day, you can run the test suite to verify your solution:
```powershell
python week1_basics/day1_test.py
python week1_basics/day2_test.py
# ... etc.
```

### Manual Verification
- We will execute the scripts directly under PowerShell to verify interactive tasks (e.g., configuring VS Code on Day 1, entering variables on Day 2).
