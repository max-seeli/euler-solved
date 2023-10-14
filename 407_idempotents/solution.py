# Problem: 407
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)


from sympy import factorint
import numpy as np

def M(n):
    # Use the Chinese remainder theorem to solve the system of congruences 
    # {a = 0,1 mod p^k} for all coprime divisors of n.
    factors = [p**k for p, k in factorint(n).items()]
    modului = np.cumprod(factors).tolist()
    
    solutions = [0]
    for factor, modulus in zip(factors, modului):

        recip = pow(factor, -1, modulus//factor)
        solutions = \
            [solution * factor * recip for solution in solutions] \
            + [(solution - 1) * recip * factor + 1 for solution in solutions]
        solutions = [solution % modulus for solution in solutions]
    return max(solutions)

from tqdm import tqdm
from multiprocessing import Pool

n_range = range(1, 10**7 + 1)
num_processes = 8

for i in range (1, 10):
    M(i)

with Pool(num_processes) as pool:
    print(sum(pool.map(M, tqdm(n_range))))

