# project euler problem 43
# author: Jeklah

import itertools


def main():
    primes = [2, 3, 5, 7, 11, 13, 17]
    total = 0
    for p in itertools.permutations('0123456789'):
        if p[0] == '0':
            continue
        if all(int(''.join(p[i:i+3])) % primes[i-1] == 0 for i in range(1, 8)):
            total += int(''.join(p))
    print(total)


if __name__ == '__main__':
    main()
