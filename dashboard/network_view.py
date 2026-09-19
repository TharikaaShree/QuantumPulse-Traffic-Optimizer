import streamlit as st


def show_network():
    st.subheader("🛣️ Traffic Network")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("🟢 S1\n\nGreen: 40 sec")

    with col2:
        st.warning("🟡 S2\n\nGreen: 30 sec")

    with col3:
        st.error("🔴 S3\n\nRed: 20 sec")

    st.success("🟢 S4 → 🏥 Hospital")