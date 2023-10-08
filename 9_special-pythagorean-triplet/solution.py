# Problem: 9
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

from functools import reduce
import operator

def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

def find_pythagorean_triplet_with_sum(sum):
    for a in range(1, sum):
        for b in range(a, sum):
            c = sum - a - b
            if is_pythagorean_triplet(a, b, c):
                return a, b, c
            
    return None

triple_with_sum_1000 = find_pythagorean_triplet_with_sum(1000)
print(reduce(operator.mul, triple_with_sum_1000, 1))