# Day 15: Abstract Base Classes (ABCs)

An **Abstract Class** is a class that cannot be instantiated directly. Instead, it defines a template (an interface) that other classes must follow. Today, we learn how to use Python's `abc` module to enforce rules on subclasses at development/import time.

---

## 1. Why Use Abstract Base Classes?

Imagine you are building a system that sends notifications (Email, SMS, Push notifications). Every notification system should have a `send()` method. 
Without ABCs, a developer might write a class `SmsNotification` and name the method `send_sms()`, while another writes `EmailNotification` with method `send_mail()`. This makes writing code that handles notifications polymorphically impossible.

By defining an abstract base class `Notification` with an abstract method `send()`, Python *guarantees* that any concrete class inheriting from it *must* implement `send()`, or else Python will refuse to instantiate the class.

---

## 2. Defining an ABC: The `abc` Module

To create an abstract class, inherit from the `ABC` class in the `abc` module. Mark abstract methods using the `@abstractmethod` decorator.

```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        """Send the notification message."""
        pass

# Attempting to instantiate an ABC raises an error:
# n = Notification()  # TypeError: Can't instantiate abstract class Notification with abstract method send
```

---

## 3. Implementing Concrete Subclasses

A **Concrete Class** is a subclass that implements all abstract methods of its parent.

```python
class EmailNotification(Notification):
    def __init__(self, email_address):
        self.email_address = email_address

    # Implementing the abstract method
    def send(self, message):
        return f"Email sent to {self.email_address}: {message}"

# Valid instantiation!
email = EmailNotification("user@example.com")
print(email.send("Hello!"))  # Output: Email sent to user@example.com: Hello!
```

If you inherit from `Notification` but forget to define `send()`, trying to create an instance will result in a `TypeError`:
```python
class SmsNotification(Notification):
    pass

# sms = SmsNotification()  # TypeError!
```

---

Now, proceed to the Day 15 Assignment: [day15_assignment.py](file:///g:/30%20days%20Leaarning/30_Days_Python/week3_oop/day15_assignment.py).
