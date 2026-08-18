# Capstone Project: Mini validation ORM framework

Congratulations on reaching the final Capstone Project! 

In this project, you will build a lightweight **Object-Relational Mapper (ORM)** and data validation library, similar to Django ORM or Pydantic. It allows users to define data schemas as Python classes using validation descriptors, and automatically maps class objects to simulated database collections using a custom metaclass.

## Target Architecture

You will define a database model using the following syntax:

```python
class User(Model):
    # Descriptors for validation
    username = StringField(min_length=3, max_length=20)
    age = IntegerField(min_value=18)

# Creating an instance triggers validation
u = User(username="alice", age=25)
u.save()  # Saves to in-memory database

# Retrieve all users
all_users = User.all()
```

## Components to Implement

You will write your code in [orm.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week4_metaprogramming/capstone_project/orm.py).

1.  **`Field` (Base Descriptor)**:
    - Implements the descriptor protocol (`__get__`, `__set__`, `__set_name__`) to manage instance attributes.
2.  **`IntegerField` & `StringField` (Validation Descriptors)**:
    - Inherit from `Field`.
    - `IntegerField` validates that input is an integer and respects optional boundaries (`min_value`, `max_value`).
    - `StringField` validates that input is a string and respects length boundaries (`min_length`, `max_length`).
3.  **`ModelMeta` (Metaclass)**:
    - Intercepts class creation.
    - Inspects all class attributes to locate any `Field` descriptors. It gathers these fields and stores them in a class-level dictionary (`_fields`) for constructor validation.
    - Sets up a simulated database table/collection for the class.
4.  **`Model` (Base Class)**:
    - Uses `ModelMeta` as its metaclass.
    - Implements a constructor `__init__(self, **kwargs)` that accepts values for its defined fields. If an unknown field keyword is passed, it raises a `ValueError`.
    - Implements `save(self)` to add the current instance to the in-memory database table.
    - Implements `@classmethod` `all(cls)` to return all saved records for the class.

Let's head over to [orm.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week4_metaprogramming/capstone_project/orm.py) and code this masterclass framework!
