# Problem: 10
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while p**2 <= n:
        # If prime[p] is not changed, it is a prime
        if prime[p] == True:
            # Mark all multiples of p
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    
    primes = [p for p in range(2, n+1) if prime[p]]
    return primes

n = 2_000_000 
primes = sieve_of_eratosthenes(n)
print(sum(primes))
