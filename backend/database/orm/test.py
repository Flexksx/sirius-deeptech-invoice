from database import init_db, db_session
from models import Contract
u = Contract(created_date='2021-01-01', updated_date='2021-01-01',
             obligor_client_id=1, obligee_client_id=2, text='text', data='data')

init_db()
db_session.add(u)
db_session.commit()
