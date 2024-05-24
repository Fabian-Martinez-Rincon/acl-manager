import pandas as pd
from tkinter import filedialog
from app.excel_operations import display_data

def load_excel_file(filepath):
    return pd.read_excel(filepath)

def load_excel(self):
    self.filepath = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
    if self.filepath:
        self.df = load_excel_file(self.filepath)
        display_data(self)