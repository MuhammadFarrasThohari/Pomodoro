import customtkinter as ctk
import json
import subprocess
from tkinter import messagebox 

# Inisialisasi jendela utama
root = ctk.CTk()
root.geometry("400x300") 
root.title("Riwayat")
root.configure(fg_color="#F1F1F1")

# Label judul 
label = ctk.CTkLabel(root, text="Riwayat", font=ctk.CTkFont(size=20, weight="bold", family="Jersey 10"), text_color="#333333")
label.pack(pady=5, side="top") # Explicitly pack to top

# Navigasi bawah 
menuBawahFrame = ctk.CTkFrame(root)
menuBawahFrame.pack(side="bottom", fill="x", pady=(5,0)) 
menuBawahFrame.configure(fg_color="#F1F1F1")

def buka_home(current_wdw):
    current_wdw.destroy()
    subprocess.Popen(['python', 'Home.py'])

homeLabel = ctk.CTkLabel(menuBawahFrame, text="Back to home", text_color="black",
                          font=ctk.CTkFont("jersey 10", 15), cursor="hand2")
homeLabel.pack(side="left", padx=10, pady=6)
homeLabel.bind("<Button-1>", lambda e: buka_home(root))
homeLabel.bind("<Enter>", lambda e: homeLabel.configure(text_color='#606060'))
homeLabel.bind("<Leave>", lambda e: homeLabel.configure(text_color='black'))

# Frame utama 
frame = ctk.CTkFrame(root, fg_color="#823F3F")
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
scrollFrame = ctk.CTkScrollableFrame(frame, fg_color="#823F3F")
scrollFrame.pack(expand=True, fill="both", padx=0, pady=0) 

# Konfigurasi kolom isi
scrollFrame.grid_columnconfigure(0, weight=1)
scrollFrame.grid_columnconfigure(1, weight=1)
scrollFrame.grid_columnconfigure(2, weight=1)
scrollFrame.grid_columnconfigure(3, weight=0) 

# Function to load and display data
def load_and_display_data():
    
    for widget in scrollFrame.winfo_children():
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
        session_label = ctk.CTkLabel(scrollFrame, text=item["tanggal"], font=ctk.CTkFont(size=15, family="Jersey 10"), text_color="#F1F1F1")
        session_label.grid(row=i, column=0, padx=10, pady=0, sticky="nsew")

        task_label = ctk.CTkLabel(scrollFrame, text=item["judul"], font=ctk.CTkFont(size=15, family="Jersey 10"), text_color="#F1F1F1")
        task_label.grid(row=i, column=1, padx=10, pady=0, sticky="nsew")

        status_label = ctk.CTkLabel(scrollFrame, text="COMPLETED", font=ctk.CTkFont(size=15, family="Jersey 10"), text_color="#72E865")
        status_label.grid(row=i, column=2, padx=10, pady=0, sticky="nsew")

        delete_button = ctk.CTkButton(
            scrollFrame,
            text="Delete",
            command=lambda index=i: delete_entry(index),
            font=ctk.CTkFont(size=12, family="Jersey 10"),
            fg_color="#CC3333", hover_color="#AA2222",
            text_color="#F1F1F1",
            width=20,  height=20 
        )
        delete_button.grid(row=i, column=3, padx=5, pady=2, sticky="e")

# Delete an entry
def delete_entry(index_to_delete):
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
            load_and_display_data() 
        else:
            messagebox.showerror("Error", "Invalid index for deletion.")

# Load and display data initially
load_and_display_data()

# Menjalankan aplikasi
root.mainloop()