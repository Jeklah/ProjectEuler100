# project euler problem 30
# Author: Jeklah

import time


def main():
    start = time.time()
    total = sum(i for i in range(2, 354294) if i ==
                sum(int(j)**5 for j in str(i)))
    print(total)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
