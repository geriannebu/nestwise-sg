import streamlit as st

def render_methodology():
    st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)
    with st.expander("How NestWise works"):
        st.markdown(
            "<strong>Three pricing anchors</strong><br>"
            "1. <strong>Predicted fair value</strong> — hedonic model estimate based on flat type, size, lease, location, and amenities.<br>"
            "2. <strong>Recent transacted median</strong> — what similar flats have actually sold for in the same period.<br>"
            "3. <strong>Current asking prices</strong> — live listings scraped or provided via backend API.<br><br>"
            "<strong>Valuation labels</strong><br>"
            "NestWise translates the asking-vs-predicted gap into decision-ready signals:<br>"
            "🔥 Steal (−5% or below) &nbsp;·&nbsp; ✅ Fair (within 3%) &nbsp;·&nbsp; ⚠️ Slightly overpriced (+3–10%) &nbsp;·&nbsp; 🚩 Overpriced (&gt;10%)<br><br>"
            "<strong>Town recommendation</strong><br>"
            "If you leave town blank, the engine scores all towns on affordability, amenity fit, and proximity to your anchors, then surfaces the top 5.",
            unsafe_allow_html=True,
        )