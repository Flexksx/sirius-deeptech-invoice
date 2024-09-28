from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class InvoiceType(Base):
    __tablename__ = 'invoice_types'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    contract_id = Column(Integer, ForeignKey('contracts.id'))
    created_date = Column(Time)
    notes = Column(String)
    data = Column(JSON)
    description = Column(String)

    contract = relationship('Contract', back_populates='invoice_types')
    invoices = relationship('Invoice', back_populates='invoices')
    invoice_products = relationship(
        'InvoiceProduct', back_populates='invoice_type')
    invoice_runners = relationship(
        'InvoiceRunner', back_populates='invoice_type')
    terms = relationship('Terms', back_populates='terms')
    invoice = relationship('Invoice', back_populates='invoice_type')

    def __init__(self, name, contract_id, notes, data, description):
        self.name = name
        self.contract_id = contract_id
        self.created_date = datetime.now()
        self.notes = notes
        self.data = data
        self.description = description

    def __repr__(self):
        return f'<InvoiceType {self.id}>'
