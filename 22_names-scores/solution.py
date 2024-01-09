# Problem: 22
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import string
import os

file_rel_loc = os.path.dirname(os.path.abspath(__file__))
names_file = os.path.join(file_rel_loc, 'names.txt')


def name_value(name):
    return sum(string.ascii_uppercase.index(c) + 1 for c in name)

total = 0
with open(names_file) as f:
    names = sorted(f.read().replace('"', '').split(','))
    for i, name in enumerate(names):
        total += (i + 1) * name_value(name)

print(total)
