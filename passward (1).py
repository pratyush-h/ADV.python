def check_password_strength(password):
    strength = 0
    feedback = []
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters")
    if has_upper:
        strength += 1
    else:
        feedback.append("Add uppercase letters")
    if has_lower:
        strength += 1
    else:
        feedback.append("Add lowercase letters")
    if has_digit:
        strength += 1
    else:
        feedback.append("Add numbers")
    if has_special:
        strength += 1
    else:
        feedback.append("Add special characters")
    if strength == 5:
        return "Strong", strength
    elif strength >= 3:
        return "Medium", strength
    else:
        return "Weak", strength
password = input("Enter password: ")
message, score = check_password_strength(password)
print(f"{message} (Score: {score}/5)")