class ECommerceSystem:
    def __init__(self):
        # Product inventory
        self.products = {
            "laptop": {"price": 60000, "stock": 5},
            "phone": {"price": 20000, "stock": 10},
            "headphones": {"price": 2000, "stock": 0}
        }

        # Available coupons
        self.coupons = {
            "SAVE10": 0.10,
            "SAVE20": 0.20
        }

        # Allowed payment methods
        self.payment_methods = ["card", "upi", "cod"]

        # Orders storage
        self.orders = {}
        self.order_id = 1

    # Validate coupon
    def apply_coupon(self, coupon, amount):
        if coupon in self.coupons:
            discount = amount * self.coupons[coupon]
            return amount - discount
        else:
            print("Invalid coupon code.")
            return amount

    # Place order
    def place_order(self, product, quantity, payment_method, coupon=None):

        # Check product
        if product not in self.products:
            print("Product does not exist.")
            return

        # Check stock
        if self.products[product]["stock"] < quantity:
            print("Error: Product out of stock.")
            return

        # Check payment method
        if payment_method not in self.payment_methods:
            print("Error: Invalid payment method.")
            return

        price = self.products[product]["price"] * quantity

        # Apply coupon
        if coupon:
            price = self.apply_coupon(coupon, price)

        # Reduce stock
        self.products[product]["stock"] -= quantity

        # Create order
        order = {
            "product": product,
            "quantity": quantity,
            "amount": price,
            "payment_method": payment_method,
            "status": "Confirmed"
        }

        self.orders[self.order_id] = order
        print(f"Order {self.order_id} placed successfully. Amount: ₹{price}")

        self.order_id += 1

    # Return order
    def return_order(self, order_id):
        if order_id not in self.orders:
            print("Order not found.")
            return

        order = self.orders[order_id]

        if order["status"] == "Returned":
            print("Order already returned.")
            return

        order["status"] = "Returned"
        print("Return request accepted.")

    # Refund
    def refund(self, order_id):
        if order_id not in self.orders:
            print("Order not found.")
            return

        order = self.orders[order_id]

        if order["status"] != "Returned":
            print("Refund not allowed. Return first.")
            return

        order["status"] = "Refunded"
        print(f"Refund of ₹{order['amount']} initiated.")


# Example usage
system = ECommerceSystem()

system.place_order("laptop", 1, "card", "SAVE10")
system.place_order("headphones", 1, "upi")
system.place_order("phone", 1, "bitcoin")

system.return_order(1)
system.refund(1)