# Day 1: Class, Object, and the Constructor

Welcome to Day 1 of your journey to becoming a Python Class expert! Today, we will establish the structural bedrock of Object-Oriented Programming (OOP) in Python. 

We will cover:
1. **What is a Class and an Object?**
2. **The Constructor: `__init__`**
3. **The Role of `self`**

---

## 1. What is a Class and an Object?

Think of a **Class** as a blueprint, template, or schema. It defines the structure and behavior of something, but it doesn't contain the actual data itself.
An **Object** (also called an **Instance**) is the actual physical realization built from that blueprint.

For example, a `Car` blueprint (Class) defines that all cars have a model, color, and engine status. A specific red Tesla Model S (Object) is a concrete instance of that blueprint.

### Basic Syntax
To define a class in Python, use the `class` keyword. By convention, class names use `PascalCase` (CapitalizedWords).

```python
class Smartphone:
    pass # 'pass' is just a placeholder indicating an empty body
```

To create an object (instantiate) from the class:
```python
my_phone = Smartphone()
print(type(my_phone))  # Output: <class '__main__.Smartphone'>
```

---

## 2. The Constructor: `__init__`

When you instantiate an object, Python automatically calls a special method named `__init__` (short for *initialize*). This is known as the **constructor**. Its purpose is to set up the initial state (attributes) of the object.

```python
class Smartphone:
    def __init__(self, brand, model, price):
        # Assign values to instance attributes
        self.brand = brand
        self.model = model
        self.price = price
```

Now, when creating a smartphone, we pass these values like arguments to a function:
```python
iphone = Smartphone("Apple", "iPhone 15", 999)
pixel = Smartphone("Google", "Pixel 8", 799)

print(iphone.brand)  # Output: Apple
print(pixel.model)   # Output: Pixel 8
```

---

## 3. The Role of `self`

You will notice `self` is the first parameter of `__init__` (and almost every instance method). 
* **What is `self`?** It represents the specific object instance that is currently being created or operated on.
* **Why do we need it?** When you run `iphone.brand`, Python needs to know *which* smartphone's brand you want. Under the hood, Python translates `Smartphone("Apple", "iPhone 15", 999)` into `Smartphone.__init__(iphone, "Apple", "iPhone 15", 999)`. The object itself is passed as the first parameter.

> [!NOTE]
> `self` is not a keyword in Python; it is just a naming convention. You *could* call it `this` or `me`, but doing so is considered extremely bad practice because it violates PEP 8 and will confuse any other Python developer. Always use `self`.

---

## Summary of Syntax

```python
class Dog:
    # Constructor
    def __init__(self, name, breed):
        self.name = name    # Instance attribute
        self.breed = breed  # Instance attribute

# Instantiation
buddy = Dog("Buddy", "Golden Retriever")
```

---
Now, proceed to [day1_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week1_foundations/day1_assignment.py) to write some code and test your understanding!
