# Problem: 4
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

def is_palindrome(n):

    num_str = str(n)
    return num_str == num_str[::-1]

max_palindrome = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product) and product > max_palindrome:
            max_palindrome = product

print(max_palindrome)