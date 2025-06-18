import customtkinter as ctk

# Membuat window utama
root = ctk.CTk()
root.geometry("400x300")
root.title("Pomodoro")
root.configure(fg_color="#F1F1F1")  # Set background color

# Nilai default
menit = 0
detik = 0

# Start handler
def start_timer():
    try:
        menitFocus = int(focusEntryMinute.get())
        detikFocus = int(focusEntrySeconds.get())

        menitShortBreak = int(shortBreakEntryMinute.get())
        detikShortBreak = int(shortBreakEntrySecond.get())

        menitLongBreak = int(longBreakEntryMinute.get())
        detikLongBreak = int(longBreakEntrySecond.get())

        print(f"Starting timer with {menitFocus} minutes and {detikFocus} seconds")
        print(f"Short Break: {menitShortBreak} minutes and {detikShortBreak} seconds")
        print(f"Long Break: {menitLongBreak} minutes and {detikLongBreak} seconds")
    except:
        print("Please enter valid numbers for the timer.")
    finally:
        # Reset the timer display
        timeLabel.configure(text=f"{menitFocus:02d}:{detikFocus:02d}")
        statusLabel.configure(text="Focus")


# Container frame supaya formnya diatur posisinya dengan lebih mudah
formFrame = ctk.CTkFrame(root, fg_color="#F1F1F1")
formFrame.pack(pady=0, padx=10)

# Focus Time
focusLabel = ctk.CTkLabel(formFrame, text="Focus :", font=ctk.CTkFont(family="jersey 10", size=15), text_color="#333333")
focusLabel.grid(row=0, column=0, padx=5, pady=5)

focusEntryMinute = ctk.CTkEntry(formFrame, width=25, 
                               font=ctk.CTkFont(family="jersey 10", size=15), 
                               fg_color="transparent", text_color="black", border_width=0,
                               placeholder_text="00")
focusEntryMinute.grid(row=0, column=1, padx=0, pady=5)

focusLabelPemisah = ctk.CTkLabel(formFrame, text=":", font=ctk.CTkFont(family="jersey 10", size=15), text_color="#333333")
focusLabelPemisah.grid(row=0, column=2, padx=0, pady=5)

focusEntrySeconds = ctk.CTkEntry(formFrame, width=25, 
                                 font=ctk.CTkFont(family="jersey 10", size=15), 
                                 fg_color="transparent", text_color="black", border_width=0,
                                 placeholder_text="00")
focusEntrySeconds.grid(row=0, column=3, padx=0, pady=5)

# Short Break
shortBreakLabel = ctk.CTkLabel(formFrame, text="Short Break :", font=ctk.CTkFont(family="jersey 10", size=15), text_color="#333333")
shortBreakLabel.grid(row=0, column=4, padx=10, pady=5)

shortBreakEntryMinute = ctk.CTkEntry(formFrame, width=25, 
                                    font=ctk.CTkFont(family="jersey 10", size=15), 
                                    fg_color="transparent", text_color="black", border_width=0,
                                    placeholder_text="00")
shortBreakEntryMinute.grid(row=0, column=5, padx=0, pady=5)

shortBreakLabelPemisah = ctk.CTkLabel(formFrame, text=":", font=ctk.CTkFont(family="jersey 10", size=15), text_color="#333333")
shortBreakLabelPemisah.grid(row=0, column=6, padx=0, pady=5)

shortBreakEntrySecond = ctk.CTkEntry(formFrame, width=25, 
                                      font=ctk.CTkFont(family="jersey 10", size=15), 
                                      fg_color="transparent", text_color="black", border_width=0,
                                      placeholder_text="00")
shortBreakEntrySecond.grid(row=0, column=7, padx=0, pady=5)

# Long Break
longBreakLabel = ctk.CTkLabel(formFrame, text="Long Break :", font=ctk.CTkFont(family="jersey 10", size=15), text_color="#333333")
longBreakLabel.grid(row=0, column=8, padx=10, pady=5)

