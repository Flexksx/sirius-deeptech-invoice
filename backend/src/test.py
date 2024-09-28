import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import db_session, init_db 
from database.models import *
import random
# Create an instance of the Contract
u = Contract(created_date='2021-01-01', updated_date='2021-01-01',
             obligor_client_id=1, obligee_client_id=2, text='text', data='data')

def create_dummy_client(client_id):
    return Client(
        name=f"Client {client_id}",
        idno=f"ID{client_id}",
        company_type=random.choice(['Type A', 'Type B', 'Type C']),
        vertical=random.choice(['Vertical 1', 'Vertical 2', 'Vertical 3']),
        address=f"{client_id} Client Street",
        bank_code=f"BC{client_id}",
        bank_name=f"Bank {client_id}",
        bank_address=f"{client_id} Bank Address",
        iban=f"IBAN{client_id}",
        tva_code=f"TVA{client_id}",
        fiscal_code=f"FC{client_id}",
        director_first_name=random.choice(['John', 'Jane', 'Alice', 'Bob']),
        director_last_name=random.choice(['Doe', 'Smith', 'Johnson']),
        country=random.choice(['Country A', 'Country B', 'Country C']),
        email=f"client{client_id}@example.com",
        phone=f"+123456789{client_id}",
        data={}
    )

# Create an array of 10 dummy clients
dummy_clients = [create_dummy_client(i) for i in range(1, 11)]
for client in dummy_clients:
    db_session.add(client)
# Initialize the database and add the instance
init_db()  # Ensure the database is initialized
db_session.add(u)  # Add the new contract to the session

db_session.commit()  # Commit the session to save the changes

print("Contract added successfully.")



