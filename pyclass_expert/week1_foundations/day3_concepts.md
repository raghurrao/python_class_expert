# Day 3: Instance, Class, and Static Methods

Welcome to Day 3! Now that you know how attributes store state (State = current values stored by something) in class and instance namespaces(__dict__ shows namespace as dictionary), we will learn how **methods** define behaviors. 

Python classifies methods into three types, each with its own decorator, namespace scope, and purpose:
1. **Instance Methods**
2. **Class Methods (`@classmethod`)**
3. **Static Methods (`@staticmethod`)**

---

## 1. Instance Methods

These are the default methods. They are used to read or modify the state of a specific object instance.

* **Decorator**: None.
* **First Parameter**: `self` (points to the specific object instance).
* **Namespace Scope**: Accesses instance attributes and class attributes.

```python
class CoffeeMachine:
    def __init__(self, brand):
        self.brand = brand
        self.water_level = 100  # Instance attribute
        
    def brew(self):
        # Accessing and modifying instance state
        self.water_level -= 10
        return f"Brewing delicious coffee from {self.brand}!"
```

---

## 2. Class Methods (`@classmethod`)

Class methods act on the class namespace rather than a specific object. They are commonly used as **factory methods** (alternative constructors).

* **Decorator**: `@classmethod`
* **First Parameter**: `cls` (points to the Class itself, not the object instance).
* **Namespace Scope**: Accesses class attributes only. Cannot access instance attributes (since no instance exists when it is run!).

### Use Case: Alternative Constructors
Imagine you want to create a `CoffeeMachine` but the brand name is packed inside a JSON string or a CSV row. Instead of writing parsing logic in your main code, you build a custom factory:

```python
import json

class CoffeeMachine:
    def __init__(self, brand):
        self.brand = brand
        
    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        # cls(...) is equivalent to calling CoffeeMachine(...)
        return cls(data["brand"])

# Usage:
config = '{"brand": "DeLonghi"}'
machine = CoffeeMachine.from_json(config)
print(machine.brand)  # Output: DeLonghi
```

---

## 3. Static Methods (`@staticmethod`)

Static methods are regular utility functions that belong to the class's namespace. They do not depend on the state of the object or the class.

* **Decorator**: `@staticmethod`
* **First Parameter**: None. (Just standard function arguments).
* **Namespace Scope**: Does not access instance or class state.

### Use Case: Utility functions
If a function is conceptually related to the class (e.g., checking if a temperature is absolute zero, or validation check) but doesn't need to look at any attributes:

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
        
    @staticmethod
    def is_habitable(celsius):
        # Independent utility checking bounds
        return 0 <= celsius <= 45
```

---

## Cheat Sheet: Which one should I use?

| Method Type | Decorator | First Param | Can Access Instance (`self`)? | Can Access Class (`cls`)? | Primary Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Instance Method** | None | `self` | **Yes** | **Yes** (via `self.__class__` or name) | Regular object behavior & modification of state. |
| **Class Method** | `@classmethod` | `cls` | **No** | **Yes** | Factory methods / Alternative constructors. |
| **Static Method** | `@staticmethod` | None | **No** | **No** | Utility helper functions related to the topic. |

---
Ready to code? Proceed to [day3_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week1_foundations/day3_assignment.py)!
