from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class UserInputs:
    budget: int
    flat_type: str
    floor_area_sqm: float
    lease_commence_year: int
    town: Optional[str]
    school_scope: str
    amenity_weights: Dict[str, float]
    landmark_postals: List[str]