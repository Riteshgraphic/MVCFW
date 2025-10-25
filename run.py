from tkinter import *
import customtkinter as ctk
from prj import config
from fwfiles import routingjunction
from app.views import component as com
from app.views.configuration import sidebaroptions
from fwfiles import protocols
import time
import threading
from PIL import Image



class SplashScreen(ctk.CTk):
    def __init__(self, root):
        self.root = root
        self.splash = ctk.CTkToplevel()
        self.splash.title("EduTrack - Loading")
        self.splash.overrideredirect(True)
        center_window(self.splash, 500, 300)

        try:
            logo = ctk.CTkImage(Image.open("edutrack_logo.png"), size=(230, 120))
            ctk.CTkLabel(self.splash, image=logo, text="").pack(pady=20)
        except:
            ctk.CTkLabel(self.splash, text="EduTrack", font=("Arial", 28, "bold")).pack(pady=30)

        self.progress = ctk.CTkProgressBar(self.splash, width=350)
        self.progress.pack(pady=20)
        self.progress.set(0)

        ctk.CTkLabel(self.splash, text="Loading EduTrack...", font=("Arial", 16)).pack()

        threading.Thread(target=self.animate).start()

    def animate(self):
        for i in range(100):
            time.sleep(0.02)
            self.progress.set(i / 100)
        self.splash.after(200, self.start_main_app)

    def start_main_app(self):
        self.splash.destroy()
        self.root.deiconify()

def center_window(win, width, height):
    win.update_idletasks()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = int((screen_width / 2) - (width / 2))
    y = int((screen_height / 2) - (height / 2))
    win.geometry(f"{width}x{height}+{x}+{y}")



class EduTrackApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("EduTrack Desktop")
        screen_width  = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        def refresh_page(req):
            for widget in self.winfo_children():
                widget.destroy()

            controller_func = routingjunction.ref(
                routingjunction.ROUTING_PIPE[0],
                routingjunction.ROUTING_PIPE[1]
            )

            page_class = None
            data = {}

            if callable(controller_func):
                result = controller_func(req)

                if isinstance(result, tuple) and len(result) == 2:
                    page_class, data = result
                else:
                    page_class = result
            elif isinstance(controller_func, type):
                page_class = controller_func
            if not page_class:
                print("No valid page class found for route:", routingjunction.ROUTING_PIPE)
            
            page_widget = page_class(self, height=screen_height, width=screen_width, data=data)
            
            if hasattr(page_widget, "render"):
                page_widget.render(data)
            
            page_widget.pack(padx=0, pady=0, fill="both")
            
        routingjunction.set_refresh_callback(refresh_page)

        routingjunction.goto(routingjunction.ROUTING_PIPE)

        self.bind("<F5>", lambda event: routingjunction.goto(routingjunction.ROUTING_PIPE))

    def maximize_window(self):
        self.state("zoomed")



if __name__ == "__main__":
    root = EduTrackApp()
    root.withdraw()
    root.after(4950, root.maximize_window)
    SplashScreen(root)
    root.mainloop()


