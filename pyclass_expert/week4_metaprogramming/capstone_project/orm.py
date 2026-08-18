# Capstone Project: Mini validation ORM framework
# ----------------------------------------------------------------------
# Instructions: Complete the implementation of the validation ORM.
# Run 'python test_orm.py' to verify your solution.

# In-memory database simulation
# Format: {"ModelClassName": [instance1, instance2, ...]}
SIMULATED_DB = {}

# ======================================================================
# 1. Descriptors (Fields)
# ======================================================================

class Field:
    """
    Base descriptor class for database fields.
    """
    def __set_name__(self, owner, name):
        self.private_name = "_" + name
        self.public_name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.private_name)

    def __set__(self, instance, value):
        # To be overridden by subclasses with custom validation
        instance.__dict__[self.private_name] = value


class IntegerField(Field):
    """
    Validates integer inputs and optional range constraints.
    Requirements:
    1. Constructor accepts optional 'min_value' (int) and 'max_value' (int).
    2. Overrides '__set__(self, instance, value)':
       - Validate that 'value' is an integer. If not, raise TypeError("Value must be an integer").
       - If 'min_value' is set and value < min_value, raise ValueError.
       - If 'max_value' is set and value > max_value, raise ValueError.
       - If validation passes, store value in instance.__dict__[self.private_name].
    """
    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    # TODO: Implement __set__ validation


class StringField(Field):
    """
    Validates string inputs and optional length constraints.
    Requirements:
    1. Constructor accepts optional 'min_length' (int) and 'max_length' (int).
    2. Overrides '__set__(self, instance, value)':
       - Validate that 'value' is a string. If not, raise TypeError("Value must be a string").
       - If 'min_length' is set and len(value) < min_length, raise ValueError.
       - If 'max_length' is set and len(value) > max_length, raise ValueError.
       - If validation passes, store value in instance.__dict__[self.private_name].
    """
    def __init__(self, min_length=None, max_length=None):
        self.min_length = min_length
        self.max_length = max_length

    # TODO: Implement __set__ validation


# ======================================================================
# 2. Metaclass (ModelMeta)
# ======================================================================

class ModelMeta(type):
    """
    Metaclass that scans class variables for Field descriptors and sets up DB tables.
    Requirements:
    1. Inherit from 'type'.
    2. Overrides '__new__(mcs, name, bases, attrs)':
       - If the class being created is named "Model" itself, do not perform scanning/DB registry.
       - Create an empty dictionary 'fields_dict' to store fields.
       - Search through 'attrs' and identify any items that are instances of 'Field'.
         Add these items to 'fields_dict' mapping variable name (str) to the field instance.
       - Store 'fields_dict' inside attrs['_fields'] so it can be accessed by instances.
       - Register a table inside the global SIMULATED_DB dictionary under the class name
         key mapping to an empty list (SIMULATED_DB[name] = []).
       - Call super().__new__ to allocate the class object and return it.
    """
    # TODO: Implement ModelMeta metaclass __new__ method


# ======================================================================
# 3. Base Class (Model)
# ======================================================================

class Model(metaclass=ModelMeta):
    """
    Base model class utilizing ModelMeta.
    Requirements:
    1. Constructor accepts arbitrary keyword arguments (**kwargs).
    2. Validate kwargs:
       - For each key in kwargs, verify it is in 'self._fields'.
         If not, raise ValueError(f"Unknown field: {key}").
       - Set the attribute on 'self' using standard setattr(self, key, value),
         which will trigger descriptor validation.
       - Set any fields that were NOT provided to None (e.g. if age wasn't passed, self.age = None).
    3. Implement 'save(self)':
       - Append the instance 'self' to the collection list in SIMULATED_DB[self.__class__.__name__].
    4. Implement classmethod 'all(cls)':
       - Return the list of all saved instances corresponding to the class name from SIMULATED_DB.
    """
    # TODO: Implement Model constructor, save, and all classmethods
    pass
