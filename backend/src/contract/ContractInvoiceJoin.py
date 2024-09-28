class ContractInvoiceJoin:
    def __init__(self, contract_id: str, invoice_type_id: str) -> None:
        self.contract_id = contract_id
        self.invoice_tyoe_id = invoice_type_id

    def __repr__(self) -> str:
        return f"ContractIvoiceJoin(contract_id={self.contract_id}, invoice_type_id={self.invoice_type_id},)"