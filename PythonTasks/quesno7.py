"""quesno-7.

To find the space occupied by a folder.
"""
import os


def space_cal(pathname):
    """Calc folder space."""
    space = 0
    for filepath, _dirs, file in os.walk(pathname):
        for f_i in file:
            new_path = os.path.join(filepath, f_i)
            space += os.path.getsize(new_path)
    return space


path = input('Enter the folder path: ')
folder_space = space_cal(path)
print(folder_space)
