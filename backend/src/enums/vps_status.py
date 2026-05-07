"""VPS lifecycle statuses."""
from enum import StrEnum


class VPSStatus(StrEnum):
    PROVISIONING = "provisioning"
    RUNNING = "running"
    STOPPED = "stopped"
    DELETING = "deleting"
    ERROR = "error"
