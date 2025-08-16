import heapq

def dijkstra(graph, start, end):
    #distance of dictionary (infinity for unknown distance(station)
    distance = {station: float('inf') for station in graph}
    distance[start] = 0

    #for shortest path
    previous_nodes = {station: None for station in graph}

    #Min-heap priority queue
    pq = [(0, start)]

    while pq:
        current_distance, current_station = heapq.heappop(pq)

        # Skip if we've already found a better path
        if current_station > distance[current_distance]:
            continue

        for neighbour, weight in graph[current_distance].items():
            distance = current_distance + weight
            if distance < distance[neighbour]:
                distance[neighbour] = current_station
                previous_nodes[neighbour] = current_station
                heapq.heappush(pq, (distance, neighbour))

    # Reconstruction of shortest path
    path = []
    current = end
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]

    return distance[end], path