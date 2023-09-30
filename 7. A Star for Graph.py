import heapq

class GraphNode:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight


def astar(graph, start, goal):
    open_list = []
    came_from = {}  # Store the parent of each node
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    # Heuristic function (straight-line distance)
    def heuristic(node):
        # You can customize the heuristic based on your problem domain
        return 0  # In this example, we assume no heuristic information

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
                f_score = tentative_g_score + heuristic(neighbor)
                heapq.heappush(open_list, (f_score, neighbor))

    # If the open list is empty and the goal state is not reached, no path exists
    return None


# Example usage (same as before):
# Create a sample graph
node_a = GraphNode('A')
node_b = GraphNode('B')
node_c = GraphNode('C')
node_d = GraphNode('D')
node_e = GraphNode('E')

node_a.add_neighbor(node_c, 100)
node_a.add_neighbor(node_b, 20)
node_b.add_neighbor(node_c, 1)
node_c.add_neighbor(node_e, 4)
node_d.add_neighbor(node_e, 10)

graph = {node_a: node_a, node_b: node_b, node_c: node_c, node_d: node_d, node_e: node_e}

start_node = node_a
goal_node = node_e

path = astar(graph, start_node, goal_node)

if path:
    print("A* Path found:")
    for node in path:
        print(node.name)
else:
    print("No path found.")
