import streamlit as st


def show_title():
    st.title("🚦 QuantumPulse Traffic Optimizer")
    st.write(
        "Hybrid Quantum-Classical Urban Traffic Optimization"
    )


def show_scenario_buttons():
    st.subheader("🚦 Scenario Simulator")

    scenario = st.selectbox(
        "Select a traffic scenario",
        [
            "Normal Traffic",
            "Rush Hour",
            "Accident",
            "Road Closure",
            "🚑 Ambulance Arrival"
        ]
    )

    return scenario