import customtkinter as ctk
from . import component as com
from fwfiles import routingjunction

class Layout_default(ctk.CTkFrame):
    def __init__(self, root):
        super().__init__(root)
        self.pack(side="left", fill="y")

        self.sidebar=com.LeftSidebar(self, title="Edutrack",  content="Hello User!", buttontext="Logout")
        self.sidebar.pack(pady=10, padx=10, fill="y")


        self.loginbt=ctk.CTkButton(self, text="LOGIN", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "login"], request={"method":"GET", "data":{}}))
        self.loginbt.pack(padx=5, pady=5, fill="y")

        self.bthome=ctk.CTkButton(self, text="HOME", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "index"], request={"method":"GET", "data":{}}))
        self.bthome.pack(padx=5, pady=5, fill="y")

        self.modules=ctk.CTkButton(self, text="MASTERS", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "master"], request={"method":"GET", "data":{}}))
        self.modules.pack(padx=5, pady=5, fill="y")

        self.btinstreg=ctk.CTkButton(self, text="Create institute", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "institutereg"], request={"method":"GET", "data":{}}))
        self.btinstreg.pack(padx=5, pady=5, fill="y")
        
        self.btreg=ctk.CTkButton(self, text="Registration", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "registration"], request={"method":"GET", "data":{}}))
        self.btreg.pack(padx=5, pady=5, fill="y")

        self.btreg=ctk.CTkButton(self, text="Student Details", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "studentdetails"], request={"method":"GET", "data":{}}))
        self.btreg.pack(padx=5, pady=5, fill="y")

        self.imageframe=ctk.CTkFrame(self, width=150)
        self.imageframe.pack(padx=10, pady=10, fill="y")

        self.body=ctk.CTkFrame(root)
        self.body.pack(padx=10, pady=10, fill="both")

       