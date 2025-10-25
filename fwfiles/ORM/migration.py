import os
import json
import importlib
from sqlalchemy import text
from sqlalchemy import inspect
from fwfiles.ORM.db import Base, DBconnection
from prj.config import INSTALLED_APPS

def import_app_models():
    """Import models for all apps"""
    for app in INSTALLED_APPS:
        try:
            importlib.import_module(f"{app}.models")
        except ModuleNotFoundError:
            print(f"No models found for {app}")

def get_model_schema():
    """Return schema dict: {table_name: {"columns": {col_name: {"type": str, "default": val}}}}"""
    schema = {}
    for mapper in Base.registry.mappers:
        cls = mapper.class_
        if hasattr(cls, "__tablename__"):
            table_name = cls.__tablename__
            cols = {}
            for c in cls.__table__.columns:
                default = c.default.arg if c.default is not None else None
                cols[c.name] = {"type": str(c.type), "default": default}
            schema[table_name] = {"columns": cols, "class": cls.__name__, "module": cls.__module__}
    return schema

def sqlite_modify_table(engine, table_name, new_columns):
    """
    new_columns: list of tuples [(col_name, type, default), ...] 
    Preserves data, drops/changes columns automatically
    """
    temp_table = f"{table_name}_temp"

    col_defs = []
    for col_name, col_type, default in new_columns:
        default_str = f" DEFAULT {default}" if default is not None else ""
        col_defs.append(f"{col_name} {col_type}{default_str}")
    col_defs_str = ", ".join(col_defs)

    with engine.connect() as conn:
        conn.execute(text(f"CREATE TABLE {temp_table} ({col_defs_str})"))

    insp = inspect(engine)
    existing_cols = [c['name'] for c in insp.get_columns(table_name)]
    common_cols = [c[0] for c in new_columns if c[0] in existing_cols]
    if common_cols:
        cols_str = ", ".join(common_cols)
        with engine.connect() as conn:
            conn.execute(text(f"INSERT INTO {temp_table} ({cols_str}) SELECT {cols_str} FROM {table_name}"))

    with engine.connect() as conn:
        conn.execute(text(f"DROP TABLE {table_name}"))

    # 4️⃣ Rename temp table
    with engine.connect() as conn:
        conn.execute(text(f"ALTER TABLE {temp_table} RENAME TO {table_name}"))

def make_migrations():
    import_app_models()
    new_schema = get_model_schema()

    for app in INSTALLED_APPS:
        migrations_dir = f"migrations/{app}"
        os.makedirs(migrations_dir, exist_ok=True)

        schema_file = os.path.join(migrations_dir, "schema.json")
        old_schema = {}
        if os.path.exists(schema_file):
            with open(schema_file) as f:
                old_schema = json.load(f)

        tables_to_create = {t: c for t, c in new_schema.items() if t not in old_schema}
        tables_to_drop = [t for t in old_schema if t not in new_schema]

        tables_to_update = {}
        for t in new_schema:
            if t in old_schema:
                old_cols = old_schema[t]["columns"]
                new_cols = new_schema[t]["columns"]
                add_cols = {k:v for k,v in new_cols.items() if k not in old_cols}
                drop_cols = {k:v for k,v in old_cols.items() if k not in new_cols}
                type_change = {k:v for k,v in new_cols.items() if k in old_cols and v["type"] != old_cols[k]["type"]}
                if add_cols or drop_cols or type_change:
                    tables_to_update[t] = {"add": add_cols, "drop": drop_cols, "modify": type_change}

        filename = f"{len(os.listdir(migrations_dir))+1:04d}_auto_migration.py"
        filepath = os.path.join(migrations_dir, filename)

        with open(filepath, "w") as f:
            f.write("from fwfiles.ORM.db import DBconnection, Base\n")
            f.write("from sqlalchemy import text\n")
            f.write("from fwfiles.ORM.migration import sqlite_modify_table\n\n")

            for t, info in tables_to_create.items():
                f.write(f"from {info['module']} import {info['class']}\n")

            f.write("\n")
            f.write("def migrate():\n")
            f.write("    db = DBconnection(url='sqlite:///db.sqlite3')\n")

            for t in tables_to_drop:
                f.write(f"    with db.engine.connect() as conn:\n")
                f.write(f"        conn.execute(text('DROP TABLE IF EXISTS {t}'))\n")

            for t, changes in tables_to_update.items():
                all_new_cols = []
                for col, info in old_schema[t]['columns'].items():
                    if col not in changes['drop'] and col not in changes['modify']:
                        all_new_cols.append((col, info['type'], info.get('default')))
                for col, info in changes['modify'].items():
                    all_new_cols.append((col, info['type'], info['default']))
                for col, info in changes['add'].items():
                    all_new_cols.append((col, info['type'], info['default']))

                f.write(f"    sqlite_modify_table(db.engine, '{t}', {all_new_cols})\n")

            for t, info in tables_to_create.items():
                f.write(f"    {info['class']}.__table__.create(db.engine)\n")

            f.write("    print('Migration applied successfully!')\n")

        with open(schema_file, "w") as f:
            json.dump(new_schema, f, indent=4)

        print(f"Migration created: {filepath}")

def apply_migrations():
    import_app_models()
    db = DBconnection(url="sqlite:///db.sqlite3")

    try:
        for app in os.listdir("migrations"):
            app_dir = os.path.join("migrations", app)
            if not os.path.isdir(app_dir):
                continue
            migration_files = sorted(f for f in os.listdir(app_dir) if f.endswith(".py"))
            for mig_file in migration_files:
                module_name = f"migrations.{app}.{mig_file[:-3]}"
                try:
                    migration = importlib.import_module(module_name)
                    migration.migrate()
                except Exception as e:
                    print(f"Error applying {mig_file}: {e}")
        print("All migrations applied successfully!")

    finally:
        db.engine.dispose()
        print("DB connection closed safely.")

def reset_db():
    db_path = "db.sqlite3"
    if os.path.exists(db_path):
        db = DBconnection(url=f"sqlite:///{db_path}")
        db.engine.dispose()
        os.remove(db_path)
        print("Database file deleted successfully!")
    else:
        print("Database file does not exist.")
