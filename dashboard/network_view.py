import streamlit as st
import plotly.graph_objects as go


def show_network(scenario="Normal Traffic"):

    st.markdown(
        """
        <div class="section-title">
            🗺️ LIVE TRAFFIC NETWORK
        </div>
        """,
        unsafe_allow_html=True
    )

    nodes = {
        "S1": (0, 2),
        "S2": (2, 2),
        "S3": (2, 0),
        "S4": (0, 0),
    }

    edges = [
        ("S1", "S2"),
        ("S2", "S3"),
        ("S3", "S4"),
        ("S4", "S1"),
    ]

    # Default signal colors
    signal_colors = {
        "S1": "#22c55e",
        "S2": "#22c55e",
        "S3": "#22c55e",
        "S4": "#22c55e"
    }

    # Change signals according to scenario
    if scenario == "Rush Hour":

        signal_colors = {
            "S1": "#facc15",
            "S2": "#22c55e",
            "S3": "#facc15",
            "S4": "#22c55e"
        }

    elif scenario == "Accident":

        signal_colors = {
            "S1": "#22c55e",
            "S2": "#facc15",
            "S3": "#ef4444",
            "S4": "#22c55e"
        }

    elif scenario == "Road Closure":

        signal_colors = {
            "S1": "#22c55e",
            "S2": "#ef4444",
            "S3": "#facc15",
            "S4": "#22c55e"
        }

    elif scenario == "🚑 Emergency Vehicle":

        signal_colors = {
            "S1": "#facc15",
            "S2": "#22c55e",
            "S3": "#22c55e",
            "S4": "#22c55e"
        }

    fig = go.Figure()

    # Draw roads
    for start, end in edges:

        x1, y1 = nodes[start]
        x2, y2 = nodes[end]

        fig.add_trace(
            go.Scatter(
                x=[x1, x2],
                y=[y1, y2],
                mode="lines",
                line=dict(
                    color="#334155",
                    width=8
                ),
                hoverinfo="none"
            )
        )

    # Draw intersections
    for name, (x, y) in nodes.items():

        fig.add_trace(
            go.Scatter(
                x=[x],
                y=[y],
                mode="markers+text",

                text=[name],

                textposition="middle center",

                marker=dict(
                    size=55,
                    color=signal_colors[name],
                    line=dict(
                        color="#ffffff",
                        width=2
                    )
                ),

                textfont=dict(
                    color="white",
                    size=14
                ),

                hovertemplate=(
                    f"<b>{name}</b><br>"
                    f"Scenario: {scenario}<br>"
                    f"Signal: {signal_colors[name]}"
                    "<extra></extra>"
                )
            )
        )

    fig.update_layout(
        height=500,
        showlegend=False,

        margin=dict(
            l=10,
            r=10,
            t=10,
            b=10
        ),

        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",

        xaxis=dict(
            visible=False
        ),

        yaxis=dict(
            visible=False
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )