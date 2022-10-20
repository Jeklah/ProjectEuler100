# project euler problem 27
# Author: Jeklah

import itertools
import math


def is_prime(n):
    if n <= 1:
        return False
    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


def quadratic_primes(a, b):
    n = 0
    while True:
        if is_prime(n ** 2 + a * n + b):
            n += 1
        else:
            return n


def main():
    max_primes = 0
    max_a = 0
    max_b = 0
    for a_num, b_num in itertools.product(range(-999, 1000), range(-999, 1000)):
        primes = quadratic_primes(a_num, b_num)
        if primes > max_primes:
            max_primes = primes
            max_a = a_num
            max_b = b_num
    print(max_a * max_b)


if __name__ == '__main__':
    main()
