# project euler problem 42
# author: Jeklah

import string


def get_word_value(word):
    return sum(string.ascii_uppercase.index(letter) + 1 for letter in word)


def get_triangle_numbers(n):
    return [int(0.5 * n * (n + 1)) for n in range(1, n + 1)]


def main():
    with open('p042_words.txt') as f:
        words = f.read().replace('"', '').split(',')
    triangle_numbers = get_triangle_numbers(100)
    print(sum([1 for word in words if get_word_value(word) in triangle_numbers]))


if __name__ == '__main__':
    main()
