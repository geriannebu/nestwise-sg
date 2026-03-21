import streamlit as st

from backend.schemas.inputs import UserInputs
from backend.utils.constants import FLAT_TYPES, TOWNS, SCHOOL_OPTIONS, AMENITY_LABELS
from frontend.components.sections import render_section


def build_user_inputs() -> UserInputs:
    render_section(
        "1",
        "Tell us what you’re looking for",
        "We’ll generate price insights and recommendations.",
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        budget = st.number_input(
            "Budget (S$)",
            min_value=150000,
            max_value=2000000,
            value=650000,
            step=10000,
        )
        flat_type = st.selectbox("Flat type", FLAT_TYPES, index=2)

    with c2:
        floor_area_sqm = st.number_input(
            "Floor area (sqm)",
            min_value=35.0,
            max_value=160.0,
            value=95.0,
            step=1.0,
        )
        lease_commence_year = st.number_input(
            "Lease commence year",
            min_value=1966,
            max_value=2025,
            value=2005,
            step=1,
        )

    with c3:
        town_choice = st.selectbox(
            "Preferred town",
            ["Recommendation mode"] + TOWNS,
        )
        school_scope = st.selectbox(
            "School preference",
            SCHOOL_OPTIONS,
            index=0,
        )

    st.markdown("### Amenity priorities")
    st.caption("Rate how important each amenity is to you.")

    a1, a2, a3 = st.columns(3)

    amenity_keys = list(AMENITY_LABELS.keys())
    default_weights = {
        "mrt": 5,
        "bus": 3,
        "healthcare": 2,
        "schools": 3,
        "hawker": 4,
        "retail": 3,
    }

    amenity_weights = {}

    for idx, key in enumerate(amenity_keys):
        col = [a1, a2, a3][idx % 3]
        with col:
            amenity_weights[key] = st.slider(
                AMENITY_LABELS[key],
                min_value=1,
                max_value=5,
                value=default_weights.get(key, 3),
            )

    st.markdown("### Anchor locations")
    st.caption("Optional: add up to 2 postal codes for places you want to stay close to.")

    p1, p2 = st.columns(2)
    with p1:
        postal_1 = st.text_input("Postal code 1", value="")
    with p2:
        postal_2 = st.text_input("Postal code 2", value="")

    landmark_postals = [p.strip() for p in [postal_1, postal_2] if p.strip()]

    return UserInputs(
        budget=int(budget),
        flat_type=flat_type,
        floor_area_sqm=float(floor_area_sqm),
        lease_commence_year=int(lease_commence_year),
        town=None if town_choice == "Recommendation mode" else town_choice,
        school_scope=school_scope,
        amenity_weights=amenity_weights,
        landmark_postals=landmark_postals,
    )


def render_user_profile(inputs: UserInputs):
    town_text = inputs.town if inputs.town else "Recommendation mode"
    anchors_text = ", ".join(inputs.landmark_postals) if inputs.landmark_postals else "None"

    st.markdown("### Your search profile")
    st.markdown(
        f"""
        <div class="nw-profile">
            <div><strong>Budget:</strong> S${inputs.budget:,.0f}</div>
            <div><strong>Flat type:</strong> {inputs.flat_type}</div>
            <div><strong>Floor area:</strong> {inputs.floor_area_sqm:.1f} sqm</div>
            <div><strong>Lease commence year:</strong> {inputs.lease_commence_year}</div>
            <div><strong>Town:</strong> {town_text}</div>
            <div><strong>School preference:</strong> {inputs.school_scope}</div>
            <div><strong>Anchors:</strong> {anchors_text}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )