import customtkinter as ctk
from HomePage import HomePage

class PomodoroApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.geometry("400x300")
        self.title("Pomodoro")
        self.configure(fg_color="#F1F1F1")
        self.resizable(False, False)
        self._set_appearance_mode("system")  # Set appearance mode to system default
        self.iconbitmap("TOMAT.ico")

        HomePage(self).pack(fill="both", expand=True, pady=0)

        # Starting the app
        self.mainloop()


if __name__ == "__main__":
    PomodoroApp()