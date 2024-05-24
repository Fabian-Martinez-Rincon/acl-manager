import tkinter.font as tkfont

def display_data(app):
    for i in app.tree.get_children():
        app.tree.delete(i)

    app.tree["column"] = list(app.df.columns)
    app.tree["show"] = "headings"

    for col in app.tree["columns"]:
        app.tree.heading(col, text=col)

    for row in app.df.to_numpy().tolist():
        app.tree.insert("", "end", values=row)

    font = tkfont.Font()
    for col in app.tree["columns"]:
        max_width = font.measure(col)
        for item in app.df[col].astype(str):
            max_width = max(max_width, font.measure(item))
        app.tree.column(col, width=max_width)

def get_acl(app):
    if app.filepath:
        print("Consultando ACL...")
        display_data(app)
