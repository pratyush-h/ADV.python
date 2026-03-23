class Vehicle:
    total_rented = 0
    def calculate_fee(self, days): 
        return days * 10

class Car(Vehicle):
    def calculate_fee(self, days):
        Vehicle.total_rented += 1
        return days * 50

class Bike(Vehicle):
    def calculate_fee(self, days):
        Vehicle.total_rented += 1
        return days * 20

# --- ADD THIS TO SEE THE OUTPUT ---

# 1. Create instances (objects)
my_car = Car()
my_bike = Bike()

# 2. Call the methods and store the results
car_fee = my_car.calculate_fee(3)  # 3 days * 50
bike_fee = my_bike.calculate_bike_fee = my_bike.calculate_fee(2) # 2 days * 20

# 3. Print the results to the console
print(f"Car Rental Fee: ${car_fee}")
print(f"Bike Rental Fee: ${bike_fee}")
print(f"Total vehicles rented: {Vehicle.total_rented}")