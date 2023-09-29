# Problem: 1
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

mult_3 = [i for i in range(1000) if i % 3 == 0]
mult_5 = [i for i in range(1000) if i % 5 == 0]

print(sum(set(mult_3 + mult_5)))