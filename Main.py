import customtkinter as ctk
from HomePage import HomePage
from RiwayatPage import RiwayatPage

class PomodoroApp(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.geometry("400x300")
        self.title("Pomodoro")
        self.configure(fg_color="#F1F1F1")
        self.resizable(False, False)
        self._set_appearance_mode("system")  # Set appearance mode to system default
        self.iconbitmap("TOMAT.ico")

        self.test = "Pomodoro App"
        # Initialize pages
        self.riwayat_page = RiwayatPage(self)
        self.home_page = HomePage(self)

        self.home_page.pack(fill="both", expand=True, pady=0)
        # self.riwayat_page.pack(fill="both", expand=True, pady=0)

        # Starting the app
        self.mainloop()
    def show_RiwayatPage(self):
        self.riwayat_page.pack(fill="both", expand=True, pady=0)
        self.home_page.pack_forget()
    def show_HomePage(self):
        self.home_page.pack(fill="both", expand=True, pady=0)
        self.riwayat_page.pack_forget()


if __name__ == "__main__":
    PomodoroApp()