import streamlit as st
import pandas as pd

from backend.utils.scoring import compute_listing_scores, sync_shortlist_options


def render_comparison_page(inputs, listings_df: pd.DataFrame):
    st.markdown("## Comparison tool")

    if listings_df.empty:
        st.info("No listings available yet.")
        return

    scored_df = compute_listing_scores(
        listings_df,
        inputs.budget,
        inputs.amenity_weights,
    )
    scored_df["comparison_source"] = "Current listing"

    valid_ids = scored_df["listing_id"].tolist()
    sync_shortlist_options(valid_ids)

    st.markdown("### Step 1 — Select shortlisted flats")
    if st.session_state.shortlist_ids:
        selected = st.multiselect(
            "Choose shortlisted listings",
            options=st.session_state.shortlist_ids,
            default=st.session_state.selected_shortlist_for_compare or st.session_state.shortlist_ids[:3],
        )
        st.session_state.selected_shortlist_for_compare = selected
    else:
        st.caption("No shortlisted flats yet — shortlist some listings first.")

    selected_df = scored_df[scored_df["listing_id"].isin(st.session_state.selected_shortlist_for_compare)]

    st.markdown("### Step 2 — Compare")
    if selected_df.empty:
        st.info("Select at least one listing to compare.")
        return

    display_cols = [
        "listing_id",
        "town",
        "flat_type",
        "floor_area_sqm",
        "asking_price",
        "predicted_price",
        "recent_median_transacted",
        "asking_vs_predicted_pct",
        "valuation_label",
        "comparison_source",
    ]
    st.dataframe(selected_df[display_cols], use_container_width=True, hide_index=True)