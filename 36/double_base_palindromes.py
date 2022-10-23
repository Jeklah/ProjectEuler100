# project euler problem 36
# author: Jeklah

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


def main():
    total = sum(i for i in range(1, 1000000) if is_palindrome(i)
                and is_palindrome(bin(i)[2:]))

    print(total)


if __name__ == '__main__':
    main()
