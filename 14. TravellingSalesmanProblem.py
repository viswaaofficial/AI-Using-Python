def traveling_salesman(graph, start_vertex):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    tour = []
    total_cost = 0

    current_vertex = start_vertex
    tour.append(current_vertex)
    visited[current_vertex] = True

    for _ in range(num_vertices - 1):
        min_cost = float('inf')  # Initialize to positive infinity
        next_vertex = -1

        for neighbor in range(num_vertices):
            if not visited[neighbor] and graph[current_vertex][neighbor] < min_cost:
                min_cost = graph[current_vertex][neighbor]
                next_vertex = neighbor

        tour.append(next_vertex)
        visited[next_vertex] = True
        total_cost += min_cost
        current_vertex = next_vertex

    # Return to the starting vertex to complete the tour
    tour.append(start_vertex)
    total_cost += graph[current_vertex][start_vertex]

    return tour, total_cost

# Example graph adjacency matrix
graph = [
    [0, 2, 1, 4, 5],
    [2, 0, 3, 2, 7],
    [1, 3, 0, 8, 2],
    [4, 2, 8, 0, 6],
    [5, 7, 2, 6, 0]
]

start_vertex = 0
tour, total_cost = traveling_salesman(graph, start_vertex)

print(f"Optimal Tour: {tour}")
print(f"Total Cost: {total_cost}")
