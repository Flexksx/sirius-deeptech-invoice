# model/CompanyType.py
from enum import Enum

class CompanyType(Enum):
    PRIVATE = "Private"
    PUBLIC = "Public"
    NON_PROFIT = "Non-Profit"
    GOVERNMENT = "Government"
    OTHER = "Other"
