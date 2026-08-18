# Day 7 Assignment: Multiple Inheritance & MRO
# ----------------------------------------------------------------------
# Instructions: Complete the cooperative inheritance exercises below.
# Run 'python day7_test.py' to verify your solutions.

# ======================================================================
# Exercise 1: Cooperative Multi-inheritance Classes
# ======================================================================
# Task: Create a system where a single object gets initialized with multiple
# independent functionalities (Logging and Storing) using cooperative super().

class Loggable:
    """
    Requirements:
    1. Constructor should take 'log_format' keyword argument (default "[LOG]: {}").
    2. Store in 'self.log_format'.
    3. Call super().__init__(**kwargs) to forward any leftover arguments.
    4. Implement 'log(self, msg)' returning self.log_format.format(msg).
    """
    def __init__(self, log_format="[LOG]: {}", **kwargs):
        # TODO: Initialize and pass kwargs along MRO
        pass

    def log(self, msg):
        # TODO: Return formatted log string
        pass


class Storable:
    """
    Requirements:
    1. Constructor should take 'storage_dir' keyword argument (default "/tmp").
    2. Store in 'self.storage_dir'.
    3. Call super().__init__(**kwargs) to forward any leftover arguments.
    4. Implement 'save(self, data)' returning "Saving data to <storage_dir>".
    """
    def __init__(self, storage_dir="/tmp", **kwargs):
        # TODO: Initialize and pass kwargs along MRO
        pass

    def save(self, data):
        # TODO: Return saving status string
        pass


class SmartDoc(Loggable, Storable):
    """
    Requirements:
    1. Constructor should take 'filename' (positional) and arbitrary **kwargs.
    2. Call super().__init__(**kwargs) to cooperatively initialize Loggable and Storable.
    3. Store 'filename' in self.filename.
    """
    def __init__(self, filename, **kwargs):
        # TODO: Call super() with keyword arguments and store filename
        pass


# ======================================================================
# Exercise 2: Diamond MRO Override Chaining
# ======================================================================
# Task: Set up the Diamond Hierarchy and check method calls.
#
#       Top
#      /   \
#    Left  Right
#      \   /
#      Bottom
#
# Requirements:
# 1. Top class defines 'message(self)' returning "Top".
# 2. Left class inherits Top, overrides 'message(self)' returning "Left -> " + super().message().
# 3. Right class inherits Top, overrides 'message(self)' returning "Right -> " + super().message().
# 4. Bottom class inherits Left and Right, overrides 'message(self)' returning "Bottom -> " + super().message().

class Top:
    def message(self):
        # TODO: Return "Top"
        pass

class Left(Top):
    def message(self):
        # TODO: Return Left-mangled string
        pass

class Right(Top):
    def message(self):
        # TODO: Return Right-mangled string
        pass

class Bottom(Left, Right):
    def message(self):
        # TODO: Return Bottom-mangled string
        pass
