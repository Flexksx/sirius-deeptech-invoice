from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class InvoiceRun(Base):
    __tablename__ = 'invoice_runs'
    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    invoice_runner_id = Column(Integer, ForeignKey('invoice_runners.id'))
    status = Column(String)
    created_date = Column(Time)
    completed_date = Column(Time)

    invoice = relationship('Invoice', back_populates='invoice_runs')
    invoice_runner = relationship(
        'InvoiceRunner', back_populates='invoice_runs')

    def __init__(self, invoice_id, invoice_runner_id, status):
        self.invoice_id = invoice_id
        self.invoice_runner_id = invoice_runner_id
        self.status = status
        self.created_date = datetime.now()

    def __repr__(self):
        return f'<InvoiceRun {self.id} created on {self.created_date} with status {self.status}>'
