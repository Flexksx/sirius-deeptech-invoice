class InvoiceRunnerOneTime:
    def __init__(self, id: str, runner_id: str, start_date: str):
        self.id = id  
        self.runner_id = runner_id  
        self.start_date = start_date  

    def __repr__(self) -> str:
        return f"InvoiceRunnerOneTime(id={self.id}, runner_id={self.runner_id}, start_date='{self.start_date}')"