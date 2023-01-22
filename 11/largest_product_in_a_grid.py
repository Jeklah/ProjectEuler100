# project euler: problem 11 (https://projecteuler.net/problem=11)
# Author: Jeklah
# reading the grid from a file and finding the largest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid

import sys


def read_grid(filename):
    """
    Reading in the grid.txt file.
    """
    grid = []
    with open(filename) as f:
        grid.extend([int(x) for x in line.split()] for line in f)
    return grid


def largest_product(grid):

    def product(l):
        p = 1
        for x in l:
            p *= x
        return p

    def largest_product_in_line(l):
        largest = 0
        for i in range(len(l) - 3):
            p = product(l[i:i+4])
            if p > largest:
                largest = p
        return largest

    largest = 0
    for line in grid:
        p = largest_product_in_line(line)
        if p > largest:
            largest = p

    for i in range(len(grid)):
        line = [grid[j][i] for j in range(len(grid))]
        p = largest_product_in_line(line)
        if p > largest:
            largest = p

    for i in range(len(grid) - 3):
        for j in range(len(grid) - 3):
            line = [grid[i+k][j+k] for k in range(4)]
            p = largest_product_in_line(line)
            if p > largest:
                largest = p

    for i in range(len(grid) - 3):
        for j in range(3, len(grid)):
            line = [grid[i+k][j-k] for k in range(4)]
            p = largest_product_in_line(line)
            if p > largest:
                largest = p

    return largest


if __name__ == '__main__':
    grid = read_grid(sys.argv[1])
    print(largest_product(grid))
