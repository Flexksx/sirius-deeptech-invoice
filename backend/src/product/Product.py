from typing import List
from backend.src.product.ProductsInvoiceJoin import ProductsInvoiceJoin


class Product:
    def __init__(self, id: str, name: str, price: float):
        self.id = id  
        self.name = name  
        self.price = price  

        self.productsIvoices: List[ProductsInvoiceJoin]

    def __repr__(self) -> str:
        return f"Product(id={self.id}, name='{self.name}', price={self.price})"