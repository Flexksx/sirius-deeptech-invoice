from ..contract.Contract import Contract
from InvoiceNote import InvoiceNote
from ..terms.Terms import Terms
from datetime import datetime


class InvoiceType:
    def __init__(self, id: str, name: str, contract_id: str, created_date: datetime, notes: list[InvoiceNote], data: dict, description: str) -> None:
        self.id = id
        self.name = name
        self.contract_id = contract_id
        self.created_date = created_date
        self.notes = notes
        self.data = data
        self.description = description
        self.contract = Contract()
        self.terms = Terms()
