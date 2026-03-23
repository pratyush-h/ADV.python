menu = {"Pizza": 200, "Burger": 100, "Coke": 50}
order_total = 0
while True:
    item = input("Enter item (or 'done'): ")
    if item == 'done': break
    order_total += menu.get(item, 0)

total_with_tax = order_total * 1.1
print(f"Total Bill (incl. 10% tax): {total_with_tax}")