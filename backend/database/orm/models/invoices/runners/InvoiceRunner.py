from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class InvoiceRunner(Base):
    __tablename__ = 'invoice_runners'
    id = Column(Integer, primary_key=True)
    runner_type = Column(String)
    created_date = Column(Time, default=datetime.now)
    data = Column(JSON, nullable=True)

    run_records = relationship('DueInvoiceRunRecord', back_populates='runner')

    def __init__(self, runner_type, data):
        self.runner_type = runner_type
        self.data = data

    def __repr__(self):
        return f'<InvoiceRunner {self.id}>'
