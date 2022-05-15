# Modules
import modules
# UI
import ui
from modules import os
from modules import platform
from modules import subprocess
from modules import shutil


def readLines(text):
    if os.path.isfile(text) is True:
        file = open(text, 'r')
        text = file
    lines = []
    for line in text:
        lines.append(line)
    return lines


def replaceString(list, string1, string2):
    i = 0
    for line in list:
        if string1 in line:
            list[i] = string2
            break
        i += 1
    return list


def getIndex(list, value):
    for index, elem in enumerate(list):
        if value in elem:
            return index


def sliceText(list, start, end):
    if isinstance(start, int) is False:
        start = getIndex(list, start)
    if isinstance(end, int) is False:
        end = getIndex(list, end)
    return list[start:(end+1)]


def writeLines(list, file):
    line_count = len(list)
    i = 0
    for line in list:
        # Insert list[i] as line
        file.write(line)
        i += 1
        if i == line_count:
            file.close()
            break


def verifyOptions(proj_name, proj_path):
    if not proj_name:
        ui.ui_func.warningMsg('Project name is missing')
        return False
    if not proj_path:
        ui.ui_func.warningMsg('Specify a directory for your project')
        return False


def createFiles(event, proj_name, proj_path, site_type):
    if verifyOptions(proj_name, proj_path) is not False:
        # GET Platform (win, unix)
        operatingSystem = platform.system()
        # App PATH
        app_path = os.getcwd()
        # Working directory
        working_directory = proj_path
        # Create project folder
        os.mkdir(os.path.join(working_directory, proj_name))
        # Changes OS working directory
        os.chdir(os.path.join(working_directory, proj_name))

        # Create folders
        #
        # /css
        # /js
        # /img
        os.mkdir('css')
        print("mkdir css")
        os.mkdir('js')
        print("mkdir js")
        os.mkdir('img')
        print("mkdir img")

        # Create files
        # JS
        print("main.js")
        javascript_main = open(os.path.join("js", "main.js"), "w")
        javascript_main.close()
        print("function.js")
        javascript_functions = open(os.path.join("js", "functions.js"), "w")
        javascript_functions.close()
        # CSS
        print("style.css")
        shutil.copy(
            os.path.join(app_path, 'src', 'style.css'),
            os.path.join('css', 'style.css'))

        # Read .html template as list
        html_code = readLines(os.path.join(app_path, 'src', 'index.html'))
        # Replace html <Title> (list item)
        html_code = replaceString(
            html_code,
            '<title>WEBSITE TITLE</title>',
            ('\t<title>' + proj_name + '</title>'))
        # Check radiobutton value (website type)
        if site_type == 1:
            # Write html file
            file = open('index.html', 'w')
            writeLines(html_code, file)
        else:
            # Header.php
            file = open('header.php', 'w')
            file.write("<?php include 'functions.php'; ?>\n\n\n")
            for i in sliceText(html_code, 0, '</header>'):
                file.write(i)
            file.close()
            # Index.php
            file = open('index.php', 'w')
            file.write("<?php include 'header.php' ?>\n\n\n\n")
            for i in sliceText(html_code, '<main>', '</main>'):
                file.write(i)
            file.write("\n\n\n<?php include 'footer.php' ?>")
            file.close()
            # footer.php
            file = open('footer.php', 'w')
            for i in sliceText(html_code, '<footer>', '</html>'):
                file.write(i)
            file.close()
            # functions.php
            file = open('functions.php', 'w')
            file.write('<?php\n\n\n\n?>')
            file.close()

        # Opens created project folder
        if "Windows" in operatingSystem:
            os.startfile(os.getcwd())
        elif "Darwin" in operatingSystem:
            subprocess.Popen(["open", os.getcwd()])

        # Resets working directory
        os.chdir(app_path)
