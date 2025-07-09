import customtkinter as ctk
import json
import os

FILE_NAME = "task_data.json"

class TaskListPage(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color="#F1F1F1")
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Judul
        titleLabel = ctk.CTkLabel(self, text="Task List", font=ctk.CTkFont(size=20, weight="bold", family="Jersey 10"), text_color="#333333")
        titleLabel.grid(row=0, column=0, pady=(10,0))

        # Frame hijau utama
        formFrame = ctk.CTkFrame(self, fg_color="#4CAF50", corner_radius=0)
        formFrame.grid(row=1, column=0, padx=10, pady=(5, 0), sticky="nsew")
        formFrame.grid_rowconfigure(0, weight=1)
        formFrame.grid_columnconfigure(0, weight=1)

        # Scrollable task list
        self.scrollFrame = ctk.CTkScrollableFrame(
            formFrame, fg_color="#4CAF50", label_fg_color="#4CAF50", scrollbar_button_color="#CFCFCF"
        )
        self.scrollFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Load tasks from file
        self.tasks = self.load_tasks()
        self.checkbox_list = []
        for task in self.tasks:
            self.add_task_to_ui(task)
        add_container = ctk.CTkFrame(formFrame, fg_color="#4CAF50")
        add_container.grid(row=1, column=0, sticky="w", padx=10, pady=(5, 10))

        # Tombol bulat "+"
        self.add_btn = ctk.CTkButton(
            add_container,
            text="+",
            width=15,
            height=15,
            font=ctk.CTkFont(size=24, weight="bold"),
            fg_color="white",
            text_color="#4CAF50",
            hover_color="#E8F5E9",
            corner_radius=2000,
            command=self.show_entry
        )
        self.add_btn.pack(side="left", padx=(5, 10), pady=5)

        # Label "Add a task"
        self.add_label = ctk.CTkLabel(
            add_container,
            text="Add a task",
            font=ctk.CTkFont(family="jersey 10", size=18),
            text_color="white"
        )
        self.add_label.pack(side="left", padx=(5, 10), pady=5)

        # Entry yang muncul saat klik "+"
        self.add_entry = ctk.CTkEntry(
            add_container,
            width=200,
            font=ctk.CTkFont(family="jersey 10", size=18),
            fg_color="#4CAF50",
            text_color="white",
            placeholder_text="Enter task here"
        )
        self.add_entry.bind("<Return>", self.submit_task)

        # Menu bawah
        menuBawahFrame = ctk.CTkFrame(self, fg_color="#F1F1F1")
        menuBawahFrame.grid(row=2, column=0, sticky="ew", pady=(5, 0))
        menuBawahFrame.grid_columnconfigure(0, weight=1)

        homeLabel = ctk.CTkLabel(menuBawahFrame, text="Pomodoro", font=ctk.CTkFont("jersey 10", 15), text_color="#333333")
        homeLabel.grid(row=0, column=0, sticky="w", padx=10, pady=5)
        homeLabel.bind("<Enter>", lambda e: homeLabel.configure(text_color="#606060"))
        homeLabel.bind("<Leave>", lambda e: homeLabel.configure(text_color="#333333"))
        homeLabel.bind("<Button-1>", lambda e: self.master.show_HomePage())

        riwayatLabel = ctk.CTkLabel(menuBawahFrame, text="Riwayat", font=ctk.CTkFont("jersey 10", 15), text_color="#333333")
        riwayatLabel.grid(row=0, column=1, sticky="e", padx=10, pady=5)
        riwayatLabel.bind("<Enter>", lambda e: riwayatLabel.configure(text_color="#606060"))
        riwayatLabel.bind("<Leave>", lambda e: riwayatLabel.configure(text_color="#333333"))
        riwayatLabel.bind("<Button-1>", lambda e: self.master.show_RiwayatPage())   
    
    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        return []
    
    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.tasks, file, indent=4)
    
    def add_task_to_ui(self, task_text):
        cb = ctk.CTkCheckBox(
        self.scrollFrame,
        text=task_text,
        font=ctk.CTkFont(family="jersey 10", size=18),
        checkbox_height=20,
        checkbox_width=20,
        
        text_color="white"
    )
        cb.pack(anchor="w", padx=10, pady=4)
        self.checkbox_list.append(cb)
    
    def show_entry(self):
        self.add_label.pack_forget()
        self.add_entry.pack(side="left", pady=5)
        self.add_entry.focus()
    
    def submit_task(self, event=None):
        new_task = self.add_entry.get()
        if new_task.strip() != "":
            self.tasks.append(new_task)
            self.save_tasks()
            self.add_task_to_ui(new_task)
        self.add_entry.delete(0, 'end')
        self.add_entry.pack_forget()
        self.add_label.pack(side="left", pady=5)
