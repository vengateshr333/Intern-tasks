"""Ques no-5.

Most occuring word in a file
"""

import re
from collections import Counter


def most_occur(filename):
    """Count most occuring word."""
    with open(filename, mode='r', encoding="utf-8") as myf:
        l_i = re.split(r'[\ \.\n\!\,\=\-\. \:\, ]', myf.read())
    cmax = Counter(l_i)
    return cmax.most_common(1)[0][0]


def file_write(filename, content):
    """Func to Load content in a file."""
    with open(filename, mode='w', encoding="utf-8") as myf:
        myf.write(content)


name_file = input('choose the name for the file: ')
info = input('enter the text to write: ')
file_write(name_file, info)
word = most_occur(name_file)
print('the most occured word is: '+word)
