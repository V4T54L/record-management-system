"""Defines useful enums
"""

from enum import Enum


class ProductStatus(Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"
    INACTIVE = "inactive"


class ValidationStatus(Enum):
    SUCCESS = 1
    FAILURE = 2


class InventoryStatus(Enum):
    SUCCESS = 1
    FAILED = 2
    INVALID_DATA = 3
