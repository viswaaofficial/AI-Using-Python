import heapq

# Define the initial state and goal state
initial_state = (0, 0)  # (0 liters in 7-liter jug, 0 liters in 3-liter jug)
goal_volume = 5  # Goal is to measure 5 liters of water

# Define a function to generate possible actions
def get_actions(state):
    jug_7, jug_3 = state
    actions = []

    # Fill the 7-liter jug
    actions.append(("Fill 7L Jug", (7, jug_3)))

    # Fill the 3-liter jug
    actions.append(("Fill 3L Jug", (jug_7, 3)))

    # Pour water from 7L jug to 3L jug
    pour = min(jug_7, 3 - jug_3)
    actions.append(("Pour 7L to 3L", (jug_7 - pour, jug_3 + pour)))

    # Pour water from 3L jug to 7L jug
    pour = min(jug_3, 7 - jug_7)
    actions.append(("Pour 3L to 7L", (jug_7 + pour, jug_3 - pour)))

    # Empty the 7L jug
    actions.append(("Empty 7L Jug", (0, jug_3)))

    # Empty the 3L jug
    actions.append(("Empty 3L Jug", (jug_7, 0)))

    return actions

# Define a heuristic function (underestimating the cost)
def heuristic(state):
    jug_7, jug_3 = state
    # We underestimate the cost by considering the larger jug only
    return abs(jug_7 - goal_volume)

# Define the A* search algorithm
def astar_search():
    frontier = [(0, initial_state)]  # Priority queue (cost, state)
    explored = set()  # Set to store explored states

    while frontier:
        cost, current_state = heapq.heappop(frontier)

        if current_state[0] == goal_volume or current_state[1] == goal_volume:
            return cost, current_state

        if current_state in explored:
            continue

        explored.add(current_state)

        for action, next_state in get_actions(current_state):
            if next_state not in explored:
                heapq.heappush(frontier, (cost + 1 + heuristic(next_state), next_state))

    return None

# Perform A* search
result = astar_search()

# Display the result
if result:
    cost, final_state = result
    print("Goal reached in {} steps.".format(cost))
    print("Final state: ({}L, {}L)".format(final_state[0], final_state[1]))
else:
    print("No solution found.")
