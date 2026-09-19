from .classical import classical_signal_timing
from .qaoa import run_qaoa, convert_to_signal_timings


def compare_methods(
    traffic_data,
    queue_data=None,
    emergency_signals=None
):
    """
    Compare classical signal timing
    with QAOA optimized timing.
    """

    classical = {}

    for signal, density in traffic_data.items():
        classical[signal] = classical_signal_timing(
            density
        )

    quantum_solution = run_qaoa(
        traffic_data,
        queue_data,
        emergency_signals
    )

    quantum = convert_to_signal_timings(
        quantum_solution
    )

    print("\nCLASSICAL VS QAOA")
    print("=================")

    for signal in traffic_data:

        print(
            f"{signal} -> "
            f"Classical: {classical[signal]} sec | "
            f"QAOA: {quantum[signal]} sec"
        )

    return classical, quantum


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

    compare_methods(
        traffic_data,
        queue_data,
        emergency_signals
    )