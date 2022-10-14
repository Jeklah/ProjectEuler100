# project euler: problem 12 (https://projecteuler.net/problem=12)
# author:

import math


def get_divisors(n):
    divisors = []
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            divisors.extend((i, n // i))
    return divisors


def get_triangular_number(n):
    return n * (n + 1) // 2


def main():
    n = 1
    while len(get_divisors(get_triangular_number(n))) <= 500:
        n += 1
    print(get_triangular_number(n))


if __name__ == '__main__':
    main()
