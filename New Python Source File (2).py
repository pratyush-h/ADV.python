# Task 2: Sentence Processing
text = input("Enter a sentence: ")

# 1. Count Vowels and Consonants
vowels = "aeiou"
v_count = 0
c_count = 0

# Clean the text to check only alphabetic characters
for char in text.lower():
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

# 2. Reverse the sentence
# Using slicing [start:stop:step] with a step of -1
reversed_text = text[::-1]

# 3. Replace spaces with underscores
underscored_text = text.replace(" ", "_")

# 4. Capitalize words (Title Case)
capitalized_text = text.title()

# --- Display Results ---
print(f"\nOriginal: {text}")
print(f"Vowels: {v_count} | Consonants: {c_count}")
print(f"Reversed: {reversed_text}")
print(f"Underscored: {underscored_text}")
print(f"Capitalized: {capitalized_text}")