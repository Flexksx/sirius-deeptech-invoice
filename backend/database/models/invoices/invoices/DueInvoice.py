from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
from .enums import DueInvoicePeriod


class DueInvoice(Base):
    __tablename__ = 'due_invoices'
    id = Column(Integer, primary_key=True)
    invoice_type_id = Column(Integer, ForeignKey('invoice_types.id'))
    invoice_number = Column(String, nullable=False)
    created_date = Column(DateTime, nullable=False, default=datetime.now())
    issue_date = Column(DateTime, nullable=True)
    due_periods_count = Column(Integer, nullable=False, default=1)
    due_period = Column(Enum(DueInvoicePeriod),
                        nullable=False, default=DueInvoicePeriod.MONTH)
    due_date = Column(DateTime, nullable=False)
    description = Column(String, nullable=True)
    data = Column(JSON, nullable=True)

    invoice_type = relationship('InvoiceType', back_populates='due_invoices')

    run_records = relationship(
        'DueInvoiceRunRecord', back_populates='due_invoice')

    def __init__(self, invoice_type_id: str = None, invoice_number: str = None, created_date=None, due_date=None, description=None, data=None, issue_date=None, due_periods_count=1, due_period=DueInvoicePeriod.MONTH):
        if created_date is None:
            self.created_date = datetime.now()
        self.due_date = due_date
        self.invoice_type_id = invoice_type_id
        self.issue_date = issue_date
        if not invoice_number:
            invoice_number = f'INV-{self.issue_date.strftime("%Y%m%d")}-{self.due_date.strftime("%Y%m%d")}-{
                invoice_type_id}'
        self.invoice_number = invoice_number
        self.description = description
        self.data = data
        self.due_periods_count = due_periods_count
        self.due_period = due_period
