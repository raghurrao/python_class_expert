# Day 5: Pythonic Getters & Setters with Properties

Welcome to Day 5! Today we look at how to manage attribute access elegantly. 

In other OOP languages (like Java), the rule of thumb is: make all attributes private and write `getX()` and `setX()` methods for every single one. In Python, this is considered an **anti-pattern**. It leads to bloated code and violates the **Uniform Access Principle** (the idea that accessing attributes or properties of an object should look identical).

Python's solution is the `@property` decorator.

We will cover:
1. **The Uniform Access Principle & The Pythonic Way**
2. **Declaring Properties (`@property`, setter, deleter)**
3. **Dynamic / Computed Attributes**

---

## 1. The Pythonic Way

In Python, we start by exposing attributes as public. If we later need validation, we don't have to change all the user's code from `obj.value` to `obj.get_value()`. Instead, we convert the attribute into a **Property** without changing the public interface.

### Java style (Anti-pattern in Python)
```python
# ❌ DON'T DO THIS
class Celsius:
    def __init__(self, temp=0):
        self.set_temp(temp)

    def get_temp(self):
        return self._temp

    def set_temp(self, value):
        self._temp = value
```

### Pythonic Property style
```python
# ✅ DO THIS
class Celsius:
    def __init__(self, temp=0):
        self.temp = temp  # Triggers the setter!

    @property
    def temp(self):
        print("Getting value...")
        return self._temp

    @temp.setter
    def temp(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible!")
        self._temp = value
```

Now, we access the property exactly like a normal attribute:
```python
c = Celsius(20)      # Output: Setting value...
print(c.temp)        # Output: Getting value... \n 20
c.temp = -300        # Output: ValueError!
```

---

## 2. Property Getter, Setter, and Deleter

Properties support three actions:
* **Getter**: Reads the value (decorated with `@property`).
* **Setter**: Writes the value (decorated with `@property_name.setter`).
* **Deleter**: Deletes the value (decorated with `@property_name.deleter`).

```python
class Profile:
    def __init__(self, username):
        self._username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, val):
        if not val:
            raise ValueError("Username cannot be empty")
        self._username = val

    @username.deleter
    def username(self):
        print("Deleting username...")
        del self._username
```

---

## 3. Dynamic / Computed Attributes

Properties are also excellent for attributes that can be computed dynamically from other attributes. This prevents duplicate data fields going out of sync.

```python
class Square:
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        # Dynamically calculated. No need to store self.area in __init__!
        return self.side ** 2
```

---
Let's head to [day5_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week1_foundations/day5_assignment.py) to write some property decorators!
