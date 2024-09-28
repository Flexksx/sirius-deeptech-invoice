from sqlalchemy import Column, Integer, String, Time, ForeignKey, JSON, Double
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class InvoiceProducts(Base):
    __tablename__ = 'invoice_products'
    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Double)
    total_value = Column(Double)

    invoice = relationship('Invoice', back_populates='invoice_products')
    product = relationship('Product', back_populates='invoice_products')

    def __init__(self, invoice_id, product_id, quantity, total_value):
        self.invoice_id = invoice_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_value = total_value

    def __repr__(self):
        return f'<InvoiceProducts {self.id}>'
