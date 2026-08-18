# Python Class Mastery Curriculum: Day-by-Day 1-Month Learning Plan

This curriculum provides a structured, daily learning path to elevate you to a Python Object-Oriented Programming (OOP) expert. Each day contains a concise **Concept Guide**, an **Assignment Template** with inline exercises, and a **Test Runner** to automatically verify your solutions.

All learning materials, exercises, and projects will be structured under [pyclass_expert](file:///g:/Backup%20Fdrive/Python/pyclass_expert).

---

## User Review Required

Please review the proposed day-by-day structure. If you are satisfied, we will initialize **Day 1** (Concepts, Assignment, and Tests).

---

## Open Questions

> [!IMPORTANT]
> 1. **Workspace Sync**: Are you running Python 3.9+? (We will use features like Type Hinting and Dataclasses which are standard in modern Python).
> 2. **Pace Check**: Does 5 days a week of concepts/assignments with a weekend challenge suit your schedule?

---

## Proposed Curriculum & Changes

### Directory Structure

```
pyclass_expert/
├── week1_foundations/
│   ├── day1_concepts.md        # Classes, objects, __init__, self
│   ├── day1_assignment.py      # Exercise placeholders for Day 1
│   ├── day1_test.py            # Test suite for Day 1
│   ├── day2_...
│   └── week1_challenge.py      # Weekend challenge
├── week2_relationships/
│   ├── day6_...
│   └── week2_challenge.py
├── week3_dunder_methods/
│   ├── day11_...
│   └── week3_challenge.py
└── week4_metaprogramming/
    ├── day16_...
    └── capstone_project/       # Capstone ORM/Validation engine
```

---

### Day-by-Day Breakdown

#### **Week 1: OOP Foundations & Class Basics**
*   **Day 1: Class, Object, and the Constructor**
    *   *Concept*: Define classes, instantiate objects, explain the `__init__` constructor and the purpose of `self`.
    *   *Assignment*: Create a simple `Book` class and dynamic instantiator.
*   **Day 2: Attribute Scoping (Instance vs. Class Attributes)**
    *   *Concept*: Read/write namespaces, class-level variables vs. instance-level variables, and examining attributes using `__dict__`.
    *   *Assignment*: Build a `Student` registration tracking class using class-level counters.
*   **Day 3: Instance, Class, and Static Methods**
    *   *Concept*: Method types and decorator differences: when to use `self` (instance), `@classmethod` (factories/alternative constructors), and `@staticmethod` (isolated utilities).
    *   *Assignment*: Create a `DateUtility` and a `User` manager using different method types.
*   **Day 4: Encapsulation & Access Modifiers**
    *   *Concept*: Python naming conventions for access control: public, protected (`_variable`), and private (`__variable` with Name Mangling).
    *   *Assignment*: Build a `BankAccount` with strict validation and name-mangled variables.
*   **Day 5: Pythonic Getters & Setters with Properties**
    *   *Concept*: The `@property` decorator, setters, and deleters. Why Java-style `get_x()` and `set_x()` are anti-patterns in Python.
    *   *Assignment*: Create a `Temperature` and `Circle` class using property-based validations.
*   **Week 1 Challenge: Automated Library System** (Applying Days 1-5).

---

#### **Week 2: Inheritance, Polymorphism, & Composition**
*   **Day 6: Single & Multi-level Inheritance**
    *   *Concept*: Subclassing, method overriding, and extending base class behavior.
    *   *Assignment*: Implement a hierarchy of employee types (e.g., `Employee` -> `Manager`).
*   **Day 7: Multiple Inheritance & Method Resolution Order (MRO)**
    *   *Concept*: How multiple inheritance works, cooperative inheritance with `super()`, and how the C3 Linearization algorithm determines the MRO.
    *   *Assignment*: Solve the "Diamond Problem" using coordinated `super()` calls.
*   **Day 8: Polymorphism & Duck Typing**
    *   *Concept*: The concept of "If it walks like a duck...". Dynamic typing and writing code that accepts any class with a specific interface without explicit inheritance.
    *   *Assignment*: Create a `DocumentProcessor` that handles CSV, JSON, and PDF documents uniformly.
*   **Day 9: Abstract Base Classes (ABCs)**
    *   *Concept*: Using Python’s `abc` module, `ABC`, and `@abstractmethod` to enforce interfaces at compile/import time.
    *   *Assignment*: Define a `Notification` system requiring implementations of `send()`.
*   **Day 10: Composition vs. Inheritance**
    *   *Concept*: "Has-A" relationship vs. "Is-A" relationship. Why design systems prefer composition over deep inheritance hierarchies.
    *   *Assignment*: Create a `Car` class composed of `Engine`, `Tires`, and `Transmission` objects.
*   **Week 2 Challenge: Combat RPG Engine** (Applying Days 6-10).

---

#### **Week 3: Dunder/Magic Methods & Custom Protocols**
*   **Day 11: Object Presentation and Hashing**
    *   *Concept*: Customizing how your objects print and debug (`__str__` vs. `__repr__`), and mapping custom object hashes using `__hash__` and `__eq__` to store objects in sets/dicts.
    *   *Assignment*: Create an immutable `Point` class that can be safely used as a dictionary key.
*   **Day 12: Operator Overloading**
    *   *Concept*: Arithmetic (`__add__`, `__sub__`, `__mul__`) and comparison (`__lt__`, `__le__`, `__eq__`, etc.) magic methods.
    *   *Assignment*: Build a custom `Money` class handling different currencies and algebraic operations.
*   **Day 13: Container & Sequence Protocols**
    *   *Concept*: Implementing `__len__`, `__getitem__`, `__setitem__`, `__delitem__`, and `__contains__` to make a custom object behave exactly like a list or dictionary.
    *   *Assignment*: Build a `DeckOfCards` class supporting indexing, slicing, and membership checks.
*   **Day 14: Iterables & Callables**
    *   *Concept*: Turning objects into iterators (`__iter__` and `__next__`) and making custom objects callable as functions (`__call__`).
    *   *Assignment*: Build a custom generator-like class and a configurable mathematical function object.
*   **Day 15: Context Managers (`with` blocks)**
    *   *Concept*: The resource lifecycle, implementing `__enter__` and `__exit__`, and error handling inside context managers.
    *   *Assignment*: Build a `DatabaseConnection` mockup and a file `HTMLTag` wrapper.
*   **Week 3 Challenge: Custom Queryable Dataset Class** (Applying Days 11-15).

---

#### **Week 4: Advanced Metaprogramming & Modern Utilities**
*   **Day 16: Attribute Hooking (`__getattr__` vs `__getattribute__`)**
    *   *Concept*: Dynamic attribute resolution, intercepting attribute lookups, and routing calls dynamically.
    *   *Assignment*: Build a dynamic API client wrapper that translates attribute calls to API routes.
*   **Day 17: The Descriptor Protocol**
    *   *Concept*: Creating reusable, validation-backed properties using classes that implement `__get__`, `__set__`, and `__delete__`.
    *   *Assignment*: Build a `Validator` framework containing `IntegerField` and `StringField` descriptors.
*   **Day 18: Object Creation Lifecycle (`__new__` vs `__init__`)**
    *   *Concept*: Intercepting object creation before initialization. Implementing Singleton, caching mechanisms, and immutable custom types.
    *   *Assignment*: Build a thread-safe `DatabaseConnectionPool` Singleton.
*   **Day 19: Metaclasses & `__init_subclass__`**
    *   *Concept*: Classes that create classes. Modifying class creation, registering subclasses automatically, and using modern `__init_subclass__` hook.
    *   *Assignment*: Build a plugin registry system using custom metaclasses.
*   **Day 20: Dataclasses & Slots Optimization**
    *   *Concept*: The modern `@dataclass` decorator (`field`, post-initialization, immutability) and using `__slots__` to drastically reduce memory usage and speed up lookup.
    *   *Assignment*: Build an high-performance inventory tracking system.
*   **Capstone Project: Mini validation ORM framework** (Applying Days 16-20).

---

## Verification Plan

### Automated Tests
Each day's concepts will be tested by running:
- `python pyclass_expert/weekX_folder/dayY_test.py`

### Manual Verification
- We will execute script assignments directly to inspect debugging representation outputs.
