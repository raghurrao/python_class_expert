# Day 13: Week 2 Integration Assignment

Today is your second weekly milestone! We will consolidate everything you have learned this week (yield fixtures, scopes, sharing conftest configurations, dynamic request objects, and test parametrization) into a single, comprehensive shopping cart test suite.

---

## The Challenge: Testing `ShoppingCart`
You are provided with a package containing `day13_shop.py`. It contains:
1. **`Item`**: A class representing a product with a `name` and a `price`.
2. **`ShoppingCart`**: A class that aggregates items, calculates the subtotal, applies discount rates, and supports connection sessions.

Your job is to write a complete test suite inside `test_day13_assignment.py` following these specifications:

### 1. Fixture Design
* Write a session-scoped fixture `discount_provider` that returns a dummy class or dictionary containing valid discount codes: `"SAVE10"` (10% off) and `"SAVE20"` (20% off).
* Write a function-scoped fixture `cart` that yields a fresh `ShoppingCart` instance connected to a session. The fixture must clean up/clear the cart contents and disconnect after the test exits.

### 2. Test Parametrization
* Write a parameterized test `test_add_items_quantity` to verify adding different combinations of items and quantities:
  * e.g., (Item("Apple", 1.50), quantity=2, expected_total=3.0)
  * e.g., (Item("Banana", 0.80), quantity=5, expected_total=4.0)
* Write a parameterized exception test `test_invalid_add_quantities` that verifies passing invalid quantities (like `0`, `-3`, or `1.5` float) raises `ValueError` or `TypeError` with matching error messages.

### 3. Verification Commands
Verify your progress using:
```powershell
.venv\Scripts\python pytest_expert/verify_day13.py
```
This runs mutation testing against your tests. Your tests must catch all bugs introduced in mutated checkout calculation scripts to pass!
