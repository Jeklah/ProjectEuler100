# project euler problem 39
# author: Jeklah

import itertools
import math


def main():
    max_solutions = 0
    max_p = 0
    for p in range(1, 1001):
        solutions = 0
        for a, b in itertools.product(range(1, p), range(1, p)):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == p:
                solutions += 1
        if solutions > max_solutions:
            max_solutions = solutions
            max_p = p
    print(max_p)


if __name__ == '__main__':
    main()
