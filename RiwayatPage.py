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

        homeLabel = ctk.CTkLabel(menuBawahFrame, text="Pomodoro", text_color="black",
                                  font=ctk.CTkFont("jersey 10", 15), cursor="hand2")
        homeLabel.pack(side="left", padx=10, pady=5)
        homeLabel.bind("<Button-1>", lambda e: self.master.show_HomePage())
        homeLabel.bind("<Enter>", lambda e: homeLabel.configure(text_color="#606060"))
        homeLabel.bind("<Leave>", lambda e: homeLabel.configure(text_color="black"))

        TaskListLabel = ctk.CTkLabel(menuBawahFrame, text="Task List", font=ctk.CTkFont("jersey 10", 15), text_color="#333333")
        TaskListLabel.pack(side="right", padx=10, pady=5)
        TaskListLabel.bind("<Enter>", lambda e: TaskListLabel.configure(text_color="#606060"))
        TaskListLabel.bind("<Leave>", lambda e: TaskListLabel.configure(text_color="black"))

        # Frame utama
        frame = ctk.CTkFrame(self, fg_color="#823F3F")
        frame.pack(pady=5, padx=10, expand=True, fill="both")

        # Header
        headerFrame = ctk.CTkFrame(frame, fg_color="#823F3F")
        headerFrame.pack(fill="x")

        # Konfigurasi kolom header
        headerFrame.grid_columnconfigure(0, weight=1)
        headerFrame.grid_columnconfigure(1, weight=1)
        headerFrame.grid_columnconfigure(2, weight=1)
        headerFrame.grid_columnconfigure(3, weight=0)

        # Label header
        labelSession = ctk.CTkLabel(headerFrame, text="SESSION", font=ctk.CTkFont(size=15, weight="bold", family="Jersey 10"), text_color="#F1F1F1")
        labelSession.grid(row=0, column=0, padx=10, pady=2, sticky="nsew")

        labelTask = ctk.CTkLabel(headerFrame, text="TASK", font=ctk.CTkFont(size=15, weight="bold", family="Jersey 10"), text_color="#F1F1F1")
        labelTask.grid(row=0, column=1, padx=10, pady=2, sticky="nsew")

        labelStatus = ctk.CTkLabel(headerFrame, text="STATUS", font=ctk.CTkFont(size=15, weight="bold", family="Jersey 10"), text_color="#72E865")
        labelStatus.grid(row=0, column=2, padx=10, pady=2, sticky="nsew")

        # Scrollable frame untuk isi data
        self.scrollFrame = ctk.CTkScrollableFrame(frame, fg_color="#823F3F")
        self.scrollFrame.pack(expand=True, fill="both", padx=0, pady=0)

        # Konfigurasi kolom isi
        self.scrollFrame.grid_columnconfigure(0, weight=1)
        self.scrollFrame.grid_columnconfigure(1, weight=1)
        self.scrollFrame.grid_columnconfigure(2, weight=1)
        self.scrollFrame.grid_columnconfigure(3, weight=0)

        self.load_and_display_data()  # Memuat dan menampilkan data saat inisialisasi

    def load_and_display_data(self):

        for widget in self.scrollFrame.winfo_children():
            widget.destroy()
        
        try:
            with open("pomodoro_sessions.json", 'r') as file:
                d = json.load(file)
        except FileNotFoundError:
            d = []
        except json.JSONDecodeError:
            d = [] # Handle empty or invalid JSON

        # Menambahkan data ke scrollable frame
        for i, item in enumerate(d):
            session_label = ctk.CTkLabel(self.scrollFrame, text=item["tanggal"], font=ctk.CTkFont(size=15, family="Jersey 10"), text_color="#F1F1F1")
            session_label.grid(row=i, column=0, padx=10, pady=0, sticky="nsew")

            task_label = ctk.CTkLabel(self.scrollFrame, text=item["judul"], font=ctk.CTkFont(size=15, family="Jersey 10"), text_color="#F1F1F1")
            task_label.grid(row=i, column=1, padx=10, pady=0, sticky="nsew")

            status_label = ctk.CTkLabel(self.scrollFrame, text="COMPLETED", font=ctk.CTkFont(size=15, family="Jersey 10"), text_color="#72E865")
            status_label.grid(row=i, column=2, padx=10, pady=0, sticky="nsew")

            delete_button = ctk.CTkButton(
                self.scrollFrame,
                text="Delete",
                command=lambda index=i: self.delete_entry(index),
                font=ctk.CTkFont(size=12, family="Jersey 10"),
                fg_color="#CC3333", hover_color="#AA2222",
                text_color="#F1F1F1",
                width=20,  height=20 
            )
            delete_button.grid(row=i, column=3, padx=5, pady=2, sticky="e")

    def delete_entry(self, index_to_delete):
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this entry?"):
            try:
                with open("pomodoro_sessions.json", 'r') as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []
            except json.JSONDecodeError:
                data = []

            if 0 <= index_to_delete < len(data):
                del data[index_to_delete]
                with open("pomodoro_sessions.json", 'w') as file:
                    json.dump(data, file, indent=4)
                self.load_and_display_data() 
            else:
                messagebox.showerror("Error", "Invalid index for deletion.")
        