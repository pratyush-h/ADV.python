cart = []
def add_item():
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))
    cart.append({"name": name, "price": price, "quantity": quantity})
    print(f"Added {quantity} x {name} to cart.")
def view_cart():
    if not cart:
        print("Your cart is empty!")
        return    
    print("\nYour Shopping Cart:")
    print("-" * 40)
    total = 0
    for item in cart:
        item_total = item["price"] * item["quantity"]
        total += item_total
        print(f"{item['name']}: ${item['price']:.2f} x {item['quantity']} = ${item_total:.2f}")
    print("-" * 40)
    print(f"Total: ${total:.2f}")
def remove_item():
    if not cart:
        print("Your cart is empty!")
        return    
    item_name = input("Enter item name to remove: ")
    for i, item in enumerate(cart):
        if item["name"].lower() == item_name.lower():
            removed_item = cart.pop(i)
            print(f"Removed {removed_item['name']} from cart.")
            return
    print("Item not found in cart!")
def checkout():
    if not cart:
        print("Your cart is empty!")
        return    
    view_cart()
    confirm = input("\nProceed to checkout? (yes/no): ").lower()
    if confirm == "yes":
        print("Thank you for your purchase! Your order has been placed.")
        cart.clear()  
    else:
        print("Checkout cancelled.")
def main():
    while True:
        print("\n=== Shopping Cart Menu ===")
        print("1. Add item to cart")
        print("2. View cart")
        print("3. Remove item from cart")
        print("4. Checkout")
        print("5. Exit")        
        choice = input("Enter your choice (1-5): ")        
        if choice == "1":
            add_item()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            remove_item()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("Thank you for shopping with us!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()