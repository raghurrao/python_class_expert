# Day 6 Assignment: Single & Multi-level Inheritance
# ----------------------------------------------------------------------
# Instructions: Complete the class hierarchy. Do not change class or method names.
# Run 'python day6_test.py' to verify your solutions.

# ======================================================================
# Vehicle base class
# ======================================================================
class Vehicle:
    """
    Requirements:
    1. Constructor should take 'brand' (str) and 'speed' (int).
    2. Implement 'describe(self)' that returns string: "Brand: <brand>, Speed: <speed> km/h".
    """
    def __init__(self, brand, speed):
        # TODO: Initialize brand and speed
        pass

    def describe(self):
        # TODO: Return description string
        pass


# ======================================================================
# Car class (inherits Vehicle)
# ======================================================================
class Car(Vehicle):
    """
    Requirements:
    1. Constructor should take 'brand' (str), 'speed' (int), and 'fuel_type' (str).
    2. Call parent constructor using super().
    3. Implement 'describe(self)' that overrides parent method and returns:
       "Brand: <brand>, Speed: <speed> km/h, Fuel Type: <fuel_type>"
       Note: Use super().describe() to construct the start of the string!
    """
    def __init__(self, brand, speed, fuel_type):
        # TODO: Initialize attributes using super()
        pass

    def describe(self):
        # TODO: Use super().describe() to construct description
        pass


# ======================================================================
# ElectricCar class (inherits Car)
# ======================================================================
class ElectricCar(Car):
    """
    Requirements:
    1. Constructor should take 'brand' (str), 'speed' (int), and 'battery_capacity' (int).
    2. Call parent constructor using super(), passing fuel_type="Electric".
    3. Store battery_capacity in instance attribute.
    4. Implement 'describe(self)' that overrides parent method and returns:
       "Brand: <brand>, Speed: <speed> km/h, Fuel Type: Electric, Battery: <battery_capacity> kWh"
       Note: Use super().describe() to construct the start of the string!
    """
    def __init__(self, brand, speed, battery_capacity):
        # TODO: Initialize attributes using super()
        pass

    def describe(self):
        # TODO: Use super().describe() to construct description
        pass
