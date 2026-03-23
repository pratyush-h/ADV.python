words = ["level", "python", "radar", "world"]

# 1. Sort by length
sorted_words = sorted(words, key=len)

# 2. Identify palindromes
palindromes = [w for w in words if w == w[::-1]]

# 3. Replace spaces with hyphens
sample_strings = ["hello world", "python pro"]
hyphenated = [s.replace(" ", "-") for s in sample_strings]

# --- ADD THIS TO SEE THE OUTPUT ---
print(f"Words sorted by length: {sorted_words}")
print(f"Palindromes found:      {palindromes}")
print(f"Hyphenated strings:    {hyphenated}")