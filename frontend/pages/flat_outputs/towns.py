from typing import Optional

import pandas as pd
import streamlit as st

from backend.schemas.inputs import UserInputs
from backend.utils.formatters import fmt_sgd


def render_towns_tab(inputs: UserInputs, reco_df: Optional[pd.DataFrame]):
    st.markdown("#### Town recommendations")
    if inputs.town:
        st.info("You have chosen a specific town — recommendation mode is off.")
        return
    if reco_df is None or reco_df.empty:
        st.info("No recommendations available.")
        return

    for rank, (_, row) in enumerate(reco_df.iterrows()):
        budget_tag = '<span class="nw-reco-within">✓ Within budget</span>' if row["within_budget"] else '<span class="nw-reco-over">↑ Above budget</span>'
        medal = ["🥇","🥈","🥉","4","5"][rank] if rank < 5 else str(rank+1)
        st.markdown(f"""
        <div class="nw-reco">
            <div class="nw-reco-header">
                <div class="nw-reco-name">{medal} &nbsp; {row['town']}</div>
                <div class="nw-reco-score">{row['match_score']:.1f} / 100</div>
            </div>
            <div class="nw-reco-why">{row['why_it_matches']}</div>
            <div class="nw-reco-footer">
                <span class="nw-reco-price">Est. {fmt_sgd(row['estimated_price'])}</span>
                {budget_tag}
            </div>
        </div>
        """, unsafe_allow_html=True)