import customtkinter as ctk
from fwfiles.UI.decorators import use_masterpage
from fwfiles import routingjunction
from . import component as com

def apply_focus_highlight(widget):
    if isinstance(widget, ctk.CTkEntry):
        widget.bind("<FocusIn>", lambda e: widget.configure(border_color="#0078D7", border_width=2))
        widget.bind("<FocusOut>", lambda e: widget.configure(border_color="#000000", border_width=0))
    if isinstance(widget, ctk.CTkTextbox):
        widget.bind("<FocusIn>", lambda e: widget.configure(border_color="#0078D7", border_width=2))
        widget.bind("<FocusOut>", lambda e: widget.configure(border_color="#000000", border_width=0))
    if hasattr(widget, "winfo_children"):
        for child in widget.winfo_children():
            apply_focus_highlight(child)

@use_masterpage("app.views.layout.Layout_default")
class registration(ctk.CTkScrollableFrame):
    def __init__(self, master, height, width, data, **kwags):
        super().__init__(master, corner_radius=0, fg_color="#ffffff", height=height, **kwags)

        upperbar=ctk.CTkFrame(self, fg_color="#ffffff")
        upperbar.pack(padx=0, pady=0, fill="both")

        label=ctk.CTkButton(upperbar,text="Registration", corner_radius=0)
        label.pack(padx=0, pady=0, side="left")

        headerframe=ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        headerframe.pack(padx=20, pady=(10,0), fill="both")

        lbh=ctk.CTkLabel(headerframe, text="Personal Information")
        lbh.pack(padx=0, pady=0, fill="y", side="left")
        
        line=ctk.CTkFrame(self, height=1.5, width=width, fg_color="#DADADA")
        line.pack(padx=0, pady=0, fill="y")

        sec1=ctk.CTkFrame(self, fg_color="#ffffff")
        sec1.pack(padx=10, pady=(10,0), fill="both")

        lbid=ctk.CTkLabel(sec1, text="id :", width=100)
        lbid.pack(padx=10, pady=0, fill="x", side="left")
 
        idinput=ctk.CTkEntry(sec1, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        idinput.pack(padx=10, pady=0, fill="y", side="left")
        
        lbdate=ctk.CTkLabel(sec1, text="Date :", width=100)
        lbdate.pack(padx=10, pady=0, fill="x", side="left")
 
        dateinput=ctk.CTkEntry(sec1, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        dateinput.pack(padx=10, pady=0, fill="y", side="left")

        lbname=ctk.CTkLabel(sec1, text="Name :", width=100)
        lbname.pack(padx=10, pady=0, fill="x", side="left")

        nameinput=ctk.CTkEntry(sec1, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        nameinput.pack(padx=10, pady=0, fill="y", side="left")

        sec2=ctk.CTkFrame(self, fg_color="#ffffff")
        sec2.pack(padx=10, pady=10, fill="both")
        
        lbadhar=ctk.CTkLabel(sec2, text="Adhar no. :", width=100)
        lbadhar.pack(padx=10, pady=0, fill="x", side="left")

        adharinput=ctk.CTkEntry(sec2, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        adharinput.pack(padx=10, pady=0, fill="y", side="left")

        lbclass=ctk.CTkLabel(sec2, text="Class :", width=100)
        lbclass.pack(padx=10, pady=0, fill="x", side="left")
 
        classinput=ctk.CTkEntry(sec2, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        classinput.pack(padx=10, pady=0, fill="y", side="left")

        lbdob=ctk.CTkLabel(sec2, text="DOB :", width=100)
        lbdob.pack(padx=10, pady=0, fill="x", side="left")

        dobinput=ctk.CTkEntry(sec2, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        dobinput.pack(padx=10, pady=0, fill="y", side="left")

        sec3=ctk.CTkFrame(self, fg_color="#ffffff")
        sec3.pack(padx=10, pady=10, fill="both")

        lbgender=ctk.CTkLabel(sec3, text="Gender :", width=100)
        lbgender.pack(padx=10, pady=0, fill="x", side="left")
 
        genderinput=ctk.CTkEntry(sec3, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        genderinput.pack(padx=10, pady=0, fill="y", side="left")
        
        lbreligion=ctk.CTkLabel(sec3, text="Religion :", width=100)
        lbreligion.pack(padx=10, pady=0, fill="x", side="left")

        religioninput=ctk.CTkEntry(sec3, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        religioninput.pack(padx=10, pady=0, fill="y", side="left")

        lbnationality=ctk.CTkLabel(sec3, text="Nationality :", width=100)
        lbnationality.pack(padx=10, pady=0, fill="x", side="left")
 
        nationalityinput=ctk.CTkEntry(sec3, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        nationalityinput.pack(padx=10, pady=0, fill="y", side="left")
        
        sec4=ctk.CTkFrame(self, fg_color="#ffffff")
        sec4.pack(padx=10, pady=10, fill="both")
        
        lbcast=ctk.CTkLabel(sec4, text="Cast :", width=100)
        lbcast.pack(padx=10, pady=0, fill="x", side="left")

        castinput=ctk.CTkEntry(sec4, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        castinput.pack(padx=10, pady=0, fill="y", side="left")

        lbcategory=ctk.CTkLabel(sec4, text="Category :", width=100)
        lbcategory.pack(padx=10, pady=0, fill="x", side="left")
 
        categoryinput=ctk.CTkEntry(sec4, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        categoryinput.pack(padx=10, pady=0, fill="y", side="left")
        
        headerframe=ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        headerframe.pack(padx=20, pady=0, fill="both")

        lbh=ctk.CTkLabel(headerframe, text="Residential Information")
        lbh.pack(padx=0, pady=0, fill="y", side="left")
        
        line=ctk.CTkFrame(self, height=1.5, width=width, fg_color="#DADADA")
        line.pack(padx=0, pady=0, fill="y")
        
        sec5=ctk.CTkFrame(self, fg_color="#ffffff")
        sec5.pack(padx=10, pady=(10,0), fill="both")

        lbcity=ctk.CTkLabel(sec5, text="City :", width=100)
        lbcity.pack(padx=10, pady=0, fill="x", side="left")
 
        cityinput=ctk.CTkEntry(sec5, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        cityinput.pack(padx=10, pady=0, fill="y", side="left")

        lbstate=ctk.CTkLabel(sec5, text="State :", width=100)
        lbstate.pack(padx=10, pady=0, fill="x", side="left")
        
        stateinput=ctk.CTkEntry(sec5, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        stateinput.pack(padx=10, pady=0, fill="y", side="left")

        lbcountry=ctk.CTkLabel(sec5, text="Country :", width=100)
        lbcountry.pack(padx=10, pady=0, fill="x", side="left")
 
        countryinput=ctk.CTkEntry(sec5, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        countryinput.pack(padx=10, pady=0, fill="y", side="left")

        sec6=ctk.CTkFrame(self, fg_color="#ffffff")
        sec6.pack(padx=10, pady=10, fill="both")

        lbpadd=ctk.CTkLabel(sec6, text="Postal address :", width=100)
        lbpadd.pack(padx=10, pady=20, fill="x", side="left")
 
        paddinput=ctk.CTkTextbox(sec6, fg_color="#eeeeee", border_width=0, height=50, border_color="#000000", corner_radius=0, width=300) 
        paddinput.pack(padx=10, pady=0, fill="y", side="left")

        lbperadd=ctk.CTkLabel(sec6, text="Permanent address :", width=100)
        lbperadd.pack(padx=10, pady=20, fill="x", side="left")
        
        peraddinput=ctk.CTkTextbox(sec6, fg_color="#eeeeee", border_width=0, height=50, border_color="#000000", corner_radius=0, width=300) 
        peraddinput.pack(padx=10, pady=0, fill="y", side="left")
        
        headerframe=ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        headerframe.pack(padx=20, pady=0, fill="both")

        lbh=ctk.CTkLabel(headerframe, text="Father's Details")
        lbh.pack(padx=0, pady=0, fill="y", side="left")
        
        line=ctk.CTkFrame(self, height=1.5, width=width, fg_color="#DADADA")
        line.pack(padx=0, pady=0, fill="y")
        
        sec7=ctk.CTkFrame(self, fg_color="#ffffff")
        sec7.pack(padx=10, pady=(10,0), fill="both")

        lbftname=ctk.CTkLabel(sec7, text="Name :", width=100)
        lbftname.pack(padx=10, pady=0, fill="x", side="left")
 
        inftname=ctk.CTkEntry(sec7, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        inftname.pack(padx=10, pady=0, fill="y", side="left")

        lbftocc=ctk.CTkLabel(sec7, text="Occupation :", width=100)
        lbftocc.pack(padx=10, pady=0, fill="x", side="left")
        
        inftocc=ctk.CTkEntry(sec7, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        inftocc.pack(padx=10, pady=0, fill="y", side="left")
        
        lbftqual=ctk.CTkLabel(sec7, text="Qualification :", width=100)
        lbftqual.pack(padx=10, pady=0, fill="x", side="left")
 
        inftqual=ctk.CTkEntry(sec7, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        inftqual.pack(padx=10, pady=0, fill="y", side="left")

        sec8=ctk.CTkFrame(self, fg_color="#ffffff")
        sec8.pack(padx=10, pady=(10,0), fill="both")

        lbfttel=ctk.CTkLabel(sec8, text="Phone No :", width=100)
        lbfttel.pack(padx=10, pady=0, fill="x", side="left")
        
        infttel=ctk.CTkEntry(sec8, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        infttel.pack(padx=10, pady=0, fill="y", side="left")

        lbftemail=ctk.CTkLabel(sec8, text="Email Id :", width=100)
        lbftemail.pack(padx=10, pady=0, fill="x", side="left")
        
        inftemail=ctk.CTkEntry(sec8, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        inftemail.pack(padx=10, pady=0, fill="y", side="left")
        
        headerframe=ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        headerframe.pack(padx=20, pady=0, fill="both")

        lbh=ctk.CTkLabel(headerframe, text="Mother's Details")
        lbh.pack(padx=0, pady=0, fill="y", side="left")
        
        line=ctk.CTkFrame(self, height=1.5, width=width, fg_color="#DADADA")
        line.pack(padx=0, pady=0, fill="y")
        
        sec9=ctk.CTkFrame(self, fg_color="#ffffff")
        sec9.pack(padx=10, pady=(10,0), fill="both")

        lbmoname=ctk.CTkLabel(sec9, text="Name :", width=100)
        lbmoname.pack(padx=10, pady=0, fill="x", side="left")
 
        inmoname=ctk.CTkEntry(sec9, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        inmoname.pack(padx=10, pady=0, fill="y", side="left")

        lbmoocc=ctk.CTkLabel(sec9, text="Occupation :", width=100)
        lbmoocc.pack(padx=10, pady=0, fill="x", side="left")
        
        inmoocc=ctk.CTkEntry(sec9, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        inmoocc.pack(padx=10, pady=0, fill="y", side="left")

        lbmoqual=ctk.CTkLabel(sec9, text="Qualification :", width=100)
        lbmoqual.pack(padx=10, pady=0, fill="x", side="left")
 
        inmoqual=ctk.CTkEntry(sec9, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        inmoqual.pack(padx=10, pady=0, fill="y", side="left")

        sec10=ctk.CTkFrame(self, fg_color="#ffffff")
        sec10.pack(padx=10, pady=(10,0), fill="both")

        lbmotel=ctk.CTkLabel(sec10, text="Phone No :", width=100)
        lbmotel.pack(padx=10, pady=0, fill="x", side="left")
        
        inmotel=ctk.CTkEntry(sec10, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        inmotel.pack(padx=10, pady=0, fill="y", side="left")

        lbmoemail=ctk.CTkLabel(sec10, text="Email Id :", width=100)
        lbmoemail.pack(padx=10, pady=0, fill="x", side="left")
        
        inmoemail=ctk.CTkEntry(sec10, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=150) 
        inmoemail.pack(padx=10, pady=0, fill="y", side="left")

        bottombar=ctk.CTkFrame(self, fg_color="#ffffff")
        bottombar.pack(padx=0, pady=0, fill="both")

        submitbt=ctk.CTkButton(bottombar,text="Submit", corner_radius=0)
        submitbt.pack(padx=0, pady=0, side="right")
        
        apply_focus_highlight(self)

        options=com.sregsidebar(master)
        options.pack(padx=10, pady=10, fill="y", side="right")