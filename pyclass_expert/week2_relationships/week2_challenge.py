# Week 2 Challenge: Combat RPG Engine
# ----------------------------------------------------------------------
# Instructions: Integrate inheritance, ABCs, polymorphism, and composition
# to build a turn-based RPG battle engine.
# Run 'python week2_challenge_test.py' to verify your solutions.

from abc import ABC, abstractmethod

# ======================================================================
# Exercise 1: Weapon (Composition helper)
# ======================================================================
class Weapon:
    """
    Requirements:
    1. Constructor accepts 'name' (str) and 'bonus_damage' (int).
    2. Store these in 'self.name' and 'self.bonus_damage'.
    """
    def __init__(self, name, bonus_damage):
        # TODO: Initialize name and bonus_damage
        pass


# ======================================================================
# Exercise 2: Combatant Abstract Base Class
# ======================================================================
class Combatant(ABC):
    """
    Requirements:
    1. Must inherit from abc.ABC.
    2. Constructor accepts 'name' (str) and 'health' (int).
    3. Store them in 'self.name' and 'self.health'.
    4. Implement property 'is_alive(self)' returning True if self.health > 0 else False.
    5. Define abstract method 'attack(self, target: "Combatant")' (no implementation).
    6. Implement 'take_damage(self, amount: int)':
       - Subtract amount from self.health.
       - Ensure self.health does not drop below 0.
    """
    def __init__(self, name, health):
        # TODO: Initialize attributes
        pass

    @property
    def is_alive(self):
        # TODO: Return boolean status
        pass

    @abstractmethod
    def attack(self, target):
        # TODO: Abstract method definition
        pass

    def take_damage(self, amount):
        # TODO: Subtract health, floor at 0
        pass


# ======================================================================
# Exercise 3: Warrior Class (Inherits Combatant, Composes Weapon)
# ======================================================================
class Warrior(Combatant):
    """
    Requirements:
    1. Constructor accepts 'name' (str), 'health' (int), and 'weapon' (an instance of Weapon).
    2. Call parent constructor using super().
    3. Store 'weapon' in 'self.weapon'.
    4. Implement 'attack(self, target: Combatant)':
       - Calculate damage: 15 + self.weapon.bonus_damage.
       - Apply damage to the target by calling target.take_damage(damage).
       - Return a string message: "<Warrior name> swings <Weapon name> at <Target name> for <damage> damage!"
    """
    # TODO: Implement Warrior class


# ======================================================================
# Exercise 4: Mage Class (Inherits Combatant)
# ======================================================================
class Mage(Combatant):
    """
    Requirements:
    1. Constructor accepts 'name' (str), 'health' (int), and 'mana' (int).
    2. Call parent constructor using super().
    3. Store 'mana' in 'self.mana'.
    4. Implement 'attack(self, target: Combatant)':
       - Check if self.mana >= 10:
         - Deduct 10 mana.
         - Calculate damage: 25.
         - Call target.take_damage(damage).
         - Return message: "<Mage name> casts Fireball at <Target name> for 25 damage!"
       - If self.mana < 10 (out of mana):
         - Calculate damage: 5 (weak melee attack).
         - Call target.take_damage(damage).
         - Return message: "<Mage name> performs a weak staff strike at <Target name> for 5 damage!"
    """
    # TODO: Implement Mage class
