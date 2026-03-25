import pandas as pd
import streamlit as st

from backend.utils.formatters import fmt_sgd, valuation_tag_html


def render_listing_tab(inputs, bundle):
    listings_df = bundle["listings_df"]
    viable_count = bundle.get("viable_listing_count", len(listings_df))
    median_asking = bundle.get("median_asking_active", None)
    
    st.markdown("#### Best matches")

    if listings_df is None or listings_df.empty:
        st.info("No listings available.")
        return

    st.markdown(
    f"""
    **{viable_count} viable listings** passed your constraints.
    """
    )

    if median_asking:
        st.markdown(
            f"""
            Median asking price of comparable active listings: **S${median_asking:,.0f}**
            """
        )
    
    st.markdown("### Best matches")

    top_n = min(3, len(listings_df))
    st.markdown("##### Top picks")

    for idx, row in listings_df.head(top_n).iterrows():
        diff = row["asking_vs_predicted_pct"]
        arrow = "below" if diff < 0 else "above"
        tag = valuation_tag_html(row["valuation_label"])

        st.markdown(
            f"""
            <div class="nw-listing">
                <div class="nw-listing-header">
                    <div>
                        <div class="nw-listing-id">{row['listing_id']} · {row['town']}</div>
                        <div class="nw-listing-meta">{row['flat_type']} · {row['floor_area_sqm']} sqm · Storey {row['storey_range']}</div>
                    </div>
                    <div class="nw-listing-price">
                        <div class="nw-listing-asking">{fmt_sgd(row['asking_price'])}</div>
                        <div class="nw-listing-predicted">Predicted: {fmt_sgd(row['predicted_price'])}</div>
                    </div>
                </div>
                <div style="display:flex;align-items:center;gap:10px;font-size:0.85rem;color:var(--text-secondary)">
                    {tag}
                    <span>{abs(diff):.1f}% {arrow} model estimate</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # --- Save Flat button ---
        user = st.session_state.get("current_user")
        if user:
            st.session_state.saved_flats.setdefault(user, [])
            if st.button(f"Save flat {row['listing_id']}", key=f"save_flat_{row['listing_id']}"):
                # Check for duplicates
                saved_ids = [f["listing_id"] for f in st.session_state.saved_flats[user]]
                if row["listing_id"] not in saved_ids:
                    st.session_state.saved_flats[user].append({
                        "listing_id": row["listing_id"],
                        "town": row["town"],
                        "flat_type": row["flat_type"],
                        "floor_area_sqm": row["floor_area_sqm"],
                        "storey_range": row["storey_range"],
                        "asking_price": row["asking_price"],
                        "predicted_price": row["predicted_price"],
                        "valuation_label": row["valuation_label"],
                        "score": row.get("score", None)
                    })
                    st.success(f"Saved {row['listing_id']} ✅")
                else:
                    st.info(f"{row['listing_id']} already saved.")

        if "listing_url" in row and row["listing_url"]:
            st.link_button("View original listing →", row["listing_url"])

    st.markdown("##### All listings")
    disp = listings_df.copy()

    for col in ["asking_price", "predicted_price", "recent_median_transacted"]:
        if col in disp.columns:
            disp[col] = disp[col].map(fmt_sgd)

    if "asking_vs_predicted_pct" in disp.columns:
        disp["asking_vs_predicted_pct"] = disp["asking_vs_predicted_pct"].map(lambda x: f"{x:+.1f}%")

    cols = [
        "listing_id",
        "town",
        "flat_type",
        "floor_area_sqm",
        "storey_range",
        "asking_price",
        "predicted_price",
        "recent_median_transacted",
        "asking_vs_predicted_pct",
        "valuation_label",
    ]
    cols = [c for c in cols if c in disp.columns]

    st.dataframe(disp[cols], use_container_width=True, hide_index=True)