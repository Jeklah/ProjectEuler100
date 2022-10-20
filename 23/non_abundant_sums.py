# project euler problem 23
# non-abundant summs
# Author: Jeklah

import math


def summ_of_divisors(n):
    summ = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            summ += i
            if n / i != i:
                summ += n / i
    return summ


def is_abundant(n):
    return summ_of_divisors(n) > n


def main():
    abundant_summ = set()
    for i in range(len([i for i in range(1, 28124) if is_abundant(i)])):
        for j in range(i, len([i for i in range(1, 28124) if is_abundant(i)])):
            abundant_summ.add(([i for i in range(1, 28124)
                                if is_abundant(i)])[i] +
                              ([i for i in range(1, 28124)
                                if is_abundant(i)])[j])

    summ = sum(i for i in range(1, 28124) if i not in abundant_summ)
    print(summ)


if __name__ == '__main__':
    main()
