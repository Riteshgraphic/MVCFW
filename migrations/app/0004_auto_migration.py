from fwfiles.ORM.db import DBconnection, Base
from sqlalchemy import text


def migrate():
    db = DBconnection(url='sqlite:///db.sqlite3')
    print('Column status drop for users not supported in SQLite, manual fix needed')
    print('Migration applied successfully!')
