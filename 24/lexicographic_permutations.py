# project euler problem 24
# author: Jeklah

import itertools


def main():
    perm = itertools.permutations('0123456789')
    for _ in range(1000000):
        p = next(perm)
    print(''.join(p))


if __name__ == '__main__':
    main()
