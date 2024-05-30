import tkinter as tk
from tkinter import ttk, messagebox
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
        """Create and pack all widgets in the main window."""
        self.create_button_frame()
        self.create_treeview_frame()

    def create_button_frame(self):
        """Create the button frame with load and consult buttons."""
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        self.load_button = tk.Button(button_frame, text="Cargar Excel", command=self.load_excel)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.add_row_button = tk.Button(button_frame, text="Consultar ACL", command=self.consult_acl)
        self.add_row_button.pack(side=tk.LEFT, padx=5)

    def create_treeview_frame(self):
        tree_container = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        tree_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        vsb = ttk.Scrollbar(tree_container, orient="vertical")
        vsb.pack(side='right', fill='y')

        hsb = ttk.Scrollbar(tree_container, orient="horizontal")
        hsb.pack(side='bottom', fill='x')

        self.tree = ttk.Treeview(tree_container, show='headings', yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)

        style = ttk.Style()
        style.configure("Treeview", font=("Helvetica", 10))
        style.configure("Treeview.Heading", font=("Helvetica", 10, "bold"), background="lightblue", foreground="black")
        style.map('Treeview.Heading', background=[('active', 'blue')], foreground=[('active', 'white')])

    def load_excel(self):
        """Load an Excel file and display its content."""
        try:
            load_excel(self)
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar el archivo: {e}")

    def consult_acl(self):
        """Consult ACL and display the results."""
        try:
            get_acl(self)
        except Exception as e:
            messagebox.showerror("Error", f"Error al consultar ACL: {e}")