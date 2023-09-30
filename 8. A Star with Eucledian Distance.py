import heapq
import math

class GraphNode:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

def astar(graph, start, goal, heuristic):
    open_list = []
    came_from = {}  # Store the parent of each node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # Create the initial node
    initial_node = (0, start)
    heapq.heappush(open_list, initial_node)

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            # Goal reached, construct and return the path
            path = []
            while current_node != start:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1]

        for neighbor, weight in graph[current_node].neighbors.items():
            tentative_g_score = g_score[current_node] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + euclidean_distance(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))

    # If the open list is empty and the goal state is not reached, no path exists
    return None

# Heuristic function (Euclidean distance)
def euclidean_distance(node, goal):
    x1, y1 = node.position
    x2, y2 = goal.position
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

#Driver Code
node_a = GraphNode('A', (0, 0))
node_b = GraphNode('B', (1, 1))
node_c = GraphNode('C', (2, 2))
node_d = GraphNode('D', (3, 3))
node_e = GraphNode('E', (4, 4))

node_a.add_neighbor(node_c, 1)
node_a.add_neighbor(node_b, 2)
node_b.add_neighbor(node_c, 2)
node_c.add_neighbor(node_e, 3)
node_d.add_neighbor(node_e, 4)

graph = {node_a: node_a, node_b: node_b, node_c: node_c, node_d: node_d, node_e: node_e}

start_node = node_a
goal_node = node_e

path = astar(graph, start_node, goal_node, euclidean_distance)

if path:
    print("A* Path found:")
    for node in path:
        print(node.name)
else:
    print("No path found.")
