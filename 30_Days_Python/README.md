# 🐍 30-Day Python Mastery Curriculum

Welcome to your structured, day-by-day learning program designed to take you from a complete beginner to a **Python Expert** in 1 month! 

This repository is organized into weekly modules. Each day contains a concise concept guide, an assignment with structured exercises, and a test suite to automatically verify your solutions.

---

## 📅 Curriculum Overview

### [🟢 Week 1: Environment Setup & Python Basics](file:///g:/30%20days%20Leaarning/30_Days_Python/week1_basics)
*   **Day 1: VS Code & Python Setup** – Install Python, configure VS Code, and learn how to run Python scripts.
*   **Day 2: Variables & Operators** – Dynamic typing, casting, arithmetic/logical operations, and f-strings.
*   **Day 3: Control Flow** – Conditional branches (`if-elif-else`) and loops (`for`/`while`).
*   **Day 4: Sequences** – List and Tuple slicing, index manipulation, and sequence unpacking.
*   **Day 5: Dictionaries & Sets** – Key-value mappings, safe lookups (`.get()`), and unique sets.
*   **Week 1 Challenge** – CLI text analyzer and operations calculator.

### [🔵 Week 2: Functions, File I/O, & Modules](file:///g:/30%20days%20Leaarning/30_Days_Python/week2_functions_io)
*   **Day 6: Functions & Arguments** – Arguments, keyword parameters, and variable parameters (`*args`/`**kwargs`).
*   **Day 7: Scope & Helpers** – Local vs global variable access, lambda functions, and functional programming tools (`map`, `filter`, `zip`, `enumerate`).
*   **Day 8: File Handling** – Opening, reading, appending to text files, and handling JSON data.
*   **Day 9: Error & Exception Handling** – Handling runtime crashes with `try-except-finally` blocks and custom exception declarations.
*   **Day 10: Modules & pip** – Importing standard libraries, standard execution guards (`__name__ == '__main__'`), and third-party packages.
*   **Week 2 Challenge** – CLI JSON Task Manager with text file persistence.

### [🟡 Week 3: Object-Oriented Programming (OOP)](file:///g:/30%20days%20Leaarning/30_Days_Python/week3_oop)
*   **Day 11: Classes & Objects** – Blueprints vs instances, attributes, and instance methods.
*   **Day 12: Encapsulation & Properties** – Public/private attributes, name mangling, property getters/setters, class methods, and static methods.
*   **Day 13: Inheritance & Polymorphism** – Superclassing, method overriding, constructor routing, and Duck Typing.
*   **Day 14: Special (Dunder) Methods** – Presentation overloading (`__str__`/`__repr__`), equality checks (`__eq__`), and arithmetic operator overloading (`__add__`).
*   **Day 15: Abstract Classes (ABCs)** – Interface definitions and concrete implementation subclassing.
*   **Week 3 Challenge** – Class-oriented Inventory Management System.

### [🔴 Week 4: Advanced Python & Capstone](file:///g:/30%20days%20Leaarning/30_Days_Python/week4_advanced)
*   **Day 16: List Comprehensions & Iterators** – Creating collections inline, dict comprehensions, and building custom iterators.
*   **Day 17: Generators & Context Managers** – Lazy evaluations, yield statements, and custom context managers.
*   **Day 18: Decorators** – Functions as first-class citizens, closures, and custom function decorators.
*   **Day 19: Working with Web APIs** – HTTP requests, REST APIs, query arguments, and offline mocking.
*   **Day 20: Unit Testing & Mutation Testing** – Writing standard unit test assertions and checking robustness using mutation testing.
*   **Week 4 Challenge & Capstone** – Personal Finance Tracker CLI utilizing currency APIs and CSV serialization.

---

## 🛠️ Getting Started: Daily Learning Workflow

For each day (e.g., Day 6):
1. **Read the Concepts Guide**: Open the corresponding markdown file (e.g., `week2_functions_io/day6_concepts.md`) to learn the theory.
2. **Implement the Assignment**: Open the assignment template (e.g., `week2_functions_io/day6_assignment.py`) and write code to complete the `# TODO` sections.
3. **Run the Test Suite**: Open your terminal in VS Code (`Ctrl+``) and execute the test runner:
   ```powershell
   python week2_functions_io/day6_test.py
   ```
4. **Iterate**: Fix any assertion errors until you receive the `SUCCESS: Congratulations!` message!

---

## 🧪 Mutation Testing (Day 20)
On Day 20, you will be writing unit tests! To verify that your test assertions are robust, run the mutation checker:
```powershell
python week4_advanced/day20_verifier.py
```
This checker will temporarily inject bugs into the target functions and check if your unit tests fail. If they fail, it means your tests successfully detected the bugs!
