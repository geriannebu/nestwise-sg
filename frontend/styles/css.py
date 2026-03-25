import streamlit as st


def inject_css():
    # Load DM Sans from Google Fonts — much cleaner than Inter at small sizes
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
            --font:          'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            --bg-page:       #f5f7fa;
            --bg-surface:    #ffffff;
            --bg-soft:       #f7f8fa;
            --border:        #e4e7ed;
            --border-mid:    #d0d5dd;
            --text-1:        #0f172a;
            --text-2:        #4b5563;
            --text-3:        #9ca3af;
            --mint:          #059E87;
            --mint-light:    #e6f7f4;
            --mint-border:   #a7e8dc;
            --green-soft:    #ecfdf3;
            --green-border:  #abefc6;
            --amber-soft:    #fffaeb;
            --amber-border:  #fedf89;
            --red-soft:      #fef3f2;
            --red-border:    #fda29b;
            --shadow:        0 1px 3px rgba(0,0,0,0.06), 0 4px 16px rgba(0,0,0,0.06);
            --shadow-sm:     0 1px 2px rgba(0,0,0,0.05);
            --radius:        14px;
            --radius-lg:     18px;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           GLOBAL RESET
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        /* Only hide the background and decoration, keep the interactive layer */
        [data-testid="stHeader"] {
            background: transparent !important;
        }

        /* Hide the specific decoration line at the top if you want it clean */
        [data-testid="stDecoration"] {
            display: none !important;
        }
        [data-testid="stAppViewContainer"] { background: var(--bg-page) !important; }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           SIDEBAR — target both old + new Streamlit
           selectors so it works on any version
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        /* ── NestWise Navigation Style ── */
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
            transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
            cursor: pointer !important;
            width: 100% !important;
        }

        /* Hover: Mint Nudge */
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label:hover {
            color: var(--mint) !important;
            background: rgba(5, 158, 135, 0.08) !important;
            border-left-color: rgba(5, 158, 135, 0.4) !important;
            padding-left: 1.5rem !important; /* Visual 'nudge' effect */
        }

        /* Active: Solid NestWise Mint */
        [data-testid="stSidebar"] .stRadio div[role="radiogroup"] > label[data-checked="true"] {
            color: var(--mint) !important;
            font-weight: 700 !important;
            border-left-color: var(--mint) !important;
            background: rgba(5, 158, 135, 0.12) !important;
        }

        /* Hide the radio dot */
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

        /* Scope DM Sans to content — never touch Streamlit chrome */
        .block-container,
        .block-container p,
        .block-container li,
        .block-container span:not([data-testid]),
        .block-container label {
            font-family: var(--font) !important;
        }

        /* Streamlit default headings inside content */
        .block-container h1 { font-size: 1.9rem !important; font-weight: 800 !important; letter-spacing: -0.03em !important; color: var(--text-1) !important; }
        .block-container h2 { font-size: 1.45rem !important; font-weight: 700 !important; letter-spacing: -0.02em !important; color: var(--text-1) !important; }
        .block-container h3 { font-size: 1.05rem !important; font-weight: 700 !important; color: var(--text-1) !important; }
        .block-container p  { font-size: 0.92rem !important; line-height: 1.65 !important; color: var(--text-2) !important; }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           SIDEBAR BRAND CLASSES
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-side-brand {
            font-family: var(--font);
            font-size: 1.15rem;
            font-weight: 800;
            color: var(--text-1);
            letter-spacing: -0.03em;
            margin-bottom: 0.15rem;
        }
        .nw-side-sub {
            font-family: var(--font);
            font-size: 0.78rem;
            color: var(--text-3);
            margin-bottom: 0.2rem;
        }
        .nw-side-chip {
            display: inline-block;
            padding: 0.35rem 0.65rem;
            border-radius: 999px;
            background: var(--green-soft);
            border: 1px solid var(--green-border);
            font-family: var(--font);
            font-size: 0.76rem;
            font-weight: 700;
            color: #166534;
        }
        .nw-side-chip.muted {
            background: var(--bg-soft);
            border: 1px solid var(--border);
            color: var(--text-3);
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           SECTION HEADERS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-section { padding: 0.5rem 0 0.2rem; }
        .nw-section-step {
            font-family: var(--font);
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            color: var(--mint);
        }
        .nw-section-title {
            font-family: var(--font);
            font-size: 1.5rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            color: var(--text-1);
            margin-top: 0.15rem;
        }
        .nw-section-subtitle {
            font-family: var(--font);
            font-size: 0.86rem;
            color: var(--text-3);
            margin-top: 0.25rem;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           CARDS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-profile, .nw-listing, .nw-reco, .nw-pick, .nw-method {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            margin-bottom: 0.85rem;
            box-shadow: var(--shadow);
        }
        .nw-profile, .nw-listing, .nw-reco, .nw-pick { padding: 1rem 1.1rem; }
        .nw-method {
            padding: 1rem 1.2rem;
            font-family: var(--font);
            font-size: 0.88rem;
            line-height: 1.72;
            color: var(--text-2);
        }
        .nw-method strong { color: var(--text-1); font-weight: 700; }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           METRICS
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
            font-size: 0.72rem !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.06em !important;
            color: var(--text-3) !important;
        }
        div[data-testid="metric-container"] [data-testid="stMetricValue"] {
            font-family: var(--font) !important;
            font-size: 1.6rem !important;
            font-weight: 800 !important;
            letter-spacing: -0.03em !important;
            color: var(--text-1) !important;
        }

        /* Custom Recent Search Card for Sidebar */
        .nw-recent-search {
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 0.85rem;
            margin: 1rem 0;
            box-shadow: var(--shadow-sm);
        }

        .nw-recent-label {
            display: block;
            font-size: 0.65rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--mint);
            margin-bottom: 0.25rem;
        }

        .nw-recent-value {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-1);
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           BUDGET BANNERS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-budget-ok, .nw-budget-warn, .nw-budget-over {
            font-family: var(--font);
            font-size: 0.88rem;
            font-weight: 600;
            padding: 0.85rem 1rem;
            border-radius: var(--radius);
            margin: 0.75rem 0 0.9rem;
            box-shadow: var(--shadow-sm);
        }
        .nw-budget-ok   { background: var(--green-soft); border: 1px solid var(--green-border); color: #166534; }
        .nw-budget-warn { background: var(--amber-soft); border: 1px solid var(--amber-border); color: #92400e; }
        .nw-budget-over { background: var(--red-soft);   border: 1px solid var(--red-border);   color: #991b1b; }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           PICK CARD
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-pick { display: flex; gap: 0.85rem; align-items: flex-start; }
        .nw-pick-icon { font-size: 1.4rem; line-height: 1; flex-shrink: 0; }
        .nw-pick-label {
            font-family: var(--font);
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            color: var(--text-3);
        }
        .nw-pick-value {
            font-family: var(--font);
            font-size: 1rem;
            font-weight: 800;
            color: var(--text-1);
            margin-top: 0.15rem;
            letter-spacing: -0.02em;
        }
        .nw-pick-sub {
            font-family: var(--font);
            font-size: 0.82rem;
            color: var(--text-2);
            margin-top: 0.25rem;
            line-height: 1.5;
        }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           LISTING / RECO CARDS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-listing-header, .nw-reco-header {
            display: flex;
            justify-content: space-between;
            gap: 1rem;
            align-items: flex-start;
        }
        .nw-listing-id, .nw-reco-name {
            font-family: var(--font);
            font-size: 0.95rem;
            font-weight: 700;
            color: var(--text-1);
        }
        .nw-listing-meta, .nw-reco-why {
            font-family: var(--font);
            font-size: 0.82rem;
            color: var(--text-3);
            margin-top: 0.18rem;
            line-height: 1.5;
        }
        .nw-listing-asking {
            font-family: var(--font);
            font-size: 1rem;
            font-weight: 800;
            text-align: right;
            color: var(--text-1);
        }
        .nw-listing-predicted {
            font-family: var(--font);
            font-size: 0.78rem;
            color: var(--text-3);
            text-align: right;
            margin-top: 0.1rem;
        }
        .nw-reco-score { font-weight: 800; color: var(--text-1); }
        .nw-reco-footer {
            margin-top: 0.65rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 0.6rem;
            flex-wrap: wrap;
        }
        .nw-reco-price { font-weight: 800; color: var(--text-1); font-size: 0.92rem; }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           TAGS
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        .nw-reco-within, .nw-reco-over, .nw-tag,
        .nw-tag-steal, .nw-tag-fair, .nw-tag-slight, .nw-tag-over {
            display: inline-block;
            font-family: var(--font);
            padding: 0.22rem 0.55rem;
            border-radius: 999px;
            font-size: 0.74rem;
            font-weight: 700;
        }
        .nw-reco-within, .nw-tag-fair { background: var(--green-soft); border: 1px solid var(--green-border); color: #166534; }
        .nw-reco-over,   .nw-tag-over { background: var(--red-soft);   border: 1px solid var(--red-border);   color: #991b1b; }
        .nw-tag-steal                  { background: var(--green-soft); border: 1px solid #6ce9a6;             color: #166534; }
        .nw-tag-slight                 { background: var(--amber-soft); border: 1px solid var(--amber-border); color: #92400e; }

        /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
           STREAMLIT WIDGETS — tighter, cleaner
        ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
        div[data-testid="stDataFrame"] {
            border-radius: var(--radius-lg);
            overflow: hidden;
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
        }

        /* 1. Base State for the Primary Button */
        button[data-testid="stBaseButton-primary"] {
            background: linear-gradient(135deg, #059E87 0%, #34d1b4 100%) !important;
            border: none !important;
            border-radius: 12px !important;
            padding: 0.6rem 2rem !important;
            transition: all 0.2s ease-in-out !important; /* Smooth transition for the hover effect */
        }

        /* 2. Base Text State */
        button[data-testid="stBaseButton-primary"] p {
            color: white !important;
            font-weight: 700 !important;
            font-family: var(--font) !important;
        }

        /* 3. Hover State for the Button (Glow & Lift) */
        button[data-testid="stBaseButton-primary"]:hover {
            transform: translateY(-2px) !important;
            box-shadow: 0 6px 20px rgba(5, 158, 135, 0.35) !important;
            filter: brightness(1.1) !important; /* Makes the gradient pop slightly more */
        }

        /* 4. Ensure Text stays white during Hover */
        button[data-testid="stBaseButton-primary"]:hover p {
            color: #ffffff !important;
        }

        /* Slider labels */
        .stSlider label p {
            font-family: var(--font) !important;
            font-size: 0.84rem !important;
            font-weight: 600 !important;
            color: var(--text-2) !important;
        }

        /* Select / input labels */
        .stSelectbox label p,
        .stNumberInput label p,
        .stTextInput label p {
            font-family: var(--font) !important;
            font-size: 0.84rem !important;
            font-weight: 600 !important;
            color: var(--text-2) !important;
        }

        /* Caption text */
        .stCaption p {
            font-family: var(--font) !important;
            font-size: 0.78rem !important;
            color: var(--text-3) !important;
        }

        /* st.info / st.warning / st.error */
        .stAlert {
            font-family: var(--font) !important;
            font-size: 0.86rem !important;
            border-radius: var(--radius) !important;
        }

        /* Tab bar */
        .stTabs [data-baseweb="tab"] {
            font-family: var(--font) !important;
            font-size: 0.86rem !important;
            font-weight: 600 !important;
        }

        @media (max-width: 900px) {
            .block-container { padding-left: 1rem !important; padding-right: 1rem !important; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
