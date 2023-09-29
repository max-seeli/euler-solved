# Problem: 3
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

from math import sqrt, floor
from sympy import isprime

def largest_prime_factor(n):
    for i in range(floor(sqrt(n)), 1, -1):
        if n % i == 0 and isprime(i):
            return i
    return n

print(largest_prime_factor(600851475143))