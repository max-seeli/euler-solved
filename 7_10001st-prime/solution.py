# Problem: 7
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import math

def prime_generator():
    """Yields the next prime number."""
    primes = []
    n = 2
    while True:
        if all(n % p != 0 for p in primes):
            primes.append(n)
            yield n
        n += 1

def nth_prime(n):
    """Returns the nth prime number."""
    primes = prime_generator()
    for i in range(n):
        prime = next(primes)
    return prime

print(nth_prime(10001))