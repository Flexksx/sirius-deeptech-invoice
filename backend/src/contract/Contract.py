from datetime import datetime
from typing import List

from backend.src.invoice.InvoiceType import InvoiceType
from ....backend.database.src.Database import Database


class Contract:
    def __init__(self, id: str = None, created_date: datetime = None, updated_date: datetime = None,
                 obligor_client_id: str = None, obligatee_client_id: str = None, text: str = None, face_value: int = None):
        self.id = id
        self.created_date = created_date
        self.updated_date = updated_date
        self.obligor_client_id = obligor_client_id
        self.obligatee_client_id = obligatee_client_id
        self.text = text
        self.face_value = face_value

        self.invoice_types: List[InvoiceType] = []

        if id is not None:
            self.__from_db(id)

    def add_invoice_type(self, invoice_type: InvoiceType) -> None:
        self.invoice_types.append(invoice_type)

    def __repr__(self) -> str:
        return (f"Contract(id={self.id}, created_date={self.created_date}, updated_date={self.updated_date}, "
                f"obligor_client_id={self.obligor_client_id}, obligatee_client_id={
                    self.obligatee_client_id}, "
                f"text='{self.text}', face_value={self.face_value})")
