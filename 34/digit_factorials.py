# project euler problem 34
# author: Jeklah

import math


def digit_factorials():
    total = 0
    for i in range(3, 1000000):
        if i == sum([math.factorial(int(j)) for j in str(i)]):
            total += i
    return total


if __name__ == '__main__':
    print(digit_factorials())
