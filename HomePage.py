import customtkinter as ctk
import datetime
import os
import json


class HomePage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#F1F1F1")

        # Variabel waktu
        self.menit = 0
        self.detik = 0

        # Variabel jumlah break dan focus
        self.waktu_mulai = None
        self.jumlah_fokus = 0
        self.jumlah_Shortbreak = 0
        self.jumlah_Longbreak = 0

        # State timer
        self.timer_id = None
        self.is_paused = False
        self.current_phase = "Focus"
        self.cycle_count = 0

        # Frame input
        formFrame = ctk.CTkFrame(self, fg_color="#F1F1F1")
        formFrame.pack(padx=10)

        # Buat entry field
        self.focusEntryMinute, self.focusEntrySeconds = self.entry_field(formFrame, 0, "Focus :", 0)
        self.shortBreakEntryMinute, self.shortBreakEntrySeconds = self.entry_field(formFrame, 0, "Short Break :", 4)
        self.longBreakEntryMinute, self.longBreakEntrySeconds = self.entry_field(formFrame, 0, "Long Break :", 8)

        # Label status & waktu
        self.statusLabel = ctk.CTkLabel(self, text="Focus", font=ctk.CTkFont("jersey 10", 20), text_color="#333333")
        self.statusLabel.pack(pady=0)

        self.timeLabel = ctk.CTkLabel(self, text="00:00", font=ctk.CTkFont("jersey 10", 50), text_color="#333333")
        self.timeLabel.pack(pady=0)

        # Tombol kontrol utama
        startButton = ctk.CTkButton(self, text="Start", command=self.start_timer, width=100, height=40, fg_color="#4F9747",
                                    text_color="white", font=ctk.CTkFont("jersey 10", 15), hover=False)
        startButton.pack(pady=3)
        buttonBawahFrame = ctk.CTkFrame(self)
        buttonBawahFrame.pack()
        buttonBawahFrame.configure(fg_color="#F1F1F1")
        buttonBawahFrame.grid_columnconfigure(0, weight=1)
        buttonBawahFrame.grid_columnconfigure(1, weight=1)

        resetButton = ctk.CTkButton(buttonBawahFrame, text="Stop", fg_color="transparent", command=self.stop_timer,
                            width=100, height=40, text_color="#C72C41", font=ctk.CTkFont("jersey 10", 15),
                            hover_color="#D79CA5", border_color="#C72C41", border_width=2)
        resetButton.grid(row=0, column=0, padx=5, pady=5)

        pauseButton = ctk.CTkButton(buttonBawahFrame, text="Pause", fg_color="transparent", command=self.pause_timer,
                                    width=100, height=40, text_color="#F6A600", font=ctk.CTkFont("jersey 10", 15),
                                    hover_color="#F3E3C4", border_color="#F6A600", border_width=2)
        pauseButton.grid(row=0, column=1, padx=5, pady=5)

        judulEntry = ctk.CTkEntry(self, width=250, placeholder_text="Judul sesi (misal: Belajar AI)", 
                          font=ctk.CTkFont("jersey 10", size=15), fg_color="white", text_color="black")
        judulEntry.pack(pady=10)


        menuBawahFrame = ctk.CTkFrame(self)
        menuBawahFrame.pack(side="bottom", fill="x")
        menuBawahFrame.configure(fg_color="#F1F1F1")

        taskListLabel = ctk.CTkLabel(menuBawahFrame, text="Task List", font=ctk.CTkFont("jersey 10", 15), text_color="#333333")
        taskListLabel.pack(side="left", padx=10, pady=5)
        taskListLabel.bind("<Button-1>", lambda e: self.master.show_TaskListPage())
        taskListLabel.bind("<Enter>", lambda e: taskListLabel.configure(text_color="#606060"))
        taskListLabel.bind("<Leave>", lambda e: taskListLabel.configure(text_color="#333333"))

        riwayatLabel = ctk.CTkLabel(menuBawahFrame, text="Riwayat", font=ctk.CTkFont("jersey 10", 15), text_color="#333333")
        riwayatLabel.pack(side="right", padx=10, pady=5)
        riwayatLabel.bind("<Button-1>", lambda e: self.master.show_RiwayatPage())
        riwayatLabel.bind("<Enter>", lambda e: riwayatLabel.configure(text_color="#606060"))
        riwayatLabel.bind("<Leave>", lambda e: riwayatLabel.configure(text_color="#333333"))

    def entry_field(self, parent, row, label, column_offset):
        labelWidget = ctk.CTkLabel(parent, text=label, font=ctk.CTkFont("jersey 10", 15), text_color="#333333")
        labelWidget.grid(row=row, column=0 + column_offset, padx=5, pady=5)

        entryMinute = ctk.CTkEntry(parent, width=25, font=ctk.CTkFont("jersey 10", 15),
                                   fg_color="transparent", text_color="black", border_width=0, placeholder_text="00")
        entryMinute.grid(row=row, column=1 + column_offset, padx=0, pady=5)

        labelPemisah = ctk.CTkLabel(parent, text=":", font=ctk.CTkFont("jersey 10", 15), text_color="#333333")
        labelPemisah.grid(row=row, column=2 + column_offset, padx=0, pady=5)

        entrySecond = ctk.CTkEntry(parent, width=25, font=ctk.CTkFont("jersey 10", 15),
                                   fg_color="transparent", text_color="black", border_width=0, placeholder_text="00")
        entrySecond.grid(row=row, column=3 + column_offset, padx=0, pady=5)

        return entryMinute, entrySecond

    def update_timer_display(self):
        self.timeLabel.configure(text=f"{self.menit:02d}:{self.detik:02d}")
        self.statusLabel.configure(text=self.current_phase)

    def countdown(self):
        if not self.is_paused:
            if self.menit == 0 and self.detik == 0:
                if self.current_phase == "Focus":
                    self.cycle_count += 1
                    if self.cycle_count % 4 == 0:
                        self.switch_phase("Long Break")
                    else:
                        self.switch_phase("Short Break")
                elif self.current_phase in ["Short Break", "Long Break"]:
                    self.switch_phase("Focus")
                return

            if self.detik == 0:
                self.menit -= 1
                self.detik = 59
            else:
                self.detik -= 1

            self.update_timer_display()
            self.timer_id = self.master.after(1000, self.countdown)

    def switch_phase(self, phase):
        self.current_phase = phase
        if phase == "Focus":
            self.menit = int(self.focusEntryMinute.get() or 0)
            self.detik = int(self.focusEntrySeconds.get() or 0)
            self.jumlah_fokus += 1
        elif phase == "Short Break":
            self.menit = int(self.shortBreakEntryMinute.get() or 0)
            self.detik = int(self.shortBreakEntrySeconds.get() or 0)
            self.jumlah_Shortbreak += 1
        elif phase == "Long Break":
            self.menit = int(self.longBreakEntryMinute.get() or 0)
            self.detik = int(self.longBreakEntrySeconds.get() or 0)
            self.jumlah_Longbreak += 1

        self.update_timer_display()
        self.countdown()

    def start_timer(self):
        if (not self.focusEntryMinute.get() or not self.focusEntrySeconds.get() or
            not self.shortBreakEntryMinute.get() or not self.shortBreakEntrySeconds.get() or
            not self.longBreakEntryMinute.get() or not self.longBreakEntrySeconds.get()):
            print("Mohon isi semua field waktu.")
            return

        self.is_paused = False
        self.switch_phase("Focus")
        self.waktu_mulai = datetime.datetime.now()
        self.jumlah_fokus = 0
        self.jumlah_Shortbreak = 0
        self.jumlah_Longbreak = 0
    
    def pause_timer(self):
        self.is_paused = True
        if self.timer_id:
            self.master.after_cancel(self.timer_id)
        self.statusLabel.configure(text="Paused")

    def stop_timer(self):
        if self.waktu_mulai:
            self.waktu_selesai = datetime.datetime.now()
            judul = self.judulEntry.get() or "Tanpa Judul"
            self.simpan_riwayat_sesi(judul, self.waktu_mulai, self.waktu_selesai, self.jumlah_fokus, self.jumlah_Shortbreak, self.jumlah_Longbreak)
            print(f"Disimpan: {judul} ({self.jumlah_fokus} fokus, {self.jumlah_Shortbreak} short break, {self.jumlah_Longbreak} long break)")

        else:
            print("Belum ada sesi dimulai.")

        # Reset tampilan dan variabel
        self.waktu_mulai = None
        self.jumlah_fokus = 0
        self.jumlah_Shortbreak = 0
        self.jumlah_Longbreak = 0
        self.timeLabel.configure(text="00:00")
        self.statusLabel.configure(text="Stopped")
        self.master.after_cancel(self.timer_id) if self.timer_id else None

    def simpan_riwayat_sesi(self, judul, waktu_mulai, waktu_selesai, fokus, Sbrk, Lbrk):
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