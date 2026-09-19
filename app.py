import streamlit as st

from dashboard.components import show_title, show_scenario_buttons
from dashboard.network_view import show_network


st.set_page_config(
    page_title="QuantumPulse Traffic Optimizer",
    page_icon="🚦",
    layout="wide"
)

show_title()

scenario = show_scenario_buttons()

st.write("Selected scenario:", scenario)

show_network()