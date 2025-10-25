import tkinter
import customtkinter as ctk
from fwfiles import routingjunction
from fwfiles.protocols import request
from . import component as com
from fwfiles.UI.decorators import use_masterpage
from  ..models import User



@use_masterpage("app.views.layout.Layout_default")
class login(ctk.CTkScrollableFrame):
    def __init__(self,master, height, width, data, **kwargs):
        super().__init__(master, corner_radius=0, fg_color="#FFFFFF", height=height, **kwargs)

        idframe=ctk.CTkFrame(self, corner_radius=0, fg_color="#ffffff")
        idframe.pack(padx=0, pady=0, fill="x")

        label=ctk.CTkButton(idframe,text="Login", corner_radius=0)
        label.pack(padx=0, pady=0, side="left")
        
        formframe=ctk.CTkFrame(self, corner_radius=0, fg_color="#eeeeee")
        formframe.pack(padx=10, pady=100, fill="y")
            
        lbusername=ctk.CTkLabel(formframe, text="Username")
        lbusername.pack(padx=0, pady=0, fill="y")

        enusername=ctk.CTkEntry(formframe, corner_radius=0, border_width=0, fg_color="#cfcfcf", width=250)
        enusername.pack(padx=0, pady=0, fill="y")

        lbPassword=ctk.CTkLabel(formframe, text="Password")
        lbPassword.pack(padx=0, pady=0, fill="y")

        enPassword=ctk.CTkEntry(formframe, corner_radius=0, border_width=0, fg_color="#cfcfcf", width=250)
        enPassword.pack(padx=0, pady=0, fill="y")
        

        def submit_login():
            data={
                "username":enusername.get(),
                "password":enPassword.get()
            }
            routingjunction.goto(["Main", "login"], request={"method":"POST", "data":data})
        
        submit=ctk.CTkButton(formframe,text="Login", corner_radius=0,width=250, command=submit_login)
        submit.pack(padx=10, pady=20, fill="y")
        
        def submit_login2():
            username=enusername.get()
            password=enPassword.get()
            if username and password:
                db=User(name=username,password=password,status=1)
                db.save()
                enusername.delete(0, ctk.END)
                enPassword.delete(0, ctk.END)
                table2.refresh(data=[[u.id, u.name, u.password] for u in User.all()])
                msg="data saved successfully"
            else:
                msg="data is not saved"
            
            return 0
        
        submit2=ctk.CTkButton(formframe,text="Login2", corner_radius=0,width=250, command=submit_login2)
        submit2.pack(padx=10, pady=20, fill="y")

        headings2=("id", "Name", "Age")
        
        tdata2 = []
        if data.get("data"):
            for info in data.get("data"):
                tdata2.append([info.id, info.name, info.password])

        
        table2=com.table(self, headings=headings2, data=tdata2)
        table2.pack(padx=10, pady=10, fill="both", side="left")

        headings=("id", "Name", "Age")
        
        tdata = []
        if data.get("data"):
            for info in data.get("data"):
                tdata.append([info.id, info.name, info.password])
        
        table=com.table(self, headings=headings, data=tdata)
        table.pack(padx=10, pady=10, fill="both", side="left")

        

