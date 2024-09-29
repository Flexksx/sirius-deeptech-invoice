from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
import os

Base = declarative_base()
database_path = os.path.join(os.path.dirname(__file__), '../database.db')
engine = create_engine(f'sqlite:///{database_path}', echo=True)
db_session = scoped_session(sessionmaker(bind=engine))
Base.query = db_session.query_property()


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()
