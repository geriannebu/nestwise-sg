import streamlit as st


def inject_css():
    # DM Sans — clean fintech feel
    st.markdown(
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;0,9..40,800&display=swap" rel="stylesheet">',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <style>
        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           DESIGN TOKENS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        :root {
            --font:           'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;

            /* surfaces */
            --bg-page:        #f5f7fa;
            --bg-surface:     #ffffff;
            --bg-soft:        #f7f8fa;

            /* borders */
            --border:         #e4e7ed;
            --border-mid:     #d0d5dd;

            /* text */
            --text-1:         #0f172a;
            --text-2:         #4b5563;
            --text-3:         #9ca3af;

            /* brand */
            --mint:           #059E87;
            --mint-dark:      #037a68;
            --mint-light:     #e6f7f4;
            --mint-border:    #a7e8dc;

            /* semantic palettes */
            --green-soft:     #ecfdf3;
            --green-border:   #abefc6;
            --amber-soft:     #fffaeb;
            --amber-border:   #fedf89;
            --amber-text:     #92400e;
            --red-soft:       #fef3f2;
            --red-border:     #fda29b;
            --red-text:       #991b1b;

            /* elevation */
            --shadow:         0 1px 3px rgba(0,0,0,0.06), 0 4px 16px rgba(0,0,0,0.06);
            --shadow-sm:      0 1px 2px rgba(0,0,0,0.05);
            --shadow-card:    0 2px 8px rgba(0,0,0,0.07);

            /* geometry */
            --radius:         14px;
            --radius-lg:      18px;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           GLOBAL RESET
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        [data-testid="stHeader"]      { background: transparent !important; }
        [data-testid="stDecoration"]  { display: none !important; }
        [data-testid="stAppViewContainer"] { background: var(--bg-page) !important; }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           SIDEBAR
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
            gap: 6px !important;
            padding: 1rem 0 !important;
        }
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label {
            font-family: var(--font) !important;
            font-size: 0.9rem !important;
            font-weight: 500 !important;
            color: var(--text-2) !important;
            background: transparent !important;
            border: none !important;
            border-left: 4px solid transparent !important;
            border-radius: 0 10px 10px 0 !important;
            padding: 0.41rem 1.67rem !important;
            margin: 0.1rem 0 !important;
            transition: all 0.25s cubic-bezier(0.4,0,0.2,1) !important;
            cursor: pointer !important;
            width: 100% !important;
        }
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label:hover {
            color: var(--mint) !important;
            background: rgba(5,158,135,0.08) !important;
            border-left-color: rgba(5,158,135,0.4) !important;
            padding-left: 1.5rem !important;
        }
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label[data-checked="true"] {
            color: var(--mint) !important;
            font-weight: 700 !important;
            border-left-color: var(--mint) !important;
            background: rgba(5,158,135,0.12) !important;
        }
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label > div:first-child {
            display: none !important;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           MAIN CONTENT AREA
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .block-container {
            max-width: 1200px !important;
            padding-top: 1.2rem !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
            padding-bottom: 2rem !important;
            font-family: var(--font) !important;
            font-size: 0.95rem !important;
            color: var(--text-1) !important;
        }
        .block-container,
        .block-container p,
        .block-container li,
        .block-container span:not([data-testid]),
        .block-container label {
            font-family: var(--font) !important;
        }
        .block-container h1 { font-size:1.9rem !important; font-weight:800 !important; letter-spacing:-0.03em !important; color:var(--text-1) !important; }
        .block-container h2 { font-size:1.45rem !important; font-weight:700 !important; letter-spacing:-0.02em !important; color:var(--text-1) !important; }
        .block-container h3 { font-size:1.05rem !important; font-weight:700 !important; color:var(--text-1) !important; }
        .block-container p  { font-size:0.92rem !important; line-height:1.65 !important; color:var(--text-2) !important; }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           SIDEBAR BRAND
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-side-brand {
            font-family: var(--font); font-size:1.15rem; font-weight:800;
            color:var(--text-1); letter-spacing:-0.03em; margin-bottom:0.15rem;
        }
        .nw-side-sub {
            font-family: var(--font); font-size:0.78rem;
            color:var(--text-3); margin-bottom:0.2rem;
        }
        .nw-side-chip {
            display:inline-block; padding:0.35rem 0.65rem; border-radius:999px;
            background:var(--green-soft); border:1px solid var(--green-border);
            font-family:var(--font); font-size:0.76rem; font-weight:700; color:#166534;
        }
        .nw-side-chip.muted {
            background:var(--bg-soft); border:1px solid var(--border); color:var(--text-3);
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           SECTION HEADERS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-section { padding:0.5rem 0 0.2rem; }
        .nw-section-step {
            font-family:var(--font); font-size:0.72rem; font-weight:700;
            text-transform:uppercase; letter-spacing:0.08em; color:var(--mint);
        }
        .nw-section-title {
            font-family:var(--font); font-size:1.5rem; font-weight:800;
            letter-spacing:-0.03em; color:var(--text-1); margin-top:0.15rem;
        }
        .nw-section-subtitle {
            font-family:var(--font); font-size:0.86rem;
            color:var(--text-3); margin-top:0.25rem;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           PIPELINE STRIP
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-pipeline {
            display: flex;
            align-items: center;
            gap: 0;
            font-family: var(--font);
            font-size: 0.72rem;
            font-weight: 600;
            margin-bottom: 1rem;
            flex-wrap: wrap;
        }
        .nw-pip-step {
            padding: 5px 13px;
            background: var(--bg-soft);
            border: 1px solid var(--border);
            color: var(--text-3);
            white-space: nowrap;
        }
        .nw-pip-step:first-child { border-radius: var(--radius) 0 0 var(--radius); }
        .nw-pip-step:last-child  { border-radius: 0 var(--radius) var(--radius) 0; }
        .nw-pip-step.active {
            background: var(--mint-light);
            color: var(--mint-dark);
            border-color: var(--mint-border);
        }
        .nw-pip-arrow {
            font-size: 0.65rem;
            color: var(--border-mid);
            padding: 0 1px;
            background: var(--bg-soft);
            border-top: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
            line-height: 1;
            padding-top: 6px;
            padding-bottom: 6px;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           RESULTS SUMMARY BAND
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-results-band {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 1.1rem 1.3rem 1rem;
            box-shadow: var(--shadow-card);
            margin-bottom: 1rem;
        }
        .nw-band-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-bottom: 0.85rem;
        }
        .nw-band-title {
            font-family: var(--font);
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            color: var(--text-3);
        }
        .nw-badge-row {
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }
        .nw-badge {
            display: inline-block;
            font-family: var(--font);
            font-size: 0.72rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 999px;
        }
        .nw-badge-mode  { background:var(--mint-light); color:var(--mint-dark); border:1px solid var(--mint-border); }
        .nw-badge-rank  { background:var(--amber-soft);  color:var(--amber-text); border:1px solid var(--amber-border); }
        .nw-metrics-grid {
            display: grid;
            grid-template-columns: repeat(5, minmax(0,1fr));
            gap: 8px;
            margin-bottom: 0.8rem;
        }
        .nw-metric {
            background: var(--bg-soft);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 0.7rem 0.85rem;
        }
        .nw-metric-label {
            font-family: var(--font);
            font-size: 0.68rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            color: var(--text-3);
            margin-bottom: 4px;
        }
        .nw-metric-value {
            font-family: var(--font);
            font-size: 1.05rem;
            font-weight: 800;
            letter-spacing: -0.025em;
            color: var(--text-1);
            line-height: 1.15;
        }
        .nw-metric-sub {
            font-family: var(--font);
            font-size: 0.68rem;
            color: var(--text-3);
            margin-top: 2px;
        }
        .nw-metric.highlight .nw-metric-value { color: var(--mint); }
        .nw-metric.warn      .nw-metric-value { color: var(--red-text); }
        .nw-why-box {
            background: var(--mint-light);
            border-left: 3px solid var(--mint-border);
            border-radius: 0 var(--radius) var(--radius) 0;
            padding: 0.55rem 0.9rem;
            font-family: var(--font);
            font-size: 0.8rem;
            color: var(--mint-dark);
            line-height: 1.55;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           LISTING CARDS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-listing-card {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 1rem 1.1rem;
            margin-bottom: 0.7rem;
            box-shadow: var(--shadow-sm);
            transition: box-shadow 0.18s ease;
        }
        .nw-listing-card:hover { box-shadow: var(--shadow-card); }
        .nw-listing-card.top-pick {
            border-color: var(--mint-border);
            border-width: 1.5px;
            box-shadow: 0 0 0 3px rgba(5,158,135,0.06), var(--shadow-sm);
        }
        .nw-listing-rank-badge {
            display: inline-block;
            font-family: var(--font);
            font-size: 0.68rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            padding: 2px 9px;
            border-radius: 999px;
            margin-bottom: 5px;
        }
        .nw-listing-rank-badge.pick {
            background: var(--mint-light); color: var(--mint-dark);
            border: 1px solid var(--mint-border);
        }
        .nw-listing-rank-badge.rank {
            background: var(--bg-soft); color: var(--text-3);
            border: 1px solid var(--border);
        }
        .nw-listing-header {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            align-items: flex-start;
        }
        .nw-listing-id {
            font-family: var(--font); font-size:0.97rem;
            font-weight:700; color:var(--text-1);
        }
        .nw-listing-meta {
            font-family: var(--font); font-size:0.8rem;
            color:var(--text-3); margin-top:0.18rem; line-height:1.4;
        }
        .nw-listing-asking {
            font-family: var(--font); font-size:1.05rem;
            font-weight:800; text-align:right; color:var(--text-1);
        }
        .nw-listing-predicted {
            font-family: var(--font); font-size:0.76rem;
            color:var(--text-3); text-align:right; margin-top:0.1rem;
        }

        /* score bar row */
        .nw-scores-row {
            display: grid;
            grid-template-columns: repeat(3, minmax(0,1fr));
            gap: 7px;
            margin: 0.65rem 0 0.5rem;
        }
        .nw-score-pill {
            background: var(--bg-soft);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 7px 10px 8px;
        }
        .nw-score-label {
            font-family: var(--font); font-size:0.66rem;
            font-weight:700; text-transform:uppercase;
            letter-spacing:0.06em; color:var(--text-3); margin-bottom:3px;
        }
        .nw-score-val {
            font-family: var(--font); font-size:0.95rem;
            font-weight:800; color:var(--text-1); line-height:1;
        }
        .nw-score-val.highlight { color: var(--mint); }
        .nw-score-bar-bg {
            height: 3px; background: var(--border);
            border-radius: 2px; margin-top: 5px; overflow:hidden;
        }
        .nw-score-bar-fill {
            height: 3px; background: var(--mint); border-radius: 2px;
        }

        .nw-listing-footer {
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 0.4rem;
            margin-top: 0.2rem;
        }
        .nw-listing-diff {
            font-family: var(--font); font-size:0.78rem; color:var(--text-3);
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           GENERAL CARDS (profile, method, reco)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-profile, .nw-listing, .nw-reco, .nw-pick, .nw-method {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            margin-bottom: 0.85rem;
            box-shadow: var(--shadow);
        }
        .nw-profile, .nw-listing, .nw-reco, .nw-pick { padding:1rem 1.1rem; }
        .nw-method {
            padding:1rem 1.2rem;
            font-family: var(--font); font-size:0.88rem;
            line-height:1.72; color:var(--text-2);
        }
        .nw-method strong { color:var(--text-1); font-weight:700; }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           METRICS (st.metric)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        div[data-testid="metric-container"] {
            background: var(--bg-surface) !important;
            border: 1px solid var(--border) !important;
            border-radius: var(--radius-lg) !important;
            padding: 0.85rem 1rem !important;
            box-shadow: var(--shadow) !important;
        }
        div[data-testid="metric-container"] label {
            font-family: var(--font) !important;
            font-size: 0.72rem !important; font-weight:700 !important;
            text-transform:uppercase !important; letter-spacing:0.06em !important;
            color:var(--text-3) !important;
        }
        div[data-testid="metric-container"] [data-testid="stMetricValue"] {
            font-family: var(--font) !important;
            font-size:1.6rem !important; font-weight:800 !important;
            letter-spacing:-0.03em !important; color:var(--text-1) !important;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           SIDEBAR RECENT SEARCH CARD
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-recent-search {
            background: var(--bg-surface); border:1px solid var(--border);
            border-radius: var(--radius); padding:0.85rem;
            margin:1rem 0; box-shadow:var(--shadow-sm);
        }
        .nw-recent-label {
            display:block; font-size:0.65rem; font-weight:800;
            text-transform:uppercase; letter-spacing:0.05em;
            color:var(--mint); margin-bottom:0.25rem;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           BUDGET BANNERS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-budget-ok, .nw-budget-warn, .nw-budget-over {
            font-family:var(--font); font-size:0.88rem; font-weight:600;
            padding:0.85rem 1rem; border-radius:var(--radius);
            margin:0.75rem 0 0.9rem; box-shadow:var(--shadow-sm);
        }
        .nw-budget-ok   { background:var(--green-soft); border:1px solid var(--green-border); color:#166534; }
        .nw-budget-warn { background:var(--amber-soft);  border:1px solid var(--amber-border); color:var(--amber-text); }
        .nw-budget-over { background:var(--red-soft);    border:1px solid var(--red-border);   color:var(--red-text); }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           PICK CARD (no longer used on main page;
           kept for comparison tool compat)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-pick { display:flex; gap:0.85rem; align-items:flex-start; }
        .nw-pick-icon  { font-size:1.4rem; line-height:1; flex-shrink:0; }
        .nw-pick-label {
            font-family:var(--font); font-size:0.7rem; font-weight:700;
            text-transform:uppercase; letter-spacing:0.07em; color:var(--text-3);
        }
        .nw-pick-value {
            font-family:var(--font); font-size:1rem; font-weight:800;
            color:var(--text-1); margin-top:0.15rem; letter-spacing:-0.02em;
        }
        .nw-pick-sub {
            font-family:var(--font); font-size:0.82rem;
            color:var(--text-2); margin-top:0.25rem; line-height:1.5;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           TOWN / RECO CARDS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-reco-header { display:flex; justify-content:space-between; gap:1rem; align-items:flex-start; }
        .nw-reco-name   { font-family:var(--font); font-size:0.95rem; font-weight:700; color:var(--text-1); }
        .nw-reco-why    { font-family:var(--font); font-size:0.8rem; color:var(--text-3); margin-top:0.18rem; line-height:1.5; }
        .nw-reco-score  { font-weight:800; color:var(--text-1); }
        .nw-reco-footer {
            margin-top:0.65rem; display:flex;
            justify-content:space-between; align-items:center;
            gap:0.6rem; flex-wrap:wrap;
        }
        .nw-reco-price  { font-weight:800; color:var(--text-1); font-size:0.92rem; }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           TAGS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-reco-within, .nw-reco-over, .nw-tag,
        .nw-tag-steal, .nw-tag-fair, .nw-tag-slight, .nw-tag-over {
            display:inline-block; font-family:var(--font);
            padding:0.22rem 0.55rem; border-radius:999px;
            font-size:0.74rem; font-weight:700;
        }
        .nw-reco-within, .nw-tag-fair  { background:var(--green-soft); border:1px solid var(--green-border); color:#166534; }
        .nw-reco-over,   .nw-tag-over  { background:var(--red-soft);   border:1px solid var(--red-border);   color:var(--red-text); }
        .nw-tag-steal                   { background:var(--green-soft); border:1px solid #6ce9a6;             color:#166534; }
        .nw-tag-slight                  { background:var(--amber-soft); border:1px solid var(--amber-border); color:var(--amber-text); }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           NO-MATCH RECOVERY UI
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-no-match {
            background: var(--bg-surface);
            border: 1.5px solid var(--red-border);
            border-radius: var(--radius-lg);
            padding: 1.2rem 1.3rem;
            box-shadow: var(--shadow-sm);
            margin-bottom: 1rem;
        }
        .nw-no-match-title {
            font-family: var(--font); font-size:1rem;
            font-weight:800; color:var(--red-text); margin-bottom:4px;
        }
        .nw-no-match-sub {
            font-family: var(--font); font-size:0.84rem;
            color:var(--text-2); margin-bottom:0.9rem;
        }
        .nw-constraint-row { display:flex; flex-wrap:wrap; gap:7px; margin-bottom:1rem; }
        .nw-chip-fail {
            display:inline-block; font-family:var(--font);
            font-size:0.74rem; font-weight:700;
            padding:3px 10px; border-radius:999px;
            background:var(--red-soft); border:1px solid var(--red-border);
            color:var(--red-text);
        }
        .nw-chip-ok {
            display:inline-block; font-family:var(--font);
            font-size:0.74rem; font-weight:700;
            padding:3px 10px; border-radius:999px;
            background:var(--green-soft); border:1px solid var(--green-border);
            color:#166534;
        }
        .nw-recovery-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0,1fr));
            gap: 10px;
        }
        .nw-recovery-card {
            background: var(--bg-soft);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 0.8rem 0.9rem;
        }
        .nw-recovery-label {
            font-family:var(--font); font-size:0.68rem; font-weight:700;
            text-transform:uppercase; letter-spacing:0.06em;
            color:var(--text-3); margin-bottom:4px;
        }
        .nw-recovery-val {
            font-family:var(--font); font-size:0.95rem;
            font-weight:800; color:var(--text-1); line-height:1.2;
        }
        .nw-recovery-hint {
            font-family:var(--font); font-size:0.74rem;
            color:var(--text-3); margin-top:3px;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           SCENARIO COMPARE CARDS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-scenario-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            margin: 0.75rem 0 0.6rem;
        }
        .nw-scenario-col {
            background: var(--bg-soft);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 0.85rem 1rem;
        }
        .nw-scenario-col.changed {
            border-color: var(--mint-border);
            background: var(--mint-light);
        }
        .nw-scenario-col-label {
            font-family:var(--font); font-size:0.68rem; font-weight:700;
            text-transform:uppercase; letter-spacing:0.06em;
            color:var(--text-3); margin-bottom:5px;
        }
        .nw-scenario-col.changed .nw-scenario-col-label { color:var(--mint-dark); }
        .nw-scenario-price {
            font-family:var(--font); font-size:1.3rem;
            font-weight:800; color:var(--text-1); letter-spacing:-0.025em;
        }
        .nw-scenario-delta {
            font-family:var(--font); font-size:0.8rem;
            font-weight:600; margin-top:3px;
        }
        .nw-delta-up   { color:var(--red-text); }
        .nw-delta-down { color:#166534; }
        .nw-delta-none { color:var(--text-3); }
        .nw-scenario-insight {
            background:var(--bg-soft); border:1px solid var(--border);
            border-radius:var(--radius); padding:0.6rem 0.85rem;
            font-family:var(--font); font-size:0.81rem;
            color:var(--text-2); line-height:1.55; margin-top:0.6rem;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           DATAFRAME
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        div[data-testid="stDataFrame"] {
            border-radius: var(--radius-lg); overflow:hidden;
            border:1px solid var(--border); box-shadow:var(--shadow);
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           PRIMARY BUTTON
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        button[data-testid="stBaseButton-primary"] {
            background: linear-gradient(135deg,#059E87 0%,#34d1b4 100%) !important;
            border:none !important; border-radius:12px !important;
            padding:0.6rem 2rem !important;
            transition:all 0.2s ease-in-out !important;
        }
        button[data-testid="stBaseButton-primary"] p { color:white !important; font-weight:700 !important; font-family:var(--font) !important; }
        button[data-testid="stBaseButton-primary"]:hover {
            transform:translateY(-2px) !important;
            box-shadow:0 6px 20px rgba(5,158,135,0.35) !important;
            filter:brightness(1.1) !important;
        }
        button[data-testid="stBaseButton-primary"]:hover p { color:#ffffff !important; }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           FORM WIDGETS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .stSlider label p,
        .stSelectbox label p,
        .stNumberInput label p,
        .stTextInput label p {
            font-family:var(--font) !important; font-size:0.84rem !important;
            font-weight:600 !important; color:var(--text-2) !important;
        }
        .stCaption p { font-family:var(--font) !important; font-size:0.78rem !important; color:var(--text-3) !important; }
        .stAlert     { font-family:var(--font) !important; font-size:0.86rem !important; border-radius:var(--radius) !important; }
        .stTabs [data-baseweb="tab"] {
            font-family:var(--font) !important; font-size:0.86rem !important; font-weight:600 !important;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           SECTION DIVIDERS (inline label style)
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-sub-section-label {
            font-family: var(--font);
            font-size: 0.68rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--text-3);
            margin: 1.1rem 0 0.5rem;
        }

        @media (max-width: 900px) {
            .block-container { padding-left:1rem !important; padding-right:1rem !important; }
            .nw-metrics-grid { grid-template-columns: repeat(3,minmax(0,1fr)); }
            .nw-recovery-grid { grid-template-columns: 1fr 1fr; }
            .nw-scenario-grid { grid-template-columns: 1fr; }
        }
        @media (max-width: 600px) {
            .nw-metrics-grid  { grid-template-columns: 1fr 1fr; }
            .nw-recovery-grid { grid-template-columns: 1fr; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
