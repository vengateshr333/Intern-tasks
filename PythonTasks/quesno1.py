"""Question1.

Appending hello world
"""


def text_append(file, text):
    """Code to append a text."""
    with open(file, mode='a', encoding="utf-8") as f_i:
        f_i.write(text+'\n')


filename = input('enter the file name you want to append: ')
textadd = input('enter the text you wish to add: ')
text_append(filename, textadd)
