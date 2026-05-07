"""VPS plan tiers."""
from enum import StrEnum


class VPSPlan(StrEnum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
