from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class InvoiceRunner(Base):
    __tablename__ = 'invoice_runners'
    id = Column(Integer, primary_key=True)
    invoice_type_id = Column(Integer, ForeignKey('invoice_types.id'))
    runner_type = Column(String)

    invoice_type = relationship(
        'InvoiceType', back_populates='invoice_runners')
    invoice_runs = relationship('InvoiceRun', back_populates='invoice_runner')

    def __init__(self, invoice_type_id, runner_type):
        self.invoice_type_id = invoice_type_id
        self.runner_type = runner_type

    def __repr__(self):
        return f'<InvoiceRunner {self.id}>'
