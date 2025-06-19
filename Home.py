import customtkinter as ctk
import datetime
import os
import json
import subprocess

# Membuat window utama
root = ctk.CTk()
root.geometry("400x300")
root.title("Pomodoro")
root.configure(fg_color="#F1F1F1")
root.resizable(False, False)
root._set_appearance_mode("system")  # Atur mode tampilan sesuai sistem
root.iconbitmap("TOMAT.ico")

# Variabel waktu
menit = 0
detik = 0

# Variabel jumlah break dan focus
waktu_mulai = None
jumlah_fokus = 0
jumlah_Shortbreak = 0
jumlah_Longbreak = 0

# State timer
timer_id = None
is_paused = False
current_phase = "Focus"
cycle_count = 0

def update_timer_display():
    timeLabel.configure(text=f"{menit:02d}:{detik:02d}")
    statusLabel.configure(text=current_phase)

def countdown():
    global menit, detik, timer_id, cycle_count, current_phase

    if not is_paused:
        if menit == 0 and detik == 0:
            # Berpindah ke fase berikutnya
            if current_phase == "Focus":
                cycle_count += 1
                if cycle_count % 4 == 0:
                    switch_phase("Long Break")
                else:
                    switch_phase("Short Break")
            elif current_phase in ["Short Break", "Long Break"]:
                switch_phase("Focus")
            return

        if detik == 0:
            menit -= 1
            detik = 59
        else:
            detik -= 1

        update_timer_display()
        timer_id = root.after(1000, countdown)

def switch_phase(phase):
    global current_phase, menit, detik, jumlah_fokus, jumlah_Shortbreak, jumlah_Longbreak

    current_phase = phase
    if phase == "Focus":
        menit = int(focusEntryMinute.get() or 0)
        detik = int(focusEntrySeconds.get() or 0)
        jumlah_fokus += 1
    elif phase == "Short Break":
        menit = int(shortBreakEntryMinute.get() or 0)
        detik = int(shortBreakEntrySecond.get() or 0)
        jumlah_Shortbreak += 1
    elif phase == "Long Break":
        menit = int(longBreakEntryMinute.get() or 0)
        detik = int(longBreakEntrySecond.get() or 0)
        jumlah_Longbreak += 1

    update_timer_display()
    countdown()

def start_timer():
    global is_paused, waktu_mulai, jumlah_fokus, jumlah_Shortbreak, jumlah_Longbreak

    if (not focusEntryMinute.get() or not focusEntrySeconds.get() or
        not shortBreakEntryMinute.get() or not shortBreakEntrySecond.get() or
        not longBreakEntryMinute.get() or not longBreakEntrySecond.get()):
        print("Mohon isi semua field waktu.")
        return

    is_paused = False
    switch_phase("Focus")
    waktu_mulai = datetime.datetime.now()
    jumlah_fokus = 0
    jumlah_Shortbreak = 0
    jumlah_Longbreak = 0


def pause_timer():
    global is_paused
    is_paused = True
    if timer_id:
        root.after_cancel(timer_id)
    statusLabel.configure(text="Paused")
    

def stop_timer():
    global waktu_mulai, jumlah_fokus, jumlah_Shortbreak, jumlah_Longbreak

    if waktu_mulai:
        waktu_selesai = datetime.datetime.now()
        judul = judulEntry.get() or "Tanpa Judul"
        simpan_riwayat_sesi(judul, waktu_mulai, waktu_selesai, jumlah_fokus, jumlah_Shortbreak, jumlah_Longbreak)
        print(f"Disimpan: {judul} ({jumlah_fokus} fokus, {jumlah_Shortbreak} short break, {jumlah_Longbreak} long break)")

    else:
        print("Belum ada sesi dimulai.")

    # Reset tampilan dan variabel
    waktu_mulai = None
    jumlah_fokus = 0
    jumlah_Shortbreak = 0
    jumlah_Longbreak = 0
    timeLabel.configure(text="00:00")
    statusLabel.configure(text="Stopped")
    root.after_cancel(timer_id) if timer_id else None



