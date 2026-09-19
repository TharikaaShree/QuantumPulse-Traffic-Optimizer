import streamlit as st


def show_header():
    st.markdown(
        """
        <div class="hero">
            <div>
                <div class="brand">⚛️ QUANTUMPULSE</div>
                <div class="subtitle">
                    Quantum-Enhanced Adaptive Urban Traffic Control
                </div>
            </div>

            <div class="status">
                ● SYSTEM ONLINE
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def show_scenario_panel():

    st.markdown(
        """
        <div class="section-title">
            🚨 LIVE SCENARIO SIMULATOR
        </div>
        """,
        unsafe_allow_html=True
    )

    scenario = st.selectbox(
        "Choose a traffic event",
        [
            "Normal Traffic",
            "Rush Hour",
            "Accident",
            "Road Closure",
            "🚑 Emergency Vehicle"
        ],
        label_visibility="collapsed"
    )

    return scenario