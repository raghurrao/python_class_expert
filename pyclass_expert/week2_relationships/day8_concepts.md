# Day 8: Polymorphism & Duck Typing

Welcome to Day 8! Today we study one of Python's most beautiful features: **Polymorphism** via **Duck Typing**.

Polymorphism means "many forms". It refers to the ability to write code that behaves differently based on the type of object it is working with, even if that code uses the exact same interface (method calls).

We will cover:
1. **Polymorphism in OOP**
2. **Duck Typing: The Pythonic Way**
3. **Writing Polymorphic Clients**

---

## 1. Polymorphism in OOP

In statically typed languages (like Java), if you want to write a function that accepts different shapes and draws them, they must all inherit from a common `Shape` parent class:

```python
# Traditional inheritance-based Polymorphism
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        return "Drawing Circle"

class Square(Shape):
    def draw(self):
        return "Drawing Square"

def render(shape: Shape):
    # 'shape' must inherit from Shape
    print(shape.draw())
```

---

## 2. Duck Typing

Python is dynamically typed and follows a philosophy known as **Duck Typing**:

> *"If it walks like a duck and quacks like a duck, we can treat it as a duck."*

In Python, we don't care what type an object *is* (its class tree). We only care what it can *do* (its methods). If two completely unrelated classes both implement a `draw()` method, Python will happily accept them in the same context without requiring any shared base class!

```python
# Unrelated classes with identical method names
class Airplane:
    def fly(self):
        return "Flying high in the clouds!"

class Bird:
    def fly(self):
        return "Flapping wings and gliding!"

class Frisbee:
    def fly(self):
        return "Spinning through the park air!"
```

Notice that `Frisbee`, `Bird`, and `Airplane` share absolutely no common base class.

---

## 3. Writing Polymorphic Clients

We can write a function or class that acts as a "client", taking any object that supports the `fly()` method:

```python
def launch(flyer):
    # This works for Airplane, Bird, Frisbee, or any other class with a fly() method!
    print(flyer.fly())

launch(Airplane())  # Output: Flying high in the clouds!
launch(Bird())      # Output: Flapping wings and gliding!
launch(Frisbee())  # Output: Spinning through the park air!
```

If we pass an object that does NOT have a `fly()` method, Python will raise an `AttributeError` at runtime.

---
Let's head to [day8_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week2_relationships/day8_assignment.py) to write a polymorphic message publisher using Duck Typing!
