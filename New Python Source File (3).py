
mixed_tuple = (10, "Python", 3.14, True, 42, "AI", 7, False)
numeric_values = tuple(
    item for item in mixed_tuple 
    if isinstance(item, (int, float)) and not isinstance(item, bool)
)

print(f"Original Tuple: {mixed_tuple}")
print(f"Filtered Numeric Tuple: {numeric_values}")

try:
    print("\nAttempting to change the first element to 99...")
    mixed_tuple[0] = 99
except TypeError as error:
    print(f"Caught Error: {error}")
    print("Reason: Tuples are immutable; you cannot reassign their elements.")

tuple_one = (1, 2, 3)
tuple_two = ("A", "B", "C")
combined_tuple = tuple_one + tuple_two

print(f"\nTuple 1: {tuple_one}")
print(f"Tuple 2: {tuple_two}")
print(f"Concatenated Result: {combined_tuple}")