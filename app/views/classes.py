import customtkinter as ctk
from fwfiles.UI.decorators import use_masterpage
from fwfiles import routingjunction
from . import component as com

def apply_focus_highlight(widget):
    if isinstance(widget, ctk.CTkEntry):
        widget.bind("<FocusIn>", lambda e: widget.configure(border_color="#0078D7", border_width=2))
        widget.bind("<FocusOut>", lambda e: widget.configure(border_color="#000000", border_width=0))
    if hasattr(widget, "winfo_children"):
        for child in widget.winfo_children():
            apply_focus_highlight(child)

@use_masterpage("app.views.layout.Layout_default")
class Classes(ctk.CTkScrollableFrame):
    def __init__(self, master, height, width, data, **kwags):
        super().__init__(master, corner_radius=0, fg_color="#ffffff", height=height, **kwags)

        upperbar=ctk.CTkFrame(self, fg_color="#ffffff")
        upperbar.pack(padx=0, pady=0, fill="both")

        label=ctk.CTkButton(upperbar,text="Classes", corner_radius=0)
        label.pack(padx=0, pady=0, side="left")

        headerframe=ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        headerframe.pack(padx=20, pady=(10,0), fill="both")

        lbh=ctk.CTkLabel(headerframe, text="Add Class")
        lbh.pack(padx=0, pady=0, fill="y", side="left")
        
        line=ctk.CTkFrame(self, height=1.5, width=width, fg_color="#DADADA")
        line.pack(padx=0, pady=0, fill="y")

        sec1=ctk.CTkFrame(self, fg_color="#ffffff")
        sec1.pack(padx=10, pady=(10,0), fill="both")

        lbid=ctk.CTkLabel(sec1, text="Class Name :", width=100)
        lbid.pack(padx=10, pady=0, fill="x", side="left")
 
        idinput=ctk.CTkEntry(sec1, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        idinput.pack(padx=10, pady=0, fill="y", side="left")
        
        lbdate=ctk.CTkLabel(sec1, text="Category :", width=100)
        lbdate.pack(padx=10, pady=0, fill="x", side="left")
 
        dateinput=ctk.CTkEntry(sec1, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        dateinput.pack(padx=10, pady=0, fill="y", side="left")

        submitbt=ctk.CTkButton(sec1,text="Submit", corner_radius=0)
        submitbt.pack(padx=0, pady=0, side="right")

        headerframe=ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        headerframe.pack(padx=20, pady=(10,0), fill="both")

        lbh=ctk.CTkLabel(headerframe, text="All Classes")
        lbh.pack(padx=0, pady=0, fill="y", side="left")
        
        line=ctk.CTkFrame(self, height=1.5, width=width, fg_color="#DADADA")
        line.pack(padx=0, pady=0, fill="y")
        
        headings2=("id", "Class", "Category")
        
        tdata2 = []
        if data.get("data"):
            for info in data.get("data"):
                tdata2.append([info.id, info.name, info.password])
        
        table2=com.table(self, headings=headings2, data=tdata2)
        table2.pack(padx=10, pady=10, fill="both")

        apply_focus_highlight(self)

        self.sidebar=com.sidebar(master)
        self.sidebar.pack(pady=10, padx=10, fill="y", side="right")

        