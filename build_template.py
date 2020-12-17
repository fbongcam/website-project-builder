# Importing TKinter
# File dialog functionality
import Tkinter as tk
import tkFileDialog as fd
# Importing OS Module
import os
import platform
import subprocess
# CODE TEMPLATES
import code_templates

# GET Platform (win, unix)
platform = platform.system()

# CHOOSE DIRECTORY
#
# Disable GUI from tkinter
gui = tk.Tk()
gui.withdraw()
# Select working directory
print('\nSelect where to create project...')
working_directory = fd.askdirectory()
gui.destroy()

# CHOOSE PROJECT NAME
print('\nName your project:')
project_name = raw_input()
print("\nDirectory:\n" + os.path.join(working_directory, project_name))

# Directories to create
#
# /Project folder
#   /css
#   /js
#   /img
os.mkdir(os.path.join(working_directory, project_name))
os.mkdir(os.path.join(working_directory, project_name, 'css'))
os.mkdir(os.path.join(working_directory, project_name, 'js'))
os.mkdir(os.path.join(working_directory, project_name, 'img'))

# Changes OS working directory
os.chdir(os.path.join(working_directory, project_name))


# Create files
def createFiles(type):
    if type == "static":
        # Static website
        print("Creating a Static website...")
        html = open("index.html", "w")
        html_code = (
            code_templates.html_header +
            code_templates.html_main +
            code_templates.html_footer)
        html.write(html_code)
        html.close()
    elif type == "dynamic":
        # Dynamic website
        # Choose to include functions.php file
        php_functions = raw_input(
            "\nDo you want to include a functions.php file in your website?"
            "\n"
            "(y/n):")

        while php_functions != "y" or php_functions != "n":
            if php_functions == "y" or php_functions == "n":
                break
            else:
                php_functions = raw_input(
                    "Please answer y (yes) or n (no)\n"
                    "(y/n):")

        print("\nCreating a Dynamic website...")
        # index.php
        php_index = open("index.php", "w")
        php_index.write("""<?php include 'header.php';

        ?>
        """ + code_templates.html_main + "\n<?php include \
        'footer.php'; ?>")
        # header.php
        php_header = open("header.php", "w")

        if php_functions == "y":
            # Create functions.php
            php_functions = open("functions.php", "w")
            php_header.write(
                "<?php include 'functions.php'; ?>" + "\n")

        php_header.write("\n" + code_templates.html_header)
        php_header.close()
        # footer.php
        php_footer = open("footer.php", "w")
        php_footer.write(code_templates.html_footer)

    if type == "static" or "dynamic":
        # JS files
        javascript_main = open(os.path.join("js", "main.js"), "w")
        javascript_main.close()
        javascript_functions = open(os.path.join("js", "functions.js"), "w")
        javascript_functions.close()
        # CSS files
        css = open(os.path.join("css", "style.css"), "w")
        css.write(code_templates.css_code)
        css.close()

        print("...Done!")

        # Opens created project folder
        if "Windows" in platform:
            os.startfile(os.getcwd())
        elif "Darwin" in platform:
            subprocess.Popen(["open", os.getcwd()])


# CHOOSE TYPE OF WEBSITE
print("\nChoose between a Static or Dynamic website:")
print("[ 1 ]\tStatic (html)")
print("[ 2 ]\tDynamic (php)")

website_type = None

while website_type != "1" or website_type != "2":
    website_type = raw_input("\n(type 1 or 2):\t")

    if website_type == "1":
        createFiles("static")
        break
    elif website_type == "2":
        createFiles("dynamic")
        break
