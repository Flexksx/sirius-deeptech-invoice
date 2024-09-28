from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class InvoiceTerms(Base):
    __tablename__ = 'invoice_terms'
    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    terms_id = Column(Integer, ForeignKey('terms.id'))

    invoice = relationship('Invoice', back_populates='invoice_terms')
    terms = relationship('Terms', back_populates='invoice_terms')

    def __init__(self, invoice_id, terms_id):
        self.invoice_id = invoice_id
        self.terms_id = terms_id

    def __repr__(self):
        return f'<InvoiceTerms {self.id}>'
