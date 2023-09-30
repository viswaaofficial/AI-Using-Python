# Python program to print DFS traversal from a given
# given graph
from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation
class Graph:

    def __init__(self,vertices):

        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def DLS(self,src,target,maxDepth, currentDepth, visitedNodes):

        if src == target :
            return True

        # If reached the maximum depth, stop recursing.
        if currentDepth >= maxDepth:
            return False

        # Mark the current node as visited
        visitedNodes.add(src)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            if i not in visitedNodes:
                print(f"At depth {currentDepth}, exploring node {i}")
                if self.DLS(i, target, maxDepth, currentDepth + 1, visitedNodes):
                    return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self,src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth + 1):
            visitedNodes = set()
            print(f"Iteration {i}:")
            if self.DLS(src, target, i, 0, visitedNodes):
                return True
            print(f"Target not found at depth {i}, increasing depth limit.")

        return False

# Create a graph given in the above diagram
# g = Graph (7)
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 3)
# g.addEdge(1, 4)
# g.addEdge(2, 5)
# g.addEdge(2, 6)

# target = 6
# maxDepth = 2
# src = 0

g = Graph(7)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 0)  # Creating a cycle
g.addEdge(2, 5)
g.addEdge(5, 6)

target = 6
maxDepth = 5  # The depth limit should be greater than the cycle length to reach the target
src = 0

if g.IDDFS(src, target, maxDepth):
    print ("Target is reachable from source " +
        "within max depth")
else:
    print ("Target is NOT reachable from source " +
        "within max depth")
