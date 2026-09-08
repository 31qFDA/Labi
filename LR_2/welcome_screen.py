import tkinter as tk
from tkinter import ttk
import time
class WelcomeScreen:
    def __init__(self, parent_root, colors=None, duration=3000):
        self.parent_root = parent_root
        self.duration = duration
        self.colors = colors or {
            "bg_white": "#ffffff",
            "text_black": "#000000",
            "accent_gray": "#b1b1b1",
            "bg_dark": "#000000",
            "button_bg": "#000000",
            "button_fg": "#ffffff"
        }
        self.welcome_window = None
        self.progress_var = None
        self.start_time = None
    def show(self):
        self._create_welcome_window()
        self._center_window()
        self._animate_welcome()
    def _create_welcome_window(self):
        self.welcome_window = tk.Toplevel(self.parent_root)
        self.welcome_window.title("Добро пожаловать")
        self.welcome_window.geometry("600x400")
        self.welcome_window.resizable(False, False)
        self.welcome_window.overrideredirect(True)
        self.welcome_window.configure(bg=self.colors["bg_white"])
        frame = tk.Frame(
            self.welcome_window,
            bg=self.colors["bg_white"],
            highlightbackground=self.colors["accent_gray"],
            highlightthickness=2
        )
        frame.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        inner_frame = tk.Frame(frame, bg=self.colors["bg_white"])
        inner_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        icon_label = tk.Label(
            inner_frame,
            text="💰",
            font=("Arial", 48),
            bg=self.colors["bg_white"]
        )
        icon_label.pack(pady=(20, 10))
        title_label = tk.Label(
            inner_frame,
            text="MONEY WATCHER",
            font=("Arial", 24, "bold"),
            fg=self.colors["text_black"],
            bg=self.colors["bg_white"]
        )
        title_label.pack(pady=10)
        welcome_label = tk.Label(
            inner_frame,
            text="Добро пожаловать в приложение для учета финансов!",
            font=("Arial", 14),
            fg=self.colors["accent_gray"],
            bg=self.colors["bg_white"]
        )
        welcome_label.pack(pady=10)
        progress_frame = tk.Frame(inner_frame, bg=self.colors["bg_white"])
        progress_frame.pack(pady=30, fill=tk.X)
        self.progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(
            progress_frame,
            variable=self.progress_var,
            maximum=100,
            mode='determinate',
            length=400
        )
        progress_bar.pack(fill=tk.X)
        self.percent_label = tk.Label(
            progress_frame,
            text="0%",
            font=("Arial", 12),
            fg=self.colors["text_black"],
            bg=self.colors["bg_white"]
        )
        self.percent_label.pack(pady=(10, 0))
        loading_label = tk.Label(
            inner_frame,
            text="Загрузка приложения...",
            font=("Arial", 11),
            fg=self.colors["accent_gray"],
            bg=self.colors["bg_white"]
        )
        loading_label.pack()
        self.welcome_window.bind("<Button-1>", lambda e: self.close())
        self.welcome_window.bind("<Escape>", lambda e: self.close())
        self.welcome_window.bind("<Return>", lambda e: self.close())
        self.welcome_window.bind("<space>", lambda e: self.close())
        self.welcome_window.focus_set()
        self.welcome_window.grab_set()
    def _center_window(self):
        self.welcome_window.update_idletasks()
        screen_width = self.welcome_window.winfo_screenwidth()
        screen_height = self.welcome_window.winfo_screenheight()
        window_width = self.welcome_window.winfo_width()
        window_height = self.welcome_window.winfo_height()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.welcome_window.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.welcome_window.lift()
        self.welcome_window.attributes('-topmost', True)
        self.welcome_window.after(100, lambda: self.welcome_window.attributes('-topmost', False))
    def _animate_welcome(self):
        self.start_time = time.time()
        self._update_progress()
    def _update_progress(self):
        if not self.welcome_window or not self.welcome_window.winfo_exists():
            return
        elapsed_time = time.time() - self.start_time
        progress = min(elapsed_time / (self.duration / 1000) * 100, 100)
        self.progress_var.set(progress)
        self.percent_label.config(text=f"{int(progress)}%")
        if progress < 100:
            self.welcome_window.after(50, self._update_progress)
        else:
            self.welcome_window.after(200, self.close)
    def close(self):
        if self.welcome_window and self.welcome_window.winfo_exists():
            self.welcome_window.grab_release()
            self.welcome_window.destroy()
            self.welcome_window = None
    def is_showing(self):
        return self.welcome_window is not None and self.welcome_window.winfo_exists()