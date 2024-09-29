from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON, Double, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
from .enums import ProductUnit


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Double, nullable=False)
    unit = Column(Enum(ProductUnit), nullable=False)
    currency = Column(String, nullable=False)

    def __init__(self, name: str, description: str, price: float, unit: ProductUnit, currency: str):
        self.name = name
        self.description = description
        self.price = price
        self.unit = unit
        self.currency = currency

    def __repr__(self):
        return f'<Product {self.id}>'
