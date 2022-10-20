# project euler problem 21
# author: Jeklah

import math


def summ_of_divisors(n):
    summ = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            summ += i
            if i != n/i:
                summ += n/i
    return summ


def amicable_numbers(n):
    return sum(i for i in range(1, n)
               if i == summ_of_divisors(summ_of_divisors(i))
               and i != summ_of_divisors(i))


print(amicable_numbers(10000))
