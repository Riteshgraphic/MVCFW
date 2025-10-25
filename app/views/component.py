from tkinter import ttk
import customtkinter as ctk
from fwfiles import routingjunction



class Card(ctk.CTkFrame):
    def __init__(self, master, title="Card Title", content="Card Content...", button_text="ok", **kwargs):
        super().__init__(master, corner_radius=10, fg_color="#f8f9fa", **kwargs)

        self.title_label = ctk.CTkLabel(self, text=title, font=("Helvetica", 16, "bold"), text_color="#212529")
        self.title_label.pack(pady=(10,0), padx=10, anchor="w")

        self.content_label=ctk.CTkLabel(self, text=content)
        self.content_label.pack(pady=(0,5), padx=10, anchor="w")

        self.button=ctk.CTkButton(self,text=button_text)
        self.button.pack(pady=10, padx=10, anchor="e", fill="both")



class LeftSidebar(ctk.CTkFrame):
    def __init__(self, master, title="Card Title", content="Card Content...", buttontext="Ok", **kwargs):
        super().__init__(master, corner_radius=10, fg_color="#f8f9fa",**kwargs)

        self.title_label=ctk.CTkLabel(self, text=title, font=("Helvetica", 16, "bold"), text_color="#212529")
        self.title_label.pack(pady=(10,0), padx=10, anchor="w")

        self.content_lable=ctk.CTkLabel(self, text=content)
        self.content_lable.pack(pady=(0.5), padx=10, anchor="w")

        self.button=ctk.CTkButton(self, text=buttontext)
        self.button.pack(pady=10, padx=10, anchor="w")



class infoCard(ctk.CTkFrame):
    def __init__(self, master, title="Card Title", content="Card Content...", **kwargs):
        super().__init__(master, corner_radius=10, fg_color="#f8f9fa", **kwargs)

        self.title_label = ctk.CTkLabel(self, text=title, font=("Helvetica", 16, "bold"), text_color="#212529")
        self.title_label.pack(pady=(10,0), padx=10, anchor="w")

        self.content_label=ctk.CTkLabel(self, text=content)
        self.content_label.pack(pady=(0,5), padx=10, anchor="w")




class table(ctk.CTkFrame):
    def __init__(self, master,headings=None, data=None, height=12, **kwargs):
        super().__init__(master, corner_radius=10,fg_color="#ffffff", **kwargs)
        
        self.headings=headings or []
        self.data=data or []

        style = ttk.Style()
        style.configure("Treeview", font=("Roboto Narrow", 10))
        style.configure("Treeview.Heading", font=("Roboto", 10, "bold"))
        self.table=ttk.Treeview(self, columns=headings, show="headings", height=height)
        for col in headings:
            self.table.heading(col, text=col)
            self.table.column(col, anchor="w")
        self.table.pack(padx=10, pady=10, anchor="w", fill="both", expand=True)

        for row in self.data:
            self.table.insert("","end",values=row)
        

    def refresh(self, data):
        for i in self.table.get_children():
                self.table.delete(i)

        for row in data:
            self.table.insert("","end",values=row)

    def clear(self):
        for i in self.table.get_children():
            self.table.delete(i)
    
    

class sidebar(ctk.CTkFrame):
    def __init__(self, master, fg_color="#ffffff", corner_radius=0):
        super().__init__(master, fg_color=fg_color, corner_radius=corner_radius)

        self.mclassbt=ctk.CTkButton(self, text="Class", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "classes"], request={"method":"GET", "data":{}}))
        self.mclassbt.pack(padx=5, pady=5, fill="y")

        self.btsubject=ctk.CTkButton(self, text="Subject", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "subjects"], request={"method":"GET", "data":{}}))
        self.btsubject.pack(padx=5, pady=5, fill="y")

        self.Sessionbt=ctk.CTkButton(self, text="Session", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "session"], request={"method":"GET", "data":{}}))
        self.Sessionbt.pack(padx=5, pady=5, fill="y")

        self.exambt=ctk.CTkButton(self, text="Exam", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "exam"], request={"method":"GET", "data":{}}))
        self.exambt.pack(padx=5, pady=5, fill="y")
        
        self.feesbt=ctk.CTkButton(self, text="Fees", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "fees"], request={"method":"GET", "data":{}}))
        self.feesbt.pack(padx=5, pady=5, fill="y")

        self.Assignsubjectbt=ctk.CTkButton(self, text="Assign Subject", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "assignsubject"], request={"method":"GET", "data":{}}))
        self.Assignsubjectbt.pack(padx=5, pady=5, fill="y")

        self.Assignclassbt=ctk.CTkButton(self, text="Assign Class", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "assignclass"], request={"method":"GET", "data":{}}))
        self.Assignclassbt.pack(padx=5, pady=5, fill="y")



class sregsidebar(ctk.CTkFrame):
    def __init__(self, master, fg_color="#ffffff", corner_radius=0):
        super().__init__(master, fg_color=fg_color, corner_radius=corner_radius)

        self.juniorreg=ctk.CTkButton(self, text="Junior Student Registration", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "registration"], request={"method":"GET", "data":{}}))
        self.juniorreg.pack(padx=5, pady=5, fill="y")

        self.seniorreg=ctk.CTkButton(self, text="Senior Student Registration", fg_color="#ebebeb", text_color="#292828", command=lambda:routingjunction.goto(["Main", "seniorstudentreg"], request={"method":"GET", "data":{}}))
        self.seniorreg.pack(padx=5, pady=5, fill="y")


