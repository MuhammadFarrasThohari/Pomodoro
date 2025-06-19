import customtkinter as ctk
import json
import os

FILE_NAME = "task_data.json"

# Load dari file JSON
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

# Simpan ke file JSON
def save_tasks(task_list):
    with open(FILE_NAME, "w") as f:
        json.dump(task_list, f)

# Tambah ke UI dan simpan
def add_task_to_ui(task_text):
    cb = ctk.CTkCheckBox(
        scrollFrame,
        text=task_text,
        font=ctk.CTkFont(family="jersey 10", size=18),
        checkbox_height=20,
        checkbox_width=20,
        text_color="white"
    )
    cb.pack(anchor="w", padx=10, pady=4)
    checkbox_list.append(cb)

# Saat klik "Add a task"
def on_add_task():
    popup = ctk.CTkToplevel()
    popup.title("Tambah Task")
    popup.geometry("300x120")
    popup.grab_set()  # Fokus di popup

    label = ctk.CTkLabel(popup, text="Masukkan nama task:")
    label.pack(pady=(10, 5))

    entry = ctk.CTkEntry(popup, width=250)
    entry.pack(pady=(0, 10))
    entry.bind("<Return>", lambda event: save_and_close())

    def save_and_close():
        new_task = entry.get()
        if new_task.strip() != "":
            tasks.append(new_task)
            save_tasks(tasks)
            add_task_to_ui(new_task)
        popup.destroy()

    submit_btn = ctk.CTkButton(popup, text="Simpan", command=save_and_close)
    submit_btn.pack(pady=(0, 10))


# -------- UI ---------
root = ctk.CTk()
root.geometry("400x300")
root.title("Pomodoro")
root.configure(fg_color="#F1F1F1")
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

# Judul
titleLabel = ctk.CTkLabel(root, text="Task List", font=ctk.CTkFont(family="jersey 10", size=20), text_color="#000000")
titleLabel.grid(row=0, column=0, pady=(10, 0))

# Form hijau
formFrame = ctk.CTkFrame(root, fg_color="#4CAF50", corner_radius=0)
formFrame.grid(row=1, column=0, padx=10, pady=(5, 0), sticky="nsew")
formFrame.grid_rowconfigure(0, weight=1)
formFrame.grid_columnconfigure(0, weight=1)

# Scroll task
scrollFrame = ctk.CTkScrollableFrame(
    formFrame, fg_color="#4CAF50", label_fg_color="#4CAF50", scrollbar_button_color="#CFCFCF"
)
scrollFrame.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 0))

# Load tasks dari file
tasks = load_tasks()
checkbox_list = []
for task in tasks:
    add_task_to_ui(task)


# Container baru untuk tombol dan label
add_container = ctk.CTkFrame(formFrame, fg_color="#4CAF50")
add_container.grid(row=1, column=0, sticky="w", padx=10, pady=(5, 10))

# Tombol bulat "+"
add_btn = ctk.CTkButton(
    add_container,
    text="+",
    width=10,
    height=15,
    font=ctk.CTkFont(size=24, weight="bold"),
    fg_color="white",
    text_color="#4CAF50",
    hover_color="#E8F5E9",
    corner_radius=100,
    command=on_add_task
)
add_btn.pack(side="left", padx=(5, 10), pady=5)

# Label "Add a task"
add_label = ctk.CTkLabel(
    add_container,
    text="Add a task",
    font=ctk.CTkFont(family="jersey 10", size=18),
    text_color="white"
)
add_label.pack(side="left", pady=5)



# Menu bawah
menuBawahFrame = ctk.CTkFrame(root, fg_color="#F1F1F1")
menuBawahFrame.grid(row=2, column=0, sticky="ew")
menuBawahFrame.grid_columnconfigure((0, 1), weight=1)

taskListLabel = ctk.CTkLabel(menuBawahFrame, text="Pomodoro", text_color="black", font=ctk.CTkFont(family="jersey 10", size=18), cursor="hand2")
taskListLabel.grid(row=0, column=0, sticky="w", padx=10, pady=10)
import subprocess
import sys

def open_home_py():
    root.destroy()  # tutup window sekarang
    subprocess.Popen([sys.executable, "home.py"])

taskListLabel.bind("<Button-1>", lambda e: open_home_py())


riwayatLabel = ctk.CTkLabel(menuBawahFrame, text="Riwayat", text_color="black", font=ctk.CTkFont(family="jersey 10", size=18), cursor="hand2")
riwayatLabel.grid(row=0, column=1, sticky="e", padx=10, pady=10)
riwayatLabel.bind("<Button-1>", lambda e: print("Open Riwayat"))

root.mainloop()
