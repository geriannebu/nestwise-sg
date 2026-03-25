"""best_matches.py
Redesigned listing tab — all HTML uses inline styles only.
No dependency on external CSS class rules.
"""

import streamlit as st

from backend.utils.formatters import fmt_sgd, valuation_tag_html
from backend.utils.scoring import compute_listing_scores, RANKING_ALPHA, RANKING_LABELS

# ── tokens ─────────────────────────────────────────────────────────────
_MINT        = "#059E87"
_MINT_DARK   = "#037a68"
_MINT_LIGHT  = "#e6f7f4"
_MINT_BORDER = "#a7e8dc"
_GREEN_SOFT  = "#ecfdf3"
_GREEN_BDR   = "#abefc6"
_AMBER_SOFT  = "#fffaeb"
_AMBER_BDR   = "#fedf89"
_AMBER_TEXT  = "#92400e"
_RED_SOFT    = "#fef3f2"
_RED_BDR     = "#fda29b"
_RED_TEXT    = "#991b1b"
_TEXT1       = "#0f172a"
_TEXT2       = "#4b5563"
_TEXT3       = "#9ca3af"
_BG_SOFT     = "#f7f8fa"
_BG_WHITE    = "#ffffff"
_BORDER      = "#e4e7ed"
_FONT        = "'DM Sans', -apple-system, sans-serif"
_RADIUS      = "14px"
_RADIUS_LG   = "18px"
_SHADOW_SM   = "0 1px 2px rgba(0,0,0,0.05)"
_SHADOW_CARD = "0 2px 8px rgba(0,0,0,0.07)"


# ── helpers ────────────────────────────────────────────────────────────

def _score_bar(value: float) -> str:
    pct = max(0.0, min(100.0, float(value)))
    return (
        f'<div style="height:3px;background:{_BORDER};border-radius:2px;'
        f'margin-top:5px;overflow:hidden;">'
        f'<div style="height:3px;width:{pct:.0f}%;background:{_MINT};'
        f'border-radius:2px;"></div>'
        f'</div>'
    )


def _score_pill(label: str, value: float, highlight: bool = False) -> str:
    val_color = _MINT_DARK if highlight else _TEXT1
    return (
        f'<div style="background:{_BG_SOFT};border:1px solid {_BORDER};'
        f'border-radius:{_RADIUS};padding:7px 10px 8px;">'
        f'<div style="font-family:{_FONT};font-size:0.66rem;font-weight:700;'
        f'text-transform:uppercase;letter-spacing:0.06em;color:{_TEXT3};margin-bottom:3px;">{label}</div>'
        f'<div style="font-family:{_FONT};font-size:0.95rem;font-weight:800;'
        f'color:{val_color};line-height:1;">{value:.1f}</div>'
        f'{_score_bar(value)}'
        f'</div>'
    )


def _valuation_tag_inline(label: str) -> str:
    """Inline-styled valuation tag (no CSS class dependency)."""
    styles = {
        "🔥 Steal":              (_GREEN_SOFT, "#166534", _GREEN_BDR),
        "✅ Fair":               (_GREEN_SOFT, "#166534", _GREEN_BDR),
        "⚠️ Slightly overpriced": (_AMBER_SOFT, _AMBER_TEXT, _AMBER_BDR),
        "🚩 Overpriced":         (_RED_SOFT,   _RED_TEXT,  _RED_BDR),
    }
    bg, color, border = styles.get(label, (_BG_SOFT, _TEXT2, _BORDER))
    return (
        f'<span style="display:inline-block;font-family:{_FONT};padding:3px 9px;'
        f'border-radius:999px;font-size:0.74rem;font-weight:700;'
        f'background:{bg};border:1px solid {border};color:{color};">{label}</span>'
    )


