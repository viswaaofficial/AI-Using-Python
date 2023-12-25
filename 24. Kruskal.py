import heapq

class Kruskal:
    def __init__(self):
        self.vertices = set()
        self.edges = []

    def add_edge(self, v1, v2, weight):
        self.edges.append((weight, v1, v2))
        self.vertices.add(v1)
        self.vertices.add(v2)

    def find(self, parent, vertex):
        if parent[vertex] != vertex:
            parent[vertex] = self.find(parent, parent[vertex])
        return parent[vertex]

    def union(self, parent, rank, v1, v2):
        root1 = self.find(parent, v1)
        root2 = self.find(parent, v2)
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root2] > rank[root1]:
            parent[root1] = root2
        else:
            parent[root1] = root2
            rank[root2] += 1

    def kruskal(self):
        parent = {vertex: vertex for vertex in self.vertices}
        rank = {vertex: 0 for vertex in self.vertices}
        heapq.heapify(self.edges)

        mst = []
        while self.edges:
            weight, v1, v2 = heapq.heappop(self.edges)
            if self.find(parent, v1) != self.find(parent, v2):
                mst.append((v1, v2, weight))
                self.union(parent, rank, v1, v2)
        return mst

# Driver code
graph = Kruskal()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'D', 3)
graph.add_edge('B', 'C', 1)
graph.add_edge('B', 'D', 3)
graph.add_edge('C', 'D', 1)
graph.add_edge('C', 'E', 5)
graph.add_edge('D', 'E', 6)

mst = graph.kruskal()
print("Minimum Spanning Tree:", mst)
