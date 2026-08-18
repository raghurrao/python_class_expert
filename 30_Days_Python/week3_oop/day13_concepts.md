# Day 13: Inheritance & Polymorphism

In Object-Oriented Programming, **Inheritance** allows a new class (Subclass/Derived class) to adopt the attributes and methods of an existing class (Superclass/Base class). This promotes code reuse and structures relationships between types. **Polymorphism** allows different classes to be treated as if they were of the same type when executing actions.

---

## 1. Single Inheritance & `super()`

To inherit from a class, place the parent class name in parentheses after the subclass name. Use the `super()` function to call the parent class's constructor or methods from inside the child class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        # Call the parent class's constructor
        super().__init__(name)
        self.breed = breed

    def speak(self):  # Overriding the parent method
        return "Woof!"

buddy = Dog("Buddy", "Golden Retriever")
print(buddy.name)   # Output: Buddy (Inherited attribute!)
print(buddy.speak())  # Output: Woof! (Overridden method!)
```

---

## 2. Inheritance Chains

You can build hierarchies of inheritance. A subclass can act as the parent for another subclass.

```python
class WorkingDog(Dog):
    def __init__(self, name, breed, job):
        super().__init__(name, breed)
        self.job = job
```

---

## 3. Polymorphism & Duck Typing

**Polymorphism** means "many shapes." It is the ability to use a common interface for multiple data types.

In Python, this is closely associated with **Duck Typing**: *"If it walks like a duck and quacks like a duck, it's a duck."*
Unlike strictly typed languages, Python does not require classes to inherit from a common parent to be processed by the same code. It only requires that they implement the expected methods.

```python
class Duck:
    def swim(self):
        return "Swimming duck"

class Fish:
    def swim(self):
        return "Swimming fish"

# This function exhibits polymorphism. It handles any object that implements a swim() method.
def make_it_swim(swimmer):
    print(swimmer.swim())

make_it_swim(Duck())  # Output: Swimming duck
make_it_swim(Fish())  # Output: Swimming fish
```

---

Now, proceed to the Day 13 Assignment: [day13_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week3_oop/day13_assignment.py).
