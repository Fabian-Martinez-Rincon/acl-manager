import tkinter as tk
from tkinter import ttk
from app.file_operations import load_excel
from app.excel_operations import get_acl
import ctypes

class ExcelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de ACLs (Access Control Lists)")
        self.set_initial_window_size()
        self.filepath = None
        self.create_widgets()

    def set_initial_window_size(self):
        user32 = ctypes.windll.user32
        screen_width = user32.GetSystemMetrics(0)
        screen_height = user32.GetSystemMetrics(1)
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        self.root.geometry(f"{window_width}x{window_height}")

    def create_widgets(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        self.load_button = tk.Button(button_frame, text="Cargar Excel", command=lambda: load_excel(self))
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.add_row_button = tk.Button(button_frame, text="Consultar ACL", command=lambda: get_acl(self))
        self.add_row_button.pack(side=tk.LEFT, padx=5)

        tree_frame = tk.Frame(self.root)
        tree_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(tree_frame, show='headings')
        self.tree.pack(fill=tk.BOTH, expand=True, side='left')

        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        vsb.pack(side='right', fill='y')
        self.tree.configure(yscrollcommand=vsb.set)

        hsb = ttk.Scrollbar(tree_frame, orient="horizontal", command=self.tree.xview)
        hsb.pack(side='bottom', fill='x')
        self.tree.configure(xscrollcommand=hsb.set)

        style = ttk.Style()
        style.configure("Treeview", font=("Helvetica", 10))
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"))
