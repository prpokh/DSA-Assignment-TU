class OpenAddressingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        # Secondary hash for Double Hashing (must not return 0)
        return 7 - (key % 7)

    def insert_linear(self, key):
        index = self.hash1(key)
        i = 0
        while self.table[(index + i) % self.size] is not None:
            i += 1
        self.table[(index + i) % self.size] = key

    def insert_quadratic(self, key):
        index = self.hash1(key)
        i = 0
        while self.table[(index + i**2) % self.size] is not None:
            i += 1
        self.table[(index + i**2) % self.size] = key

    def insert_double_hash(self, key):
        index = self.hash1(key)
        step = self.hash2(key)
        i = 0
        while self.table[(index + i * step) % self.size] is not None:
            i += 1
        self.table[(index + i * step) % self.size] = key

# --- Comparison Test ---
keys = [12, 22, 32] # All these will collide if size is 10
size = 10

# 1. Linear Probing
lp = OpenAddressingHashTable(size)
for k in keys: lp.insert_linear(k)
print(f"Linear Probing:    {lp.table}")

# 2. Quadratic Probing
qp = OpenAddressingHashTable(size)
for k in keys: qp.insert_quadratic(k)
print(f"Quadratic Probing: {qp.table}")

# 3. Double Hashing
dh = OpenAddressingHashTable(size)
for k in keys: dh.insert_double_hash(k)
print(f"Double Hashing:    {dh.table}")