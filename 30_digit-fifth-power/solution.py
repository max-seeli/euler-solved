# Problem: 30
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import numpy as np
import time
from tqdm import tqdm

def is_digit_fifth_power(n):
    return n == sum([int(d)**5 for d in str(n)])

total = 0
# 9**5 = 59049
# 6*9**5 = 354294
# 7*9**5 = 413343 < 999999 (max number of 6 digits)
for i in tqdm(range(2, 1000000)):
    if is_digit_fifth_power(i):
        total += i
print(f"Sum: {total}")
