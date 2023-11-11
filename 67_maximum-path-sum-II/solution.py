# Problem: 67
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import os

file_rel_loc = os.path.dirname(os.path.abspath(__file__))
triangle_file = os.path.join(file_rel_loc, 'triangle.txt')

triangle = []

with open(triangle_file, "r") as f:
    for line in f:
        triangle.append([int(x) for x in line.split()])

for i in range(len(triangle) - 2, -1, -1):
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

print(triangle[0][0])
