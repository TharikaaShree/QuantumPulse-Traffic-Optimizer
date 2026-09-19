import streamlit as st

from dashboard.components import (
    show_header,
    show_scenario_panel,
    show_metrics,
    show_emergency_corridor,
    show_optimization_comparison,
    show_optimizer_explanation
)
from dashboard.network_view import show_network


st.set_page_config(
    page_title="QuantumPulse",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown(
    """
    <style>

    .stApp {
        background:
            radial-gradient(
                circle at top right,
                #162447 0%,
                #0b1220 35%,
                #060a12 100%
            );
        color: white;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    .hero {
        background: linear-gradient(
            135deg,
            rgba(30, 41, 59, 0.95),
            rgba(15, 23, 42, 0.95)
        );

        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 20px;
        padding: 28px;
        margin-bottom: 25px;

        display: flex;
        justify-content: space-between;
        align-items: center;

        box-shadow: 0 10px 35px rgba(0,0,0,0.35);
    }

    .brand {
        font-size: 30px;
        font-weight: 800;
        letter-spacing: 2px;
    }

    .subtitle {
        margin-top: 7px;
        color: #94a3b8;
        font-size: 15px;
    }

    .status {
        color: #22c55e;
        font-weight: 700;
        font-size: 14px;
    }

    .section-title {
        font-size: 20px;
        font-weight: 700;
        margin: 20px 0 12px 0;
    }
    
    .metric-card {
    background: linear-gradient(
        145deg,
        rgba(30, 41, 59, 0.95),
        rgba(15, 23, 42, 0.95)
    );

    .emergency-panel {
    background: linear-gradient(
        135deg,
        rgba(127, 29, 29, 0.35),
        rgba(30, 41, 59, 0.95)
    );

    border: 1px solid rgba(239, 68, 68, 0.45);

    border-radius: 18px;

    padding: 22px;

    margin-top: 25px;

    box-shadow: 0 8px 30px rgba(0,0,0,0.25);
}

.emergency-title {
    color: #fca5a5;

    font-size: 18px;

    font-weight: 800;

    letter-spacing: 1px;
}

.emergency-route {
    margin-top: 20px;

    font-size: 25px;

    font-weight: 700;

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 18px;
}

.emergency-route span {
    background: rgba(34,197,94,0.15);

    border: 1px solid rgba(34,197,94,0.5);

    border-radius: 12px;

    padding: 10px 16px;
}

.emergency-label {
    margin-top: 15px;

    text-align: center;

    color: #94a3b8;

    font-size: 12px;

    letter-spacing: 1px;
}

    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;

    padding: 20px;

    min-height: 150px;

    box-shadow: 0 8px 25px rgba(0,0,0,0.25);

    transition: transform 0.2s ease,
                border-color 0.2s ease;
}

.metric-card:hover {
    transform: translateY(-4px);
    border-color: rgba(34,197,94,0.5);
}

.metric-icon {
    font-size: 24px;
    margin-bottom: 10px;
}

.metric-label {
    color: #94a3b8;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 1px;
}

.metric-value {
    color: white;
    font-size: 30px;
    font-weight: 800;
    margin-top: 6px;
}

.metric-sub {
    color: #64748b;
    font-size: 11px;
    margin-top: 5px;
    font-weight: 600;
}

    </style>
    """,
    unsafe_allow_html=True
)

show_header()

scenario = show_scenario_panel()

show_metrics()

show_network(scenario)

show_emergency_corridor(scenario)

show_optimization_comparison()
show_optimizer_explanation(scenario)