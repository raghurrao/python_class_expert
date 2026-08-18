# Day 16: Attribute Hooking (__getattr__ vs. __getattribute__)

Welcome to Week 4! This week we cover **Metaprogramming**—writing code that intercepts, creates, or modifies class and object execution dynamically.

Today we explore how to capture and control attribute access.

We will cover:
1. **The Fallback Lookup (`__getattr__`)**
2. **The Global Interceptor (`__getattribute__`)**
3. **Preventing Infinite Recursion**
4. **Writing to Attributes (`__setattr__`)**

---

## 1. The Fallback Lookup: `__getattr__`

If a user tries to access an attribute that does **not** exist in the object's namespace, Python raises an `AttributeError`. However, if you implement `__getattr__(self, name)`, Python calls it as a **fallback** instead of crashing.

```python
class DynamicDict:
    def __init__(self):
        self.data = {"theme": "dark"}

    def __getattr__(self, name):
        # Triggered ONLY when the attribute is missing (e.g. obj.theme is fine, but obj.font is missing)
        print(f"Attribute '{name}' not found. Fetching from dictionary...")
        if name in self.data:
            return self.data[name]
        raise AttributeError(f"No attribute named '{name}'")
```

Usage:
```python
d = DynamicDict()
print(d.data)    # Normal access (does not trigger __getattr__)
print(d.theme)   # Triggers __getattr__, outputs "dark"
# print(d.font)  # Triggers __getattr__, raises AttributeError
```

---

## 2. The Global Interceptor: `__getattribute__`

If you want to intercept **every single** attribute access (even if the attribute *does* exist), implement `__getattribute__(self, name)`.

```python
class LoggingObject:
    def __init__(self):
        self.secret = "42"

    def __getattribute__(self, name):
        print(f"LOG: Accessing attribute '{name}'")
        return super().__getattribute__(name)  # Redirects to standard lookup
```

Usage:
```python
obj = LoggingObject()
print(obj.secret)
# Output:
# LOG: Accessing attribute 'secret'
# 42
```

---

## 3. The Infinite Recursion Trap ⚠️

A major hazard when writing `__getattribute__` (and sometimes `__setattr__`) is infinite recursion.

If you try to read `self.secret` inside `__getattribute__` like this:
```python
# ❌ NEVER DO THIS
def __getattribute__(self, name):
    if name == "special":
        return self.data  # <-- ⚠️ This lookup of 'self.data' triggers __getattribute__ again!
```
Python will call `__getattribute__` inside `__getattribute__` forever until the stack overflows (`RecursionError`).

### The Solution: Use `super()`
Always bypass self-lookup by calling the base class `super()` implementation:
```python
# ✅ DO THIS
def __getattribute__(self, name):
    # Triggers standard lookup bypassing this method
    return super().__getattribute__(name)
```

---

## 4. Writing Attributes: `__setattr__`

To intercept writes/assignments (e.g. `obj.name = "Alice"`), implement `__setattr__(self, name, value)`. You must use `super().__setattr__` to write to the dictionary safely.

```python
class LockedObject:
    def __setattr__(self, name, value):
        if name == "read_only":
            raise AttributeError("Cannot write to read_only attribute")
        super().__setattr__(name, value)  # Safe write
```

---
Let's head to [day16_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week4_metaprogramming/day16_assignment.py) to write a dynamic JSON wrapper and read-only validator!
