# project euler problem 22
# author: Jeklah

import csv


def get_names():
    """
    Read names from a file
    """
    names = []
    with open('names.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            names.extend(iter(row))
    return names


def sort_names(names):
    """
    Sort the names
    """
    names.sort()
    return names


def get_score(name):
    """
    Get the score of the names.
    """
    return sum(ord(char) - 64 for char in name)


def get_total_score(names):
    """
    Get total score
    """
    return sum(get_score(name) * (i + 1) for i, name in enumerate(names))


def main():
    """
    Run program
    """
    names = get_names()
    names = sort_names(names)
    print(get_total_score(names))


if __name__ == '__main__':
    main()
