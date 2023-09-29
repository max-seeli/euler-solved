# Problem: 4
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import itertools

def is_palindrome(n):

    num_str = str(n)
    return num_str == num_str[::-1]

max_palindrome = 0
for pair in itertools.product(range(100, 1000), repeat=2):
    
    product = pair[0] * pair[1]
    if is_palindrome(product) and product > max_palindrome:
        max_palindrome = product

print(max_palindrome)