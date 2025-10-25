from fwfiles.ORM.db import DBconnection, Base
from sqlalchemy import text


def migrate():
    db = DBconnection(url='sqlite:///db.sqlite3')
    with db.engine.connect() as conn:
        conn.execute(text('DROP TABLE IF EXISTS users'))
    print('Migration applied successfully!')
