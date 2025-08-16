import networkx as nx
# A Python library for creating and analyzing graphs (nodes + edges).
import matplotlib.pyplot as plt
# actually draw and display the graph.
import scipy as sp

# Define the adjacency list (graph data with weights)
graph_data = {
    "AA": {"AB": 4, "AC": 2},
    "AB": {"AA": 4, "AC": 1, "AD": 5},
    "AC": {"AA": 2, "AB": 1, "AD": 8, "AE": 10},
    "AD": {"AB": 5, "AC": 8, "AF": 2},
    "AE": {"AC": 10, "AF": 3, "AG": 6},
    "AF": {"AD": 2, "AE": 3, "AH": 4},
    "AG": {"AE": 6, "AH": 1, "AI": 7},
    "AH": {"AF": 4, "AG": 1, "AJ": 3},
    "AI": {"AG": 7, "AJ": 2},
    "AJ": {"AH": 3, "AI": 2}
}

# Create a new undirected graph
# Undirected = edge AA → AB is the same as AB → AA.
G = nx.Graph()

# Add edges with weights
for node, neighbors in graph_data.items():
    for neighbor, weight in neighbors.items():
        G.add_edge(node, neighbor, weight=weight)
        # G.add_edge() automatically adds the nodes if they don’t exist yet.
        # weight=weight attaches the numeric distance as an edge attribute.

# Layout: Kamada-Kawai (respects edge weights)
pos = nx.kamada_kawai_layout(G, weight="weight")
# kamada_kawai_layout computes 2D positions for nodes.

# It tries to place nodes so that:
#
# Short edges (small weights) appear closer together.
#
# Long edges (large weights) appear further apart.

# Draw the graph
plt.figure(figsize=(10, 8))
nx.draw(
    G, pos,
    with_labels=True,
    node_color="lightblue",
    node_size=500,
    font_size=10,
    font_weight="bold"
)

# Draw edge labels (weights)
edge_labels = nx.get_edge_attributes(G, "weight") # gets a dictionary of weights.
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

# Title and save
plt.title("Weighted Graph Visualization (Distances Shown Correctly)")
plt.savefig("graph_weighted.png")
plt.show()
