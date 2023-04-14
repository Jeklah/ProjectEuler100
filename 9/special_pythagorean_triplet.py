# project euler: problem 9 (https://projecteuler.net/problem=9)
# Author: Jeklah

def special_pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a, 1000):
            c = 1000 - a - b
            if a**2 + b**2 == c**2:
                return a * b * c


if __name__ == '__main__':
    print(special_pythagorean_triplet())
