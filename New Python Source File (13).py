def power(base, exp):
    res = 1
    for _ in range(abs(exp)):
        res *= base
    return res if exp >= 0 else 1/res

# --- ADD THIS TO SEE THE OUTPUT ---

# 1. Positive exponent: 2^3 = 8
print(f"2 to the power of 3: {power(2, 3)}")

# 2. Negative exponent: 2^-2 = 0.25
print(f"2 to the power of -2: {power(2, -2)}")

# 3. Base cases: 5^0 = 1
print(f"5 to the power of 0: {power(5, 0)}")