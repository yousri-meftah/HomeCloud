"""VPS lifecycle statuses."""
from enum import Enum


class VPSStatus(str, Enum):
    PROVISIONING = "provisioning"
    RUNNING = "running"
    STOPPED = "stopped"
    DELETING = "deleting"
    ERROR = "error"
