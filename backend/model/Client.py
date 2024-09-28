# model/Client.py
from datetime import datetime
from model.Contract import Contract
from model.CompanyType import CompanyType
from model.VerticalType import VerticalType
from typing import List

class Client:
    def __init__(self, id: int, name: str, idno: str, company_type: CompanyType, created_date: datetime,
                 vertical: VerticalType, address: str, tva_code: str, bank_code: str, bank_name: str,
                 iban: str, bank_address: str, fiscal_code: str,
                 director_first_name: str, director_last_name: str, country: str, email: str):
        self.id = id  
        self.name = name  
        self.idno = idno  
        self.company_type = company_type  
        self.created_date = created_date  
        self.vertical = vertical  
        self.address = address  
        self.tva_code = tva_code 
        self.bank_code = bank_code  
        self.bank_name = bank_name  
        self.iban = iban  
        self.bank_address = bank_address  
        self.fiscal_code = fiscal_code   
        self.director_first_name = director_first_name 
        self.director_last_name = director_last_name 
        self.country = country 
        self.email = email  

        self.contracts: List[Contract] = []

    def add_contract(self, contract: Contract) -> None:
        self.contracts.append(contract)

    def __repr__(self) -> str:
        return (f"Contract(id={self.id}, name='{self.name}', idno='{self.idno}', "
                f"company_type='{self.company_type}', created_date={self.created_date}, "
                f"vertical='{self.vertical}', address='{self.address}', tva_code='{self.tva_code}', "
                f"bank_code='{self.bank_code}', bank_name='{self.bank_name}', iban='{self.iban}', "
                f"bank_address='{self.bank_address}', fiscal_code='{self.fiscal_code}', "
                f"person_id={self.person_id}, director_first_name='{self.director_first_name}', "
                f"director_last_name='{self.director_last_name}', country={self.country}, "
                f"email='{self.email}')")
