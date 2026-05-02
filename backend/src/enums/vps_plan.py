"""VPS plan tiers."""
from enum import Enum


class VPSPlan(str, Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
