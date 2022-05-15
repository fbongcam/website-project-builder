from modules import fd
from modules import messagebox
from modules import os


def updateDir(event, selected_path):
    working_directory = fd.askdirectory(
        initialdir='/Users/' + os.environ['USER'])
    selected_path.set(working_directory)


def mouseHover(event, widget, property, value):
    widget[str(property)] = value


def draw_dir_button(event, canvas, fill, outline):
    canvas.delete('all')
    canvas.create_oval(15, 23, 19, 27, fill=fill, outline=outline)
    canvas.create_oval(23, 23, 27, 27, fill=fill, outline=outline)
    canvas.create_oval(31, 23, 35, 27, fill=fill, outline=outline)


def warningMsg(msg):
    messagebox.showwarning(
        'Warning',
        msg
    )
