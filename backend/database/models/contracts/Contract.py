from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Contract(Base):
    __tablename__ = 'contracts'
    id = Column(Integer, primary_key=True)
    created_date = Column(Time)
    updated_date = Column(Time)
    obligor_client_id = Column(Integer, ForeignKey('clients.id'))
    obligee_client_id = Column(Integer, ForeignKey('clients.id'))
    text = Column(String)
    data = Column(JSON)

    obligor_client = relationship(
        'Client', back_populates='obligor_contracts', foreign_keys=[obligor_client_id])
    obligee_client = relationship(
        'Client', back_populates='obligee_contracts', foreign_keys=[obligee_client_id])
    invoice_types = relationship('InvoiceType', back_populates='contract')

    def __init__(self, created_date=None, updated_date=None, obligor_client_id=None, obligee_client_id=None, text=None, data=None):
        if created_date is None:
            self.created_date = datetime.now()
        if updated_date is None:
            self.updated_date = datetime.now()
        self.obligor_client_id = obligor_client_id
        self.obligee_client_id = obligee_client_id
        self.text = text
        self.data = data

    def __repr__(self):
        return f'<Contract {self.id}>'
