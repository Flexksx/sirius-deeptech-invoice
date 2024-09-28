from typing import List
from backend.src.product.Product import Product
from src.contract.Contract import Contract
from InvoiceNote import InvoiceNote
from src.terms.Terms import Terms
from datetime import datetime


class InvoiceType:
    def __init__(self, id: str, name: str, contract_id: str, created_date: datetime, notes: List[InvoiceNote], data: dict, description: str) -> None:
        self.id = id
        self.name = name
        self.contract_id = contract_id
        self.created_date = created_date
        self.notes: List[InvoiceNote]
        self.data = data
        self.description = description
        self.terms = Terms()

        self.productsInvoices: List[Product] = []
        self.tems: List[Terms] = []

    def add_product(self, product: Product) -> None:
        self.productsInvoices.append(product)

    def add_term(self, term: Terms) -> None:
        self.terms.append(term)
