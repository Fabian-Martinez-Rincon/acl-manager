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
        self.create_logo()
        self.create_button_frame()
        self.create_selected_label()
        # self.create_selected_label()
        self.create_treeview_frame()
    
    def create_logo(self):
        self.logo_frame = tk.Frame(self.root)
        self.logo_frame.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)

        self.logo_image = tk.PhotoImage(file="assets/logo.png")
        self.logo_label = tk.Label(self.logo_frame, image=self.logo_image)
        self.logo_label.pack(side=tk.LEFT)

        self.title_label = tk.Label(self.logo_frame, text="Gestor de Permisos", font=("Helvetica", 16, "bold"))
        self.title_label.pack(side=tk.LEFT, padx=10)

        tk.Label(self.logo_frame, text="", width=5).pack(side=tk.LEFT, expand=True)

    def create_button_frame(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.TOP, pady=10, padx=10, fill=tk.X)

        button_style = {'side': tk.LEFT, 'padx': 5, 'pady': 5}

        self.load_button = tk.Button(button_frame, text="Cargar Excel", command=self.load_excel, bg="lightblue", fg="black", font=("Helvetica", 10, "bold"))
        self.load_button.pack(**button_style)

        self.get_acl_button = tk.Button(button_frame, text="CONSULTAR PERMISOS", command=lambda: self.process("GET"), bg="lightblue", fg="black", font=("Helvetica", 10, "bold"))
        self.get_acl_button.pack(**button_style)

        self.set_acl_button = tk.Button(button_frame, text="SETEAR PERMISOS", command=lambda: self.process("SET"), bg="lightblue", fg="black", font=("Helvetica", 10, "bold"))
        self.set_acl_button.pack(**button_style)

        self.set_acl_recursive_button = tk.Button(button_frame, text="SET ACL Recursivo", command=lambda: self.process("SET RECURSIVO"), bg="lightblue", fg="black", font=("Helvetica", 10, "bold"))
        self.set_acl_recursive_button.pack(**button_style)

        self.delete_acl_button = tk.Button(button_frame, text="DELETE ACL", command=lambda: self.process("DELETE"), bg="lightblue", fg="black", font=("Helvetica", 10, "bold"))
        self.delete_acl_button.pack(**button_style)

        self.delete_acl_recursive_button = tk.Button(button_frame, text="DELETE ACL Recursivo", command=lambda: self.process("DELETE RECURSIVO"), bg="lightblue", fg="black", font=("Helvetica", 10, "bold"))
        self.delete_acl_recursive_button.pack(**button_style)

    def create_selected_label(self):
        """Create a label to display the selected row."""
        self.selected_label_frame = tk.Frame(self.root)
        self.selected_label_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)

        label_font = ("Helvetica", 12)
        button_font = ("Helvetica", 10, "bold")
        entry_bg_color = "#f0f0f0"

        self.selected_label = tk.Label(self.selected_label_frame, text="Selecciona una fila y una de las opciones", font=label_font)
        self.selected_label.pack(side=tk.LEFT, padx=10)

        self.copy_button = tk.Button(self.selected_label_frame, text="Copiar", command=self.copy_selected_text, font=button_font, bg="lightblue", fg="black")
        self.copy_button.pack(side=tk.LEFT, padx=10)

        self.selected_entry = tk.Entry(self.selected_label_frame, state='readonly', width=80, bg=entry_bg_color, font=("Helvetica", 10))
        self.selected_entry.pack(side=tk.LEFT, padx=10)

        tk.Label(self.selected_label_frame, text="", width=5).pack(side=tk.RIGHT)

    def copy_selected_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.selected_entry.get())
        messagebox.showinfo("Copiado", "El texto seleccionado ha sido copiado al portapapeles.")


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
        style.theme_use("clam")
        style.configure("Treeview", 
                    font=("Helvetica", 10),
                    rowheight=25,
                    background="white",
                    foreground="black",
                    fieldbackground="white")
        style.configure("Treeview.Heading", 
                        font=("Helvetica", 11, "bold"), 
                        background="lightblue", 
                        foreground="black")
        style.map('Treeview', 
                background=[('selected', 'blue')],
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
