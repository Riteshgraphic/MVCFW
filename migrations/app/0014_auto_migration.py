from fwfiles.ORM.db import DBconnection, Base
from sqlalchemy import text
from fwfiles.ORM.migration import sqlite_modify_table


def migrate():
    db = DBconnection(url='sqlite:///db.sqlite3')
    sqlite_modify_table(db.engine, 'users', [('id', 'INTEGER', None), ('name', 'VARCHAR(255)', None), ('status', 'VARCHAR(255)', None), ('password', 'VARCHAR(255)', None)])
    print('Migration applied successfully!')
