import streamlit as st


def classify_listing(row):
    pct = row["asking_vs_predicted_pct"]
    if pct <= -5:
        return "🔥 Steal"
    if pct <= 3:
        return "✅ Fair"
    if pct <= 10:
        return "⚠️ Slightly overpriced"
    return "🚩 Overpriced"


def compute_listing_scores(listings_df, budget, amenity_weights):
    df = listings_df.copy()
    df["budget_gap"] = budget - df["asking_price"]
    df["budget_score"] = df["budget_gap"].apply(lambda x: max(0, min(100, 50 + x / 5000)))
    df["value_score"] = 100 - df["asking_vs_predicted_pct"].clip(lower=-20, upper=20).abs() * 3
    df["overall_value_score"] = (0.55 * df["value_score"] + 0.45 * df["budget_score"]).round(1)
    return df.sort_values("overall_value_score", ascending=False)


def sync_shortlist_options(valid_ids):
    st.session_state.shortlist_ids = [x for x in st.session_state.shortlist_ids if x in valid_ids]
    st.session_state.selected_shortlist_for_compare = [
        x for x in st.session_state.selected_shortlist_for_compare if x in valid_ids
    ]