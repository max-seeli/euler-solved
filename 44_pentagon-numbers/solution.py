# Problem: 44
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import math

def is_pentagonal(n):
    return (1 + math.sqrt(1 + 24*n)) % 6 == 0

def pentagonal(n):
    return n*(3*n - 1) // 2

def is_sum_pentagonal(j, k):
    return is_pentagonal(pentagonal(j) + pentagonal(k))

def is_diff_pentagonal(j, k):
    return is_pentagonal(pentagonal(k) - pentagonal(j))

i = 1
while True:
    for j in range(1, i):
        if is_diff_pentagonal(j, i) and is_sum_pentagonal(j, i):
            print(pentagonal(i) - pentagonal(j))
            exit()
    i += 1
