from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache: return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache: 
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # last=False pops the FIRST item (the Least Recently Used one)
            self.cache.popitem(last=False)

# --- TEST THE CACHE ---

# 1. Create a cache that only holds 2 items
my_cache = LRUCache(2)

# 2. Add some data
my_cache.put(1, "Data A")
my_cache.put(2, "Data B")

# 3. Access item 1 (this makes it "Recently Used")
print(f"Getting key 1: {my_cache.get(1)}") 

# 4. Add a 3rd item (this will trigger the eviction of key 2)
my_cache.put(3, "Data C")

# 5. Check what's left
print(f"Key 1 (should exist): {my_cache.get(1)}")
print(f"Key 2 (should be -1/evicted): {my_cache.get(2)}")
print(f"Key 3 (should exist): {my_cache.get(3)}")