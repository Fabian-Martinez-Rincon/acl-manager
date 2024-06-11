import tkinter as tk
from tkinter import ttk, messagebox

class NewPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Nueva Página")
        self.root.configure(bg='#333333')
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Bienvenido a la nueva página", font=("Helvetica", 16, "bold"), bg='#333333', fg='white').pack(pady=20)

def redirect_to_new_page(self):
    new_window = tk.Toplevel(self.root)
    NewPage(new_window)
