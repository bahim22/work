# %% [markdown]
# # Prac file opening, printing and json module
#
# ## Import library/modules => open json file => load as variable name
#

# %%
import filecmp
from pprint import pprint as pp
import json

# %%
# with open('data/monthlySalesbyCategoryMultiple.json') as json_data:
with open('../Data/sample-return/data/DelveData.jsonc') as json_data:
    d = json.load(json_data)
    print(d)

# %%


def json_open2(file=''):
    '''
        import json and create func with file param
        and ask for input on script init

        open, load, then print the file w/ json
    '''
    import os

    # from os import path

    file = str(input('Enter full path to json filename: '))
    if os.path.isfile(file):
        with open(file) as data:
            dd = json.load(data)
            print(dd)
    else:
        print(f'{file} does not exist.')

# %%


def json_open(file=''):
    '''
        import json and create func with file param
        and ask for input on script init
        open, load, then print the file w/ json
        if file doesn't exist print error
    '''
    import os
    # from sys import path
    from pprint import pprint as pp

    if file == '':
        file = str(input('Enter full path to json filename: '))
    else:
        file = file
    if os.path.isfile(file):
        with open(file) as data:
            dd = json.load(data)
            pp(dd)
    else:
        print(f'{file} does not exist.')


# %%
"""
    function called and succeeded:
        pretty printed ( and reg print) json data
        printed error if file couldn't be found
        requested user input for file if not explicitly stated
            with param during func call

"""

json_open('../Data/sample-return/data/DelveData.jsonc')

# %%
pp(d)

# %%
fOpen = open('conv.py')
count = 0

for line in fOpen:
    count = count + 1
print('Line Count:', count)

# %%
fOpen = open('cleanfiles.py')
print(len(fOpen.read()))
# inp = fOpen.read()
# print(len(inp))

# %%


def file_length(file=''):
    # Can default to only asking for file or allow param at script init
    # file = str(input('Enter full path to json filename: '))
    # fOpen = open(file)
    from os import path

    if file == '':
        file = str(input('Enter full path to filename: '))
    else:
        file = file
    if path.isfile(file):
        # f_open = open(file)
        # inp = f_open.read()
        file_length = len(open(file).read())
        print(f'The specified file is: {file_length} lines long')
        # print(f'The specified file is: {len(inp)} lines long')
    else:
        print('File doesn\'t exist')
# print(len(fOpen.read()))


# %%
file_length()

# %%


def file_open():
    fOpen = open('conv.py')

    count = 0

    for _ in fOpen:
        count += 1
    f_len = char_len()
    # f_length = len(fOpen.read())
    print(f'Line Count: {count} \
           \n  Character Count: {f_len}')


def char_len():
    f_length = len(open('conv.py').read())
    return f_length


# %%
file_open()

# %%

f1 = '../requirements.txt'
f2 = '../requirements3.txt'

r = filecmp.cmp(f1, f2, shallow=False)
print(r)

# %%
open_f1 = open(f1, 'r')
open_f2 = open(f2, 'r')

i = 0

for line1 in open_f1:
    i += 1
    total = i.__add__(i) / 2
    print('File 1 Line #: ', i, ' Total file 1 lines: ', total)

x = 0

for line2 in open_f2:
    x += 1
    total = x
    print('File 2 Line #: ', x, 'Total file 2 lines: ', total)

open_f1.close()
open_f2.close()

# %%
open_f1 = open(f1, 'r')
open_f2 = open(f2, 'r')

i = 0

for line1 in open_f1:
    i += 1

    for line2 in open_f2:

        if line1 == line2:
            print('Line ', i, ': Identical')
        else:
            print('Line ', i, ':')

            print('\tFile 1:', line1, end='')
            print('\tFile 2:', line2, end='')
        break

open_f1.close()
open_f2.close()

# %%
# general math
mth = [2 + 2,
       50 - 5*6,
       (50 - 5*6) / 4]

x, y = list(mth), list()
print(x, y)

sum(x)
print(x)

mth2 = 8 / 5  # classic div. returns float (floating point number)
mth3 = 17 // 3
# floor div discards frac part; div that rounds down to nearest int.
mt3 = 16 * 2
mt4 = 17 % 3  # the % operator will return remainder after reg. div.
mt5 = 5 * 3 + 2  # floored quotient * divisor + remainder

print(f'{mth}, {mth2}, {list([6,6,6,6])}')
print(mth, mth2, mth3, mt4)
