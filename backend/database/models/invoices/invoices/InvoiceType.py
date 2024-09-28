from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class InvoiceType(Base):
    __tablename__ = 'invoice_types'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contract_id = Column(Integer, ForeignKey('contracts.id'))
    created_date = Column(DateTime, default=datetime.now)
    notes = Column(String)
    data = Column(JSON)
    description = Column(String)

    contract = relationship('Contract', back_populates='invoice_types')
    due_invoices = relationship('DueInvoice', back_populates='invoice_type')
    products = relationship('Product', secondary='invoice_type_products')

    def __init__(self, name, contract_id, notes, data, description):
        self.name = name
        self.contract_id = contract_id
        self.created_date = datetime.now()
        self.notes = notes
        self.data = data
        self.description = description

    def __repr__(self):
        return f'<InvoiceType {self.id}>'
