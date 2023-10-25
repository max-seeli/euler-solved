# Problem: 15
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

"""
Explanation:
    This is a combinatorics problem. The number of paths from the top left to
    the bottom right corner of a grid of size n x n. Can also be seen as the task
    of rearranging n moves down and n moves to the right in an arbitrary order.
    Equivalently, we can think of the problem of arranging n 0s and n 1s in a string
    of length 2n. The number of ways to do this is given by the binomial coefficient
    (2n n). This can be computed by the factorial formula (2n)! / (n! * n!).
"""

import math

def lattice_paths(n):
    return math.factorial(2*n) // (math.factorial(n) * math.factorial(n))

print(lattice_paths(20))