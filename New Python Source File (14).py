s = input("Enter string: ")
counts = {"vowels": 0, "consonants": 0, "digits": 0, "special": 0}
for char in s:
    if char.isdigit(): counts["digits"] += 1
    elif char.isalpha():
        if char.lower() in "aeiou": counts["vowels"] += 1
        else: counts["consonants"] += 1
    elif not char.isspace(): counts["special"] += 1
print(counts)