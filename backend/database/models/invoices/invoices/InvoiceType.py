from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
from .enums import InvoiceTypeFrequency


class InvoiceType(Base):
    __tablename__ = 'invoice_types'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    created_date = Column(DateTime, default=datetime.now)
    notes = Column(String, nullable=True)
    data = Column(JSON, nullable=True)
    description = Column(String, nullable=True)

    frequency = Column(Enum(InvoiceTypeFrequency),
                       nullable=False, default=InvoiceTypeFrequency.ONCE)
    invoices_count = Column(Integer, nullable=False, default=1)
    needed_starting_date = Column(DateTime, nullable=True)
    contract_id = Column(Integer, ForeignKey('contracts.id'))

    # Relationship to Product (one-to-many)
    products = relationship('Product', back_populates='invoice_type')

    contract = relationship('Contract', back_populates='invoice_types')
    due_invoices = relationship('DueInvoice', back_populates='invoice_type')

    def __init__(self, name, contract_id: int = None, notes=None, data=None, description=None, frequency=InvoiceTypeFrequency.ONCE, invoices_count=1, needed_starting_date=None):
        self.name = name
        self.contract_id = contract_id
        self.created_date = datetime.now()
        self.notes = notes
        self.data = data
        self.description = description
        self.frequency = frequency
        self.invoices_count = invoices_count
        self.needed_starting_date = needed_starting_date

    def __repr__(self):
        return f'<InvoiceType {self.id}>'
