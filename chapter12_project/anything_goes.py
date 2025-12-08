# FILE NAME - anything_goes.py
# Remember to cite any sources you used to help you complete this project!

# NAME: Nick Carlson
# DATE: 12/3/2025
# BRIEF DESCRIPTION: Final Project

# Library of audiovisual, literary, and musical media. Entries can be added and removed.
# Menu for choosing one of the three, then another menu to show only a certain genre, favorites, or others
# can then choose a specific book, song, movie, etc. to bring up a brief description or synopsis.

import os

# 1 From here to * is sourced from https://www.geeksforgeeks.org/python/python-list-all-files-in-directory-and-subdirectories/
def list_files_walk(start_path='.'):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            print(os.path.join(root, file))

# Specify the directory path you want to start from
directory_path = './chapter12_project'
list_files_walk(directory_path) # *

# Source - https://stackoverflow.com/questions/973473/getting-a-list-of-all-subdirectories-in-the-current-directory
# Posted by user136036, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-08, License - CC BY-SA 4.0

def fast_scandir(dirname):
    subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(fast_scandir(dirname))
    return subfolders

print(fast_scandir("./chapter12_project"))

# Source - https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory
# Posted by sloth, modified by community. See post 'Timeline' for change history
# Retrieved 2025-12-08, License - CC BY-SA 4.0

import os
files = [f for f in os.listdir('.') if os.path.isfile(f)]
print(files)








########################################
#          REFLECTION QUESTIONS
########################################

'''
Remember to cite any sources you used to help you complete this project.
You can do that here in this section or cite as comments throughout your code.

1. How did you choose the goal of your program?


2. What part of this project challenged you the most? How did you work through that challenge?


3. If you had 10 more hours to improve or expand your program, what would you change? Why?


'''