def simpan_riwayat_sesi(judul, waktu_mulai, waktu_selesai, fokus, Sbrk, Lbrk):
    durasi = waktu_selesai - waktu_mulai

    log = {
        "tanggal": waktu_mulai.strftime("%Y-%m-%d"),
        "judul": judul,
        "mulai": waktu_mulai.strftime("%H:%M:%S"),
        "selesai": waktu_selesai.strftime("%H:%M:%S"),
        "jumlah_fokus": fokus,
        "jumlah_Shortbreak": Sbrk,
        "jumlah_Longbreak": Lbrk,
        "total_durasi": str(durasi)
    }

    path = "pomodoro_sessions.json"
    if os.path.exists(path):
        with open(path, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(log)

    with open(path, "w") as f:
        json.dump(data, f, indent=4)


# Form input
formFrame = ctk.CTkFrame(root, fg_color="#F1F1F1")
formFrame.pack(pady=0, padx=10)

def entry_field(row, label, column_offset):
    labelWidget = ctk.CTkLabel(formFrame, text=label, font=ctk.CTkFont("jersey 10", 15), text_color="#333333")
    labelWidget.grid(row=row, column=0 + column_offset, padx=5, pady=5)

    entryMinute = ctk.CTkEntry(formFrame, width=25, font=ctk.CTkFont("jersey 10", 15), fg_color="transparent",
                               text_color="black", border_width=0, placeholder_text="00")
    entryMinute.grid(row=row, column=1 + column_offset, padx=0, pady=5)

    labelPemisah = ctk.CTkLabel(formFrame, text=":", font=ctk.CTkFont("jersey 10", 15), text_color="#333333")
    labelPemisah.grid(row=row, column=2 + column_offset, padx=0, pady=5)

    entrySecond = ctk.CTkEntry(formFrame, width=25, font=ctk.CTkFont("jersey 10", 15), fg_color="transparent",
                                text_color="black", border_width=0, placeholder_text="00")
    entrySecond.grid(row=row, column=3 + column_offset, padx=0, pady=5)

    return entryMinute, entrySecond

focusEntryMinute, focusEntrySeconds = entry_field(0, "Focus :", 0)
shortBreakEntryMinute, shortBreakEntrySecond = entry_field(0, "Short Break :", 4)
longBreakEntryMinute, longBreakEntrySecond = entry_field(0, "Long Break :", 8)

# Label status & waktu
statusLabel = ctk.CTkLabel(root, text="Focus", font=ctk.CTkFont("jersey 10", 20), text_color="#333333")
statusLabel.pack(pady=0)

timeLabel = ctk.CTkLabel(root, text="00:00", font=ctk.CTkFont("jersey 10", 50), text_color="#333333")
timeLabel.pack(pady=0)

# Tombol kontrol utama
startButton = ctk.CTkButton(root, text="Start", command=start_timer, width=100, height=40, fg_color="#4F9747",
                            text_color="white", font=ctk.CTkFont("jersey 10", 15), hover=False)
startButton.pack(pady=3)

buttonBawahFrame = ctk.CTkFrame(root)
buttonBawahFrame.pack()
buttonBawahFrame.configure(fg_color="#F1F1F1")
buttonBawahFrame.grid_columnconfigure(0, weight=1)
buttonBawahFrame.grid_columnconfigure(1, weight=1)

resetButton = ctk.CTkButton(buttonBawahFrame, text="Stop", fg_color="transparent", command=stop_timer,
                            width=100, height=40, text_color="#C72C41", font=ctk.CTkFont("jersey 10", 15),
                            hover_color="#D79CA5", border_color="#C72C41", border_width=2)
resetButton.grid(row=0, column=0, padx=5, pady=5)

pauseButton = ctk.CTkButton(buttonBawahFrame, text="Pause", fg_color="transparent", command=pause_timer,
                            width=100, height=40, text_color="#F6A600", font=ctk.CTkFont("jersey 10", 15),
                            hover_color="#F3E3C4", border_color="#F6A600", border_width=2)
pauseButton.grid(row=0, column=1, padx=5, pady=5)

# Navigasi bawah
menuBawahFrame = ctk.CTkFrame(root)
menuBawahFrame.pack(side="bottom", fill="x")
menuBawahFrame.configure(fg_color="#F1F1F1")

judulEntry = ctk.CTkEntry(root, width=250, placeholder_text="Judul sesi (misal: Belajar AI)", 
                          font=ctk.CTkFont("jersey 10", size=15), fg_color="white", text_color="black")
judulEntry.pack(pady=10)

def buka_task_list(current_wdw):
    current_wdw.destroy()
    subprocess.Popen(['python', 'Riwayat.py'])

taskListLabel = ctk.CTkLabel(menuBawahFrame, text="Task List", text_color="black",
                             font=ctk.CTkFont("jersey 10", 15), cursor="hand2")
taskListLabel.pack(side="left", padx=10, pady=10)
taskListLabel.bind("<Button-1>", lambda e: print("Open Task List"))


def buka_riwayat(current_wdw):
    current_wdw.destroy()
    subprocess.Popen(['python', 'Riwayat.py'])


riwayatLabel = ctk.CTkLabel(menuBawahFrame, text="Riwayat", text_color="black",
                            font=ctk.CTkFont("jersey 10", 15), cursor="hand2")
riwayatLabel.pack(side="right", padx=10, pady=10)
riwayatLabel.bind("<Button-1>", lambda e: buka_riwayat(root))

riwayatLabel.bind("<Enter>", lambda e: riwayatLabel.configure(text_color="#606060"))
riwayatLabel.bind("<Leave>", lambda e: riwayatLabel.configure(text_color="black"))

root.mainloop()
