# project euler problem 44
# author: Jeklah

import math


def pentagon(n):
    return n * (3 * n - 1) / 2


def is_pentagon(n):
    return (math.sqrt(24 * n + 1) + 1) % 6 == 0


def main():
    i = 1
    while True:
        p_i = pentagon(i)
        for j in range(i - 1, 0, -1):
            p_j = pentagon(j)
            if is_pentagon(p_i + p_j) and is_pentagon(p_i - p_j):
                print(p_i - p_j)
                return
        i += 1


if __name__ == '__main__':
    main()
