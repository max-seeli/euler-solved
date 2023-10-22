# Problem: 14
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import time

def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return 3*n+1
    
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        n = collatz(n)
        sequence.append(n)
    return sequence

def longest_collatz_sequence(n):
    longest_starting_number = 1
    longest = 0
    for i in range(1, n):
        len_collatz = len(collatz_sequence(i))
        if len_collatz > longest:
            longest_starting_number = i
            longest = len_collatz
    return longest_starting_number, longest

print(longest_collatz_sequence(1000000))
