# Day 13: ShoppingCart Library to Test

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
        """Prepares cart session."""
        self.active_session = True

    def disconnect(self):
        """Cleans up cart session."""
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
