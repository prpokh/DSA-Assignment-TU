class ChainedHashTable:
    def __init__(self, size):
        self.size = size
        # Create an array where each element is an empty list (the "chain")
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        
        # Check if the key already exists in the chain to update it
        for i, kv_pair in enumerate(self.table[index]):
            if kv_pair[0] == key:
                self.table[index][i] = (key, value)
                return
        
        # Otherwise, append the new key-value pair to the list
        self.table[index].append((key, value))

    def search(self, key):
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Bucket {i}: {chain}")

# --- Testing ---
ht = ChainedHashTable(5)
ht.insert("Apple", 100)
ht.insert("Banana", 200)
ht.insert("Cherry", 300) # Might collide depending on hash
ht.insert("Date", 400)

ht.display()
print(f"\nSearching for 'Banana': {ht.search('Banana')}")