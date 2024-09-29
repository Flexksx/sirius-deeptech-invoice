from database import init_db, db_session
from models import *

client = Client(
    name='Test Client',
    address='Test Address',
    country='Test Country',
)
init_db()
db_session.add(client)
db_session.commit()
