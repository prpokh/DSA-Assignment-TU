class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            # Union by rank
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

def kruskal_mst(vertices, edges):
    # Sort edges based on weight: (u, v, weight)
    edges.sort(key=lambda x: x[2])
    
    ds = DisjointSet(vertices)
    mst = []
    mst_weight = 0
    
    for u, v, weight in edges:
        # If u and v are in different sets, adding this edge won't form a cycle
        if ds.union(u, v):
            mst.append((u, v, weight))
            mst_weight += weight
            
    return mst, mst_weight

# --- Example Usage ---
# Graph represented as (u, v, weight)
num_vertices = 4
graph_edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

mst_result, total_weight = kruskal_mst(num_vertices, graph_edges)

print("Edges in the Constructed MST:")
for u, v, weight in mst_result:
    print(f"{u} -- {v} == {weight}")
print(f"Minimum Spanning Tree Weight: {total_weight}")