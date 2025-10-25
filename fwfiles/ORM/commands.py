import sys
from .migration import make_migrations, apply_migrations, reset_db
from .generalcommands import show_apps, runserver

def handle_command(command, app_name=None):
    if len(sys.argv) < 2:
        print("Usage: python manager.py [command]")
    else:
        cmd = sys.argv[1]

        if cmd == "makemigrations":
            make_migrations()
        elif cmd == "migrate":
            apply_migrations()
        elif cmd == "reset_db":
            reset_db()
        elif command == "show_apps":
            show_apps()
        elif command == "runserver":
            runserver()
        else:
            print(f"Unknown command: {command}")
            

