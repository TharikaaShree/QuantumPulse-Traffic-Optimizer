def classical_signal_timing(traffic_density):
    """
    Simple rule-based traffic signal timing.

    traffic_density: number representing traffic density
    returns: green light duration in seconds
    """

    if traffic_density < 30:
        return 20

    elif traffic_density < 60:
        return 30

    else:
        return 45
    

if __name__ == "__main__":
    traffic_data = {
        "S1": 30,
        "S2": 80,
        "S3": 20,
        "S4": 60
    }

    for signal, density in traffic_data.items():
        timing = classical_signal_timing(density)
        print(signal, "Density:", density, "Green:", timing, "seconds")