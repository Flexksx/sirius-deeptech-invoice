from sqlalchemy import Column, Integer, String, Time, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    idno = Column(String, nullable=True)
    company_type = Column(String, nullable=True)
    created_date = Column(DateTime)
    vertical = Column(String, nullable=True)
    address = Column(String, nullable=True)
    bank_code = Column(String, nullable=True)
    bank_name = Column(String, nullable=True)
    bank_address = Column(String, nullable=True)
    iban = Column(String, nullable=True)
    tva_code = Column(String, nullable=True)
    fiscal_code = Column(String, nullable=True)
    director_first_name = Column(String, nullable=True)
    director_last_name = Column(String, nullable=True)
    country = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    data = Column(JSON, nullable=True)

    # Relații separate pentru obligor și obligee
    obligor_contracts = relationship(
        'Contract', back_populates='obligor_client', foreign_keys='Contract.obligor_client_id')
    obligee_contracts = relationship(
        'Contract', back_populates='obligee_client', foreign_keys='Contract.obligee_client_id')

    def __init__(self, name: str = None, idno: str = None, company_type: str = None, vertical: str = None, address: str = None, bank_code: str = None, bank_name: str = None, bank_address: str = None, iban: str = None, tva_code: str = None, fiscal_code: str = None, director_first_name: str = None, director_last_name: str = None, country: str = None, email: str = None, phone: str = None, data: dict = None):
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
        self.data = data if data is not None else {}

    def __repr__(self):
        return f'<Client {self.id}>'
