# project euler problem 38
# author: Jeklah

def pandigital(n):
    return False if len(n) != 9 else all(str(i) in n for i in range(1, 10))


def pandigital_multiples():
    max_pandigital = 0
    for i in range(1, 9999):
        n = 1
        pandigital_string = ""
        while len(pandigital_string) < 9:
            pandigital_string += str(i * n)
            n += 1
        if pandigital(pandigital_string) and int(pandigital_string) > max_pandigital:
            max_pandigital = int(pandigital_string)
    return max_pandigital


if __name__ == "__main__":
    print(pandigital_multiples())
