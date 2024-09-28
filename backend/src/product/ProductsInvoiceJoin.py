class ProductsInvoicesJoin:
    def __init__(self, invoice_type_id: int, product_id: int, quantity: int, line_total: float):
        self.invoice_type_id = invoice_type_id  
        self.product_id = product_id  
        self.quantity = quantity  
        self.line_total = line_total 

    def __repr__(self) -> str:
        return (f"ProductsInvoicesJoin(invoice_type_id={self.invoice_type_id}, product_id={self.product_id}, "
                f"quantity={self.quantity}, line_total={self.line_total})")