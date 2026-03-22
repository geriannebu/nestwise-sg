import streamlit as st
from backend.services.predictor_service import get_prediction_bundle
from backend.schemas.inputs import UserInputs

def render_scenario_testing_output(user_inputs: UserInputs):
    st.markdown("#### Scenario Testing")
    st.caption("Test how changes in flat type, floor area, lease age, and amenity priorities affect your estimated flat price.")

    # --- Original prediction for reference ---
    original_bundle = get_prediction_bundle(user_inputs)
    original_price = original_bundle["predicted_price"]

    # --- Flat type ---
    flat_type_options = ["2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE"]
    adjusted_flat_type = st.selectbox(
        "Test a different flat type",
        options=flat_type_options,
        index=flat_type_options.index(user_inputs.flat_type)
    )

    # --- Floor area using + / - stepper ---
    adjusted_area = st.number_input(
        "Floor area for testing (sqm)",
        min_value=10.0,
        max_value=200.0,
        value=user_inputs.floor_area_sqm,
        step=1.0,
        format="%.1f"
    )

    # --- Lease commence year using + / - stepper ---
    adjusted_lease_year = st.number_input(
        "Lease commence year for testing",
        min_value=1950,
        max_value=2026,
        value=user_inputs.lease_commence_year,
        step=1
    )

    # --- Amenity scoring ---
    adjusted_amenities = {}
    st.markdown("**Adjust amenity priorities (1-5)**")
    amenity_names = list(user_inputs.amenity_weights.keys())
    num_cols = 3  # sliders per row
    for i in range(0, len(amenity_names), num_cols):
        cols = st.columns(num_cols)
        for j, amenity in enumerate(amenity_names[i:i+num_cols]):
            adjusted_score = cols[j].slider(
                f"{amenity} priority",
                min_value=1,
                max_value=5,
                value=int(user_inputs.amenity_weights[amenity]),
                step=1
            )
            adjusted_amenities[amenity] = adjusted_score

   

    # --- Create scenario input object ---
    scenario_inputs = UserInputs(
        budget=user_inputs.budget,
        flat_type=adjusted_flat_type,
        floor_area_sqm=adjusted_area,
        lease_commence_year=adjusted_lease_year,
        town=user_inputs.town,
        school_scope=user_inputs.school_scope,
        amenity_weights=adjusted_amenities,
        landmark_postals=user_inputs.landmark_postals
    )

    # --- Compute scenario predicted price ---
    bundle = get_prediction_bundle(scenario_inputs)
    scenario_price = bundle["predicted_price"]
    price_diff = scenario_price - original_price  # difference from original

    # --- Display metrics ---
    st.markdown("**Scenario Predicted Price:**")
    st.metric("Predicted flat value", f"${scenario_price:,.0f}")

    # --- Insights ---
    st.markdown("**Scenario Insights:**")

    if adjusted_flat_type != user_inputs.flat_type:
        diff = scenario_price - original_price
        st.info(f"Testing flat type {adjusted_flat_type} changes predicted price by ${diff:,.0f}.")

    if adjusted_area != user_inputs.floor_area_sqm:
        diff = scenario_price - original_price
        st.info(f"Changing floor area to {adjusted_area} sqm changes predicted price by ${diff:,.0f}.")

    if adjusted_lease_year != user_inputs.lease_commence_year:
        diff = scenario_price - original_price
        st.info(f"Changing lease commence year to {adjusted_lease_year} changes predicted price by ${diff:,.0f}.")

    for amenity, new_score in adjusted_amenities.items():
        if new_score != user_inputs.amenity_weights[amenity]:
            diff = scenario_price - original_price
            st.info(f"Changing {amenity} priority from {user_inputs.amenity_weights[amenity]} to {new_score} changes predicted price by ${diff:,.0f}.")