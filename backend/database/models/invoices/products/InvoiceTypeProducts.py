from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON, Double
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class InvoiceTypeProducts(Base):
    __tablename__ = 'invoice_type_products'
    invoice_type_id = Column(Integer, ForeignKey(
        'invoice_types.id'), primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    quantity = Column(Double)
    total_value = Column(Double)

    def __init__(self, invoice_type_id, product_id, quantity, total_value):
        self.invoice_type_id = invoice_type_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_value = total_value

    def __repr__(self):
        return f'<InvoiceTypeProducts {self.invoice_type_id} {self.product_id}>'
