from typing import Any, Dict

import pandas as pd
import pydeck as pdk
import streamlit as st

from backend.schemas.inputs import UserInputs
from backend.utils.constants import AMENITY_COLORS, AMENITY_LABELS


def top_priority_keys(weights: dict, top_n: int = 3):
    return [k for k, _ in sorted(weights.items(), key=lambda x: x[1], reverse=True)[:top_n]]


def render_map_tab(inputs: UserInputs, map_bundle: Dict[str,Any]):
    st.markdown("#### Interactive map")
    st.caption("Showing top-priority amenities, anchor postals, and selected / recommended towns.")

    top_am = top_priority_keys(inputs.amenity_weights, 3)
    visible = st.multiselect(
        "Amenity layers",
        options=list(AMENITY_LABELS.keys()),
        default=top_am,
        format_func=lambda k: AMENITY_LABELS[k],
    )

    town_pts   = map_bundle["town_points"]
    amenities  = map_bundle["amenities_df"]
    anchors    = map_bundle["anchor_points"]
    filtered   = amenities[amenities["amenity_type"].isin(visible)] if not amenities.empty else amenities

    layers = []
    if not town_pts.empty:
        layers += [
            pdk.Layer("ScatterplotLayer", data=town_pts, get_position="[lon, lat]",
                      get_fill_color=AMENITY_COLORS["town"], get_radius=1000, pickable=True),
            pdk.Layer("TextLayer", data=town_pts, get_position="[lon, lat]",
                      get_text="town", get_size=16, get_color=[0,0,0,200], get_alignment_baseline="bottom"),
        ]
    if anchors:
        adf = pd.DataFrame(anchors)
        layers += [
            pdk.Layer("ScatterplotLayer", data=adf, get_position="[lon, lat]",
                      get_fill_color=AMENITY_COLORS["anchor"], get_radius=600, pickable=True),
            pdk.Layer("TextLayer", data=adf, get_position="[lon, lat]",
                      get_text="label", get_size=14, get_color=[90,0,90,220], get_alignment_baseline="bottom"),
        ]
    for k in visible:
        sub = filtered[filtered["amenity_type"]==k] if not filtered.empty else pd.DataFrame()
        if sub.empty: continue
        layers.append(pdk.Layer("ScatterplotLayer", data=sub, get_position="[lon, lat]",
                                get_fill_color=AMENITY_COLORS[k], get_radius=260, pickable=True))

    deck = pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state=pdk.ViewState(
            latitude=map_bundle["center_lat"],
            longitude=map_bundle["center_lon"],
            zoom=11.2, pitch=0,
        ),
        layers=layers,
        tooltip={"html":"<b>{town}</b><br/>{amenity_label}<br/>{postal_code}",
                 "style":{"backgroundColor":"white","color":"black"}},
    )
    st.pydeck_chart(deck, use_container_width=True)

    ml, mr = st.columns(2)
    with ml:
        st.markdown("**Anchor points**")
        st.dataframe(pd.DataFrame(anchors) if anchors else pd.DataFrame({"status":["None entered"]}),
                     use_container_width=True, hide_index=True)
    with mr:
        st.markdown("**Towns displayed**")
        st.dataframe(town_pts if not town_pts.empty else pd.DataFrame({"status":["None"]}),
                     use_container_width=True, hide_index=True)
        
