class InvoiceRun:
    def __init__(self, id: int, invoice_id: int, runner_id: int, created_date: str, completed_date: str, status: bool):
        self.id = id 
        self.invoice_id = invoice_id 
        self.runner_id = runner_id 
        self.created_date = created_date 
        self.completed_date = completed_date 
        self.status = status 

    def __repr__(self) -> str:
        return (f"InvoiceRun(id={self.id}, invoice_id={self.invoice_id}, runner_id={self.runner_id}, "
                f"created_date='{self.created_date}', completed_date='{self.completed_date}', "
                f"status={self.status})")