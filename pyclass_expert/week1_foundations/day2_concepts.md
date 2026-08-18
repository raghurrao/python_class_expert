# Day 2: Attribute Scoping (Instance vs. Class Attributes)

Today we are going under the hood to see how Python manages variables inside classes and objects. Understanding namespaces is one of the key indicators of a Python expert.

We will cover:
1. **Instance Attributes vs. Class Attributes**
2. **The Namespace Lookup Process (`__dict__`)**
3. **The Pitfall of Attribute Reassignment**

---

## 1. Instance vs. Class Attributes

Python classes can contain two types of attributes (variables):

### Instance Attributes
Instance attributes are specific to each object. They are defined inside methods (usually the constructor) using `self`. Changes to one object's instance attribute do not affect any other objects.

```python
class Dog:
    def __init__(self, name):
        self.name = name  # Instance attribute (unique to each dog)
```

### Class Attributes
Class attributes are shared across all instances of a class. They are defined directly inside the class body, outside of any methods.

```python
class Dog:
    species = "Canine"  # Class attribute (shared by all dogs)
    
    def __init__(self, name):
        self.name = name
```

If we create two dogs:
```python
buddy = Dog("Buddy")
bella = Dog("Bella")

print(buddy.species)  # Output: Canine
print(bella.species)  # Output: Canine
```

---

## 2. Namespace Lookup & `__dict__`

Under the hood, Python uses dictionaries to store object namespaces. You can inspect these namespaces using the `__dict__` attribute.

```python
print(buddy.__dict__) 
# Output: {'name': 'Buddy'}  (Note that 'species' is NOT in the instance dictionary!)

print(Dog.__dict__)
# Output contains: 'species': 'Canine'
```

### The Lookup Order
When you access `buddy.species`, Python does this:
1. Looks for `"species"` in the instance dictionary `buddy.__dict__`. (Not found)
2. Looks for `"species"` in the class dictionary `Dog.__dict__`. (Found! Returns `"Canine"`)
3. If not found in the class, it looks up the inheritance tree (which we cover in Week 2).

---

## 3. The Reassignment Pitfall

A very common source of bugs in Python is mutating or reassigning class attributes through an instance.

### What happens if we reassign via an instance?
```python
buddy.species = "Feline"  # ⚠️ This does NOT change the class attribute!
```
Instead, Python creates a new **instance attribute** named `species` in `buddy.__dict__`.

```python
print(buddy.__dict__)  # Output: {'name': 'Buddy', 'species': 'Feline'}
print(bella.species)   # Output: Canine (Bella is unaffected!)
print(Dog.species)     # Output: Canine (The class attribute remains unchanged!)
```

### How to correctly modify a Class Attribute?
If you want to modify a class attribute for *all* instances, you must access it directly through the class:
```python
Dog.species = "Lupine"
print(bella.species)  # Output: Lupine
```

---

## Practical Example: Instance Counter
Class attributes are excellent for configuration constants or tracking global metadata, like the number of instances created:

```python
class User:
    user_count = 0  # Class attribute to track total users
    
    def __init__(self, username):
        self.username = username
        # Increment the class attribute when a new user is created
        User.user_count += 1

alice = User("alice")
bob = User("bob")
print(User.user_count)  # Output: 2
```

---
Now, let's head to [day2_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week1_foundations/day2_assignment.py) to practice namespace lookup rules!
