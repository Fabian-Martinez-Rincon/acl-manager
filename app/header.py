import tkinter as tk

def create_logo(root):
    logo_frame = tk.Frame(root, bg='#333333')
    logo_frame.pack(side=tk.TOP, pady=10, padx=35, fill=tk.X)

    logo_image = tk.PhotoImage(file="assets/logo.png")
    logo_label = tk.Label(logo_frame, image=logo_image, bg='#333333')
    logo_label.image = logo_image
    logo_label.pack(side=tk.LEFT)

    title_label = tk.Label(logo_frame, text="Gestor de Permisos", font=("Helvetica", 16, "bold"), bg='#333333', fg='white')
    title_label.pack(side=tk.LEFT, padx=10)

    tk.Label(logo_frame, text="", bg='#333333').pack(side=tk.LEFT, expand=True)

    load_button = tk.Button(logo_frame, text="CARGAR EXCEL", bg="lightgrey", fg="black", font=("Helvetica", 10, "bold"))
    load_button.pack(side=tk.LEFT)

    redirect_button = tk.Button(logo_frame, text="MANUAL", command=lambda: redirect_to_new_page(root), bg="lightgrey", fg="black", font=("Helvetica", 10, "bold"))
    redirect_button.pack(side=tk.LEFT, padx=10)

    return logo_frame

def redirect_to_new_page(root):
        new_window = tk.Toplevel(root)
        NewPage(new_window)

class NewPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Manual de Permisos")
        self.root.configure(bg='#333333')
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Manual ACL", font=("Helvetica", 16, "bold"), bg='#333333', fg='white').pack(pady=20)

        # Lista de botones y sus descripciones
        buttons_info = [
            ("CONSULTAR", "Consultar los permisos actuales del sistema."),
            ("SETEAR", "Configurar nuevos permisos en el sistema."),
            ("SETEAR", "Configurar permisos de manera recursiva en directorios."),
            ("ELIMINAR", "Eliminar los permisos configurados."),
            ("ELIMINAR", "Eliminar permisos de manera recursiva en directorios."),
            ("CARGAR EXCEL", "Cargar un archivo Excel con la configuración de permisos."),
            ("REDIRIGIR", "Redirigir a una nueva página o funcionalidad.")
        ]

        for btn_text, description in buttons_info:
            frame = tk.Frame(self.root, bg='#333333')
            frame.pack(pady=5, padx=20, fill=tk.X)

            button = tk.Button(frame, text=btn_text, bg="lightgrey", fg="black", font=("Helvetica", 10, "bold"))
            button.pack(side=tk.LEFT, padx=10)

            label = tk.Label(frame, text=description, font=("Helvetica", 10), bg='#333333', fg='white', anchor="w")
            label.pack(side=tk.LEFT, fill=tk.X, expand=True)