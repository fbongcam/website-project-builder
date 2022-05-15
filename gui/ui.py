# Modules
from modules import tk
import ui_functions as ui_func
from main import createFiles


gui = tk.Tk()
gui.title("Website Template Builder")
# Window Size
gui.geometry("350x455")
gui.resizable(False, False)
gui.configure(background="#53585F")


# Menubar
menubar = tk.Menu(gui)
appmenu = tk.Menu(menubar, name='apple')
menubar.add_cascade(menu=appmenu)
appmenu.add_command(label='About')
appmenu.add_separator()
gui['menu'] = menubar


# Project name
# Label
proj_label = tk.Label(
    gui,
    text='Project name',
    bg='#53585F',
    fg='#717882')
proj_label.place(x=65, y=44)

# Entry
proj_entry_input = tk.Entry(
    gui,
    bg="#4C535A",
    fg='#fcfcfc',
    insertbackground='#717882',
    relief=tk.FLAT,
    borderwidth=20,
    highlightthickness=0)
proj_entry_input.place(x=65, y=79, width=220, height=50)


# Directory
# Label
dir_label = tk.Label(
    gui,
    text='Directory...',
    bg='#53585F',
    fg='#717882')
dir_label.place(x=65, y=145)

# Directory select button
# Modifiable string
selected_path = tk.StringVar()
dot_icon = tk.Canvas(
    gui,
    bg="#4C535A",
    bd=0,
    highlightthickness=0,
    width=50,
    height=50,
    cursor='pointinghand',
    )
ui_func.draw_dir_button(None, dot_icon, '#fcfcfc', '#fcfcfc')
dot_icon.place(x=236, y=178)
dot_icon.bind(
    '<Enter>', lambda x: ui_func.draw_dir_button(
        x, dot_icon, '#717882', '#717882'))
dot_icon.bind(
    '<Leave>', lambda x: ui_func.draw_dir_button(
        x, dot_icon, '#fcfcfc', '#fcfcfc'))
dot_icon.bind(
    '<Button-1>', lambda x: ui_func.updateDir(x, selected_path))

# Dir path
dir_path = tk.Entry(
    gui,
    bg="#4C535A",
    fg='#fcfcfc',
    textvariable=selected_path,
    state='disabled',
    disabledbackground='#4C535A',
    relief=tk.FLAT,
    borderwidth=20,
    highlightthickness=0)
dir_path.place(x=65, y=178, width=220, height=50)

dir_path.lower()

# Website type
# Label
website_label = tk.Label(
    gui,
    text='Website type',
    bg='#53585F',
    fg='#717882')
website_label.place(x=65, y=242)
# Options
site_type = tk.IntVar()
R1 = tk.Radiobutton(
    gui,
    text="HTML",
    variable=site_type,
    value=1,
    bg="#53585F",
    fg="#fcfcfc",
    justify=tk.LEFT,)
R1.select()
R1.place(x=65, y=277)
R2 = tk.Radiobutton(
    gui,
    text="PHP",
    variable=site_type,
    value=2,
    bg="#53585F",
    fg="#fcfcfc",
    justify=tk.LEFT)
R2.place(x=65, y=300)
# React option (radiobutton)
"""
R3 = tk.Radiobutton(
    gui,
    text="React",
    variable=site_type,
    value=3,
    bg="#53585F",
    fg="#fcfcfc",
    state=tk.DISABLED,
    justify=tk.LEFT)
R3.place(x=65, y=323)
"""

# Create button
create_button = tk.Label(
    gui,
    bg="#4C535A",
    fg='#fcfcfc',
    font=14,
    text='Create files',
    relief=tk.FLAT,
    highlightthickness=0,
    cursor='pointinghand')
create_button.bind(
    '<Enter>', lambda x: ui_func.mouseHover(x, create_button, 'bg', '#717882'))
create_button.bind(
    '<Leave>', lambda x: ui_func.mouseHover(x, create_button, 'bg', '#4C535A'))
create_button.place(x=65, y=356, width=220, height=50)

create_button.bind(
    '<Button-1>', lambda x: createFiles(
        x, proj_entry_input.get(), dir_path.get(), site_type.get())
)

gui.mainloop()
