from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class DueInvoice(Base):
    __tablename__ = 'due_invoices'
    id = Column(Integer, primary_key=True)
    invoice_type_id = Column(Integer, ForeignKey('invoice_types.id'))
    invoice_number = Column(String)
    created_date = Column(Time)
    due_date = Column(Time)
    description = Column(String, nullable=True)
    data = Column(JSON, nullable=True)

    invoice_type = relationship('InvoiceType', back_populates='due_invoices')

    run_records = relationship(
        'DueInvoiceRunRecord', back_populates='due_invoice')

    def __init__(self, invoice_type_id, invoice_number, created_date=None, due_date=None, description=None, data=None):
        if created_date is None:
            self.created_date = datetime.now()
        self.invoice_type_id = invoice_type_id
        self.invoice_number = invoice_number
        self.due_date = due_date
        self.description = description
        self.data = data