def _listing_card_html(row, rank: int, is_top: bool) -> str:
    tag   = _valuation_tag_inline(row["valuation_label"])
    diff  = row["asking_vs_predicted_pct"]
    arrow = "below" if diff < 0 else "above"

    card_border = f"1.5px solid {_MINT_BORDER}" if is_top else f"1px solid {_BORDER}"
    card_shadow = (
        f"0 0 0 3px rgba(5,158,135,0.06), {_SHADOW_SM}" if is_top else _SHADOW_SM
    )
    badge_bg    = _MINT_LIGHT if is_top else _BG_SOFT
    badge_color = _MINT_DARK  if is_top else _TEXT3
    badge_bdr   = _MINT_BORDER if is_top else _BORDER
    badge_text  = "#1 NestWise pick" if is_top else f"#{rank}"

    val_score = row.get("value_score",   0.0)
    am_score  = row.get("amenity_score", 0.0)
    fin_score = row.get("final_score",   0.0)

    pill_row = (
        f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));'
        f'gap:7px;margin:0.65rem 0 0.5rem;">'
        f'{_score_pill("Value score",   val_score)}'
        f'{_score_pill("Amenity score", am_score)}'
        f'{_score_pill("Final score",   fin_score, highlight=True)}'
        f'</div>'
    )

    return (
        f'<div style="background:{_BG_WHITE};border:{card_border};'
        f'border-radius:{_RADIUS_LG};padding:1rem 1.1rem;'
        f'margin-bottom:0.7rem;box-shadow:{card_shadow};">'

        # rank badge
        f'<span style="display:inline-block;font-family:{_FONT};font-size:0.67rem;'
        f'font-weight:700;text-transform:uppercase;letter-spacing:0.06em;'
        f'padding:2px 9px;border-radius:999px;margin-bottom:5px;'
        f'background:{badge_bg};color:{badge_color};border:1px solid {badge_bdr};">'
        f'{badge_text}</span>'

        # header row
        f'<div style="display:flex;justify-content:space-between;gap:1rem;align-items:flex-start;">'
        f'<div>'
        f'<div style="font-family:{_FONT};font-size:0.97rem;font-weight:700;color:{_TEXT1};">'
        f'{row["listing_id"]} &nbsp;&middot;&nbsp; {row["town"]}</div>'
        f'<div style="font-family:{_FONT};font-size:0.8rem;color:{_TEXT3};margin-top:3px;">'
        f'{row["flat_type"]} &nbsp;&middot;&nbsp; {row["floor_area_sqm"]} sqm'
        f' &nbsp;&middot;&nbsp; Storey {row["storey_range"]}</div>'
        f'</div>'
        f'<div style="text-align:right;white-space:nowrap;">'
        f'<div style="font-family:{_FONT};font-size:1.05rem;font-weight:800;color:{_TEXT1};">'
        f'{fmt_sgd(row["asking_price"])}</div>'
        f'<div style="font-family:{_FONT};font-size:0.76rem;color:{_TEXT3};margin-top:2px;">'
        f'Fair value: {fmt_sgd(row["predicted_price"])}</div>'
        f'</div>'
        f'</div>'

        # score pills
        + pill_row +

        # footer
        f'<div style="display:flex;align-items:center;justify-content:space-between;'
        f'flex-wrap:wrap;gap:6px;margin-top:4px;">'
        f'{tag}'
        f'<span style="font-family:{_FONT};font-size:0.78rem;color:{_TEXT3};">'
        f'{abs(diff):.1f}% {arrow} model estimate</span>'
        f'</div>'

        f'</div>'
    )


# ── no-match recovery UI ───────────────────────────────────────────────

def _chip(text: str, ok: bool) -> str:
    bg     = _GREEN_SOFT if ok else _RED_SOFT
    color  = "#166534"   if ok else _RED_TEXT
    border = _GREEN_BDR  if ok else _RED_BDR
    return (
        f'<span style="display:inline-block;font-family:{_FONT};font-size:0.74rem;'
        f'font-weight:700;padding:3px 10px;border-radius:999px;'
        f'background:{bg};border:1px solid {border};color:{color};">{text}</span>'
    )


def _recovery_card(label: str, value: str, hint: str) -> str:
    return (
        f'<div style="background:{_BG_SOFT};border:1px solid {_BORDER};'
        f'border-radius:{_RADIUS};padding:0.8rem 0.9rem;">'
        f'<div style="font-family:{_FONT};font-size:0.67rem;font-weight:700;'
        f'text-transform:uppercase;letter-spacing:0.06em;color:{_TEXT3};margin-bottom:4px;">{label}</div>'
        f'<div style="font-family:{_FONT};font-size:0.95rem;font-weight:800;'
        f'color:{_TEXT1};line-height:1.2;">{value}</div>'
        f'<div style="font-family:{_FONT};font-size:0.74rem;color:{_TEXT3};margin-top:3px;">{hint}</div>'
        f'</div>'
    )


