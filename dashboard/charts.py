import streamlit as st
import pandas as pd


def show_comparison():
    st.subheader("📊 Before vs After Optimization")

    data = {
        "Metric": [
            "Waiting Time",
            "Queue Length",
            "Fuel Consumption",
            "CO₂ Emission"
        ],
        "Before": [
            82,
            31,
            18,
            42
        ],
        "After": [
            54,
            19,
            14,
            33
        ]
    }

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )