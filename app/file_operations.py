import pandas as pd
from tkinter import filedialog
from app.excel_operations import display_data

def load_excel_file(filepath):
    return pd.read_excel(filepath)

def load_excel(app):
    app.filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if app.filepath:
        try:
            app.df = load_excel_file(app.filepath)
            print("Datos cargados:", app.df.head())  # Imprimir los primeros registros del DataFrame
            display_data(app)
        except Exception as e:
            print("Error al cargar el archivo:", e)
            tk.messagebox.showerror("Error", f"Error al cargar el archivo: {e}")
