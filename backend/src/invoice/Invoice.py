class Invoice:
    def __init__(self, id: int, invoice_number: str, invoice_date: str, invoice_due_date: str, invoice_type_id: int):
        self.id = id 
        self.invoice_number = invoice_number  
        self.invoice_date = invoice_date 
        self.invoice_due_date = invoice_due_date  
        self.invoice_type_id = invoice_type_id 

    def __repr__(self) -> str:
        return (f"Invoice(id={self.id}, invoice_number='{self.invoice_number}', "
                f"invoice_date='{self.invoice_date}', invoice_due_date='{self.invoice_due_date}', "
                f"invoice_type_id={self.invoice_type_id})")