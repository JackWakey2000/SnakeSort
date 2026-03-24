# Imports
from os import *
from os.path import *
from shutil import *
from tkinter import *
from tkinter import ttk

# Define Sort()
def Sort():

    # Getting pathToSort
    global pathToSort
    pathToSort = pathToSort.get()

    # Join the paths
    if pathToSort[-1] != "/" and pathToSort[-1] != "\\":
        pathToSort += "/"

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

# Window Setup
root = Tk()
root.title = "SnakeSort"

# Button Frame
buttonframe = ttk.Frame(root, padding=(5, 5, 45, 5), width=100, height=100)

# Setting pathToSort & Creating "Sort" Button
pathToSort = StringVar()
pathToSort_entry = ttk.Entry(buttonframe, width=40, textvariable=pathToSort).grid(row=1, sticky=W, padx=5, pady=5)
ttk.Button(root, text="Sort", command=Sort).grid(row=1, padx=5, pady=5, sticky=SE)

# Main Loop & Extra
root.resizable(True, True)
root.mainloop()