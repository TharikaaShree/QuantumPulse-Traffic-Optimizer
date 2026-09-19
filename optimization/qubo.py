from qiskit_optimization import QuadraticProgram


def create_traffic_qubo(traffic_data):
    """
    Create a QUBO model for traffic signal optimization.

    Each intersection has a binary decision:
        0 = normal green time
        1 = extended green time

    traffic_data:
        Dictionary containing traffic density at each intersection.
    """

    problem = QuadraticProgram("TrafficSignalOptimization")

    # Create one binary variable for each intersection
    for signal in traffic_data:
        problem.binary_var(name=signal)

    # Objective function
    linear_coefficients = {}

    for signal, density in traffic_data.items():

        # Higher traffic density should encourage
        # the optimizer to select extended green time.
        coefficient = -float(density)

        linear_coefficients[signal] = coefficient

    problem.minimize(linear=linear_coefficients)

    return problem


if __name__ == "__main__":

    # Example traffic data
    traffic_data = {
        "S1": 30,
        "S2": 80,
        "S3": 20,
        "S4": 60
    }

    qubo_problem = create_traffic_qubo(traffic_data)

    print("QUBO Problem:")
    print(qubo_problem.prettyprint())