# project euler problem 25
# author: Jeklah

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def main():
    for i, f in enumerate(fib()):
        if len(str(f)) == 1000:
            print(i + 1)
            break


if __name__ == '__main__':
    main()
