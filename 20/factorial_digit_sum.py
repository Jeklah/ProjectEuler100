# project euler problem 20
# Author: Jeklah

import math


def factorial_digit_sum(n):
    return sum([int(x) for x in str(math.factorial(n))])


if __name__ == '__main__':
    print(factorial_digit_sum(100))
