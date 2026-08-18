# Day 12: Encapsulation & Class/Static Methods

Today, we look at **Encapsulation**—hiding internal data representation from outside modifications—and explore method types that don't depend directly on object instances.

---

## 1. Access Modifiers & Name Mangling

Python does not have strict keyword-based access control (like Java's `private` or `protected`). Instead, it uses naming conventions:
*   **Public**: Accessible anywhere. E.g., `self.name`
*   **Protected**: Intended for internal use within the class and subclasses. Prefixed with a single underscore. E.g., `self._tax_rate`
*   **Private**: Intended to be completely hidden. Prefixed with a double underscore. E.g., `self.__salary`

### Name Mangling
For private variables (with `__`), Python alters the internal attribute name under the hood to include the class name. This is called **Name Mangling**.
```python
class Account:
    def __init__(self):
        self.__balance = 100

acc = Account()
# print(acc.__balance)  # Raises AttributeError!
print(acc._Account__balance)  # Output: 100 (Name mangling: _ClassName__attribute)
```

---

## 2. Properties (Getters & Setters)

Instead of writing verbose Java-style getters/setters (`get_balance()`, `set_balance(x)`), Python uses the `@property` decorator. This allows you to treat methods like attributes while executing validation logic when getting or setting them.

```python
class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):  # Getter
        return self._balance

    @balance.setter
    def balance(self, value):  # Setter
        if value < 0:
            raise ValueError("Balance cannot be negative!")
        self._balance = value

acc = Account(100)
print(acc.balance)  # Output: 100 (Accessed like a field, but calls the property method!)
acc.balance = 150   # Valid update
# acc.balance = -5  # Raises ValueError!
```

---

## 3. Class Methods & Static Methods

*   **Instance Methods**: Take `self` as the first argument. Operates on a specific instance.
*   **Class Methods (`@classmethod`)**: Take `cls` (the class itself) as the first argument. Useful as alternative constructors (factories).
*   **Static Methods (`@staticmethod`)**: Take neither `self` nor `cls`. Act like normal functions placed within the class namespace for logical grouping.

```python
class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    @classmethod
    def create_admin(cls, name):
        # Alternative constructor (factory method)
        return cls(name, "Admin")

    @staticmethod
    def is_valid_username(username):
        return len(username) >= 3

# Using class method
admin = User.create_admin("Alice")
print(admin.role)  # Output: Admin

# Using static method
print(User.is_valid_username("ab"))  # Output: False
```

---

Now, proceed to the Day 12 Assignment: [day12_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week3_oop/day12_assignment.py).
