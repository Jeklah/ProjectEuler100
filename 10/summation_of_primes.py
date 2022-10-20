# project euler: problem 10 (http://projecteuler.net/problem=10)
# Author: Jeklah

import math


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    return all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1))


def sum_primes(n):
    return sum(i for i in range(1, n) if is_prime(i))


if __name__ == "__main__":
    print(sum_primes(2000000))
