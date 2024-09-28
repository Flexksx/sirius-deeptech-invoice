class InvoiceRunnerSchedule:
    def __init__(self, id: str, runner_id: str, frequency: str, start_date: str):
        self.id = id  
        self.runner_id = runner_id 
        self.frequency = frequency  
        self.start_date = start_date  

    def __repr__(self) -> str:
        return (f"InvoiceRunnerSchedule(id={self.id}, runner_id={self.runner_id}, "
                f"frequency='{self.frequency}', start_date='{self.start_date}')")