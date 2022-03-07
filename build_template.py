#!/usr/bin/env python

# Importing TKinter
# File dialog functionality
import Tkinter as tk
import tkFileDialog as fd
# Importing OS Module
import os
import platform
import subprocess
import sys


class textstyle:
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'


# CODE TEMPLATES
#
# HTML
html_header = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <!-- Toolbar color (mobile browsers) -->
  <meta name="theme-color" content="#fff">
  <!-- Edge compatibility -->
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="WEBSITE DESCRIPTION!">

  <title>WEBSITE TITLE</title>

  <link rel="stylesheet" """ + \
  """type="text/css" title="style" href="css/style.css">
</head>
<body>

    <!-- Header -->
    <header>
        <nav></nav>
    </header>
"""
html_main = """
    <main>
        <!-- CONTENT GOES HERE -->
    </main>
"""
html_footer = """
  <!-- Footer -->
  <footer>
  </footer>

  <script src="js/functions.js"></script>
  <script src="js/main.js"></script>
</body>
</html>
"""

#
# CSS
css_code = """@charset "UTF-8";


/* Fonts (@import) */


/*----------------*/
/*     BASE     */
/*----------------*/

body {

}

/* Titles */
h1, h2, h3, h4, h5, h6 {

}

h1 {

}

h2 {

}

h3 {

}

h4 {

}

h5 {

}

h6 {

}

/* Paragraphs */
p {

}

/* Lists */
ul {

}

li {

}

/* Links */
a:link, a:active, a:visited {

}

a:hover {

}

img {

}

/*----------------*/
/*----------------*/




/*-----------------*/
/*     Header      */
/*-----------------*/

header {

}

nav {

}

/*-----------------*/
/*-----------------*/




/*----------------*/
/*    Content     */
/*----------------*/

main {

}

/*----------------*/
/*----------------*/




/*----------------*/
/*    Footer      */
/*----------------*/

footer {

}

/*----------------*/
/*----------------*/


"""

# SETTINGS
scss = False
website_type = None
bootstrap = False

# GET Platform (win, unix)
platform = platform.system()

# CHOOSE DIRECTORY
#
# Disable GUI from tkinter
gui = tk.Tk()
gui.withdraw()
# Select working directory
print('\nSelect where to create project...')
print('(A new directory will be'),
print('created with your project name in next step)')
gui.update()
working_directory = fd.askdirectory()

# ABORT OPERATION IF NO PATH SELECTED
if working_directory == '':
    sys.exit('No path provided.')

# Clear window
os.system('cls' if os.name == 'nt' else 'clear')

# CHOOSE PROJECT NAME
print('\nName your project:')
project_name = raw_input(textstyle.BOLD)
while os.path.exists(os.path.join(working_directory, project_name)):
    print(textstyle.END + "\nPath already exists.\n")
    project_name = raw_input(textstyle.BOLD)

print(textstyle.END)
print(
    "Directory:\n" +
    os.path.join(
        working_directory, textstyle.BOLD + project_name + textstyle.END
        )
    )

# Create project folder
os.mkdir(os.path.join(working_directory, project_name))
# Changes OS working directory
os.chdir(os.path.join(working_directory, project_name))


# Create files
def createFiles(type, scss):
    # Clear terminal
    if type == "static":
        os.system('cls' if os.name == 'nt' else 'clear')
        # Static website
        print("\nCreating a Static website...")
        print(textstyle.BOLD + "index.html")
        html = open("index.html", "w")
        html_code = (
            html_header +
            html_main +
            html_footer)
        html.write(html_code)
        html.close()
    elif type == "dynamic":
        # Dynamic website
        # Choose to include functions.php file
        php_functions = raw_input(
            "\nDo you want to include a " + textstyle.RED + "functions.php" +
            textstyle.END + " file in your website?"
            "\n"
            "(" + textstyle.BOLD + "y" + textstyle.END + "/" +
            textstyle.BOLD + "n" + textstyle.END + "):"
            )

        while php_functions != "y" or php_functions != "n":
            if php_functions == "y" or php_functions == "n":
                break
            else:
                php_functions = raw_input(
                    "Please answer y (yes) or n (no)\n"
                    "(" + textstyle.BOLD + "y" + textstyle.END + "/" +
                    textstyle.BOLD + "n" + textstyle.END + "):"
                    )
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nCreating a Dynamic website...")
        # index.php
        print(textstyle.BOLD + "index.php")
        php_index = open("index.php", "w")
        php_index.write("""<?php include 'header.php';

        ?>
        """ + html_main + "\n<?php include \
        'footer.php'; ?>")
        # header.php
        print("header.php")
        php_header = open("header.php", "w")

        if php_functions == "y":
            # Create functions.php
            print("functions.php")
            php_functions = open("functions.php", "w")
            php_header.write(
                "<?php include 'functions.php'; ?>" + "\n")

        php_header.write("\n" + html_header)
        php_header.close()
        # footer.php
        print("footer.php")
        php_footer = open("footer.php", "w")
        php_footer.write(html_footer)

    # Create folders
    #
    # /css
    # /js
    # /img
    os.mkdir(os.path.join(working_directory, project_name, 'css'))
    print("mkdir css")
    os.mkdir(os.path.join(working_directory, project_name, 'js'))
    print("mkdir js")
    os.mkdir(os.path.join(working_directory, project_name, 'img'))
    print("mkdir img")
    # JS files
    print("main.js")
    javascript_main = open(os.path.join("js", "main.js"), "w")
    javascript_main.write("/*\n\tmain.js\n\t@author AUTHOR GOES HERE\n*/")
    javascript_main.close()
    print("function.js")
    javascript_functions = open(os.path.join("js", "functions.js"), "w")
    javascript_functions.write(
        "/*\n\tfunctions.js\n\t@author AUTHOR GOES HERE\n*/")
    javascript_functions.close()

    if scss is True:
        # SCSS files
        print("style.scss")
        scss = open(os.path.join("css", "style.scss"), "w")
        scss.write("@import 'variables.scss'")
        scss.close()
        print("variables.scss" + textstyle.END)
        scss = open(os.path.join("css", "variables.scss"), "w")
        scss.close()
    else:
        # CSS files
        print("style.css" + textstyle.END)
        css = open(os.path.join("css", "style.css"), "w")
        css.write(css_code)
        css.close()
    print("...Done!\n")

    # Opens created project folder
    if "Windows" in platform:
        os.startfile(os.getcwd())
    elif "Darwin" in platform:
        subprocess.Popen(["open", os.getcwd()])


# CHOOSE TYPE OF WEBSITE
print(
    "\nChoose between a " + textstyle.RED + "Static" + textstyle.END + " or " +
    textstyle.RED + "Dynamic" + textstyle.END + " website:"
    )
print("[" + textstyle.BOLD + "1" + textstyle.END + "]\tStatic (html)")
print("[" + textstyle.BOLD + "2" + textstyle.END + "]\tDynamic (php)")

while website_type != "1" or website_type != "2":
    website_type = raw_input("\n(type 1 or 2):\t")
    if website_type == "1" or website_type == "2":
        break

print(
    "\nWill you use " + textstyle.RED + "SASS" + textstyle.END
    + " in your project?"
    )

while scss != "y" or scss != "n":
    scss_input = raw_input(
        "(" + textstyle.BOLD + "y" + textstyle.END + "/" +
        textstyle.BOLD + "n" + textstyle.END + "):"
    )
    if scss_input == "y":
        scss = True
        break
    if scss_input == "n":
        break

if website_type == "1":
    createFiles("static", scss)

if website_type == "2":
    createFiles("dynamic", scss)
