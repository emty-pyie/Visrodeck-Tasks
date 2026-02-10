import customtkinter as ctk
from visrodeckTODO.manager import TaskManager
from ui.startup_frame import StartupFrame
from ui.dashboard_frame import DashboardFrame

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Setup
        self.title("VisroDeck Task Manager")
        self.geometry("900x700")
        self.minsize(800, 600)
        
        # Theme Setup
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue") # Standard CTK theme
        
        # Backend Setup
        self.manager = TaskManager()
        
        # Frame Container
        self.container = ctk.CTkFrame(self, fg_color="transparent")
        self.container.pack(fill="both", expand=True)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        
        # Initialize Frames
        self.frames = {}
        self.show_startup()

    def show_startup(self):
        if "startup" in self.frames:
            self.frames["startup"].destroy()
            
        self.frames["startup"] = StartupFrame(
            self.container, 
            on_get_started=self.show_dashboard,
            fg_color="transparent"
        )
        self.frames["startup"].grid(row=0, column=0, sticky="nsew")

    def show_dashboard(self):
        if "dashboard" in self.frames:
            self.frames["dashboard"].destroy()
            
        self.frames["dashboard"] = DashboardFrame(
            self.container, 
            manager=self.manager,
            fg_color="transparent"
        )
        self.frames["dashboard"].grid(row=0, column=0, sticky="nsew")

if __name__ == "__main__":
    app = App()
    app.mainloop()
