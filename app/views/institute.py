import customtkinter as ctk
from fwfiles.UI.decorators import use_masterpage
from fwfiles import routingjunction

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

        lbh=ctk.CTkLabel(headerframe, text="Institute Information")
        lbh.pack(padx=0, pady=0, fill="y", side="left")
        
        line=ctk.CTkFrame(self, height=1.5, width=width, fg_color="#DADADA")
        line.pack(padx=0, pady=0, fill="y")

        sec1=ctk.CTkFrame(self, fg_color="#ffffff")
        sec1.pack(padx=10, pady=(10,0), fill="both")

        lbid=ctk.CTkLabel(sec1, text="School Name :", width=100)
        lbid.pack(padx=10, pady=0, fill="x", side="left")
 
        idinput=ctk.CTkEntry(sec1, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        idinput.pack(padx=10, pady=0, fill="y", side="left")
        
        lbdate=ctk.CTkLabel(sec1, text="Address Line 1 :", width=100)
        lbdate.pack(padx=10, pady=0, fill="x", side="left")
 
        dateinput=ctk.CTkEntry(sec1, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        dateinput.pack(padx=10, pady=0, fill="y", side="left")

        lbname=ctk.CTkLabel(sec1, text="Address Line 2 :", width=100)
        lbname.pack(padx=10, pady=0, fill="x", side="left")

        nameinput=ctk.CTkEntry(sec1, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        nameinput.pack(padx=10, pady=0, fill="y", side="left")

        sec2=ctk.CTkFrame(self, fg_color="#ffffff")
        sec2.pack(padx=10, pady=10, fill="both")
        
        lbadhar=ctk.CTkLabel(sec2, text="Address Line 3. :", width=100)
        lbadhar.pack(padx=10, pady=0, fill="x", side="left")

        adharinput=ctk.CTkEntry(sec2, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        adharinput.pack(padx=10, pady=0, fill="y", side="left")

        lbclass=ctk.CTkLabel(sec2, text="Affiliation Board :", width=100)
        lbclass.pack(padx=10, pady=0, fill="x", side="left")
 
        classinput=ctk.CTkEntry(sec2, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        classinput.pack(padx=10, pady=0, fill="y", side="left")

        lbdob=ctk.CTkLabel(sec2, text="Contact No. :", width=100)
        lbdob.pack(padx=10, pady=0, fill="x", side="left")

        dobinput=ctk.CTkEntry(sec2, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        dobinput.pack(padx=10, pady=0, fill="y", side="left")

        sec3=ctk.CTkFrame(self, fg_color="#ffffff")
        sec3.pack(padx=10, pady=10, fill="both")

        lbgender=ctk.CTkLabel(sec3, text="Email :", width=100)
        lbgender.pack(padx=10, pady=0, fill="x", side="left")
 
        genderinput=ctk.CTkEntry(sec3, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        genderinput.pack(padx=10, pady=0, fill="y", side="left")
        
        lbreligion=ctk.CTkLabel(sec3, text="Country :", width=100)
        lbreligion.pack(padx=10, pady=0, fill="x", side="left")

        religioninput=ctk.CTkEntry(sec3, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        religioninput.pack(padx=10, pady=0, fill="y", side="left")

        lbnationality=ctk.CTkLabel(sec3, text="State :", width=100)
        lbnationality.pack(padx=10, pady=0, fill="x", side="left")
 
        nationalityinput=ctk.CTkEntry(sec3, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        nationalityinput.pack(padx=10, pady=0, fill="y", side="left")
        
        sec4=ctk.CTkFrame(self, fg_color="#ffffff")
        sec4.pack(padx=10, pady=10, fill="both")
        
        lbcast=ctk.CTkLabel(sec4, text="City :", width=100)
        lbcast.pack(padx=10, pady=0, fill="x", side="left")

        castinput=ctk.CTkEntry(sec4, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        castinput.pack(padx=10, pady=0, fill="y", side="left")

        lbcategory=ctk.CTkLabel(sec4, text="Pincode :", width=100)
        lbcategory.pack(padx=10, pady=0, fill="x", side="left")
 
        categoryinput=ctk.CTkEntry(sec4, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        categoryinput.pack(padx=10, pady=0, fill="y", side="left")

        lbcategory=ctk.CTkLabel(sec4, text="Website :", width=100)
        lbcategory.pack(padx=10, pady=0, fill="x", side="left")
 
        categoryinput=ctk.CTkEntry(sec4, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=250) 
        categoryinput.pack(padx=10, pady=0, fill="y", side="left")
        
        headerframe=ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        headerframe.pack(padx=20, pady=0, fill="both")

        lbh=ctk.CTkLabel(headerframe, text="Management Information")
        lbh.pack(padx=0, pady=0, fill="y", side="left")
        
        line=ctk.CTkFrame(self, height=1.5, width=width, fg_color="#DADADA")
        line.pack(padx=0, pady=0, fill="y")
        
        sec5=ctk.CTkFrame(self, fg_color="#ffffff")
        sec5.pack(padx=10, pady=(10,0), fill="both")

        lbcity=ctk.CTkLabel(sec5, text="Principal Name :", width=100)
        lbcity.pack(padx=10, pady=0, fill="x", side="left")
 
        cityinput=ctk.CTkEntry(sec5, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=450) 
        cityinput.pack(padx=10, pady=0, fill="y", side="left")

        lbstate=ctk.CTkLabel(sec5, text="Contact :", width=100)
        lbstate.pack(padx=10, pady=0, fill="x", side="left")
        
        stateinput=ctk.CTkEntry(sec5, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=450) 
        stateinput.pack(padx=10, pady=0, fill="y", side="left")

        sec6=ctk.CTkFrame(self, fg_color="#ffffff")
        sec6.pack(padx=10, pady=10, fill="both")

        lbcountry=ctk.CTkLabel(sec6, text="Manager :", width=100)
        lbcountry.pack(padx=10, pady=0, fill="x", side="left")
 
        countryinput=ctk.CTkEntry(sec6, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=450) 
        countryinput.pack(padx=10, pady=0, fill="y", side="left")

        lbpadd=ctk.CTkLabel(sec6, text="Mobile No. :", width=100)
        lbpadd.pack(padx=10, pady=0, fill="x", side="left")
 
        paddinput=ctk.CTkEntry(sec6, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=450) 
        paddinput.pack(padx=10, pady=0, fill="y", side="left")
        
        headerframe=ctk.CTkFrame(self, fg_color="#FFFFFF", corner_radius=0)
        headerframe.pack(padx=20, pady=0, fill="both")

        lbh=ctk.CTkLabel(headerframe, text="Security")
        lbh.pack(padx=0, pady=0, fill="y", side="left")
        
        line=ctk.CTkFrame(self, height=1.5, width=width, fg_color="#DADADA")
        line.pack(padx=0, pady=0, fill="y")
        
        sec7=ctk.CTkFrame(self, fg_color="#ffffff")
        sec7.pack(padx=10, pady=(10,0), fill="both")

        lbftname=ctk.CTkLabel(sec7, text="Password :", width=100)
        lbftname.pack(padx=10, pady=0, fill="x", side="left")
 
        inftname=ctk.CTkEntry(sec7, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=450) 
        inftname.pack(padx=10, pady=0, fill="y", side="left")

        lbftocc=ctk.CTkLabel(sec7, text="Confirm Password :", width=100)
        lbftocc.pack(padx=10, pady=0, fill="x", side="left")
        
        inftocc=ctk.CTkEntry(sec7, fg_color="#eeeeee", border_width=0, border_color="#000000", corner_radius=0, width=450) 
        inftocc.pack(padx=10, pady=0, fill="y", side="left")
        
        bottombar=ctk.CTkFrame(self, fg_color="#ffffff")
        bottombar.pack(padx=0, pady=0, fill="both")

        submitbt=ctk.CTkButton(bottombar,text="Submit", corner_radius=0)
        submitbt.pack(padx=0, pady=10, side="right")
        
        apply_focus_highlight(self)