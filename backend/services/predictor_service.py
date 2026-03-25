import numpy as np

from backend.services.listings_service import mock_active_listings
from backend.services.recommendation_service import mock_recommend_towns
from backend.schemas.inputs import UserInputs


def mock_predict_price(inputs: UserInputs) -> float:
    base = {
        "2 ROOM": 320000,
        "3 ROOM": 410000,
        "4 ROOM": 560000,
        "5 ROOM": 700000,
        "EXECUTIVE": 850000,
    }

    mul = 1.0
    if inputs.town in {"Bishan", "Queenstown", "Bukit Merah", "Kallang/Whampoa", "Toa Payoh"}:
        mul = 1.18
    elif inputs.town in {"Yishun", "Woodlands", "Jurong West", "Choa Chu Kang", "Sembawang"}:
        mul = 0.92

    pred = (
        base[inputs.flat_type] * mul
        + max(0, (inputs.floor_area_sqm - 70) * 3800)
        - max(0, (2026 - inputs.lease_commence_year) * 2500)
        + 70000 * sum(inputs.amenity_weights.values()) / len(inputs.amenity_weights)
        + min(len(inputs.landmark_postals), 2) * 15000
    )
    return max(pred, 180000)


def mock_recent_transaction_median(inputs: UserInputs) -> float:
    return mock_predict_price(inputs) * np.random.uniform(0.95, 1.05)


def get_prediction_bundle(inputs: UserInputs):
    predicted_price = round(mock_predict_price(inputs))
    recent_median_transacted = round(mock_recent_transaction_median(inputs))
    listings_df = mock_active_listings(inputs)
    recommendations_df = mock_recommend_towns(inputs) if not inputs.town else None

    return {
        "predicted_price": predicted_price,
        "recent_median_transacted": recent_median_transacted,
        "confidence_low": round(predicted_price * 0.96),
        "confidence_high": round(predicted_price * 1.04),
        "recent_period": "last 6 months",
        "listings_df": listings_df,
        "recommendations_df": recommendations_df,
    }