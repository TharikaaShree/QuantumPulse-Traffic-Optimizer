import networkx as nx


def find_emergency_route(graph, start, destination):
    """
    Find the shortest route for an emergency vehicle.
    """

    route = nx.shortest_path(
        graph,
        source=start,
        target=destination,
        weight="distance"
    )

    distance = nx.shortest_path_length(
        graph,
        source=start,
        target=destination,
        weight="distance"
    )

    return route, distance


def create_green_corridor(route):
    """
    Create a green signal plan for intersections
    along the emergency vehicle route.
    """

    signal_plan = {}

    for intersection in route:
        signal_plan[intersection] = {
            "signal": "GREEN",
            "priority": "EMERGENCY"
        }

    return signal_plan