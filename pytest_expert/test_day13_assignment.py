# Day 13 Assignment: Week 2 Integration Milestone
# -----------------------------------------------------------------
# Task 1a: Create a session-scoped fixture 'discount_provider' returning {"SAVE10": 0.1, "SAVE20": 0.2}.
# Task 1b: Create a function-scoped fixture 'cart' injecting 'discount_provider', 
#          connecting the cart, yielding it, and disconnecting in teardown.
# Task 2: Implement test methods in the class 'TestShoppingCart'.
# -----------------------------------------------------------------

import pytest
from .day13_shop import Item, ShoppingCart

# Task 1a: Define the session-scoped 'discount_provider' fixture
@pytest.fixture(scope="session")
def discount_provider():
    # Replace pass with your implementation returning the dict:
    pass


# Task 1b: Define the function-scoped 'cart' fixture
@pytest.fixture
def cart(discount_provider):
    # Replace pass with your implementation:
    pass


class TestShoppingCart:
    # Task 2a: Test that a disconnected cart raises a RuntimeError
    # Hint: Instantiate ShoppingCart manually (not using the fixture) and check get_total()
    def test_cart_session_required(self):
        # Replace pass with assertion:
        pass

    # Task 2b: Parameterized test verifying correct subtotal calculations.
    # Parametrize with:
    # 1. name="Apple", price=1.50, qty=2, expected_total=3.00
    # 2. name="Banana", price=0.80, qty=5, expected_total=4.00
    # 3. name="Milk", price=2.50, qty=1, expected_total=2.50
    # Remember to request the 'cart' fixture inside the parameters!
    def test_add_items_quantity(self, cart, name, price, qty, expected_total):
        # Replace pass with your assertions:
        pass

    # Task 2c: Parameterized test checking invalid inputs.
    # Parametrize with:
    # 1. qty=0, expected_exc=ValueError
    # 2. qty=-2, expected_exc=ValueError
    # 3. qty="two", expected_exc=TypeError
    # 4. qty=1.5, expected_exc=TypeError
    # Verify the expected exception is raised when calling cart.add_item()
    def test_invalid_add_quantities(self, cart, qty, expected_exc):
        # Replace pass with your assertions:
        pass

    # Task 2d: Test applying discounts
    # Add a product (e.g. Item("Laptop", 1000.0)), apply_discount("SAVE20"), 
    # and assert get_total() equals 800.0. Also verify invalid code "SAVE99" applies 0% discount.
    def test_apply_discount(self, cart):
        # Replace pass with your assertions:
        pass
