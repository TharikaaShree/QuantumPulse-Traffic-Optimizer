from copy import deepcopy


def apply_scenario(traffic, scenario):
    """
    Apply a traffic scenario to the current traffic state.
    """

    updated_traffic = deepcopy(traffic)

    if scenario == "Normal":
        return updated_traffic

    elif scenario == "Rush Hour":
        for data in updated_traffic.values():
            data["vehicles"] = min(
                data["capacity"],
                int(data["vehicles"] * 1.6)
            )

            data["queue"] = min(
                data["capacity"],
                int(data["queue"] * 1.7)
            )

    elif scenario == "Accident":
        # Accident at S3
        updated_traffic["S3"]["capacity"] = 30
        updated_traffic["S3"]["vehicles"] = 30
        updated_traffic["S3"]["queue"] = 28

    elif scenario == "Road Closure":
        # Road/intersection S2 temporarily unavailable
        updated_traffic["S2"]["capacity"] = 10
        updated_traffic["S2"]["vehicles"] = 5
        updated_traffic["S2"]["queue"] = 5

    elif scenario == "Ambulance Arrival":
        # Emergency vehicle appears at S2
        updated_traffic["S2"]["emergency"] = True
        updated_traffic["S2"]["emergency_vehicle"] = "AMBULANCE"

    else:
        raise ValueError(f"Unknown scenario: {scenario}")

    return updated_traffic