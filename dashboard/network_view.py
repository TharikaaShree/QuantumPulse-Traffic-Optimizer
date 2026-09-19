import streamlit as st
import plotly.graph_objects as go


def show_network():

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

    fig = go.Figure()

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
                    color="#22c55e",
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
                    "Traffic signal<br>"
                    "Click for details"
                    "<extra></extra>"
                )
            )
        )

    fig.update_layout(
        height=500,
        showlegend=False,
        margin=dict(l=10, r=10, t=10, b=10),
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