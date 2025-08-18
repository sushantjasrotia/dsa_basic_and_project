import json
from main import dijkstra

with open("metro_graph.json","r") as file:
    metro_graph = json.load(file)

print("Welcome to Metro Station path finder 🚇")
print("Available Station:", ",".join(metro_graph.keys()))

start_station = input("Enter your starting :").strip().upper()
end_station = input("Enter your destination station :").strip().upper()

if start_station not in metro_graph or end_station not in metro_graph:
    print("Invalid station name! Please check the available station.")

else:
    distance, path = dijkstra(metro_graph, start_station, end_station)
    print("\n Shortest path found!!!!")
    print("Path:", "➡️".join(path))
    print("Total Distance:", distance, "km")