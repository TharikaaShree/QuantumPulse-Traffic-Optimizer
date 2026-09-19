from qiskit.primitives import StatevectorSampler
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
from qiskit_optimization.algorithms import MinimumEigenOptimizer

from .qubo import create_traffic_qubo


def run_qaoa(
    traffic_data,
    queue_data=None,
    emergency_signals=None
):
    """
    Run QAOA for adaptive traffic signal optimization.

    Returns:
        Dictionary containing:
        0 = normal green
        1 = extended green
    """

    problem = create_traffic_qubo(
        traffic_data,
        queue_data,
        emergency_signals
    )

    sampler = StatevectorSampler(
        seed=42
    )

    optimizer = COBYLA(
        maxiter=50
    )

    qaoa = QAOA(
        sampler=sampler,
        optimizer=optimizer,
        reps=2
    )

    minimum_eigen_optimizer = MinimumEigenOptimizer(
        qaoa
    )

    result = minimum_eigen_optimizer.solve(
        problem
    )

    optimized_solution = {}

    for variable, value in zip(
        problem.variables,
        result.x
    ):
        optimized_solution[
            variable.name
        ] = int(round(value))

    return optimized_solution


def convert_to_signal_timings(solution):
    """
    Convert binary decisions into green-light timings.

    0 -> 30 seconds
    1 -> 45 seconds
    """

    timings = {}

    for signal, decision in solution.items():

        if decision == 1:
            timings[signal] = 45
        else:
            timings[signal] = 30

    return timings


def print_results(
    traffic_data,
    queue_data,
    emergency_signals,
    solution,
    timings
):
    """
    Display optimization results.
    """

    print("\nTraffic Data")
    print("============")

    for signal in traffic_data:

        print(
            f"{signal} -> "
            f"Traffic: {traffic_data[signal]}, "
            f"Queue: {queue_data.get(signal, 0)}"
        )

    print("\nEmergency Signals")
    print("=================")

    if emergency_signals:
        print(", ".join(emergency_signals))
    else:
        print("None")

    print("\nQAOA Solution")
    print("=============")

    for signal, decision in solution.items():

        print(
            f"{signal} -> "
            f"Decision: {decision}"
        )

    print("\nOptimized Signal Timings")
    print("========================")

    for signal, timing in timings.items():

        print(
            f"{signal} -> "
            f"{timing} seconds"
        )


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

    solution = run_qaoa(
        traffic_data,
        queue_data,
        emergency_signals
    )

    timings = convert_to_signal_timings(
        solution
    )

    print_results(
        traffic_data,
        queue_data,
        emergency_signals,
        solution,
        timings
    )