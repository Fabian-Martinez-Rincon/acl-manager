import tkinter.font as tkfont

def truncate_path(path, max_length=30):
    if len(path) <= max_length:
        return path
    else:
        parts = path.split('/')
        return '.../' + '/'.join(parts[-2:])

def display_data(app):
    longest_string = ""
    max_length = 0

    def print_cell_content(item_id, column_name):
        nonlocal longest_string, max_length
        cell_content = app.tree.set(item_id, column_name)
        print(cell_content, " ", len(cell_content))

        if len(cell_content) > max_length:
            longest_string = cell_content
            max_length = len(cell_content)

    for i in app.tree.get_children():
        app.tree.delete(i)

    app.tree["column"] = list(app.df.columns)
    app.tree["show"] = "headings"

    for col in app.tree["columns"]:
        app.tree.heading(col, text=col)

    for row in app.df.to_numpy().tolist():
        row[0] = truncate_path(row[0])
        item_id = app.tree.insert("", "end", values=row)
        print_cell_content(item_id, app.tree["columns"][0])

    font = tkfont.Font()
    for col in app.tree["columns"]:
        max_width = font.measure(col)

        for item in app.df[col].astype(str):
            max_width = max(max_width, font.measure(item))
        app.tree.column(col, width=max_width)
    
    print("Longest string: ", longest_string)
    print("Length: ", max_length)

def get_acl(app):
    if app.filepath:
        print("Hola mundo")
        display_data(app)
