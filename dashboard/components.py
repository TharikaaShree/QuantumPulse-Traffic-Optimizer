import streamlit as st


# =========================================================
# HEADER
# =========================================================

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
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# SCENARIO SELECTOR
# =========================================================

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


# =========================================================
# LIVE TRAFFIC METRICS
# =========================================================

def show_metrics(scenario="Normal Traffic"):

    st.markdown(
        """
        <div class="section-title">
            📊 LIVE TRAFFIC METRICS
        </div>
        """,
        unsafe_allow_html=True
    )

    # Demo traffic values for different scenarios
    metrics = {

        "Normal Traffic": {
            "vehicles": 128,
            "waiting": "42s",
            "queue": 18,
            "co2": "32kg"
        },

        "Rush Hour": {
            "vehicles": 245,
            "waiting": "78s",
            "queue": 42,
            "co2": "61kg"
        },

        "Accident": {
            "vehicles": 186,
            "waiting": "96s",
            "queue": 57,
            "co2": "74kg"
        },

        "Road Closure": {
            "vehicles": 154,
            "waiting": "83s",
            "queue": 48,
            "co2": "66kg"
        },

        "🚑 Emergency Vehicle": {
            "vehicles": 142,
            "waiting": "35s",
            "queue": 15,
            "co2": "29kg"
        }
    }

    current = metrics.get(
        scenario,
        metrics["Normal Traffic"]
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🚗 Vehicles",
            current["vehicles"]
        )

    with col2:

        st.metric(
            "🕐 Avg Waiting",
            current["waiting"]
        )

    with col3:

        st.metric(
            "🚦 Queue Length",
            current["queue"]
        )

    with col4:

        st.metric(
            "🌱 CO₂ Estimate",
            current["co2"]
        )


# =========================================================
# EMERGENCY GREEN CORRIDOR
# =========================================================

def show_emergency_corridor(scenario):

    if scenario == "🚑 Emergency Vehicle":

        st.markdown(
            "### 🚑 Emergency Route"
        )

        st.caption(
            "Priority corridor activated for emergency vehicle"
        )

        st.markdown(
            "🚑 **S2** 🟢  →  **S3** 🟢  →  **S4** 🟢  →  🏥 **Hospital**"
        )

        st.caption(
            "Emergency route: S2 → S3 → S4 → Hospital"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Before Optimization",
                "8.4 min"
            )

        with col2:

            st.metric(
                "After Optimization",
                "5.9 min",
                delta="-2.5 min"
            )


# =========================================================
# CLASSICAL VS QUANTUM-HYBRID
# =========================================================

def show_optimization_comparison():

    st.markdown(
        "### ⚛️ Optimization Comparison"
    )

    st.caption(
        "Classical traffic control vs Quantum-Hybrid optimization"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Classical Method",
            "8.4 min",
            "Baseline"
        )

    with col2:

        st.metric(
            "Quantum-Hybrid",
            "5.9 min",
            "-2.5 min"
        )

    st.markdown(
        "#### Average Waiting Time"
    )

    comparison_col1, comparison_col2 = st.columns(2)

    with comparison_col1:

        st.progress(0.84)

        st.caption(
            "Classical — 84%"
        )

    with comparison_col2:

        st.progress(0.59)

        st.caption(
            "Quantum-Hybrid — 59%"
        )
# =========================================================
# OPTIMIZER EXPLANATION
# =========================================================

def show_optimizer_explanation(scenario):

    st.markdown(
        "### 🧠 Optimizer Decision"
    )

    if scenario == "Normal Traffic":

        st.info(
            "Traffic is balanced across the network. "
            "Signals remain coordinated using normal timing."
        )

    elif scenario == "Rush Hour":

        st.info(
            "High traffic density detected. "
            "Green time is increased at high-demand intersections "
            "to reduce queue buildup."
        )

    elif scenario == "Accident":

        st.info(
            "Accident detected near S3. "
            "Traffic is redistributed and signal timing is adjusted "
            "to reduce congestion around the affected intersection."
        )

    elif scenario == "Road Closure":

        st.info(
            "Road closure detected. "
            "The optimizer reallocates signal timing to support "
            "alternative traffic routes."
        )

    elif scenario == "🚑 Emergency Vehicle":

        st.success(
            "Emergency vehicle detected. "
            "A priority green corridor is created from "
            "S2 → S3 → S4 to reduce emergency travel time."
        )