# project euler: problem 9 (https://projecteuler.net/problem=9)

import itertools
import math


def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2


def main():
    for a, b in itertools.product(range(1, 1000), range(1, 1000)):
        c = math.sqrt(a**2 + b**2)
        if is_pythagorean_triplet(a, b, c) and a + b + c == 1000:
            print(a * b * c)
            return


if __name__ == "__main__":
    main()
