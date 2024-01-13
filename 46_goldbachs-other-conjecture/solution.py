# Problem: 46
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(math.sqrt(n)) + 1, 2):
        if n % x == 0:
            return False
    return True

def is_goldbach(n):
    for i in range(1, int(math.sqrt(n/2)) + 1):
        if is_prime(n - 2*i*i):
            return True
    return False


i = 9
while True:
    if not is_prime(i) and not is_goldbach(i):
        print(i)
        break
    i += 2