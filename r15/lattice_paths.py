# project euler problem 15: Lattice paths

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?


def lattice_paths(x, y):
    if x == 0 or y == 0:
        return 1
    else:
        return lattice_paths(x-1, y) + lattice_paths(x, y-1)


if __name__ == '__main__':
    print(lattice_paths(20, 20))
