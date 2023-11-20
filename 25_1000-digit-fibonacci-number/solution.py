# Problem: 25
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

fibonacci = [1, 1]

while len(str(fibonacci[-1])) < 1000:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(len(fibonacci))