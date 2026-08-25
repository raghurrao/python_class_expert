import os
import sys
import ast
import subprocess
import shutil

TARGET_FILE = "test_day13_assignment.py"
SHOP_FILE = "day13_shop.py"
SHOP_BACKUP = "day13_shop.py.backup"

CLEAN_CODE = """# Day 13: ShoppingCart Library to Test

class Item:
    def __init__(self, name, price):
        if not isinstance(name, str):
            raise TypeError("Item name must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("Item price must be a number")
        if price < 0:
            raise ValueError("Item price cannot be negative")
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self, discount_provider=None):
        self.items = []  # List of tuples: (item, quantity)
        self.discount_provider = discount_provider
        self.active_session = False
        self.discount_rate = 0.0

    def connect(self):
        self.active_session = True

    def disconnect(self):
        self.active_session = False
        self.items = []
        self.discount_rate = 0.0

    def add_item(self, item, quantity=1):
        if not self.active_session:
            raise RuntimeError("Cart session is not active")
        if not isinstance(item, Item):
            raise TypeError("Must add an Item instance")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        
        # If item already exists, increase quantity
        for i, (existing_item, q) in enumerate(self.items):
            if existing_item.name == item.name:
                self.items[i] = (existing_item, q + quantity)
                return True
        
        self.items.append((item, quantity))
        return True

    def apply_discount(self, code):
        if not self.active_session:
            raise RuntimeError("Cart session is not active")
        if self.discount_provider and code:
            self.discount_rate = self.discount_provider.get(code, 0.0)
        return self.discount_rate

    def get_total(self):
        if not self.active_session:
            raise RuntimeError("Cart session is not active")
        subtotal = sum(item.price * qty for item, qty in self.items)
        return subtotal * (1.0 - self.discount_rate)
"""

MUTANTS = {
    "mutant_total_no_discount": {
        "desc": "ShoppingCart.get_total() ignores discount rate",
        "code": CLEAN_CODE.replace("return subtotal * (1.0 - self.discount_rate)", "return subtotal")
    },
    "mutant_add_negative_qty": {
        "desc": "ShoppingCart.add_item() allows quantity <= 0 (does not raise ValueError)",
        "code": CLEAN_CODE.replace('raise ValueError("Quantity must be greater than zero")', "pass")
    },
    "mutant_add_dup_overwrite": {
        "desc": "ShoppingCart.add_item() overwrites quantity for duplicate items instead of accumulating",
        "code": CLEAN_CODE.replace("self.items[i] = (existing_item, q + quantity)", "self.items[i] = (existing_item, quantity)")
    },
    "mutant_total_math_err": {
        "desc": "ShoppingCart.get_total() applies discount as absolute subtraction rather than percentage",
        "code": CLEAN_CODE.replace("return subtotal * (1.0 - self.discount_rate)", "return subtotal - self.discount_rate")
    }
}

REQUIRED_TESTS = {
    "test_cart_session_required",
    "test_add_items_quantity",
    "test_invalid_add_quantities",
    "test_apply_discount"
}

def check_ast():
    if not os.path.exists(TARGET_FILE):
        print(f"[ERROR] {TARGET_FILE} not found.")
        return False

    with open(TARGET_FILE, "r") as f:
        tree = ast.parse(f.read())

    discount_provider_session = False
    cart_yield_ok = False
    cart_injected = False
    class_found = False
    found_methods = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if node.name == "discount_provider":
                # Check scope="session"
                for dec in node.decorator_list:
                    if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Attribute) and dec.func.attr == "fixture":
                        for kw in dec.keywords:
                            if kw.arg == "scope" and isinstance(kw.value, ast.Constant) and kw.value.value == "session":
                                discount_provider_session = True
            elif node.name == "cart":
                # Check yield
                for child in ast.walk(node):
                    if isinstance(child, ast.Yield):
                        cart_yield_ok = True
                # Check args contains discount_provider
                args = [arg.arg for arg in node.args.args]
                if "discount_provider" in args:
                    cart_injected = True

        elif isinstance(node, ast.ClassDef) and node.name == "TestShoppingCart":
            class_found = True
            for child in node.body:
                if isinstance(child, ast.FunctionDef) and child.name.startswith("test_"):
                    found_methods.add(child.name)

    if not discount_provider_session:
        print("   [FAIL] discount_provider fixture must be scope='session'")
        return False
    if not cart_yield_ok:
        print("   [FAIL] cart fixture must use yield for setup/teardown")
        return False
    if not cart_injected:
        print("   [FAIL] cart fixture must accept 'discount_provider' as an argument")
        return False
    if not class_found:
        print("   [FAIL] TestShoppingCart class was not found.")
        return False

    missing = REQUIRED_TESTS - found_methods
    if missing:
        print(f"   [FAIL] TestShoppingCart class is missing required test methods: {missing}")
        return False

    print("   [PASS] AST structure, scopes, and classes verify OK.")
    return True

def run_tests():
    cmd = [sys.executable, "-m", "pytest", TARGET_FILE, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout

def write_shop_file(content):
    with open(SHOP_FILE, "w") as f:
        f.write(content)

def main():
    print("====================================================")
    print("[RUNNING] Running Verification Suite for Day 13...")
    print("====================================================")

    if not check_ast():
        sys.exit(1)

    if os.path.exists(SHOP_FILE):
        shutil.copyfile(SHOP_FILE, SHOP_BACKUP)

    try:
        print("\nTesting against correct code...")
        write_shop_file(CLEAN_CODE)
        code, out = run_tests()
        if code != 0:
            print("[FAIL] Tests failed on correct code! Output:")
            print(out)
            sys.exit(1)
        print("[PASS] All tests passed successfully on correct code.")

        print("\nTesting against broken code (Mutation Testing)...")
        failed_mutants = []
        for name, mutant in MUTANTS.items():
            print(f"Applying mutant: {mutant['desc']}...")
            write_shop_file(mutant["code"])
            code, out = run_tests()

            if code == 0:
                print(f"   [FAIL] Your tests did NOT catch this bug! They passed when they should have failed.")
                failed_mutants.append(name)
            else:
                print(f"   [PASS] Your tests successfully caught this bug (tests failed as expected).")

        print("\n----------------------------------------------------")
        if failed_mutants:
            print("[ERROR] Verification Failed!")
            print("Your test suite is missing coverage for some buggy scenarios.")
            print("Ensure you verify subtotal multiplications, quantity constraints, and discount calculations.")
            sys.exit(1)
        else:
            print("[SUCCESS] You have completed the Week 2 Integration Milestone!")
            sys.exit(0)

    finally:
        if os.path.exists(SHOP_BACKUP):
            shutil.copyfile(SHOP_BACKUP, SHOP_FILE)
            os.remove(SHOP_BACKUP)
        else:
            write_shop_file(CLEAN_CODE)

if __name__ == "__main__":
    main()
