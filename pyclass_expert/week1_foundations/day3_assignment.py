# Day 3 Assignment: Instance, Class, and Static Methods
# ----------------------------------------------------------------------
# Instructions: Complete the tasks below. Do not change the class or method names.
# Run 'python day3_test.py' to verify your solutions.

# ======================================================================
# Exercise 1: Alternative Constructors with Classmethods
# ======================================================================
# Task: Complete the 'User' class.
# 1. Implement the constructor __init__(self, username, email) to store them 
#    in instance attributes of the same name.
# 2. Implement a class method named 'from_string' that takes a string argument 'csv_str'
#    formatted as "username,email" (e.g. "alice,alice@gmail.com").
#    It must parse this string and return a new instance of the 'User' class.

from importlib import _bootstrap_external
class User:
    def __init__(self, username, email):
        # TODO: Initialize instance attributes
        self.username = username
        self.email = email

    @classmethod
    def from_string(cls, csv_str):
        # TODO: Parse string and return a new instance using 'cls'
        data = csv_str.split(",")
        return cls(data[0],data[1])


# ======================================================================
# Exercise 2: Static Utilities with Staticmethods
# ======================================================================
# Task: Complete the 'MathHelper' class.
# 1. The constructor should accept no arguments and initialize an instance attribute
#    named 'history' to an empty list.
# 2. Implement a static method named 'is_prime' that accepts an integer 'n'.
#    It must return True if the number is prime, and False otherwise. (Note: Primes are > 1).
# 3. Implement an instance method named 'check_and_log' that accepts an integer 'n'.
#    It must check if 'n' is prime (calling the static method 'is_prime'),
#    append a string record like "n is prime" or "n is composite" to the 'history' list,
#    and return the boolean result.

class MathHelper:
    def __init__(self):
        # TODO: Initialize 'history' list
        self.history = []

    @staticmethod
    def is_prime(n):
        # TODO: Return True if n is prime, else False
        if n < 2:
            return False
        else:
            prm = True

            for i in range(2,n):
                if n%i == 0:
                    prm = False
                    break
            
            return prm

    def check_and_log(self, n):
        # TODO: Use is_prime to evaluate, log result to self.history, and return boolean
        if self.is_prime(n):
            self.history.append(f"{n} is prime")
            return True
        else:
            self.history.append(f"{n} is composite")
            return False



# ======================================================================
# Exercise 3: Instance state and Class methods
# ======================================================================
# Task: Complete the 'Booking' class.
# 1. Add a class attribute 'tax_rate' initialized to 0.12 (12%).
# 2. Constructor should accept 'base_price' (float) and 'nights' (integer).
# 3. Implement an instance method 'get_total_cost' that returns the calculated cost:
#    Cost = base_price * nights * (1 + tax_rate). Access 'tax_rate' using 'self.tax_rate' 
# 'self.tax_rate' Look for tax_rate on this object (self) first. If it doesn't exist on the object, Python looks in the class..
# 4. Implement a class method 'set_tax_rate' that accepts 'new_rate' and updates the
#    class attribute 'tax_rate' globally.

class Booking:
    # TODO: Implement tax_rate, constructor, get_total_cost, and set_tax_rate
    tax_rate = 0.12

    def __init__(self,base_price,nights):
        self.base_price = float(base_price)
        self.nights = int(nights)

    def get_total_cost(self):
       Cost = self.base_price * self.nights * (1 + self.__class__.tax_rate)
       return Cost

    @classmethod
    def set_tax_rate(cls,new_rate):
        cls.tax_rate = new_rate

