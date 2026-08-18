# Day 6: Single & Multi-level Inheritance

Welcome to Week 2! This week we cover class relationships and code reusability. 

**Inheritance** allows a new class (subclass or child class) to inherit attributes and methods from an existing class (base class or parent class). This prevents code duplication.

We will cover:
1. **Single Inheritance & Method Overriding**
2. **Chaining Methods with `super()`**
3. **Multi-level Inheritance**

---

## 1. Single Inheritance & Method Overriding

In single inheritance, a child class inherits from one parent class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Generic animal sound"

# Dog inherits from Animal
class Dog(Animal):
    # Method Overriding: Replacing the parent method with a child-specific one
    def speak(self):
        return "Woof!"
```

When we call `Dog("Buddy").speak()`, Python uses the overridden method:
```python
d = Dog("Buddy")
print(d.name)   # Output: Buddy (Inherited attribute)
print(d.speak())  # Output: Woof! (Overridden method)
```

---

## 2. Constructor Chaining with `super()`

If a child class has its own constructor (`__init__`), it overrides the parent constructor. To make sure the parent constructor still sets up its attributes, we use the `super()` function to call the parent constructor.

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class __init__ to initialize 'name'
        super().__init__(name)
        self.breed = breed  # Child-specific attribute
```

`super()` can also be used to extend the behavior of regular methods, rather than replacing them completely:

```python
class Animal:
    def description(self):
        return f"This is an animal named {self.name}."

class Dog(Animal):
    def description(self):
        # Retrieve parent description and append child information
        parent_desc = super().description()
        return f"{parent_desc} It is a dog of breed {self.breed}."
```

---

## 3. Multi-level Inheritance

Multi-level inheritance is when a class inherits from a child class, creating a chain of inheritance: `BaseClass -> SubClass -> SubSubClass`.

```python
class Vehicle:
    def start(self):
        return "Vehicle started"

class Car(Vehicle):
    def honk(self):
        return "Beep beep!"

class ElectricCar(Car):
    def charge(self):
        return "Charging battery..."
```

An instance of `ElectricCar` has access to all methods up the chain:
```python
tesla = ElectricCar()
print(tesla.start())   # Inherited from Vehicle
print(tesla.honk())    # Inherited from Car
print(tesla.charge())  # Defined in ElectricCar
```

---
Let's head to [day6_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week2_relationships/day6_assignment.py) to code a multi-level inheritance hierarchy!
