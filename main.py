# Imports
from os import *
from os.path import *
from termcolor import *
from shutil import *

# Set "clear" var
if name == "nt":
    clear = "cls"
else:
    clear = "clear"

# Welcome
system(clear)
cprint("Welcome to SnakeSort!", attrs=["bold", "underline"])

# Getting pathToSort & Confirming
pathToSort = input("What is the path of the directory you want to sort? ")
if pathToSort[-1] != "/" and pathToSort[-1] != "\\":
    pathToSort += "/"
    print(pathToSort)
if input("Are you sure? (Y/n) ") == "n":
    raise SystemExit

# List files/dirs in pathToSort
pathArr = listdir(pathToSort)

# Sorting the files
system(clear)
print("Sorting...")
for i in range(len(pathArr)):
    checkNow = pathArr[i]
    if isdir(pathToSort + checkNow):
        try:
            mkdir(f"{pathToSort}/Directories")
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Directories/{checkNow}")
        except FileExistsError:
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Directories/{checkNow}")
    elif checkNow.lower().endswith(".txt"):
        try:
            mkdir(f"{pathToSort}/Plain Text")
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Plain Text")
        except FileExistsError:
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Plain Text")
    elif checkNow.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".webp", ".gif")):
        try:
            mkdir(f"{pathToSort}/Images")
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Images")
        except FileExistsError:
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Images")
    elif checkNow.lower().endswith((".mp4", ".mov", ".mkv", ".avi", ".webm")):
        try:
            mkdir(f"{pathToSort}/Videos")
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Videos")
        except FileExistsError:
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Videos")
    elif checkNow.lower().endswith((".mp3", ".wav", ".ogg", ".aac", ".flac")):
        try:
            mkdir(f"{pathToSort}/Audio")
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Audio")
        except FileExistsError:
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Audio")
    elif checkNow.lower().endswith((".py", ".js", ".java", ".cs", ".cpp", ".json", ".ts")):
        try:
            mkdir(f"{pathToSort}/Scripts")
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Scripts")
        except FileExistsError:
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Scripts")
    elif checkNow.lower().endswith(".lnk"):
        try:
            mkdir(f"{pathToSort}/Links")
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Links")
        except FileExistsError:
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Links")
    elif checkNow.lower().endswith(".exe"):
        try:
            mkdir(f"{pathToSort}/Executables")
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Executables")
        except FileExistsError:
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Executables")
    elif checkNow.lower().endswith(".bin"):
        try:
            mkdir(f"{pathToSort}/Binaries")
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Binaries")
        except FileExistsError:
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Binaries")
    elif checkNow.lower().endswith(".dll"):
        try:
            mkdir(f"{pathToSort}/DLLs")
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/DLLs")
        except FileExistsError:
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/DLLs")
    else:
        try:
            mkdir(f"{pathToSort}/Other (Unknown extention)")
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Other (Unknown extention)")
        except FileExistsError:
            move(f"{pathToSort}/{checkNow}", f"{pathToSort}/Other (Unknown extention)")

# Final print
system(clear)
print(f"Directory sorted: {pathToSort}")