# Problem: 23
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import math
from tqdm import tqdm

def is_abundant(n):
    divisors = [1]
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n / i:
                divisors.append(n / i)
    return sum(divisors) > n

def is_sum_of_two_abundant(n, abundants):
    for i in abundants:
        if i > n:
            return False
        if (n - i) in abundants:
            return True
    return False

abundants = []
for i in range(1, 28124):
    if is_abundant(i):
        abundants.append(i)

sum_of_non_abundants = 0
for i in tqdm(range(1, 28124)):
    if not is_sum_of_two_abundant(i, abundants):
        sum_of_non_abundants += i

print(sum_of_non_abundants)
