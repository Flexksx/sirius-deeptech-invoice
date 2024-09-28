from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class DueInvoiceRunRecord(Base):
    __tablename__ = 'due_invoice_records'
    id = Column(Integer, primary_key=True)
    due_invoice_id = Column(Integer, ForeignKey('due_invoices.id'))
    runner_id = Column(Integer, ForeignKey('invoice_runners.id'))
    status = Column(String)
    created_date = Column(Time, default=datetime.now)
    completed_date = Column(Time, nullable=True)
    data = Column(JSON, nullable=True)

    due_invoice = relationship('DueInvoice', back_populates='run_records')
    runner = relationship('InvoiceRunner', back_populates='run_records')

    def __init__(self, due_invoice_id, runner_id, status, data):
        self.due_invoice_id = due_invoice_id
        self.runner_id = runner_id
        self.status = status
        self.data = data

    def __repr__(self):
        return f'<DueInvoiceRunRecord {self.id}>'
