# Define the initial state and goal state
initial_state = {'farmer': 'left', 'wolf': 'left', 'goat': 'left', 'cabbage': 'left'}
goal_state = {'farmer': 'right', 'wolf': 'right', 'goat': 'right', 'cabbage': 'right'}

# Define the maximum depth for depth-limited search
max_depth = 7  # Adjust this value as needed


# Define a function to check if a state is valid
def is_valid(state):
    # Check if the wolf and goat are left alone without the farmer
    if state['wolf'] == state['goat'] and state['goat'] != state['farmer']:
        return False
    # Check if the goat and cabbage are left alone without the farmer
    if state['goat'] == state['cabbage'] and state['cabbage'] != state['farmer']:
        return False
    return True


# Define a recursive function for depth-limited search
# ...

def depth_limited_search(state, goal, depth, current_depth=0):
    if state == goal:
        return [state], current_depth
    if depth == 0:
        return None, current_depth

    shortest_path = None

    for item in state.keys():
        if state[item] == state['farmer']:
            new_state = state.copy()
            new_state['farmer'] = 'left' if state['farmer'] == 'right' else 'right'
            new_state[item] = new_state['farmer']

            if is_valid(new_state):
                result_path, result_depth = depth_limited_search(new_state, goal, depth - 1, current_depth + 1)
                if result_path is not None:
                    if shortest_path is None or result_depth < current_depth:
                        shortest_path = [state] + result_path
                        current_depth = result_depth

    return shortest_path, current_depth

# Perform depth-limited search
solution_path, depth_found = depth_limited_search(initial_state, goal_state, max_depth)

# Display the solution path and depth
if solution_path:
    print("Solution Path:")
    for step, state in enumerate(solution_path):
        print(f"Step {step}: {state}")
    print(f"Depth Found: {depth_found}")
else:
    print("No solution found within the specified depth limit.")
