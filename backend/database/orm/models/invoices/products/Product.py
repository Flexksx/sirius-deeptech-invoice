from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON, Double
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Double)
    unit = Column(String)
    currency = Column(String)

    invoice_products = relationship(
        'InvoiceProducts', back_populates='product')

    def __init__(self, name, description, price, unit, currency):
        self.name = name
        self.description = description
        self.price = price
        self.unit = unit
        self.currency = currency

    def __repr__(self):
        return f'<Product {self.id}>'
