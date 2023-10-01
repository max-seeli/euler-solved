# Problem: 145
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

from tqdm import tqdm

def reverse(n):
    num_str = str(n)
    return int(num_str[::-1])

def has_only_odd_digits(n):
    num_str = str(n)
    for digit in num_str:
        if int(digit) % 2 == 0:
            return False
    return True

limit = 1_000_000_000
counter = 0

for n in tqdm(range(1, limit)):
    reverse_n = reverse(n)
    if reverse_n < n or n % 10 == 0:
        # reverse(n) < n: we already counted this number
        # n % 10 == 0: reverse(n) would have a leading zero
        continue
    if has_only_odd_digits(n + reverse_n):
        counter += 2 # n and reverse(n) are reversible

print(counter)
