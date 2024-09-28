from sqlalchemy import Column, Integer, String, Time, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    idno = Column(String)
    company_type = Column(String)
    created_date = Column(DateTime)
    vertical = Column(String)
    address = Column(String)
    bank_code = Column(String)
    bank_name = Column(String)
    bank_address = Column(String)
    iban = Column(String)
    tva_code = Column(String)
    fiscal_code = Column(String)
    director_first_name = Column(String)
    director_last_name = Column(String)
    country = Column(String)
    email = Column(String)
    phone = Column(String)
    data = Column(JSON)

    # Relații separate pentru obligor și obligee
    obligor_contracts = relationship(
        'Contract', back_populates='obligor_client', foreign_keys='Contract.obligor_client_id')
    obligee_contracts = relationship(
        'Contract', back_populates='obligee_client', foreign_keys='Contract.obligee_client_id')

    def __init__(self, name, idno, company_type, vertical, address, bank_code, bank_name, bank_address, iban, tva_code, fiscal_code, director_first_name, director_last_name, country, email, phone, data):
        self.name = name
        self.idno = idno
        self.company_type = company_type
        self.created_date = datetime.now()
        self.vertical = vertical
        self.address = address
        self.bank_code = bank_code
        self.bank_name = bank_name
        self.bank_address = bank_address
        self.iban = iban
        self.tva_code = tva_code
        self.fiscal_code = fiscal_code
        self.director_first_name = director_first_name
        self.director_last_name = director_last_name
        self.country = country
        self.email = email
        self.phone = phone
        self.data = data

    def __repr__(self):
        return f'<Client {self.id}>'
