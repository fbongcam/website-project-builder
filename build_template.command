#!/usr/bin/env python

from __future__ import print_function
# Importing TKinter
# File dialog functionality
import Tkinter as tk
import tkFileDialog as fd
# Importing OS Module
import os
import platform
import subprocess
import sys
from zipfile import ZipFile
import imp
import shutil


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
def createFiles(type, scss, bootstrap):
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

    if scss:
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

    if bootstrap is True:
        file = None
        if type == 'static':
            file = open(os.path.join("index.html"), "r+")
        if type == 'dynamic':
            file = open(os.path.join("header.php"), "r+")
        textlines = file.readlines()
        file.seek(0)
        file.truncate()
        # Add bootstrap CDNs
        for i in range(len(textlines)):
            if not scss:
                if 'link rel="stylesheet"' in textlines[i]:
                    textlines[i] = (
                        '<link href="https://cdn.jsdelivr.net/npm/bootstrap' +
                        '@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"' +
                        'integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT' +
                        '94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="ano' +
                        'nymous">\n' + textlines[i]
                    )
            if (type == 'static' and
                    '<script src="js/functions.js">' in textlines[i]):
                textlines[i] = (
                    '<script src="https://cdn.jsdelivr.net/npm/bootstrap' +
                    '@5.1.3/dist/js/bootstrap.bundle.min.js"' +
                    ' integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+' +
                    'OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"' +
                    ' crossorigin="anonymous"></script>\n' + textlines[i])
        # Write lines
        for elem in textlines:
            file.write(str(elem))
        file.close()
        if type == 'dynamic':
            file = open(os.path.join('footer.php'), "r+")
            textlines = file.readlines()
            file.seek(0)
            file.truncate()
            for i in range(len(textlines)):
                if '<script src="js/functions.js">' in textlines[i]:
                    textlines[i] = (
                        '<script ' +
                        'src="https://cdn.jsdelivr.net/npm/bootstrap' +
                        '@5.1.3/dist/js/bootstrap.bundle.min.js"' +
                        ' integrity="sha384-ka7Sk0Gln' +
                        '4gmtz2MlQnikT1wXgYsOg+' +
                        'OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"' +
                        ' crossorigin="anonymous"></script>\n'
                        + textlines[i])
            for elem in textlines:
                file.write(str(elem))
            file.close()
        if scss:
            non_standard_modules = ['requests']

            # Check non standard modules
            for module in non_standard_modules:
                try:
                    if imp.find_module(module):
                        __import__(
                            module, globals(), locals(), fromlist=[], level=-1)
                except ImportError:
                    print("\nMissing module\t" + module)
                    print(
                        "\nDownloading "
                        + textstyle.BOLD + module + textstyle.END + "...")
                    subprocess.call(
                        "python -m pip install " + module, shell=True)
                    __import__(
                        module, globals(), locals(), fromlist=[], level=-1)

            bootstrap_url = (
                "https://api.github.com/repos/twbs/bootstrap/releases/latest"
                )
            request = sys.modules['requests'].get(bootstrap_url)
            json = request.json()
            source_code_url = json["zipball_url"]
            file = (
                sys.modules['requests'].get(
                        source_code_url, stream=True, timeout=5
                    )
                )
            fileSize = file.headers['content-length']

            # Download and Write file
            filename = 'bootstrap_source.zip'
            with open(filename, 'wb') as f:
                data = 0
                for chunk in file.iter_content(chunk_size=1024*10):
                    print(
                            textstyle.BOLD +
                            '\nFetching bootstrap:\t' +
                            textstyle.END + str(data) +
                            '/' + str(fileSize) + ' bytes', end='\r'
                        )
                    f.write(chunk)
                    data += 1024*10
            # Extract SCSS files
            print("\nExtracting...")
            filePath = None
            ZipFile(filename).extractall('css')
            # Delete archive
            print("Cleaning up")
            # Change working directory to CSS folder
            os.chdir(os.path.join('css'))
            filesInCSS = os.listdir('.')
            for file in filesInCSS:
                if 'bootstrap' in file:
                    # Rename folder
                    os.rename(file, 'bootstrap')
            # Enter bootstrap dir
            os.chdir(os.path.join('bootstrap'))
            filesInBootstrap = os.listdir('.')
            # Remove all files except .scss
            for file in filesInBootstrap:
                if file != 'scss':
                    if os.path.isdir(file):
                        shutil.rmtree(file)
                    else:
                        os.remove(file)
            # Move SCSS files
            destination = os.path.abspath('.')
            os.chdir(os.path.join('scss'))
            source = os.path.abspath('.')
            for file in os.listdir('.'):
                shutil.move(source + '/' + file, destination + '/' + file)
            os.chdir(os.path.join('../'))
            shutil.rmtree('scss')
            # GO BACK TO MAIN FOLDER
            os.chdir(os.path.join(working_directory, project_name))
            # REMOVE BOOTSTRAP ARCHIVE
            os.remove(filename)
            # ADD IMPORTS TO SCSS (BOOTSTRAP)
            file = open(os.path.join("css/style.scss"), "r+")
            textlines = file.readlines()
            file.seek(0)
            file.truncate()
            # FIND '@import'
            for i in range(len(textlines)):
                if '@import' in textlines[i]:
                    textlines[i] = (
                        '@import \'bootstrap/bootstrap\';\n' +
                        textlines[i]
                    )
            # Write lines
            for elem in textlines:
                file.write(elem)
            file.close()
    print("Done!\n")
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

while True:
    scss_input = raw_input(
        "(" + textstyle.BOLD + "y" + textstyle.END + "/" +
        textstyle.BOLD + "n" + textstyle.END + ")?\t"
    )
    if scss_input == "y":
        scss = True
        break
    if scss_input == "n":
        break

print(
    "\nInclude " + textstyle.RED + "Bootstrap" + textstyle.END
    + "?"
    )

while True:
    bootstrap_input = raw_input(
        "(" + textstyle.BOLD + "y" + textstyle.END + "/" +
        textstyle.BOLD + "n" + textstyle.END + ")?\t"
    )
    if bootstrap_input == "y":
        bootstrap = True
        break
    if bootstrap_input == "n":
        break

if website_type == "1":
    createFiles("static", scss, bootstrap)

if website_type == "2":
    createFiles("dynamic", scss, bootstrap)
