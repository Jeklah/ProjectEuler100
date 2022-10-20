# project euler problem 29
# Author: Jeklah

import itertools
import time


def main():
    start = time.time()
    powers = {a**b for a, b in itertools.product(range(2, 101), range(2, 101))}
    print(len(powers))
    print(time.time() - start)


if __name__ == '__main__':
    main()
