# Day 4: Encapsulation & Access Modifiers

Welcome to Day 4! Today we explore **Encapsulation**, one of the core principles of OOP. Encapsulation is the practice of hiding an object's internal state and requiring all interaction to occur through public methods.

In languages like Java or C++, you have keywords like `public`, `protected`, and `private`. Python does not have these keywords. Instead, Python relies on **naming conventions** and a mechanism called **Name Mangling**.

We will cover:
1. **Public Attributes (No Underscores)**
2. **Protected Attributes (Single Underscore `_`)**
3. **Private Attributes (Double Underscore `__`) & Name Mangling**

---

## 1. Public Attributes

By default, all attributes and methods in a Python class are public. Anyone can read or modify them from outside the class.

```python
class User:
    def __init__(self, username):
        self.username = username  # Public attribute

u = User("alice")
u.username = "bob"  # Anyone can modify it directly
print(u.username)   # Output: bob
```

---

## 2. Protected Attributes (`_`)

If you want to signal to other developers that an attribute or method is internal and should **not** be accessed from outside the class (except in subclasses), prefix it with a **single underscore** `_`.

```python
class User:
    def __init__(self, username):
        self.username = username
        self._login_attempts = 0  # Protected attribute (by convention)
```

> [!WARNING]
> The single underscore is purely a **convention**. Python does not prevent you from accessing `u._login_attempts` from outside. It is a "gentleman's agreement" that you should treat it as private.

```python
u = User("alice")
print(u._login_attempts)  # ⚠️ Works, but is considered bad practice!
```

---

## 3. Private Attributes (`__`) & Name Mangling

If you want to make an attribute strongly internal, prefix it with a **double underscore** `__` (and no trailing underscores). This triggers **Name Mangling**.

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute (name-mangled)
```

If we try to access `__balance` directly:
```python
account = BankAccount("Alice", 1000)
# print(account.__balance)  # ❌ Raises AttributeError: 'BankAccount' object has no attribute '__balance'
```

### How Name Mangling Works
Python changes the name of `__balance` behind the scenes to prevent accidental lookup or overriding. The new name is formatted as `_ClassName__attributeName`.

```python
# We can still access it if we use the mangled name:
print(account._BankAccount__balance)  # Output: 1000
```

> [!IMPORTANT]
> Python's name mangling is NOT for security or encryption. It is designed to prevent naming collisions in inheritance hierarchies (e.g., if a subclass accidentally defines an attribute with the same name). Never store plain text passwords or secrets in name-mangled variables expecting them to be secure.

### The Correct Way: Public Methods for Private Data
Instead of direct access, expose public methods to read or write the private attribute safely:

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
```

---
Now, let's complete [day4_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week1_foundations/day4_assignment.py)!
