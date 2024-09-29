from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Terms(Base):
    __tablename__ = 'terms'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    description = Column(String, nullable=True)
    value = Column(JSON, nullable=True)
    invoice_type_id = Column(Integer, ForeignKey('invoice_types.id'))

    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __repr__(self):
        return f'<Terms {self.id}>'
