class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs_recursive(self, node, visited):
        if node not in visited:
            print(node)  # Process the current node (e.g., print it)
            visited.add(node)  # Mark the node as visited
            for neighbor in self.graph.get(node, []):
                self.dfs_recursive(neighbor, visited)

    def dfs_iterative(self, start):
        visited = set()  # To keep track of visited nodes
        stack = []  # Initialize a stack for iterative DFS
        stack.append(start)  # Start from the initial node

        while stack:
            node = stack.pop()  # Pop a node from the stack
            if node not in visited:
                print(node)  # Process the current node (e.g., print it)
                visited.add(node)  # Mark the node as visited

                # Push unvisited neighbors onto the stack
                for neighbor in reversed(self.graph.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)

# Example usage:
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('E', 'F')

print("DFS Traversal (Recursive):")
visited_nodes = set()
graph.dfs_recursive('A', visited_nodes)

print("\nDFS Traversal (Iterative):")
graph.dfs_iterative('A')
