import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database import db_session, init_db 
from database.models import Contract

# Create an instance of the Contract
u = Contract(created_date='2021-01-01', updated_date='2021-01-01',
             obligor_client_id=1, obligee_client_id=2, text='text', data='data')

# Initialize the database and add the instance
init_db()  # Ensure the database is initialized
db_session.add(u)  # Add the new contract to the session
db_session.commit()  # Commit the session to save the changes

print("Contract added successfully.")
