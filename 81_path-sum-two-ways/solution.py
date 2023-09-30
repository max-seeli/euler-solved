# Problem: 81
# Author: Maximilian Seeliger (maximilian.seeliger@gmail.com)

import os
import numpy as np

def read_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    matrix = np.zeros((len(lines), len(lines)))
    for i, line in enumerate(lines):
        matrix[i, :] = np.array([int(n) for n in line.split(',')])
    return matrix

def min_path_sum(matrix):
    n = len(matrix)
    path_sum = np.zeros((n, n))
    path_sum[0, 0] = matrix[0, 0]
    for i in range(1, n):
        path_sum[i, 0] = path_sum[i-1, 0] + matrix[i, 0]
        path_sum[0, i] = path_sum[0, i-1] + matrix[0, i]
    for i in range(1, n):
        for j in range(1, n):
            path_sum[i, j] = min(path_sum[i-1, j], path_sum[i, j-1]) + matrix[i, j]
    return int(path_sum[-1, -1])

file_rel_loc = os.path.dirname(os.path.abspath(__file__))
matrix = read_matrix(os.path.join(file_rel_loc, 'matrix.txt'))

print(min_path_sum(matrix))
