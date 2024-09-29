from sqlalchemy import Column, Integer, String, ForeignKey, Double, Enum
from sqlalchemy.orm import relationship
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
    quantity = Column(Integer, nullable=True)
    invoice_type_id = Column(Integer, ForeignKey(
        'invoice_types.id'), nullable=True)

    invoice_type = relationship('InvoiceType', back_populates='products')

    def __init__(self, name: str, description: str, price: float, unit: ProductUnit, currency: str, quantity: int, invoice_type_id: int):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.price = price
        self.unit = unit
        self.currency = currency
        self.invoice_type_id = invoice_type_id

    def __repr__(self):
        return f'<Product {self.id}>'
