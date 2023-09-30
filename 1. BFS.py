from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()  # To keep track of visited nodes
        queue = deque()  # Initialize a queue for BFS
        queue.append(start)  # Start from the initial node

        while queue:
            node = queue.popleft()  # Dequeue a node from the queue
            if node not in visited:
                print(node)  # Process the current node (e.g., print it)
                visited.add(node)  # Mark the node as visited

                # Add unvisited neighbors to the queue
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)

# Example usage:
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'F')
graph.add_edge('B', 'E')
graph.add_edge('C', 'D')
graph.add_edge('E', 'D')

print("BFS Traversal:")
graph.bfs('A')