def _render_no_match(inputs, bundle) -> None:
    report  = bundle.get("filter_report", {})
    budget  = inputs.budget
    pred    = bundle.get("predicted_price", 0)
    gap     = report.get("budget_gap", max(0, pred - budget))
    suggest = report.get("suggested_budget",
                         round((pred * 1.05) / 10_000) * 10_000)
    town    = inputs.town
    ftype   = inputs.flat_type
    area    = inputs.floor_area_sqm

    budget_ok = budget >= pred * 0.90
    area_tight = area > 80

    c_budget = _chip(
        f"Budget {fmt_sgd(budget)} — below median asking" if not budget_ok
        else f"Budget: {fmt_sgd(budget)}",
        budget_ok,
    )
    c_type = _chip(f"Flat type: {ftype}", True)
    c_area = _chip(
        f"Floor area &ge; {area:.0f} sqm — restrictive" if area_tight
        else f"Floor area &ge; {area:.0f} sqm",
        not area_tight,
    )
    c_town = _chip(f"Town: {town}" if town else "Recommendation mode", True)

    budget_hint = (
        f"Median asking for {ftype} is ~{fmt_sgd(pred)}. "
        f"Increase by ~{fmt_sgd(gap)} to unlock matches."
        if gap > 0
        else "Budget looks competitive — relax other filters."
    )
    town_hint = (
        f"Try nearby towns like Ang Mo Kio or Clementi." if town
        else "Recommendation mode will surface affordable towns."
    )
    area_hint = (
        "Reducing minimum area to &ge; 75 sqm could unlock listings."
        if area_tight
        else "Floor area looks reasonable — budget is the binding constraint."
    )

    rc1 = _recovery_card("Budget adjustment",  fmt_sgd(suggest),       budget_hint)
    rc2 = _recovery_card("Alternative towns",  "Explore nearby areas",  town_hint)
    rc3 = _recovery_card("Relax floor area",   "Try &ge; 75 sqm",       area_hint)

    html = (
        f'<div style="background:{_BG_WHITE};border:1.5px solid {_RED_BDR};'
        f'border-radius:{_RADIUS_LG};padding:1.2rem 1.3rem;'
        f'box-shadow:{_SHADOW_SM};margin-bottom:1rem;">'

        f'<div style="font-family:{_FONT};font-size:1rem;font-weight:800;'
        f'color:{_RED_TEXT};margin-bottom:4px;">No listings matched your filters</div>'
        f'<div style="font-family:{_FONT};font-size:0.84rem;color:{_TEXT2};'
        f'margin-bottom:0.9rem;">Your search returned 0 viable listings after hard filters. '
        f'Here&rsquo;s which constraints are binding and how to adjust.</div>'

        # constraint chips
        f'<div style="font-family:{_FONT};font-size:0.67rem;font-weight:700;'
        f'text-transform:uppercase;letter-spacing:0.07em;color:{_TEXT3};'
        f'margin-bottom:6px;">Constraint diagnosis</div>'
        f'<div style="display:flex;flex-wrap:wrap;gap:7px;margin-bottom:1rem;">'
        f'{c_budget}{c_type}{c_area}{c_town}'
        f'</div>'

        # recovery cards
        f'<div style="font-family:{_FONT};font-size:0.67rem;font-weight:700;'
        f'text-transform:uppercase;letter-spacing:0.07em;color:{_TEXT3};'
        f'margin-bottom:8px;">Recovery options</div>'
        f'<div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;">'
        f'{rc1}{rc2}{rc3}'
        f'</div>'

        f'</div>'
    )

    st.markdown(html, unsafe_allow_html=True)


# ── main tab renderer ──────────────────────────────────────────────────

