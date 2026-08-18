# Week 2 Challenge Test Runner
# ----------------------------------------------------------------------
# Run this file in your terminal: python week2_challenge_test.py
# It will verify if your challenge code is correct!

import sys
import os
from abc import ABC

# Ensure the project root is in sys.path to support package-style imports
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

try:
    import pyclass_expert.week2_relationships.week2_challenge as challenge
except ImportError as e:
    print(f"[FAIL] Could not import week2_challenge.py. Error: {e}")
    sys.exit(1)

passed_tests = 0
total_tests = 0

def run_test(test_name, test_fn):
    global passed_tests, total_tests
    total_tests += 1
    try:
        test_fn()
        print(f"[PASS] {test_name}")
        passed_tests += 1
    except AssertionError as e:
        print(f"[FAIL] {test_name}")
        print(f"   AssertionError: {e}\n")
    except Exception as e:
        print(f"[FAIL] {test_name}")
        print(f"   Unexpected Error: {type(e).__name__}: {e}\n")

print("Starting Week 2 Challenge Tests...\n")

# 1. Weapon & Combatant ABC tests
def test_weapon_and_abc():
    assert hasattr(challenge, 'Weapon'), "Weapon class missing"
    assert hasattr(challenge, 'Combatant'), "Combatant class missing"
    assert issubclass(challenge.Combatant, ABC), "Combatant must be abstract (inherit ABC)"
    
    # Assert Combatant cannot be instantiated directly
    try:
        challenge.Combatant("Generic", 100)
        raise AssertionError("Combatant is abstract and should not be instantiated directly")
    except TypeError:
        pass

run_test("Combatant ABC contract rules", test_weapon_and_abc)

# 2. Warrior Tests
def test_warrior():
    assert hasattr(challenge, 'Warrior'), "Warrior class missing"
    assert issubclass(challenge.Warrior, challenge.Combatant), "Warrior must inherit Combatant"
    
    wep = challenge.Weapon("Excalibur", 10)
    w = challenge.Warrior("Arthur", 100, wep)
    assert w.name == "Arthur"
    assert w.health == 100
    assert w.weapon is wep
    assert w.is_alive is True
    
    # Create target dummy
    class Dummy(challenge.Combatant):
        def attack(self, target):
            pass
            
    dummy = Dummy("Training Dummy", 50)
    
    # Attack
    msg = w.attack(dummy)
    # Damage = 15 + 10 = 25
    assert dummy.health == 25
    assert msg == "Arthur swings Excalibur at Training Dummy for 25 damage!", f"Message format mismatch: '{msg}'"
    
    # Verify lethal damage floor
    w.attack(dummy)
    assert dummy.health == 0
    assert dummy.is_alive is False

run_test("Warrior combat mechanics and weapon composition", test_warrior)

# 3. Mage Tests
def test_mage():
    assert hasattr(challenge, 'Mage'), "Mage class missing"
    assert issubclass(challenge.Mage, challenge.Combatant), "Mage must inherit Combatant"
    
    m = challenge.Mage("Merlin", 80, 15)
    assert m.name == "Merlin"
    assert m.health == 80
    assert m.mana == 15
    
    class Dummy(challenge.Combatant):
        def attack(self, target):
            pass
            
    dummy = Dummy("Training Dummy", 100)
    
    # First attack (uses mana)
    msg1 = m.attack(dummy)
    assert m.mana == 5, f"Expected mana 5, got {m.mana}"
    assert dummy.health == 75, f"Expected dummy health 75, got {dummy.health}"
    assert msg1 == "Merlin casts Fireball at Training Dummy for 25 damage!"
    
    # Second attack (not enough mana, falls back to melee strike)
    msg2 = m.attack(dummy)
    assert m.mana == 5, "Mana should remain unchanged on weak strike"
    assert dummy.health == 70, f"Expected dummy health 70, got {dummy.health}"
    assert msg2 == "Merlin performs a weak staff strike at Training Dummy for 5 damage!"

run_test("Mage combat mana constraints and alternative attacks", test_mage)

print(f"\n----------------------------------------------------")
print(f"Summary: Passed {passed_tests} / {total_tests} tests.")
if passed_tests == total_tests:
    print(f"SUCCESS: Congratulations! You have successfully completed the Week 2 Challenge.")
    print(f"You have fully mastered Week 2 class relationships!")
else:
    print(f"FAILED: Some tests failed. Check the errors above and fix your code in week2_challenge.py")