longBreakEntryMinute = ctk.CTkEntry(formFrame, width=25, 
                                   font=ctk.CTkFont(family="jersey 10", size=15), 
                                   fg_color="transparent", text_color="black", border_width=0,
                                   placeholder_text="00")
longBreakEntryMinute.grid(row=0, column=9, padx=0, pady=5)

longBreakLabelPemisah = ctk.CTkLabel(formFrame, text=":", font=ctk.CTkFont(family="jersey 10", size=15), text_color="#333333")
longBreakLabelPemisah.grid(row=0, column=10, padx=0, pady=5)

longBreakEntrySecond = ctk.CTkEntry(formFrame, width=25, 
                                     font=ctk.CTkFont(family="jersey 10", size=15), 
                                     fg_color="transparent", text_color="black", border_width=0,
                                     placeholder_text="00")
longBreakEntrySecond.grid(row=0, column=11, padx=0, pady=5)

# Label untuk memampilkan status timer
statusLabel = ctk.CTkLabel(root, text="Focus", font=ctk.CTkFont(family="jersey 10", size=20), text_color="#333333")
statusLabel.pack(pady=0)

# Label untuk memanpilkan waktu
timeLabel = ctk.CTkLabel(root, text=f"{menit:02d}:{detik:02d}", font=ctk.CTkFont(family="jersey 10", size=50), text_color="#333333")
timeLabel.pack(pady=0)

# Button untuk kontrol timer
startButton = ctk.CTkButton(root, text="Start", command=start_timer, width=100, height=40, fg_color="#4F9747", text_color="white", font=ctk.CTkFont(family="jersey 10", size=15), hover=False)
startButton.pack(pady=3)

buttonBawahFrame = ctk.CTkFrame(root)
buttonBawahFrame.pack()
buttonBawahFrame.configure(fg_color="#F1F1F1")
buttonBawahFrame.grid_columnconfigure(0, weight=1)
buttonBawahFrame.grid_columnconfigure(1, weight=1)

resetButton = ctk.CTkButton(buttonBawahFrame, text="Stop", fg_color="transparent", command=lambda: print("Stop Timer"), width=100, height=40, text_color="#C72C41", font=ctk.CTkFont(family="jersey 10", size=15), hover_color="#C72C41", border_color="#C72C41", border_width=2)
resetButton.grid(row=0, column=0, padx=5, pady=5),
pauseButton = ctk.CTkButton(buttonBawahFrame, text="Pause", fg_color="transparent", command=lambda: print("Pause Timer"), width=100, height=40, text_color="#F6A600", font=ctk.CTkFont(family="jersey 10", size=15), hover_color="#F6A600", border_color="#F6A600", border_width=2)
pauseButton.grid(row=0, column=1, padx=5, pady=5)

menuBawahFrame = ctk.CTkFrame(root)
menuBawahFrame.pack(side="bottom", fill="x")
menuBawahFrame.configure(fg_color="#F1F1F1")


# Label Task List yang bisa diklik
taskListLabel = ctk.CTkLabel(menuBawahFrame, text="Task List", text_color="black", font=ctk.CTkFont(family="jersey 10", size=15), cursor="hand2")
taskListLabel.pack(side="left", padx=10, pady=10)
import subprocess
import sys

def open_tasklist_py():
    root.destroy()  # tutup window sekarang
    subprocess.Popen([sys.executable, "tasklist.py"])

taskListLabel.bind("<Button-1>", lambda e: open_tasklist_py())


# Label Riwayat yang bisa diklik
riwayatLabel = ctk.CTkLabel(menuBawahFrame, text="Riwayat", text_color="black", font=ctk.CTkFont(family="jersey 10", size=15), cursor="hand2")
riwayatLabel.pack(side="right", padx=10, pady=10)
riwayatLabel.bind("<Button-1>", lambda e: print("Open Riwayat"))


root.mainloop()