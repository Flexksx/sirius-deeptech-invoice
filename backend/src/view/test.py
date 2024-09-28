from ... import db_session, init_db  # Use relative import to access db_session and init_db
from database.models import Contract  # Import the Contract model

# Create an instance of the Contract
u = Contract(created_date='2021-01-01', updated_date='2021-01-01',
             obligor_client_id=1, obligee_client_id=2, text='text', data='data')

# Initialize the database and add the instance
init_db()
db_session.add(u)
db_session.commit()
