# project euler problem 16 - power digit sum

def power_digit_sum(n):
    return sum(int(i) for i in str(2**n))


if __name__ == '__main__':
    print(power_digit_sum(1000))
