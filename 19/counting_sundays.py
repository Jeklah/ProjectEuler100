# Project euler problem 19
# Counting Sundays
# Author: Jeklah

import datetime
import itertools


def main():
    sundays = sum(datetime.date(year, month, 1).weekday() == 6 for year,
                  month in itertools.product(range(1901, 2001), range(1, 13)))

    print(sundays)


if __name__ == "__main__":
    main()
