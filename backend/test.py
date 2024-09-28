from database import db_session,init_db
from database.models import *
u = Contract(created_date='2021-01-01', updated_date='2021-01-01',
             obligor_client_id=1, obligee_client_id=2, text='text', data='data')

init_db()
db_session.add(u)
db_session.commit()
