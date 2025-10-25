from tkinter import *
import customtkinter as ctk
from . import component as com
from . import configuration as conf
from fwfiles.UI.decorators import use_masterpage


@use_masterpage("app.views.layout.Layout_default")
class index(ctk.CTkScrollableFrame):
    def __init__(self, master, height, width, data={}, **kwargs):
        super().__init__(master, corner_radius=0, fg_color="#ffffff", height=height, width=width, **kwargs)

        servicetray=ctk.CTkFrame(self, fg_color="#ffffff", corner_radius=10)
        servicetray.pack(pady=10, padx=10, fill="both")

        imagebanner=ctk.CTkFrame(servicetray, width=1500)
        imagebanner.pack(pady=10, padx=10, fill="both")

        servicecardtray1=ctk.CTkFrame(servicetray, fg_color="#ebebeb")
        servicecardtray1.pack(pady=10, padx=10, fill="both", expand=True)

        cards = []
        for i in conf.servicecard:
            card = com.Card(servicecardtray1, title=i["title"], content=i["content"])
            cards.append(card)

        def arrange_cards(event=None):
            width = servicecardtray1.winfo_width()
            card_width = 250  
            cols = max(1, width // card_width)  

            for idx, card in enumerate(cards):
                row = idx // cols
                col = idx % cols
                card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
                
            for c in range(cols):
                servicecardtray1.grid_columnconfigure(c, weight=1)

        servicecardtray1.bind("<Configure>", arrange_cards)


