# Problem: 20
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import math

def factorial_digit_sum(n):
    return sum([int(i) for i in str(math.factorial(n))])

print(factorial_digit_sum(100))