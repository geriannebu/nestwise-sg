import streamlit as st

from frontend.pages.flat_outputs.price_story import render_price_story_tab
from frontend.pages.flat_outputs.best_matches import render_listing_tab
from frontend.pages.flat_outputs.towns import render_towns_tab
from frontend.pages.flat_outputs.map_view import render_map_tab
from frontend.pages.flat_outputs.scenario_testing import render_scenario_testing_output


def render_flat_finder_page(inputs, bundle, map_bundle):
    subtab1, subtab2, subtab3, subtab4 = st.tabs([
        "📊 Price analysis",
        "🏘️ Best matches",
        "⭐ Town insights + scenario testing",
        "📍 Map",
    ])

    with subtab1:
        render_price_story_tab(bundle)

    with subtab2:
        render_listing_tab(bundle["listings_df"])

    with subtab3:
        render_towns_tab(inputs, bundle["recommendations_df"])
        st.markdown("---")
        render_scenario_testing_output(inputs)  # <-- only pass inputs now

    with subtab4:
        render_map_tab(inputs, map_bundle)