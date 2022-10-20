# project euler problem 28
# Author: Jeklah

import time


def main():
    start = time.time()
    total = 1 + sum(4 * i ** 2 - 6 * i + 6 for i in range(3, 1002, 2))
    print(total)
    print(time.time() - start)


if __name__ == '__main__':
    main()
