import networkx as nx

def create_traffic_network():
    """
    Create a simple 4-intersection traffic network.
    """

    graph = nx.Graph()

    # Add intersections
    intersections = ["S1", "S2", "S3", "S4"]

    for intersection in intersections:
        graph.add_node(intersection)

    # Add roads connecting intersections
    roads = [
        ("S1", "S2", 2.0),
        ("S2", "S3", 1.5),
        ("S3", "S4", 2.0),
        ("S4", "S1", 1.8),
        ("S1", "S3", 2.5),
        ("S2", "S4", 2.2),
    ]

    for start, end, distance in roads:
        graph.add_edge(start, end, distance=distance)

    return graph