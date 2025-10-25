import sys
from fwfiles.ORM.commands import handle_command

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python manage.py [command] [app_name(optional)]")
    else:
        command = sys.argv[1]
        app_name = sys.argv[2] if len(sys.argv) > 2 else None
        handle_command(command, app_name)


