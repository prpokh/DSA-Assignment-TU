from collections import deque

class Graph:
    def __init__(self):
        # Using a dictionary to store the adjacency list
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        # For undirected graphs, uncomment the next line:
        # if v not in self.graph: self.graph[v] = []
        # self.graph[v].append(u)

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])
        visited.add(start_node)
        
        result = []
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start_node, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start_node)
        traversal = [start_node]
        
        for neighbor in self.graph.get(start_node, []):
            if neighbor not in visited:
                traversal.extend(self.dfs(neighbor, visited))
        return traversal

# --- Example Usage ---
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

start = 2
print(f"BFS starting from node {start}: {g.bfs(start)}")
print(f"DFS starting from node {start}: {g.dfs(start)}")