# project euler problem 41
# author: Jeklah

import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(math.sqrt(n)) + 1, 2))


def is_pandigital(n):
    n = str(n)
    return False if len(n) > 9 else all(str(i) in n for i in range(1, len(n) + 1))


def main():
    max_pandigital_prime = 0
    for i in range(1, 100000000):
        if is_pandigital(i) and is_prime(i):
            max_pandigital_prime = i
    print(max_pandigital_prime)


if __name__ == '__main__':
    main()
