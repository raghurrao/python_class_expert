# Day 9: Abstract Base Classes (ABCs)

Welcome to Day 9! While **Duck Typing** is great, there are times you want to enforce strict rules on class designs. For example, if you are building a plugin system, you want to guarantee that every plugin has a `run()` method.

Python provides **Abstract Base Classes (ABCs)** via the `abc` module to define interfaces and enforce contracts.

We will cover:
1. **What is an Abstract Base Class?**
2. **Declaring ABCs with `abc.ABC` and `@abstractmethod`**
3. **Enforcing subclass constraints**

---

## 1. What is an Abstract Base Class?

An Abstract Base Class (ABC) is a class that is:
* **Non-instantiable**: You cannot create objects directly from it.
* **A template/contract**: It defines method signatures that must be implemented by any concrete subclass.

---

## 2. Declaring ABCs

To create an ABC, inherit from `abc.ABC` and use the `@abstractmethod` decorator to mark methods as abstract.

```python
from abc import ABC, abstractmethod

# DatabaseConnector acts as an interface definition
class DatabaseConnector(ABC):
    
    @abstractmethod
    def connect(self):
        """Must be overridden by all concrete subclasses to establish connection."""
        pass

    @abstractmethod
    def execute_query(self, query):
        """Must be overridden to run SQL/queries."""
        pass
```

---

## 3. Enforcing Constraints

If you try to create an instance of `DatabaseConnector` directly:
```python
# conn = DatabaseConnector()
# ❌ Raises TypeError: Can't instantiate abstract class DatabaseConnector with abstract methods connect, execute_query
```

If we write a subclass that only implements `connect` but forgets `execute_query`:
```python
class PostgresConnector(DatabaseConnector):
    def connect(self):
        return "Connected to Postgres!"

# pg = PostgresConnector()
# ❌ Raises TypeError: Can't instantiate abstract class PostgresConnector with abstract method execute_query
```

To make it concrete and instantiable, we must override **all** abstract methods:
```python
class PostgresConnector(DatabaseConnector):
    def connect(self):
        return "Connected to Postgres!"

    def execute_query(self, query):
        return f"Executing query: {query}"

# ✅ Works perfectly!
pg = PostgresConnector()
print(pg.connect())
```

---
Let's head to [day9_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week2_relationships/day9_assignment.py) to design an abstract File System interface!
