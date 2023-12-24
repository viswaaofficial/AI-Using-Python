import heapq

def dijkstra(graph, start, destination):
    # Initialize distances dictionary with infinity for all nodes except start node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Create a priority queue to store nodes with their distances
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the node with the minimum distance from the priority queue
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the current distance is greater than the stored distance
        if current_distance > distances[current_node]:
            continue

        # Stop the algorithm if the destination node is reached
        if current_node == destination:
            break

        # Explore neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update the distance if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances[destination]



graph = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'C': 1, 'D': 3},
    'C': {'A': 2, 'B': 1, 'D': 6},
    'D': {'B': 3, 'C': 6}
}

start_node = input("Enter start vertex: ").upper()
destination_node = input("Enter the destination vertex: ").upper()
shortest_distance = dijkstra(graph, start_node, destination_node)
print(f"Shortest distance from node {start_node} to node {destination_node}: {shortest_distance}")
