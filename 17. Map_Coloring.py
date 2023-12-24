def isSafe(graph, node, color, color_assignment):
    for neighbor in graph[node]:
        if color_assignment[neighbor] == color:
            return False
    return True

def graphColoring(graph, colors, node, color_assignment):
    if node == len(graph):
        return True

    for color in colors:
        if isSafe(graph, node, color, color_assignment):
            color_assignment[node] = color

            if graphColoring(graph, colors, node + 1, color_assignment):
                return True

            color_assignment[node] = None

    return False

graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

colors = ['Red', 'Green', 'Blue']
color_assignment = [None] * len(graph)

if graphColoring(graph, colors, 0, color_assignment):
    print("Graph can be colored")
    print("Color assignment:", color_assignment)
else:
    print("Graph cannot be colored")
