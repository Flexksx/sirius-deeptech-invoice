from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class DueInvoice(Base):
    __tablename__ = 'due_invoices'
    id = Column(Integer, primary_key=True)
    invoice_type_id = Column(Integer, ForeignKey('invoice_types.id'))
    invoice_number = Column(String, nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.now())
    due_date = Column(DateTime, nullable=False)
    description = Column(String, nullable=True)
    data = Column(JSON, nullable=True)

    invoice_type = relationship('InvoiceType', back_populates='due_invoices')

    run_records = relationship(
        'DueInvoiceRunRecord', back_populates='due_invoice')

    def __init__(self, invoice_type_id, invoice_number, created_date=None, due_date=None, description=None, data=None):
        if created_date is None:
            self.created_date = datetime.now()
        self.due_date = due_date
        self.invoice_type_id = invoice_type_id
        if not invoice_number:
            invoice_number = f'INV-{self.due_date.strftime("%Y%m%d")}'
        self.invoice_number = invoice_number
        self.description = description
        self.data = data
