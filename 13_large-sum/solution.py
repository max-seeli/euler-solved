# Problem: 13
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import os
import numpy as np

file_rel_loc = os.path.dirname(os.path.abspath(__file__))
numbers_file = os.path.join(file_rel_loc, 'numbers.txt')

X = np.loadtxt(numbers_file).astype(object) # object dtype to avoid overflow

sum = X.sum()
print('{:f}'.format(sum)[:10]) # 11 digits to avoid rounding errors}')