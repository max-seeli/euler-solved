# Problem: 2
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

fib = [1, 2]
while fib[-1] < 4_000_000:
    fib.append(fib[-1] + fib[-2])

print(sum(i for i in fib if i % 2 == 0))