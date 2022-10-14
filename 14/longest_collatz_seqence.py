# project euler: problem 14 (http://projecteuler.net/problem=14)

def collatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        n = collatz(n)
        sequence.append(n)
    return sequence

def longest_collatz_sequence(n):
    longest = 0
    for i in range(1, n):
        length = len(collatz_sequence(i))
        if length > longest:
            longest = length
            number = i
    return number

if __name__ == '__main__':
    print(longest_collatz_sequence(1000000))
