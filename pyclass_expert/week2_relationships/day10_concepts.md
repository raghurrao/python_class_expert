# Day 10: Composition vs. Inheritance

Welcome to Day 10! Today we explore a fundamental software design principle: **"Favor object composition over class inheritance."**

While inheritance is useful, beginners often overuse it. For example, inheriting `AdminUser` from `User`, and `SuperAdminUser` from `AdminUser` can lead to tight coupling. If you change a method in `User`, it can break subclasses down the line. This is known as the **Fragile Base Class** problem.

**Composition** offers a more flexible alternative.

We will cover:
1. **Inheritance (Is-A) vs. Composition (Has-A)**
2. **Implementing Composition**
3. **Why Composition is more flexible**

---

## 1. Inheritance (Is-A) vs. Composition (Has-A)

* **Inheritance (Is-A)**: A `Car` **is a** `Vehicle`. A `Dog` **is an** `Animal`. Use this when class types have a strict hierarchical relationship.
* **Composition (Has-A)**: A `Car` **has an** `Engine`. A `Computer` **has a** `CPU`. Instead of inheriting features, you build classes by nesting references to other objects.

---

## 2. Implementing Composition

Let's build a `Computer` using composition instead of inheritance:

```python
class CPU:
    def __init__(self, model, cores):
        self.model = model
        self.cores = cores

    def process(self):
        return f"CPU {self.model} processing data..."

class RAM:
    def __init__(self, size_gb):
        self.size_gb = size_gb

    def load(self):
        return f"Loading data into {self.size_gb}GB RAM..."

class Computer:
    def __init__(self, cpu: CPU, ram: RAM):
        # Nested references to component objects
        self.cpu = cpu
        self.ram = ram

    def run(self):
        # Delegate responsibilities to components
        return f"{self.cpu.process()} | {self.ram.load()}"
```

Usage:
```python
my_cpu = CPU("Intel i7", 8)
my_ram = RAM(16)

my_pc = Computer(my_cpu, my_ram)
print(my_pc.run())
# Output: CPU Intel i7 processing data... | Loading data into 16GB RAM...
```

---

## 3. Why Composition is Flexible

With inheritance, if you want a `GamingComputer`, you have to subclass `Computer`. What if you want a `LiquidCooledGamingComputer`? You'd have to subclass again. 

With composition, you just swap component objects dynamically at runtime:

```python
class LiquidCooler:
    def cool(self):
        return "Cooling system active!"

class GamingComputer:
    def __init__(self, cpu, ram, cooler):
        self.cpu = cpu
        self.ram = ram
        self.cooler = cooler  # Swap/Add components easily!
```

Composition allows you to create highly modular, testable, and loosely coupled code.

---
Let's head to [day10_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week2_relationships/day10_assignment.py) to compose an e-commerce order system!
