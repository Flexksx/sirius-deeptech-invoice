from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Numeric, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from sqlalchemy import create_engine

# Correct format for SQLite
engine = create_engine('sqlite:////home/liviu/GigaHack24/sirius-deeptech-invoice/backend/database/database.db')


Base = declarative_base()

class Client(Base):
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    idno = Column(String, nullable=False)
    company_type = Column(String, nullable=False)
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    vertical = Column(String, nullable=False)
    address = Column(String, nullable=False)
    tva_code = Column(String, nullable=False)
    bank_code = Column(String, nullable=False)
    bank_name = Column(String, nullable=False)
    iban = Column(String, nullable=False)
    bank_address = Column(String, nullable=False)
    fiscal_code = Column(String, nullable=False)
    director_first_name = Column(String, nullable=False)
    director_last_name = Column(String, nullable=False)
    country = Column(String, nullable=False)
    email = Column(String, nullable=False)

class InvoiceType(Base):
    __tablename__ = 'invoice_type'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    contract_id = Column(Integer, ForeignKey('contracts.id'), nullable=False)
    created_date = Column(TIMESTAMP, default=datetime.utcnow)
    notes = Column(Text, nullable=False)
    data = Column(Text, nullable=False)
    description = Column(Text, nullable=False)

# Define other models similarly...

# Create an SQLite database connection
engine = create_engine('/home/liviu/GigaHack24/sirius-deeptech-invoice/backend/database/database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Insert a new client
new_client = Client(
    name='John Doe',
    idno='123456789',
    company_type='LLC',
    vertical='Finance',
    address='123 Main St',
    tva_code='TVA123',
    bank_code='BC123',
    bank_name='Bank of Example',
    iban='IBAN123',
    bank_address='Bank Address',
    fiscal_code='FISCAL123',
    director_first_name='John',
    director_last_name='Doe',
    country='Country',
    email='john.doe@example.com'
)

session.add(new_client)

# Insert other data similarly...
session.commit()  # Save changes to the database
new_invoice_type = InvoiceType(
    name='Standard Invoice',
    contract_id=1,  # Ensure this ID exists in contracts table
    notes='Some notes',
    data='Additional data',
    description='Description of invoice type'
)

session.add(new_invoice_type)
session.commit()
