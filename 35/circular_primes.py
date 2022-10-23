# project euler problem 35
# author: Jeklah

import math


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    return all(n % divisor != 0 for divisor in range(3, sqr, 2))


def is_circular_prime(n):
    if not is_prime(n):
        return False

    n = str(n)
    for _ in range(len(n)):
        n = n[1:] + n[0]
        if not is_prime(int(n)):
            return False
    return True


def main():
    circular_primes = [i for i in range(2, 1000000) if is_circular_prime(i)]
    print(len(circular_primes))


if __name__ == '__main__':
    main()
