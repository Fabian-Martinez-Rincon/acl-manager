import tkinter as tk
from tkinter import ttk, messagebox
from app.file_operations import load_excel
from app.excel_operations import get_acl
from app.header import create_logo
import ctypes

class ExcelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de ACLs (Access Control Lists)")
        self.set_initial_window_size()
        self.root.configure(bg='#333333')
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
        create_logo(self.root)
        self.create_button_frame()
        self.create_selected_label()
        self.create_treeview_frame()
    

    def create_button_frame(self):
        background_style_button = {'bg': 'lightgrey', 'fg': 'black', 'font': ('', 10, 'bold')}
        button_frame = tk.Frame(self.root, bg='#333333')
        button_frame.pack(side=tk.TOP, pady=10, padx=35, fill=tk.X)

        button_style = {'side': tk.LEFT, 'padx': 5, 'pady': 5}

        self.get_acl_button = tk.Button(button_frame, text="CONSULTAR", command=lambda: self.process("GET"), **background_style_button)
        self.get_acl_button.pack(**button_style)

        self.set_acl_button = tk.Button(button_frame, text="SETEAR", command=lambda: self.process("SET"), **background_style_button)
        self.set_acl_button.pack(**button_style)

        self.set_acl_recursive_button = tk.Button(button_frame, text="SETEAR R", command=lambda: self.process("SET RECURSIVO"), **background_style_button)
        self.set_acl_recursive_button.pack(**button_style)

        self.delete_acl_button = tk.Button(button_frame, text="ELIMINAR", command=lambda: self.process("DELETE"), **background_style_button)
        self.delete_acl_button.pack(**button_style)

        self.delete_acl_recursive_button = tk.Button(button_frame, text="ELIMINAR R", command=lambda: self.process("DELETE RECURSIVO"), **background_style_button)
        self.delete_acl_recursive_button.pack(**button_style)
        

    def create_selected_label(self):
        """Create a label to display the selected row."""
        background_style_button = {'bg': 'lightgrey', 'fg': 'black', 'font': ('', 10, 'bold')}

        self.selected_label_frame = tk.Frame(self.root, bg='#333333')
        self.selected_label_frame.pack(side=tk.TOP, fill=tk.X, padx=35, pady=10)

        label_font = ("Helvetica", 12)
        button_font = ("Helvetica", 10, "bold")
        entry_bg_color = "#f0f0f0"

        self.selected_label = tk.Label(self.selected_label_frame, text="Selecciona una fila y una de las opciones", font=label_font, bg='#333333', fg='white')
        self.selected_label.pack(side=tk.LEFT, padx=10)

        self.copy_button = tk.Button(self.selected_label_frame, text="COPIAR", command=self.copy_selected_text, **background_style_button)
        self.copy_button.pack(side=tk.LEFT, padx=10)

        self.selected_entry = tk.Entry(self.selected_label_frame, width=80, bg=entry_bg_color, font=("Helvetica", 10))
        self.selected_entry.pack(side=tk.LEFT, padx=10)

        tk.Label(self.selected_label_frame, text="" , bg='#333333', width=5).pack(side=tk.RIGHT)

    def copy_selected_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.selected_entry.get())
        messagebox.showinfo("Copiado", "El texto seleccionado ha sido copiado al portapapeles.")


    def create_treeview_frame(self):
        tree_container = tk.Frame(self.root, bd=2, relief=tk.SUNKEN)
        tree_container.pack(fill=tk.BOTH, expand=True, padx=35, pady=35)

        vsb = ttk.Scrollbar(tree_container, orient="vertical")
        vsb.pack(side='right', fill='y')

        hsb = ttk.Scrollbar(tree_container, orient="horizontal")
        hsb.pack(side='bottom', fill='x')

        self.tree = ttk.Treeview(tree_container, show='headings', yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        vsb.config(command=self.tree.yview)
        hsb.config(command=self.tree.xview)

        style = ttk.Style()
        style.configure("Treeview", 
                    font=("Helvetica", 10),
                    rowheight=25,
                    background="lightgrey",
                    foreground="black",
                    fieldbackground="black")
        style.map('Treeview', 
                background=[('selected', '#0077FF')],
                foreground=[('selected', 'white')])

        # self.tree.bind("<ButtonRelease-1>", self.select_item)

    def select_item(self, event):
        selected_item = self.tree.focus()
        item_values = self.tree.item(selected_item, 'values')
        if item_values:
            self.selected_entry.config(state='normal')
            self.selected_entry.delete(0, tk.END)
            self.selected_entry.insert(0, ', '.join(item_values))
            self.selected_entry.config(state='readonly')

    def load_excel(self):
        """Load an Excel file and display its content."""
        try:
            load_excel(self)
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar el archivo: {e}")

    def process(self, arg):
        """Consult ACL and display the results."""
        try:
            selected_item = self.tree.focus()
            if not selected_item:
                messagebox.showwarning("Advertencia", "No se ha seleccionado ninguna fila.")
                return
            selected_row = self.tree.item(selected_item, 'values')
            file_path = selected_row[0]
            command = ""

            if arg == "GET":
                command = f'getfacl {file_path}'
            elif arg == "SET":
                acl_commands = []
                headers = self.tree["columns"]
                for header, value in zip(headers[1:], selected_row[1:]):
                    acl_commands.append(f'setfacl -m g:{header}:{value} {file_path}')
                command = "; ".join(acl_commands)
            elif arg == "SET RECURSIVO":
                acl_commands = []
                headers = self.tree["columns"]
                for header, value in zip(headers[1:], selected_row[1:]):
                    acl_commands.append(f'setfacl -R -m g:{header}:{value} {file_path}')
                command = "; ".join(acl_commands)
            elif arg == "DELETE":
                command = f'setfacl -b {file_path}'
            elif arg == "DELETE RECURSIVO":
                acl_commands = []
                command = f'setfacl -R -b {file_path}'
            
            self.selected_entry.config(state='normal')
            self.selected_entry.delete(0, tk.END)
            self.selected_entry.insert(0, command)
            self.selected_entry.config(state='readonly')
        except Exception as e:
            messagebox.showerror("Error", f"Error al consultar ACL: {e}")

    def copy_selected_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.selected_entry.get())
        self.root.update()
        copied_text = self.root.clipboard_get()
        if copied_text == self.selected_entry.get():
            messagebox.showinfo("Copiar", "Texto copiado al portapapeles.")
        else:
            messagebox.showerror("Error", "El texto no se pudo copiar correctamente. Intenta nuevamente.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ExcelApp(root)
    root.mainloop()
