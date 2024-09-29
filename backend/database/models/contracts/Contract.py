from sqlalchemy import Column, DateTime, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, nullable=True, default=datetime.now())
    name = Column(String, nullable=True)
    updated_date = Column(DateTime, nullable=True)
    obligor_client_id = Column(Integer, ForeignKey('clients.id'))
    obligee_client_id = Column(Integer, ForeignKey('clients.id'))
    text = Column(String, nullable=True)
    data = Column(JSON, nullable=True)

    obligor_client = relationship(
        'Client', back_populates='obligor_contracts', foreign_keys=[obligor_client_id])
    obligee_client = relationship(
        'Client', back_populates='obligee_contracts', foreign_keys=[obligee_client_id])
    invoice_types = relationship('InvoiceType', back_populates='contract')

    def __init__(self, name: str = None, created_date: datetime = None, updated_date: datetime = None, obligor_client_id: int = None, obligee_client_id: int = None, text: str = None, data: dict = None):
        self.name = name if name is not None else 'Contract'
        self.created_date = created_date if created_date is not None else datetime.now()
        self.updated_date = updated_date if updated_date is not None else datetime.now()
        self.obligor_client_id = obligor_client_id
        self.obligee_client_id = obligee_client_id
        self.text = text
        self.data = data

    def __repr__(self):
        return f'<Contract {self.id}>'