def render_listing_tab(inputs, bundle) -> None:
    listings_df  = bundle.get("listings_df")
    rank_profile = bundle.get("ranking_profile", "balanced")
    alpha        = RANKING_ALPHA.get(rank_profile, 0.5)
    rank_label   = RANKING_LABELS.get(rank_profile, "Balanced")

    # no-match state
    if listings_df is None or listings_df.empty:
        _render_no_match(inputs, bundle)
        return

    # ensure scores present
    if "final_score" not in listings_df.columns:
        listings_df = compute_listing_scores(
            listings_df,
            budget=inputs.budget,
            amenity_weights=inputs.amenity_weights,
            ranking_profile=rank_profile,
        )

    top_n = min(5, len(listings_df))

    # section header
    rank_short = rank_label.split(" (")[0].strip()
    st.markdown(
        f'<div style="display:flex;justify-content:space-between;align-items:baseline;'
        f'margin-bottom:0.6rem;flex-wrap:wrap;gap:4px;">'
        f'<span style="font-family:{_FONT};font-size:1rem;font-weight:800;color:{_TEXT1};">'
        f'Top {top_n} ranked listings</span>'
        f'<span style="font-family:{_FONT};font-size:0.75rem;color:{_TEXT3};">'
        f'FinalScore = {round(alpha*100)}% amenity &middot; {round((1-alpha)*100)}% value'
        f' &nbsp;&middot;&nbsp; {rank_short}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # listing cards
    for rank_idx, (_, row) in enumerate(listings_df.head(top_n).iterrows()):
        is_top = rank_idx == 0
        st.markdown(_listing_card_html(row, rank_idx + 1, is_top), unsafe_allow_html=True)

        btn_cols = st.columns([1.5, 1.5, 5])
        user = st.session_state.get("current_user")
        btn_idx = 0
        if user:
            st.session_state.saved_flats.setdefault(user, [])
            with btn_cols[btn_idx]:
                if st.button("💾 Save", key=f"save_{row['listing_id']}"):
                    saved_ids = [f["listing_id"] for f in st.session_state.saved_flats[user]]
                    if row["listing_id"] not in saved_ids:
                        st.session_state.saved_flats[user].append({
                            "listing_id":     row["listing_id"],
                            "town":           row["town"],
                            "flat_type":      row["flat_type"],
                            "floor_area_sqm": row["floor_area_sqm"],
                            "storey_range":   row["storey_range"],
                            "asking_price":   row["asking_price"],
                            "predicted_price": row["predicted_price"],
                            "valuation_label": row["valuation_label"],
                            "final_score":    row.get("final_score"),
                        })
                        st.success(f"Saved {row['listing_id']} ✅")
                    else:
                        st.info(f"{row['listing_id']} already saved.")
            btn_idx += 1

        if "listing_url" in row and row["listing_url"]:
            with btn_cols[btn_idx]:
                st.link_button("View →", row["listing_url"])

    # comparison table
    st.markdown(
        f'<div style="font-family:{_FONT};font-size:0.68rem;font-weight:700;'
        f'text-transform:uppercase;letter-spacing:0.08em;color:{_TEXT3};'
        f'margin:1.1rem 0 0.5rem;">Full comparison table</div>',
        unsafe_allow_html=True,
    )

    disp = listings_df.copy()
    for col in ["asking_price", "predicted_price", "recent_median_transacted"]:
        if col in disp.columns:
            disp[col] = disp[col].map(fmt_sgd)
    if "asking_vs_predicted_pct" in disp.columns:
        disp["asking_vs_predicted_pct"] = disp["asking_vs_predicted_pct"].map(
            lambda x: f"{x:+.1f}%"
        )
    for sc in ["value_score", "amenity_score", "final_score", "overall_value_score"]:
        if sc in disp.columns:
            disp[sc] = disp[sc].map(lambda x: f"{x:.1f}")

    display_cols = [
        "listing_id", "town", "flat_type", "floor_area_sqm", "storey_range",
        "asking_price", "predicted_price", "asking_vs_predicted_pct",
        "valuation_label", "value_score", "amenity_score", "final_score",
    ]
    display_cols = [c for c in display_cols if c in disp.columns]
    st.dataframe(disp[display_cols], use_container_width=True, hide_index=True)
