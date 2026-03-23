# 1. Input: Taking two integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# 2. Arithmetic Operations
sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2

# Handling division by zero
if num2 != 0:
    div_result = num1 / num2
else:
    div_result = "Undefined (cannot divide by zero)"

# 3. Even/Odd Check
def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# 4. Type Conversion
num1_float = float(num1)

# Displaying Results
print("-" * 30)
print(f"Results for {num1} and {num2}:")
print(f"Sum:        {sum_result}")
print(f"Difference: {diff_result}")
print(f"Product:    {prod_result}")
print(f"Division:   {div_result}")
print("-" * 30)
print(f"{num1} is {check_even_odd(num1)}")
print(f"{num2} is {check_even_odd(num2)}")
print(f"Converted {num1} to float: {num1_float} (Type: {type(num1_float).__name__})")