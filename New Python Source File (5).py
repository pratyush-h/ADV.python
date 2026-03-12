# Custom Exceptions
class InventoryError(Exception):
    """Base class for inventory-related exceptions."""
    pass


class OutOfStockError(InventoryError):
    """Raised when product stock is insufficient."""
    pass


class InvalidProductIDError(InventoryError):
    """Raised when product ID does not exist."""
    pass


class InvalidQuantityError(InventoryError):
    """Raised when quantity is invalid."""
    pass


# Inventory Management System
class InventorySystem:

    def __init__(self):
        self.products = {
            101: {"name": "Laptop", "stock": 5},
            102: {"name": "Phone", "stock": 10},
            103: {"name": "Headphones", "stock": 0}
        }

    def purchase_product(self, product_id, quantity):

        # Check product ID
        if product_id not in self.products:
            raise InvalidProductIDError("Product ID does not exist.")

        # Check quantity
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0.")

        product = self.products[product_id]

        # Check stock
        if product["stock"] < quantity:
            raise OutOfStockError(
                f"{product['name']} has only {product['stock']} items left."
            )

        # Reduce stock
        product["stock"] -= quantity

        print(f"Purchase successful: {quantity} {product['name']} bought.")


# Using the system
inventory = InventorySystem()

try:
    inventory.purchase_product(103, 1)

except InvalidProductIDError as e:
    print("Invalid Product:", e)

except InvalidQuantityError as e:
    print("Invalid Quantity:", e)

except OutOfStockError as e:
    print("Stock Error:", e)

except InventoryError as e:
    print("Inventory Error:", e)

except Exception as e:
    print("Unexpected Error:", e)