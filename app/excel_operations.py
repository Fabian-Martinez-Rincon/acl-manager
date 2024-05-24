import tkinter.font as tkfont

def display_data(app):
    # for i in app.tree.get_children():
    #     app.tree.delete(i)

    app.tree["column"] = list(app.df.columns)
    app.tree["show"] = "headings"

    for col in app.tree["columns"]:
        app.tree.heading(col, text=col)

    for row in app.df.to_numpy().tolist():
        app.tree.insert("", "end", values=row)

    # Adjust column widths based on the maximum width of the items in each column
    margin = 10
    font = tkfont.Font()
    for col in app.tree["columns"]:
        max_width = font.measure(col) + margin
        for item in app.df[col].astype(str):
            max_width = max(max_width, font.measure(item) + margin)
        app.tree.column(col, width=max_width)


def get_acl(app):
    if app.filepath:
        print("Dios Mio")
        display_data(app)