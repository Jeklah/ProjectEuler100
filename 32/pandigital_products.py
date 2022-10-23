# project euler problem 32
# author: Jeklah

import itertools


def is_pandigital(n):
    return False if len(n) != 9 else all(str(i) in n for i in range(1, 10))


def main():
    products = [i * j for i, j in itertools.product(range(1, 100), range(
        100, 10000)) if is_pandigital(str(i) + str(j) + str(i * j))]

    print(sum(set(products)))


if __name__ == '__main__':
    main()
