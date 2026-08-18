# Day 17: The Descriptor Protocol

Welcome to Day 17! Today we study a very advanced Python topic: **Descriptors**.

Descriptors are the engine behind many of Python's built-in features, including `@property`, `@classmethod`, `@staticmethod`, and even normal method lookups!

A Descriptor is simply a class that implements one or more of the descriptor protocol methods: `__get__`, `__set__`, or `__delete__`. Instances of this class can then be used as attributes in *other* classes to manage how those attributes are read and written.

We will cover:
1. **The Descriptor Methods**
2. **Dynamic Naming with `__set_name__`**
3. **Writing a validation descriptor**

---

## 1. The Descriptor Methods

A class becomes a descriptor by defining:
*   `__get__(self, instance, owner)`: Triggers when the attribute is read.
    *   `instance`: The object calling the attribute (e.g., `user` in `user.age`).
    *   `owner`: The class of the object (e.g., `User` class).
*   `__set__(self, instance, value)`: Triggers when the attribute is written (`user.age = 25`).
*   `__delete__(self, instance)`: Triggers when the attribute is deleted (`del user.age`).

---

## 2. Dynamic Naming with `__set_name__`

In modern Python (3.6+), we use a helper method named `__set_name__(self, owner, name)` to capture the variable name the descriptor is assigned to.

```python
class FieldDescriptor:
    def __set_name__(self, owner, name):
        # 'name' is the name of the class attribute (e.g. 'age')
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        instance.__dict__[self.private_name] = value
```

> [!IMPORTANT]
> **Why do we store data in `instance.__dict__`?**
> A descriptor is declared at the **class level**, meaning there is only *one* descriptor object shared across all instances of the class. If we stored data in `self.value` inside the descriptor, every object instance would share and overwrite the same value! We must store the state inside `instance.__dict__` so each object maintains its own independent value.

---

## 3. Writing a Validation Descriptor

Descriptors are perfect for creating reusable validation logic. Instead of writing `@property` getters and setters in ten different classes to validate positive integers, we write a single descriptor class:

```python
class PositiveNumber:
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError(f"{self.private_name[1:]} must be a positive number")
        instance.__dict__[self.private_name] = value

class Product:
    # Reusable descriptors!
    price = PositiveNumber()
    weight = PositiveNumber()

    def __init__(self, price, weight):
        self.price = price      # Triggers price descriptor __set__
        self.weight = weight    # Triggers weight descriptor __set__
```

Now we have clean, declarative validation without code duplication!

---
Let's head to [day17_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week4_metaprogramming/day17_assignment.py) to build a reusable String validator descriptor!
