import tkinter as tk
from tkinter import ttk, filedialog
import tkinter.font as tkfont
import pandas as pd
import ctypes

def load_excel(app):
    app.filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if app.filepath:
        app.df = pd.read_excel(app.filepath)
        display_data(app)

def display_data(app):
    for i in app.tree.get_children():
        app.tree.delete(i)

    app.tree["column"] = list(app.df.columns)
    app.tree["show"] = "headings"

    for col in app.tree["columns"]:
        app.tree.heading(col, text=col)

    for row in app.df.to_numpy().tolist():
        app.tree.insert("", "end", values=row)

    margin = 10
    font = tkfont.Font()
    for col in app.tree["columns"]:
        max_width = font.measure(col) + margin
        for item in app.df[col].astype(str):
            max_width = max(max_width, font.measure(item) + margin)
        app.tree.column(col, width=max_width)

def get_acl(app):
    if app.filepath:
        display_data(app)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelApp(root)
    root.mainloop()
