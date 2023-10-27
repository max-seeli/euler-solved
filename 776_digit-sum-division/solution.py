# Problem: 776
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

from tqdm import tqdm
import math
import scipy.special

def d(n):
    return sum([int(i) for i in str(n)])

def F(N):
    return sum([n / d(n) for n in tqdm(range(1, N+1))])


average_digit = 4.5
def approx_d(n):
    return max(average_digit * math.log10(n), 1)

def approx_F(N):
    return sum([n / approx_d(n) for n in tqdm(range(1, N+1))])


def approx_F2(N):
    return N**2 / (average_digit * math.log10(N)) 
# Print result in scientific notation rounded to twelve significant digits after the decimal point. Use a lowercase e to separate the mantissa and the exponent.
print("{:.12e}".format(approx_F2(1234567890123456789)))