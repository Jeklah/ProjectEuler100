# project euler problem 26
# author: Jeklah

"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


def reciprocal_cycle_length(denominator):
    # returns the length of the recurring cycle of 1/denominator
    # returns 0 if there is no recurring cycle
    numerator = 1
    remainder = numerator % denominator
    remainder_list = []
    while remainder not in remainder_list:
        remainder_list.append(remainder)
        remainder = (remainder * 10) % denominator
    if remainder == 0:
        # no recurring cycle
        return 0
    else:
        return len(remainder_list) - remainder_list.index(remainder)


# main
cycle_lengths = [reciprocal_cycle_length(i) for i in range(2, 1000)]
print(cycle_lengths.index(max(cycle_lengths)) + 2)

# output
# 983

# runtime
# 0m0.056s
