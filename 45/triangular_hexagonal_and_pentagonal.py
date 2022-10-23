# project euler 45: Triangular, pentagonal, and hexagonal
# author: Jeklah

import math


def is_pentagonal(n):
    """Checks if a number is pentagonal"""
    return (1 + math.sqrt(1 + 24 * n)) % 6 == 0


def is_hexagonal(n):
    """Checks if a number is hexagonal"""
    return (1 + math.sqrt(1 + 8 * n)) % 4 == 0


def main():
    """Main function"""
    n = 286
    while True:
        t = n * (n + 1) // 2
        if is_pentagonal(t) and is_hexagonal(t):
            print(t)
            break
        n += 1


if __name__ == "__main__":
    main()
