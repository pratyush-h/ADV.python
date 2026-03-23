contacts = {}

def add_contact(name, phone): 
    contacts[name] = phone

def search_contact(name): 
    return contacts.get(name, "Not found")

def delete_contact(name): 
    contacts.pop(name, None)

# --- ADD THIS TO SEE THE OUTPUT ---

# 1. Add some data
add_contact("Alice", "555-0101")
add_contact("Bob", "555-0202")
print("Contacts added successfully.")

# 2. Search for a contact
print(f"Searching for Alice: {search_contact('Alice')}")
print(f"Searching for Charlie: {search_contact('Charlie')}")

# 3. Delete a contact and check again
delete_contact("Bob")
print(f"Bob after deletion: {search_contact('Bob')}")

# 4. View the final dictionary
print(f"Current Contact List: {contacts}")