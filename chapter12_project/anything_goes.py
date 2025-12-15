# FILE NAME - anything_goes.py
# Remember to cite any sources you used to help you complete this project!

# NAME: Nick Carlson
# DATE: 12/3/2025
# BRIEF DESCRIPTION: Final Project

# Library of audiovisual, literary, and musical media. Entries can be added and removed.
# Menu for choosing one of the three, then another menu to show only a certain genre, favorites, or others
# can then choose a specific book, song, movie, etc. to bring up a brief description or synopsis.

import os

os.chdir("./chapter12_project")

# lists all files and directories via path
# 1 From here to * is sourced from https://www.geeksforgeeks.org/python/python-list-all-files-in-directory-and-subdirectories/
def list_files_walk(start_path='.'):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            print(os.path.join(root, file))

# Specify the directory path you want to start from
# directory_path = os.curdir
# list_files_walk(directory_path) # *

# Source - https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
# Posted by user136036, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-08, License - CC BY-SA 4.0
# makes a list with all subdirectories in specified directory(folder)

def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

# print(fast_scandir(os.curdir))

# Source - https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory
# Posted by sloth, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-08, License - CC BY-SA 4.0
# makes a list with all files in current directory(folder)

def curdir_file_fun():
    curdir_files = [f for f in os.listdir(os.curdir) if os.path.isfile(f)]
    return curdir_files

# creates or modifies a file(depends in the file exists or not)
def create_file():
    new_file_name = input("Enter the name of the file to edit/create: ")
    file_extension = input("Enter the file extension(i.e. txt, py, md): ")
    new_file = new_file_name + "." + file_extension
    file = open(new_file, "w")
    file_entry = input("Enter what will be in the file(this will overwrite anything in the file): ")
    file.write(file_entry)
    file.close()

def read_file(to_read):
    # find file in current file list
    open_file = open(curdir_file_list[to_read-1], "r")
    print(open_file.read())

dir_list = ["/workspaces/Intro-to-Python/chapter12_project"]
end = False    
while end == False:
    #print Files
    print("\nFiles:")
    curdir_file_list = curdir_file_fun()
    curdir_folder_list = fast_scandir(os.curdir)
    for file in curdir_file_list:
        print(f"{curdir_file_list.index(file) + 1}. {file}")
    print()
    #print Folders
    print("Folders:")
    for folder in curdir_folder_list:
        print(f"{len(curdir_file_list) + curdir_folder_list.index(folder) + 1}. {folder}")
    print()
    #print Edit/Create
    print(f"{len(curdir_file_list) + len(curdir_folder_list) + 1}. Edit/Create")
    #print All Files
    print(f"{len(curdir_file_list) + len(curdir_folder_list) + 2}. All Files")
    #print Back
    print(f"{len(curdir_file_list) + len(curdir_folder_list) + 3}. Back")
    #print End Program
    print(f"{len(curdir_file_list) + len(curdir_folder_list) + 4}. End Program")
    #take input
    num = int(input("\nEnter the number next to the option you want to choose: "))
    print()
    #error
    if num < 1 or num > (len(curdir_file_list) + len(curdir_folder_list) + 4):
        print("Invalid number.")
    #choose file
    elif num <= (len(curdir_file_list)):
        read_file(num)
    #choose folder
    elif num <= (len(curdir_file_list) + len(curdir_folder_list)):
        dir_list.append(curdir_folder_list[num - len(curdir_file_list) - 1])
        os.chdir(dir_list[-1])
    #choose edit/create file
    elif num == (len(curdir_file_list) + len(curdir_folder_list) + 1):
        create_file()
    #choose all files
    elif num == (len(curdir_file_list) + len(curdir_folder_list) + 2):
        list_files_walk(dir_list[-1])
    #choose back
    elif num == (len(curdir_file_list) + len(curdir_folder_list) + 3):
        if len(dir_list) == 1:
            print("You cannot go back.")
        else:
            dir_list.pop(-1)
            os.chdir(dir_list[-1])
    #choose end
    elif num == (len(curdir_file_list) + len(curdir_folder_list) + 4):
        end = True


# Files
# Folders
# Edit/Create
# All Files
# Back
# End Program




########################################
#          REFLECTION QUESTIONS
########################################

'''
Remember to cite any sources you used to help you complete this project.
You can do that here in this section or cite as comments throughout your code.

1. How did you choose the goal of your program?
It seemed like a reasonably simple program to make with room for improvement

2. What part of this project challenged you the most? How did you work through that challenge?
Lining up all of the information so that I could properly write the code. I wrote it down.

3. If you had 10 more hours to improve or expand your program, what would you change? Why?
I would include the ability to listen to mp3 and maybe mp4 files and also fix an issue with folders.

'''
