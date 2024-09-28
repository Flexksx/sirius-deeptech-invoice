from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Terms(Base):
    __tablename__ = 'terms'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    data = Column(JSON, nullable=True)
    invoice_type_id = Column(Integer, ForeignKey('invoice_types.id'))

    def __init__(self, name, description, data):
        self.name = name
        self.description = description
        self.data = data

    def __repr__(self):
        return f'<Terms {self.id}>'
