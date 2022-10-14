# project euler: problem 13 (https://projecteuler.net/problem=13)

import sys


def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        lines = [int(line) for line in lines]
        print(str(sum(lines))[:10])


if __name__ == '__main__':
    main()
