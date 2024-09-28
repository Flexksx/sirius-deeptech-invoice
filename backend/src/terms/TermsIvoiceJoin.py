class TermsInvoicesJoin:
    def __init__(self, invoice_type_id: int, terms_id: int):
        self.invoice_type_id = invoice_type_id 
        self.terms_id = terms_id 

    def __repr__(self) -> str:
        return f"TermsInvoicesJoin(invoice_type_id={self.invoice_type_id}, terms_id={self.terms_id})"
