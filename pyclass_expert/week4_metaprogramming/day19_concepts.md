# Day 19: Metaclasses & __init_subclass__

Welcome to Day 19! Today we look at the ultimate form of Python metaprogramming: **Metaclasses**.

If classes are blueprints for creating objects, **metaclasses are blueprints for creating classes**. In Python, everything is an object, including classes. And every class is an instance of a metaclass (by default, the built-in metaclass `type`).

We will cover:
1. **Understanding `type`**
2. **Writing a Custom Metaclass**
3. **The Modern Alternative: `__init_subclass__`**

---

## 1. Classes are Objects (The `type` Metaclass)

When you define a class:
```python
class MyClass:
    pass
```
Python reads this and creates a class object behind the scenes using `type(...)`. You can dynamically create classes using `type` directly:

```python
# type(class_name, parent_classes, attributes_dict)
NewClass = type("NewClass", (object,), {"attribute": 42})

instance = NewClass()
print(instance.attribute)  # Output: 42
```

---

## 2. Writing a Custom Metaclass

A custom metaclass inherits from `type`. It overrides `__new__(cls, name, bases, attrs)` to modify class blueprints before they are loaded into the runtime.

### Example: Verifying method presence
Let's write a metaclass that forces all classes to have a `version` attribute, otherwise failing compile/import time:

```python
class VersionEnforcerMeta(type):
    def __new__(mcs, name, bases, attrs):
        # Prevent enforcement on the abstract base class itself
        if name != "VersionedBase":
            if "version" not in attrs:
                raise TypeError(f"Class '{name}' must define a 'version' class attribute")
        
        return super().__new__(mcs, name, bases, attrs)

class VersionedBase(metaclass=VersionEnforcerMeta):
    pass
```

If we inherit from `VersionedBase` but forget to define `version`:
```python
# class Plugin(VersionedBase):
#     pass
# ❌ Raises TypeError: Class 'Plugin' must define a 'version' class attribute
```

---

## 3. The Modern Alternative: `__init_subclass__`

Writing custom metaclasses is powerful but can be complex. In Python 3.6+, a new hook was introduced: `__init_subclass__`. This class method runs on a parent class whenever a subclass is created, allowing similar dynamic registrations and validations without needing metaclasses.

### Example: Automated Plugin Registry
```python
class PluginRegistry:
    plugins = {}

    def __init_subclass__(cls, name=None, **kwargs):
        super().__init_subclass__(**kwargs)
        # Automatically register any subclass when it gets defined!
        registry_name = name or cls.__name__
        PluginRegistry.plugins[registry_name] = cls

class AudioPlugin(PluginRegistry, name="audio"):
    pass

class VideoPlugin(PluginRegistry, name="video"):
    pass

print(PluginRegistry.plugins)
# Output: {'audio': <class 'AudioPlugin'>, 'video': <class 'VideoPlugin'>}
```

---
Let's head to [day19_assignment.py](file:///g:/Backup%20Fdrive/Python/pyclass_expert/week4_metaprogramming/day19_assignment.py) to write a dynamic attribute enforcer and auto-register subclasses!
