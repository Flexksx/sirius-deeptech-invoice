from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    invoice_number = Column(String)
    invoice_type_id = Column(Integer, ForeignKey('invoice_types.id'))
    created_date = Column(Time)
    due_date = Column(Time)
    invoice_date = Column(Time)

    invoice_type = relationship('InvoiceType', back_populates='invoice')
    invoice_products = relationship(
        'InvoiceProducts', back_populates='invoice')
    invoice_terms = relationship('InvoiceTerms', back_populates='invoice')
    invoice_runs = relationship('InvoiceRun', back_populates='invoice')

    def __init__(self, invoice_number, invoice_type_id, due_date, invoice_date):
        self.invoice_number = invoice_number
        self.invoice_type_id = invoice_type_id
        self.created_date = datetime.now()
        self.due_date = due_date
        self.invoice_date = invoice_date

    def __repr__(self):
        return f'<Invoice {self.id}>'
