import tkinter.font as tkfont

def truncate_path(path):
    path = path.replace(' ', '')
    return path


def display_data(app):
    # Clear the Treeview
    for item in app.tree.get_children():
        app.tree.delete(item)

    # Set up columns in the Treeview
    app.tree["column"] = list(app.df.columns)
    app.tree["show"] = "headings"

    for col in app.tree["columns"]:
        app.tree.heading(col, text=col)

    # Insert rows into the Treeview and truncate paths in the first column
    for row in app.df.to_numpy().tolist():
        row[0] = truncate_path(row[0])
        app.tree.insert("", "end", values=row)

    # Adjust column widths
    adjust_column_widths(app)

def adjust_column_widths(app):
    font = tkfont.Font()
    fixed_width = 650  # adjust this value to your needs
    for index, col in enumerate(app.tree["columns"]):
        if index == 0:  # if it's the first column
            app.tree.column(col, width=fixed_width)
        else:
            max_width = font.measure(col)
            for item in app.df[col].astype(str):
                max_width = max(max_width, font.measure(item))
            app.tree.column(col, width=max_width + 10)  # Adding margin for better readability

def get_acl(app):
    """
    Function to handle ACL retrieval and display.
    """
    if app.filepath:
        print("Displaying ACL data...")
        display_data(app)