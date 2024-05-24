from tkinter import Tk
from app.ui import ExcelApp

def main():
    root = Tk()
    app = ExcelApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
