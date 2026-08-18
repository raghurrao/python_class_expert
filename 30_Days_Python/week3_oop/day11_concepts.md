# Day 11: Classes & Object Basics

Object-Oriented Programming (OOP) is a programming paradigm that organizes code around **Objects** rather than functions or actions. Today, we begin our exploration of OOP in Python by understanding how to build class blueprints and create object instances from them.

---

## 1. What is a Class and an Object?

*   **Class**: A blueprint, template, or schema that defines the characteristics and behaviors of a category of things. It doesn't contain actual data.
*   **Object (Instance)**: A concrete realization created from the class blueprint. It contains actual values and can execute behaviors.

For example, a `Car` blueprint (Class) defines that all cars have a make, model, and year. A specific blue Toyota Camry in your driveway (Object) is a concrete instance of that class.

---

## 2. Syntax: Defining a Class & the Constructor

By convention, Python class names use `PascalCase` (CapitalizedWords).

```python
class Smartphone:
    # The Constructor
    def __init__(self, brand, model, price):
        # Assign values to instance attributes
        self.brand = brand
        self.model = model
        self.price = price
```

### The Constructor: `__init__`
When you instantiate an object, Python automatically calls the special method `__init__` (short for *initialize*). Its primary purpose is to set up the initial state (attributes) of the new object.

### The Role of `self`
The `self` parameter represents the specific object instance that is currently being created or operated on. When you run `self.brand = brand`, you are telling Python to store the value of the `brand` argument inside the specific object currently being created.

---

## 3. Instance Methods

An **instance method** is a function defined inside a class that can access and modify attributes of the object instance. The first parameter of any instance method must be `self`.

```python
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_powered_on = False

    def power_toggle(self):
        self.is_powered_on = not self.is_powered_on
        status = "ON" if self.is_powered_on else "OFF"
        return f"Phone is now {status}"

# Instantiation (Creating Objects)
iphone = Smartphone("Apple", "iPhone 15", 999)
print(iphone.is_powered_on)  # Output: False
print(iphone.power_toggle())  # Output: Phone is now ON
print(iphone.is_powered_on)  # Output: True
```

---

Now, proceed to the Day 11 Assignment: [day11_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week3_oop/day11_assignment.py).
