from RunnerType import RunnerType

class InvoiceRunner:
    def __init__(self, id: str, invoice_type_id: str, runner_type: RunnerType):
        self.id = id 
        self.invoice_type_id = invoice_type_id  
        self.runner_type = runner_type  

    def __repr__(self) -> str:
        return (f"InvoiceRunner(id={self.id}, invoice_type_id={self.invoice_type_id}, "
                f"runner_type={self.runner_type.name})")