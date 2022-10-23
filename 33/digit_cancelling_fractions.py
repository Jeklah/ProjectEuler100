# project euler problem 33
# author: Jeklah

def main():
    '''Main function'''
    numerator = 1
    denominator = 1
    for i in range(10, 100):
        for j in range(i + 1, 100):
            if i % 10 == 0 or j % 10 == 0:
                continue
            if (i % 10 == j // 10 and i / j == i // 10 / (j % 10)) or \
               (i // 10 == j % 10 and i / j == i % 10 / (j // 10)):
                numerator *= i
                denominator *= j
    print(denominator // numerator)


if __name__ == '__main__':
    main()
