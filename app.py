import streamlit as st

from dashboard.components import show_header, show_scenario_panel
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

    </style>
    """,
    unsafe_allow_html=True
)


show_header()

scenario = show_scenario_panel()

show_network()