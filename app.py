import streamlit as st

from frontend.styles.css import inject_css
from frontend.state.session import init_session_state

from frontend.components.hero import render_hero
import frontend.components.input_forms as forms

from frontend.components.sections import render_section
from frontend.components.methodology import render_methodology
from frontend.components.cards import (
    render_value_cards,
    render_budget_banner,
    render_nestwise_pick,
)

from backend.services.predictor_service import get_prediction_bundle
from backend.services.map_service import get_map_bundle

from frontend.pages.flat_finder import render_flat_finder_page
from frontend.pages.comparison_tool import render_comparison_page
from frontend.pages.account import render_account_page


st.set_page_config(
    page_title="NestWise SG",
    page_icon="🪺",
    layout="wide",
    initial_sidebar_state="expanded",
)

PAGES = [
    "Flat Discovery",
    "Comparison Tool",
    "Account",
]


def main():
    init_session_state()
    inject_css()

    page = render_sidebar()

    if page == "Flat Discovery":
        render_discovery_page()
    elif page == "Comparison Tool":
        render_compare_shell()
    elif page == "Account":
        render_account_shell()


def render_sidebar():
    # ALL sidebar calls must use st.sidebar.xxx directly.
    # Never use `with st.sidebar:` — it resets context and collapses the sidebar.
    st.sidebar.markdown('<div class="nw-side-brand">NestWise SG</div>', unsafe_allow_html=True)
    st.sidebar.markdown('<div class="nw-side-sub">Housing search, but clearer</div>', unsafe_allow_html=True)
    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "Navigation",
        PAGES,
        label_visibility="collapsed",
    )

    st.sidebar.markdown("---")

    if st.session_state.get("current_user"):
        st.sidebar.markdown(
            f'<div class="nw-side-chip">Logged in as {st.session_state.current_user}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.sidebar.markdown(
            '<div class="nw-side-chip muted">Not logged in</div>',
            unsafe_allow_html=True,
        )

    if (
        st.session_state.get("insights_generated")
        and st.session_state.get("latest_bundle") is not None
    ):
        inputs_s = st.session_state.get("latest_inputs")
        bundle_s = st.session_state.get("latest_bundle")

        if inputs_s and bundle_s:
            # ─── BEAUTIFIED INSIGHTS CARD ───
            st.sidebar.markdown(f"""
                <div class="nw-recent-search">
                    <span class="nw-recent-label">Latest Search Insights</span>
                    <div style="margin-top: 10px;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                            <span style="font-size: 0.8rem; color: var(--text-3);">Budget</span>
                            <span style="font-size: 0.8rem; font-weight: 700; color: var(--text-1);">S${inputs_s.budget:,}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                            <span style="font-size: 0.8rem; color: var(--text-3);">Flat Type</span>
                            <span style="font-size: 0.8rem; font-weight: 600; color: var(--text-1);">{inputs_s.flat_type}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                            <span style="font-size: 0.8rem; color: var(--text-3);">Location</span>
                            <span style="font-size: 0.8rem; font-weight: 600; color: var(--text-1);">{inputs_s.town or 'All Regions'}</span>
                        </div>
                        <hr style="margin: 10px 0; border: none; border-top: 1px solid rgba(5, 158, 137, 0.15);">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-size: 0.75rem; color: var(--mint); font-weight: 700; text-transform: uppercase;">Predicted</span>
                            <span style="font-size: 1.1rem; font-weight: 800; color: var(--mint);">S${bundle_s['predicted_price']:,.0f}</span>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            if st.sidebar.button("🗑️ Clear current results", use_container_width=True):
                st.session_state.insights_generated = False
                st.session_state.latest_inputs = None
                st.session_state.latest_bundle = None
                st.session_state.latest_map_bundle = None
                st.rerun()
                
    return page


def render_discovery_page():
    render_hero()

    st.markdown(
        '<div id="nw-form-anchor" style="position:relative;top:-20px"></div>',
        unsafe_allow_html=True,
    )

    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

    inputs = forms.build_user_inputs()

    st.markdown("---")
    forms.render_user_profile(inputs)

    c1, c2, c3 = st.columns([3, 1.1, 3])
    with c2:
        go = st.button("🔍 Search", type="primary", use_container_width=True)

    if go:
        run_search(inputs)

    if not st.session_state.get("insights_generated") or st.session_state.get("latest_bundle") is None:
        st.markdown("---")
        render_section(
            "4",
            "How NestWise works",
            "A quick guide to how pricing and recommendation outputs are produced.",
        )
        render_methodology()
        return

    latest_inputs = st.session_state.latest_inputs
    latest_bundle = st.session_state.latest_bundle
    latest_map_bundle = st.session_state.latest_map_bundle

    st.markdown("---")
    render_section(
        "4",
        "Your results",
        "Price analysis, listings, town matching, scenario testing, and map outputs.",
    )

    render_value_cards(latest_bundle, latest_inputs.budget)
    render_budget_banner(latest_bundle, latest_inputs.budget)
    render_nestwise_pick(latest_inputs, latest_bundle)

    render_flat_finder_page(
        inputs=latest_inputs,
        bundle=latest_bundle,
        map_bundle=latest_map_bundle,
    )

    st.markdown("---")
    render_section(
        "5",
        "Methodology",
        "How to interpret the outputs and labels.",
    )
    render_methodology()


def run_search(inputs):
    st.session_state.insights_generated = True

    with st.spinner("Generating insights..."):
        bundle = get_prediction_bundle(inputs)
        map_bundle = get_map_bundle(inputs, bundle["recommendations_df"])

    st.session_state.latest_inputs = inputs
    st.session_state.latest_bundle = bundle
    st.session_state.latest_map_bundle = map_bundle

    if st.session_state.current_user is not None:
        st.session_state.user_histories.setdefault(st.session_state.current_user, [])
        st.session_state.user_histories[st.session_state.current_user].append({
            "budget": inputs.budget,
            "flat_type": inputs.flat_type,
            "town": inputs.town or "Recommendation mode",
            "predicted_price": bundle["predicted_price"],
            "recent_median_transacted": bundle["recent_median_transacted"],
        })


def render_compare_shell():
    st.markdown("# Comparison Tool")
    st.caption("Compare shortlisted or generated listings side by side.")

    if (
        not st.session_state.get("insights_generated")
        or st.session_state.get("latest_bundle") is None
    ):
        st.info("Run a search in Flat Discovery first to unlock the comparison tool.")
        return

    render_comparison_page(
        inputs=st.session_state.latest_inputs,
        listings_df=st.session_state.latest_bundle["listings_df"],
    )


def render_account_shell():
    st.markdown("# Account")
    st.caption("Log in, sign up, and manage saved history.")
    render_account_page()


if __name__ == "__main__":
    main()
