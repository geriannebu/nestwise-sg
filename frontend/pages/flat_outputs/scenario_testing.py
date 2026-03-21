import streamlit as st


def render_scenario_testing_output(inputs, bundle):
    st.markdown("#### Scenario testing")

    st.caption("Test how changes in budget or home preferences may affect your estimated fit.")

    delta_budget = st.slider(
        "Adjust budget for testing",
        min_value=-100000,
        max_value=100000,
        value=0,
        step=10000,
    )

    adjusted_budget = inputs.budget + delta_budget
    predicted_price = bundle["predicted_price"]

    gap = adjusted_budget - predicted_price

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Current budget", f"${inputs.budget:,.0f}")
    with c2:
        st.metric("Scenario budget", f"${adjusted_budget:,.0f}")
    with c3:
        st.metric("Scenario gap vs predicted", f"${gap:,.0f}")

    if gap >= 0:
        st.success("Under this scenario, the predicted flat value is within budget.")
    else:
        st.warning("Under this scenario, the predicted flat value is above budget.")