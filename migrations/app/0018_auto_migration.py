from fwfiles.ORM.db import DBconnection, Base
from sqlalchemy import text
from fwfiles.ORM.migration import sqlite_modify_table


def migrate():
    db = DBconnection(url='sqlite:///db.sqlite3')
    with db.engine.connect() as conn:
        conn.execute(text('DROP TABLE IF EXISTS users'))
    print('Migration applied successfully!')
