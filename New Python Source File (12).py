text = input("Enter sentence: ").lower()
chars = [c for c in text if c.isalnum()]
unique = [c for c in chars if chars.count(c) == 1]
print(f"Unique characters: {unique}")