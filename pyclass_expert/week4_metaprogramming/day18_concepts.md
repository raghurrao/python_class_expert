# Day 18: Object Creation Lifecycle (__new__ vs. __init__)

Welcome to Day 18! Today we look at how Python objects are actually born.

Most Python developers believe `__init__` is the constructor. That is not entirely true.
*   **`__new__`** is the actual constructor. It is a class method that allocates memory and returns a brand-new instance of the class.
*   **`__init__`** is the initializer. It takes the instance created by `__new__` and configures its attributes.

We will cover:
1. **The Life Cycle of an Instance**
2. **Implementing `__new__`**
3. **The Singleton Design Pattern**

---

## 1. The Life Cycle of an Instance

When you run `obj = MyClass(1, 2)`, Python performs the following steps:
1.  Calls `instance = MyClass.__new__(MyClass, 1, 2)`.
2.  If the returned object is an instance of `MyClass`, Python then calls `MyClass.__init__(instance, 1, 2)`.
3.  Returns the initialized `instance`.

---

## 2. Implementing `__new__`

Since `__new__` creates the object, it must return a new object instance. We do this by calling the base class `object.__new__(cls)`.

```python
class Demo:
    def __new__(cls, *args, **kwargs):
        print("1. Creating instance via __new__")
        instance = super().__new__(cls)
        return instance

    def __init__(self, val):
        print(f"2. Initializing instance via __init__ with val: {val}")
        self.val = val

d = Demo(100)
# Output:
# 1. Creating instance via __new__
# 2. Initializing instance via __init__ with val: 100
```

---

## 3. The Singleton Design Pattern

A **Singleton** is a design pattern that limits a class to having exactly **one** object instance. Every subsequent instantiation of the class returns the *same* instance that was created the first time.

This is perfect for database connection pools, loggers, or configuration managers.

### Implementing Singleton with `__new__`
We store the unique instance in a class-level variable, `_instance`. If it is `None`, we create it; otherwise, we return the cached reference:

```python
class DatabasePool:
    _instance = None  # Class-level cache

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Allocating database connection pool instance...")
            cls._instance = super().__new__(cls)
        return cls._instance
```

Let's test this:
```python
pool1 = DatabasePool()
pool2 = DatabasePool()

print(pool1 is pool2)  # Output: True (They point to the exact same memory address!)
```

> [!WARNING]
> Keep in mind that even though `__new__` returns the same cached instance, Python **will still call `__init__`** on that instance every time you run `DatabasePool()`. If your `__init__` resets configuration, you'll need flags (like `_initialized = False`) to prevent re-initialization.

---
Let's head to [day18_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week4_metaprogramming/day18_assignment.py) to write a Singleton logger and an uppercase string subclass!
