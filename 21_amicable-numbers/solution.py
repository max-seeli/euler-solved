# Problem: 21
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

def d(n):
    return sum(i for i in range(1, n) if n % i == 0)

print(sum(i for i in range(1, 10000) if d(d(i)) == i and d(i) != i))