import streamlit as st


def init_session_state():
    defaults = {
        "insights_generated": False,
        "latest_inputs": None,
        "latest_bundle": None,
        "latest_map_bundle": None,
        "shortlist_ids": [],
        "selected_shortlist_for_compare": [],
        "custom_compare_rows": [],
        "current_user": None,
        "users": {},  # email -> {"password": "..."}
        "user_histories": {},  # email -> [search dicts]
        "saved_flats": {},  # email -> [saved flats]
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value