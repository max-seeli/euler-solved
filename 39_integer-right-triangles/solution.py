# Problem: 39
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import numpy as np
import time
from tqdm import tqdm

max_solutions = 0
max_p = 0
for p in tqdm(range(1, 1001)):
    solutions = 0
    for a in range(1, p):
        for b in range(a, p):
            c = p - a - b
            if a**2 + b**2 == c**2:
                solutions += 1
    if solutions > max_solutions:
        max_solutions = solutions
        max_p = p
print(f"Max solutions: {max_solutions} for p={max_p}")
