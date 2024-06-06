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
        self.create_selected_label()
        self.create_treeview_frame()

    def create_button_frame(self):
        """Create the button frame with load and consult buttons."""
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        self.load_button = tk.Button(button_frame, text="Cargar Excel", command=self.load_excel)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.add_row_button = tk.Button(button_frame, text="GET ACL", command=self.get_acl)
        self.add_row_button.pack(side=tk.LEFT, padx=5)

        self.add_row_button = tk.Button(button_frame, text="SET ACL", command=self.set_acl)
        self.add_row_button.pack(side=tk.LEFT, padx=5)

    def create_selected_label(self):
        """Create a label to display the selected row."""
        self.selected_label_frame = tk.Frame(self.root)
        self.selected_label_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        self.selected_label = tk.Label(self.selected_label_frame, text="Selecciona una fila y una de las opciones")
        self.selected_label.pack(side=tk.LEFT)

        self.copy_button = tk.Button(self.selected_label_frame, text="Copiar", command=self.copy_selected_text)
        self.copy_button.pack(side=tk.LEFT, padx=10)

        self.selected_entry = tk.Entry(self.selected_label_frame, state='readonly', width=100)
        self.selected_entry.pack(side=tk.LEFT, padx=10)

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
        style.configure("Treeview", rowheight=25, background="white", foreground="black", fieldbackground="white")
        style.map('Treeview', background=[('selected', 'blue')], foreground=[('selected', 'white')])

        self.tree.bind("<ButtonRelease-1>", self.on_tree_select)

    def load_excel(self):
        """Load an Excel file and display its content."""
        try:
            load_excel(self)
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar el archivo: {e}")

    def get_acl(self):
        """Consult ACL and display the results."""
        try:
            selected_item = self.tree.focus()
            if not selected_item:
                messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna fila.")
                return
            selected_row = self.tree.item(selected_item, 'values')
            headers = self.tree["columns"]
            file_path = selected_row[0]
            command = f'getfacl {file_path}'
            self.selected_entry.config(state='normal')
            self.selected_entry.delete(0, tk.END)
            self.selected_entry.insert(0, command)
            self.selected_entry.config(state='readonly')
            get_acl(self)
        except Exception as e:
            messagebox.showerror("Error", f"Error al consultar ACL: {e}")

    def set_acl(self):
        """Set ACL and display the results."""
        try:
            selected_item = self.tree.focus()
            if not selected_item:
                messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna fila.")
                return
            selected_row = self.tree.item(selected_item, 'values')
            headers = self.tree["columns"]

            file_path = selected_row[0]
            acl_commands = []

            for header, value in zip(headers[1:], selected_row[1:]):
                acl_commands.append(f'setfacl -R -m g:{header}:{value} {file_path}')

            result_text = "; ".join(acl_commands)
            self.selected_entry.config(state='normal')
            self.selected_entry.delete(0, tk.END)
            self.selected_entry.insert(0, result_text)
            self.selected_entry.config(state='readonly')
        except Exception as e:
            messagebox.showerror("Error", f"Error al configurar ACL: {e}")


    def on_tree_select(self, event):
        pass
        # selected_item = self.tree.focus()
        # selected_row = self.tree.item(selected_item, 'values')
        # self.selected_entry.config(state='normal')
        # self.selected_entry.delete(0, tk.END)
        # self.selected_entry.insert(0, selected_row)
        # self.selected_entry.config(state='readonly')

    def copy_selected_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.selected_entry.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelApp(root)
    root.mainloop()
