from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class DBconnection:
    def __init__(self, url="sqlite:///db.sqlite3", echo=True):
        self.engine = create_engine(url, echo=echo)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

