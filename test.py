import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.title("Navigasi Halaman")

        # Container utama untuk halaman-halaman
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for F in (HalamanUtama, TaskList, Riwayat):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.tampilkan_halaman(HalamanUtama)

    def tampilkan_halaman(self, page):
        frame = self.frames[page]
        frame.tkraise()


class HalamanUtama(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Ini Halaman Utama")
        label.pack(pady=10)
        tombol_task = ctk.CTkButton(self, text="Ke Task List", command=lambda: controller.tampilkan_halaman(TaskList))
        tombol_task.pack(pady=5)
        tombol_riwayat = ctk.CTkButton(self, text="Ke Riwayat", command=lambda: controller.tampilkan_halaman(Riwayat))
        tombol_riwayat.pack(pady=5)


class TaskList(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Ini Halaman Task List")
        label.pack(pady=10)
        tombol_kembali = ctk.CTkButton(self, text="Kembali", command=lambda: controller.tampilkan_halaman(HalamanUtama))
        tombol_kembali.pack(pady=5)


class Riwayat(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text="Ini Halaman Riwayat")
        label.pack(pady=10)
        tombol_kembali = ctk.CTkButton(self, text="Kembali", command=lambda: controller.tampilkan_halaman(HalamanUtama))
        tombol_kembali.pack(pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()
