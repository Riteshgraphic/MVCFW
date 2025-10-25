from fwfiles.ORM.db import DBconnection, Base
from sqlalchemy import text
from fwfiles.ORM.migration import sqlite_modify_table

from app.models import User

def migrate():
    db = DBconnection(url='sqlite:///db.sqlite3')
    User.__table__.create(db.engine)
    print('Migration applied successfully!')
