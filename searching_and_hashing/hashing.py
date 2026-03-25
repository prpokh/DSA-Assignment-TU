class SimpleHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        """Generates an index for a given string key."""
        # Sum the ASCII values of the characters and take the modulo
        return sum(ord(char) for char in str(key)) % self.size

    def insert(self, key, value):
        """Inserts a key-value pair into the table."""
        index = self._hash_function(key)
        self.table[index] = value
        print(f"Inserted '{value}' at index {index}")

    def get(self, key):
        """Retrieves a value based on the key."""
        index = self._hash_function(key)
        return self.table[index]

# --- Testing the Implementation ---
my_hash = SimpleHashTable(10)

my_hash.insert("name", "Alice")
my_hash.insert("id", 4021)

print(f"Value for 'name': {my_hash.get('name')}")