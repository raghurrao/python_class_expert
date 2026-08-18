# Day 7: Multiple Inheritance & Method Resolution Order (MRO)

Welcome to Day 7! Today we dive into one of Python's most powerful (and complex) OOP features: **Multiple Inheritance** and the **Method Resolution Order (MRO)**.

Multiple inheritance allows a class to inherit from more than one parent class.

We will cover:
1. **Multiple Inheritance & The Diamond Problem**
2. **Method Resolution Order (MRO)**
3. **Cooperative Inheritance & `super()`**

---

## 1. Multiple Inheritance & The Diamond Problem

Imagine the following hierarchy:
```
    Base (defines ping)
    /  \
   A    B  (override ping)
    \  /
     C     (inherits A and B)
```
If we instantiate `C` and call `c.ping()`, which class's `ping` method is executed: `A`'s or `B`'s? This ambiguity is known as the **Diamond Problem**.

Python solves this using a deterministic lookup order called **C3 Linearization**.

---

## 2. Method Resolution Order (MRO)

The MRO is the list of classes Python checks, from left to right, when looking up an attribute or method. 

You can inspect the MRO of any class using the `.mro()` method or the `__mro__` attribute:

```python
class Base:
    def ping(self):
        return "Base"

class A(Base):
    def ping(self):
        return "A"

class B(Base):
    def ping(self):
        return "B"

class C(A, B):
    pass

print(C.mro())
# Output: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]
```

When calling `C().ping()`, Python checks:
1. Class `C` (Not found)
2. Class `A` (Found! Returns `"A"`)
3. Class `B` and `Base` are skipped because Python found `ping` in `A` first.

---

## 3. Cooperative Inheritance & `super()`

A common misconception is that `super()` calls the parent class. In multiple inheritance, `super()` calls the **next class in the MRO list**, which might actually be a **sibling class**, not a parent class!

To make multiple inheritance work correctly, all constructors must cooperatively call `super().__init__(*args, **kwargs)` and accept arbitrary parameters to pass along:

```python
class ComponentA:
    def __init__(self, color="red", **kwargs):
        print("Initializing ComponentA...")
        super().__init__(**kwargs)  # Pass remaining args along the MRO
        self.color = color

class ComponentB:
    def __init__(self, size="medium", **kwargs):
        print("Initializing ComponentB...")
        super().__init__(**kwargs)  # Pass remaining args along the MRO
        self.size = size

class CombinedDevice(ComponentA, ComponentB):
    def __init__(self, name, **kwargs):
        print("Initializing CombinedDevice...")
        super().__init__(**kwargs)
        self.name = name
```

If we inspect the MRO of `CombinedDevice`:
```python
print(CombinedDevice.mro())
# Output: [CombinedDevice, ComponentA, ComponentB, object]
```

If we instantiate it:
```python
device = CombinedDevice("Gadget", color="blue", size="large")
# Output:
# Initializing CombinedDevice...
# Initializing ComponentA...
# Initializing ComponentB...
```
Notice how `super()` in `ComponentA` called the constructor of `ComponentB` because `ComponentB` is the next class in `CombinedDevice`'s MRO! This is called **Cooperative Inheritance**.

---
Let's head to [day7_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week2_relationships/day7_assignment.py) to practice structuring cooperative calls!
