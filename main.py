# Imports
from os import *
from os.path import *
from shutil import *
from tkinter import *
from tkinter import ttk
from tkinter.font import *
import pyglet

# Get Consolas Font
pyglet.font.add_file("consolas.ttf")

# Define Sort()
def Sort():

    # Getting pathToSort
    global pathToSortVar
    pathToSort = pathToSortVar.get()

    # Join the paths
    if pathToSort[-1] != "/" and pathToSort[-1] != "\\":
        pathToSort += "/"

    # Check if directory
    if not isdir(pathToSort):
        return 0

    # Get files in folder
    pathArr = listdir(pathToSort)

    # Iterate through each file
    for i in range(len(pathArr)):

        # Get the current element
        checkNow = pathArr[i]

        # Check if directory
        if isdir(pathToSort + checkNow):
            try:
                mkdir(f"{pathToSort}/Directories")
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Directories/{checkNow}")
            except FileExistsError:
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Directories/{checkNow}")

        # Check if plain text
        elif checkNow.lower().endswith(".txt"):
            try:
                mkdir(f"{pathToSort}/Plain Text")
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Plain Text")
            except FileExistsError:
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Plain Text")

        # Check if image
        elif checkNow.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif")):
            try:
                mkdir(f"{pathToSort}/Images")
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Images")
            except FileExistsError:
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Images")
        
        # Check if video
        elif checkNow.lower().endswith((".mp4", ".mov", ".mkv", ".avi", ".webm")):
            try:
                mkdir(f"{pathToSort}/Videos")
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Videos")
            except FileExistsError:
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Videos")

        # Check if audio
        elif checkNow.lower().endswith((".mp3", ".wav", ".ogg", ".aac", ".flac")):
            try:
                mkdir(f"{pathToSort}/Audio")
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Audio")
            except FileExistsError:
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Audio")

        # Check if script
        elif checkNow.lower().endswith((".py", ".js", ".java", ".cs", ".cpp", ".json", ".ts")):
            try:
                mkdir(f"{pathToSort}/Scripts")
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Scripts")
            except FileExistsError:
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Scripts")

        # Check if link
        elif checkNow.lower().endswith(".lnk"):
            try:
                mkdir(f"{pathToSort}/Links")
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Links")
            except FileExistsError:
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Links")
        
        # Check if executable
        elif checkNow.lower().endswith(".exe"):
            try:
                mkdir(f"{pathToSort}/Executables")
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Executables")
            except FileExistsError:
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Executables")

        # Check if binary
        elif checkNow.lower().endswith(".bin"):
            try:
                mkdir(f"{pathToSort}/Binaries")
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Binaries")
            except FileExistsError:
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Binaries")

        # Check if DLL
        elif checkNow.lower().endswith(".dll"):
            try:
                mkdir(f"{pathToSort}/DLLs")
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/DLLs")
            except FileExistsError:
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/DLLs")

        # Other
        else:
            try:
                mkdir(f"{pathToSort}/Other (Unknown extention)")
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Other (Unknown extention)")
            except FileExistsError:
                move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Other (Unknown extention)")
    return 1

# Define onClick()
def onClick():
    sort = Sort()
    if sort == 0:
        errortext.set("Error - Check if path is valid, a directory and doesnt\n include a folder named \"Directories\", then try agian")
    else:
        errortext.set("")
        if odchkboxvar.get() == True:
            startfile(pathToSortVar.get())
        if cgchkboxvar.get() == True:
            raise SystemExit

# Window Setup
root = Tk()
root.title("SnakeSort")
root.geometry("500x250")

# Title
title = ttk.Label(root, text="Welcome to SnakeSort GUI!")
title.place(relx=0.5, rely=0, anchor=N)

# Title Font
titleFont = Font(title, family="consolas", size=15)
titleFont.configure(underline = True, weight = BOLD)
title.config(font=(titleFont))

# Main Font & Style
mainFont = Font(family="consolas", size=9)
mainStyle = ttk.Style()
mainStyle.configure("Custom.TButton", font=(mainFont))

# Instructions Label
instructions = ttk.Label(root, font=mainFont, text="    Please enter your directory to sort below\n        and click sort when you are ready.")
instructions.place(rely=0.3, relx=0.45, anchor="center")

# Open Folder Checkbox
odchkboxvar = BooleanVar(value=True)
opendirchkbx = ttk.Checkbutton(root, text="Open folder after sort?", onvalue=True, offvalue=False, variable=odchkboxvar)
opendirchkbx.place(rely=0.45, relx=0.5, anchor="center")

# Close Gui Checkbox
cgchkboxvar = BooleanVar(value=True)
opendirchkbx = ttk.Checkbutton(root, text="Close GUI after sort?", onvalue=True, offvalue=False, variable=cgchkboxvar)
opendirchkbx.place(rely=0.55, relx=0.5, anchor="center")

# Setting pathToSort & Creating "Sort" Button
pathToSortVar = StringVar()
pathToSortEntry = ttk.Entry(root, width=30, textvariable=pathToSortVar, font=mainFont)
pathToSortEntry.place(relx=0.05, rely=0.7, anchor=W)
pathToSortEntry.insert(END, "default")        
button = ttk.Button(root, text="Sort", command=onClick, style="Custom.TButton")
button.place(relx=0.95, rely=0.7, anchor=E)

# Status Label
errortext = StringVar(value="")
errorlabel = ttk.Label(root, textvariable=errortext, font=mainFont)
errorlabel.place(rely=0.875, relx=0.5, anchor="center")
errorlabel.config(font=("consolas", 6), foreground="red")

# Main Loop & Extra
root.resizable(False, False)
root.mainloop()