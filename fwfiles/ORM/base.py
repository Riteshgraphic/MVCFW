from .db import Base, DBconnection

db=DBconnection()

class Model(Base):
    __abstract__=True


    @classmethod
    def create_table(cls):
        db.create_tables()

    @classmethod
    def all(cls):
        return db.session.query(cls).all()
    
    @classmethod
    def filter(cls, **kwargs):
        return db.session.query(cls).filter_by(**kwargs).all()

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    