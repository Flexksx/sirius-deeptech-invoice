from enum import Enum

class TermType(Enum):
    PAYMENT = "Payment"
    DELIVERY = "Delivery"
    SERVICE = "Service"
    WARRANTY = "Warranty"
    LIABILITY = "Liability"
    CONFIDENTIALITY = "Confidentiality"
    CANCELLATION = "Cancellation"
    RETURNS = "Returns"
    FORCE_MAJEURE = "Force Majeure"
    INDEMNITY = "Indemnity"
    ARBITRATION = "Arbitration"
    TERMINATION = "Termination"
