from tkinter import *
import customtkinter as ctk
from . import component as com
from . import configuration as conf
from fwfiles.UI.decorators import use_masterpage
from fwfiles import routingjunction


@use_masterpage("app.views.layout.Layout_default")
class master(ctk.CTkScrollableFrame):
    def __init__(self, master, height, inputwidth=120, data={}, **kwargs):
        super().__init__(master, corner_radius=0, fg_color="#ffffff", height=height, **kwargs)

        Buttonfeame=ctk.CTkFrame(self, corner_radius=10, fg_color="#ffffff")
        Buttonfeame.pack(padx=10, pady=10, fill="y")

        for masterelm in conf.masters:
            voucherbtn=ctk.CTkButton(Buttonfeame, text=masterelm["btncnt"],)
            voucherbtn.pack(padx=10, pady=10, fill="both", side="left")
   
        headings=("id", "Name", "Age", "Course")
        
        data = [
            (1, "Ritesh", 22, "Python"),
            (2, "Aman", 21, "Data Science"),
            (3, "Neha", 23, "AI & ML"),
            (4, "Sonia", 24, "Web Dev"),
        ]       
        tableframe=ctk.CTkFrame(self, fg_color="#FFFFFF", width=inputwidth,)
        tableframe.pack(padx=10, fill="both", expand=True)

        table=com.table(tableframe, headings=headings, data=data, height=25)
        table.pack(padx=10, side="left", fill="both", expand=True)
        
        self.sidebar=com.sidebar(master)
        self.sidebar.pack(pady=10, padx=10, fill="y", side="right")
