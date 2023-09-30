import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(initial_state, goal_state):
    open_list = []
    closed_set = set()

    def heuristic_function(state):
        # Calculate the Manhattan distance heuristic
        heuristic = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != goal_state[i][j]:
                    for x in range(3):
                        for y in range(3):
                            if state[i][j] == goal_state[x][y]:
                                heuristic += abs(i - x) + abs(j - y)
        return heuristic

    # Create the initial node
    initial_node = Node(initial_state, None, 0, heuristic_function(initial_state))
    heapq.heappush(open_list, initial_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal_state:
            # Goal state reached, construct and return the path
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_set.add(tuple(map(tuple, current_node.state)))  # Convert list to tuple

        for neighbor_state, step_cost in get_neighbors(current_node.state):
            if tuple(map(tuple, neighbor_state)) in closed_set:  # Convert list to tuple
                continue

            new_cost = current_node.cost + step_cost
            heuristic = heuristic_function(neighbor_state)
            neighbor_node = Node(neighbor_state, current_node, new_cost, heuristic)

            if not any(node for node in open_list if node.state == neighbor_state and node.cost <= new_cost):
                heapq.heappush(open_list, neighbor_node)

    # If the open list is empty and the goal state is not reached, no path exists
    return None

def get_neighbors(state):
    neighbors = []
    zero_row, zero_col = find_zero_position(state)

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = zero_row + dr, zero_col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_state = [list(row) for row in state]
            new_state[zero_row][zero_col], new_state[new_row][new_col] = new_state[new_row][new_col], new_state[zero_row][zero_col]
            neighbors.append((new_state, 1))  # Step cost of 1 for each move

    return neighbors

def find_zero_position(state):
    for row in range(3):
        for col in range(3):
            if state[row][col] == 0:
                return row, col

# Example usage:
initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

path = astar(initial_state, goal_state)

if path:
    print("A* Path found:")
    for state in path:
        for row in state:
            print(row)
        print()
else:
    print("No path found.")
