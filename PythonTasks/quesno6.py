"""Quesno-6.

printing first column in csv and copying in new csv.
"""

import pandas as pd


def first_col(path, newfile):
    """To print the first column."""
    d_f = pd.read_excel(path)
    new_df = d_f[d_f.columns[0]]
    new_df.to_excel(newfile, index=False)
    return d_f[d_f.columns[0]]


filepath = input('Enter the file path: ')
new_filename = input('Enter the new excel file name: ')
ans = first_col(filepath, new_filename)
print(ans)
