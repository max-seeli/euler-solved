# Problem: 840
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

from sympy import isprime

MD = {}

def D(p):
    if p == 1 or isprime(p):
        return 1
    else:
        for i in range(2, p):
            if p % i == 0:
                q = p // i
                p = i
                if p not in MD:
                    MD[p] = D(p)
                if q not in MD:
                    MD[q] = D(q)
                return MD[p] * q + MD[q] * p

def partition(n):
    p = [0] * n     # An array to store a partition
    k = 0         # Index of last element in a partition
    p[k] = n     # Initialize first partition
                 # as number itself
 
    # This loop first prints current partition,
    # then generates next partition.The loop
    # stops when the current partition has all 1s
    while True:
         
            # print current partition
            yield p[:k + 1]
 
            # Generate next partition
 
            # Find the rightmost non-one value in p[].
            # Also, update the rem_val so that we know
            # how much value can be accommodated
            rem_val = 0
            while k >= 0 and p[k] == 1:
                rem_val += p[k]
                k -= 1
 
            # if k < 0, all the values are 1 so
            # there are no more partitions
            if k < 0:
                return
 
            # Decrease the p[k] found above
            # and adjust the rem_val
            p[k] -= 1
            rem_val += 1
 
            # If rem_val is more, then the sorted
            # order is violated. Divide rem_val in
            # different values of size p[k] and copy
            # these values at different positions after p[k]
            while rem_val > p[k]:
                p[k + 1] = p[k]
                rem_val = rem_val - p[k]
                k += 1
 
            # Copy rem_val to next position
            # and increment position
            p[k + 1] = rem_val
            k += 1

def P(partition):
    total = 1
    for p in partition:
        total *= D(p)
    return total

def G(n):
    total = 0
    for p in partition(n):
        total += P(p)
    return total

from tqdm import tqdm

def S(N):
    total = 0
    for n in tqdm(range(1, N + 1)):
        total += G(n)
    return total

print(G(5))


from sympy import factorint
import itertools
from functools import reduce
import operator

number = 28

def dalt(number):

    if number == 1 or isprime(number):
        return 1
    
    factors = factorint(number)
    non_unique_factors = []
    for factor, pow in factors.items():
        non_unique_factors += [factor] * pow

    Dalt = 0
    for combination in itertools.combinations(non_unique_factors, len(non_unique_factors) - 1):
        Dalt += reduce(operator.mul, combination)
    return Dalt

import time

for i in range(1,2000):
    # time the two functions
    start = time.time()
    D(i)
    end = time.time()
    t1 = end - start
    start = time.time()
    dalt(i)
    end = time.time()
    t2 = end - start
    print("D1" if t1 < t2 else "D2", i, t1, t2, t1/t2)