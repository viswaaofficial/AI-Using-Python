import heapq
class Graph:
    def __init__(self):
        self.ed = {}
        self.adjlis = {}
    def add_vertex(self,v):
        self.adjlis[v] = []
    def add_edge(self,v1,v2,w):
        self.ed[(v1,v2)] = w
        self.ed[(v2,v1)] = w
        self.adjlis[v1].append(v2)
        self.adjlis[v2].append(v1)
    def prims(self,sv):
        hp = [(0,sv,None)]
        visited = set()
        mst = []
        while(hp):
            w,v,p = heapq.heappop(hp)
            if v not in visited:
                visited.add(v)
                if p is not None:
                    mst.append((w,v,p))
                for nei in self.adjlis[v]:
                    if nei not in visited:
                        heapq.heappush(hp,(self.ed[(v,nei)],nei,v))
        return mst
graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')

graph.add_edge('A', 'B', 7)
graph.add_edge('A', 'C', 8)
graph.add_edge('C', 'D', 4)
graph.add_edge('C', 'B', 3)
graph.add_edge('C', 'E', 3)
graph.add_edge('B', 'D', 6)
graph.add_edge('D', 'E', 2)
graph.add_edge('D', 'F', 5)
graph.add_edge('E', 'F', 2)

minimum_spanning_tree = graph.prims('A')
for ed in minimum_spanning_tree:
    print(ed)