from prj import config
import os
import sys
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def show_apps():
    for i in config.INSTALLED_APPS:
        print(i)




class RunServer:
    def __init__(self, project_dir=None, entry_script="run.py"):
        self.project_dir = project_dir or os.getcwd()
        self.entry_script = entry_script
        self.process = None

    def start_process(self):
        if self.process:
            self.process.kill()
            self.process.wait()
        print(f"Starting {self.entry_script} ...")
        self.process = subprocess.Popen([sys.executable, self.entry_script])

    def on_any_event(self, event):
        if event.src_path.endswith(".py"):
            print(f"[Hot-Reload] Change detected: {event.src_path}")
            self.start_process()

    def run(self):
        from watchdog.observers import Observer
        from watchdog.events import FileSystemEventHandler

        class Handler(FileSystemEventHandler):
            def __init__(self, server):
                self.server = server
            def on_any_event(self, event):
                self.server.on_any_event(event)

        # Start observer
        handler = Handler(self)
        observer = Observer()
        observer.schedule(handler, self.project_dir, recursive=True)
        observer.start()

        # Start initial process
        self.start_process()
        print(f"Watching {self.project_dir} for changes...")

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
            if self.process:
                self.process.kill()
        observer.join()


# ----------------- Command line entry -----------------
def runserver():
    server = RunServer()
    server.run()
