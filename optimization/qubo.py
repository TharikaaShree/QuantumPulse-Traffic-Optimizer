from qiskit_optimization import QuadraticProgram


def create_traffic_qubo(
    traffic_data,
    queue_data=None,
    emergency_signals=None
):
    """
    Create a QUBO model for adaptive traffic signal optimization.

    Binary decision:
        0 = normal green time (30 seconds)
        1 = extended green time (45 seconds)

    The model considers:
        - traffic density
        - queue length
        - emergency priority
        - penalty for extending too many signals
    """

    if queue_data is None:
        queue_data = {}

    if emergency_signals is None:
        emergency_signals = []

    problem = QuadraticProgram(
        "TrafficSignalOptimization"
    )

    # Create binary variable for every intersection
    for signal in traffic_data:
        problem.binary_var(name=signal)

    linear_coefficients = {}

    for signal, density in traffic_data.items():

        queue = queue_data.get(signal, 0)

        # Traffic and queue benefit
        traffic_pressure = float(density) * 0.5
        queue_pressure = float(queue) * 1.0

        # Emergency priority
        emergency_bonus = 0

        if signal in emergency_signals:
            emergency_bonus = 40

        # Negative coefficient means:
        # choosing extended green reduces the objective
        benefit = (
            traffic_pressure
            + queue_pressure
            + emergency_bonus
        )

        # Penalty for using extended green
        extension_penalty = 25

        coefficient = extension_penalty - benefit

        linear_coefficients[signal] = coefficient

    problem.minimize(
        linear=linear_coefficients
    )

    return problem


if __name__ == "__main__":

    traffic_data = {
        "S1": 30,
        "S2": 80,
        "S3": 20,
        "S4": 60
    }

    queue_data = {
        "S1": 10,
        "S2": 30,
        "S3": 5,
        "S4": 20
    }

    emergency_signals = [
        "S2",
        "S3"
    ]

    qubo = create_traffic_qubo(
        traffic_data,
        queue_data,
        emergency_signals
    )

    print("Traffic QUBO")
    print("============")

    print(qubo.prettyprint())