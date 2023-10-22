# Problem: 12
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import math

def get_divisors(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
    return divisors

def get_triangular_number(n):
    return n * (n + 1) // 2

def get_first_triangular_number_with_more_than_n_divisors(n):
    i = 1
    while True:
        triangular_number = get_triangular_number(i)
        divisors = get_divisors(triangular_number)
        if len(divisors) > n:
            return triangular_number
        i += 1

print(get_first_triangular_number_with_more_than_n_divisors(500))