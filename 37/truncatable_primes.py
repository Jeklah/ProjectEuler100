# project euler problem 37
# author: Jeklah

import math


def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    return all(n % i != 0 for i in range(3, int(math.sqrt(n)) + 1, 2))


def is_truncatable_prime(n):
    if not is_prime(n):
        return False
    s = str(n)
    for i in range(1, len(s)):
        if not is_prime(int(s[i:])):
            return False
        if not is_prime(int(s[:-i])):
            return False
    return True


def main():
    truncatable_primes = []
    n = 10
    while len(truncatable_primes) < 11:
        if is_truncatable_prime(n):
            truncatable_primes.append(n)
        n += 1
    print(sum(truncatable_primes))


if __name__ == '__main__':
    main()
