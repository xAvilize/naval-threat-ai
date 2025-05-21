import networkx as nx
import json
import os

def get_optimal_route():
    path = os.path.join(os.path.dirname(__file__), "data", "routes.json")
    with open(path) as f:
        data = json.load(f)

    G = nx.Graph()
    for edge in data["edges"]:
        G.add_edge(edge["from"], edge["to"], weight=edge["cost"])

    path = nx.dijkstra_path(G, "A", "C")
    return { "path": path }
