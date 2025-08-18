import heapq

def dijkstra(graph, start, end):
    # Distance dictionary (infinity for unknown distance)
    distance = {station: float('inf') for station in graph}
    distance[start] = 0

    # For shortest path reconstruction
    previous_nodes = {station: None for station in graph}

    # Min-heap priority queue
    pq = [(0, start)]

    while pq:
        current_distance, current_station = heapq.heappop(pq)

        # Skip if we've already found a better path
        if current_distance > distance[current_station]:
            continue

        for neighbour, weight in graph[current_station].items():
            new_distance = current_distance + weight
            if new_distance < distance[neighbour]:
                distance[neighbour] = new_distance
                previous_nodes[neighbour] = current_station
                heapq.heappush(pq, (new_distance, neighbour))

    # Reconstruction of shortest path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    return distance[end], path
