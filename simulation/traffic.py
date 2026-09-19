def create_traffic_state():
    """
    Create the current traffic condition
    for each intersection.
    """

    traffic = {
        "S1": {
            "vehicles": 30,
            "queue": 12,
            "capacity": 100,
            "signal": "GREEN",
            "green_time": 30
        },

        "S2": {
            "vehicles": 75,
            "queue": 35,
            "capacity": 100,
            "signal": "RED",
            "green_time": 30
        },

        "S3": {
            "vehicles": 20,
            "queue": 8,
            "capacity": 100,
            "signal": "GREEN",
            "green_time": 30
        },

        "S4": {
            "vehicles": 55,
            "queue": 25,
            "capacity": 100,
            "signal": "RED",
            "green_time": 30
        }
    }

    return traffic


def calculate_density(vehicles, capacity):
    """
    Calculate traffic density as a percentage.
    """

    if capacity == 0:
        return 0

    return round((vehicles / capacity) * 100, 2)


def calculate_waiting_time(queue):
    """
    Estimate waiting time based on queue length.
    """

    return round(queue * 0.5, 2)