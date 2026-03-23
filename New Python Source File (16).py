class Book:
    def __init__(self, title):
        self.title = title
        print(f"Book '{self.title}' initialized.")
    
    def __del__(self):
        print(f"Book '{self.title}' removed from memory.")

# --- ADD THIS TO SEE THE OUTPUT ---

# 1. This triggers __init__
my_book = Book("The Great Gatsby")

# 2. This manually triggers __del__ (Optional)
# If you don't delete it manually, Python will do it automatically when the script ends.
del my_book 

print("Program execution finished.")