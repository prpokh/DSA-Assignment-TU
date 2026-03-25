import heapq

def prims_mst(vertices, adj_list):
    # (weight, node, parent)
    min_heap = [(0, 0, -1)] 
    visited = [False] * vertices
    mst = []
    total_weight = 0

    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)

        # If node is already in MST, skip it
        if visited[u]:
            continue

        # Add node to MST
        visited[u] = True
        total_weight += weight
        if parent != -1:
            mst.append((parent, u, weight))

        # Check neighbors
        for v, edge_weight in adj_list[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (edge_weight, v, u))

    return mst, total_weight

# --- Example Usage ---
# Adjacency List: { node: [(neighbor, weight), ...] }
num_vertices = 5
adj = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

mst_result, weight_sum = prims_mst(num_vertices, adj)

print("Edges in the Prim's MST:")
for u, v, w in mst_result:
    print(f"{u} - {v} (Weight: {w})")
print(f"Total MST Weight: {weight_sum}")