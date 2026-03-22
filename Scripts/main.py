# Imports
from os import *
from os.path import *
from termcolor import *

# set "clear" var
if name == "nt":
    clear = "cls"
else:
    clear = "clear"

# Welcome
system(clear)
cprint("Welcome to SnakeSort!", attrs=["bold", "underline"])

# Getting pathToSort
pathToSort = input("What is the path of the directory you want to sort? ")
if pathToSort[-1] != "/" and pathToSort[-1] != "\\":
    pathToSort += "/"

# List files/dirs in pathToSort
pathArr = listdir(pathToSort)

# Set arrays
filesArr = []
dirArr = []

# Check if files are file/dir
for i in range(len(pathArr)):
    if isfile(pathToSort + pathArr[i]):
        filesArr.append(pathArr[i])
    else:
        dirArr.append(pathArr[i])

# Print the two arrs
system(clear)
print(f"Directory sorted: {pathToSort}\n")
print(f"Files: {filesArr}\n")
print(f"Dirs: {dirArr}\n")