import customtkinter as ctk
import json

# Inisialisasi jendela utama
root = ctk.CTk()
root.geometry("400x300")
root.title("Riwayat")
root.configure(fg_color="#F1F1F1")

# Label judul
label = ctk.CTkLabel(root, text="Riwayat", font=ctk.CTkFont(size=20, weight="bold", family="Jersey 10"), text_color="#333333")
label.pack(pady=5)

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

# Label header
labelSession = ctk.CTkLabel(headerFrame, text="SESSION", font=ctk.CTkFont(size=15, weight="bold", family="Jersey 10"), text_color="#F1F1F1")
labelSession.grid(row=0, column=0, padx=10, pady=2, sticky="nsew")

labelTask = ctk.CTkLabel(headerFrame, text="TASK", font=ctk.CTkFont(size=15, weight="bold", family="Jersey 10"), text_color="#F1F1F1")
labelTask.grid(row=0, column=1, padx=10, pady=2, sticky="nsew")

labelStatus = ctk.CTkLabel(headerFrame, text="STATUS", font=ctk.CTkFont(size=15, weight="bold", family="Jersey 10"), text_color="#F1F1F1")
labelStatus.grid(row=0, column=2, padx=10, pady=2, sticky="nsew")

# Scrollable frame untuk isi data
scrollFrame = ctk.CTkScrollableFrame(frame, fg_color="#823F3F")
scrollFrame.pack(expand=True, fill="both", padx=0, pady=0)

# Konfigurasi kolom isi
scrollFrame.grid_columnconfigure(0, weight=1)
scrollFrame.grid_columnconfigure(1, weight=1)
scrollFrame.grid_columnconfigure(2, weight=1)


with open("pomodoro_sessions.json") as file:
    d = json.load(file)
    print(d[0]['tanggal'])
    print(d[0]['judul'])



# Menambahkan data ke scrollable frame
for i, item in enumerate(d):
    session_label = ctk.CTkLabel(scrollFrame, text=item["tanggal"], font=ctk.CTkFont(size=15, family="Jersey 10"), text_color="#F1F1F1")
    session_label.grid(row=i, column=0, padx=10, pady=0, sticky="nsew")

    task_label = ctk.CTkLabel(scrollFrame, text=item["judul"], font=ctk.CTkFont(size=15, family="Jersey 10"), text_color="#F1F1F1")
    task_label.grid(row=i, column=1, padx=10, pady=0, sticky="nsew")

    status_label = ctk.CTkLabel(scrollFrame, text="COMPLETED", font=ctk.CTkFont(size=15, family="Jersey 10"), text_color="#72E865")
    status_label.grid(row=i, column=2, padx=10, pady=0, sticky="nsew")


# Menjalankan aplikasi
root.mainloop()
