import customtkinter as ctk
import json
from tkinter import messagebox

class RiwayatPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#F1F1F1")
        self.master = master

        label = ctk.CTkLabel(self, text="Riwayat", font=ctk.CTkFont(size=20, weight="bold", family="Jersey 10"), text_color="#333333")
        label.pack(pady=5, side="top")

        # Navigasi bawah
        menuBawahFrame = ctk.CTkFrame(self)
        menuBawahFrame.pack(side="bottom", fill="x", pady=(5, 0))
        menuBawahFrame.configure(fg_color="#F1F1F1")