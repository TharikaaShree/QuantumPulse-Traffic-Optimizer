from optimization.classical import classical_signal_timing
from optimization.qaoa import (
    run_qaoa,
    convert_to_signal_timings
)


def test_classical_signal_timing():
    assert classical_signal_timing(20) == 20
    assert classical_signal_timing(40) == 30
    assert classical_signal_timing(80) == 45


def test_qaoa_solution():
    traffic_data = {
        "S1": 30,
        "S2": 80,
        "S3": 20,
        "S4": 60
    }

    solution = run_qaoa(traffic_data)

    assert len(solution) == 4

    for signal, decision in solution.items():
        assert decision in [0, 1]


def test_signal_timings():
    solution = {
        "S1": 0,
        "S2": 1,
        "S3": 0,
        "S4": 1
    }

    timings = convert_to_signal_timings(solution)

    for signal, timing in timings.items():
        assert 20 <= timing <= 60