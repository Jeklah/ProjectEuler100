# project euler problem 801

from math import gcd
from functools import reduce
from operator import mul

def main():
    N = 1000000000000000000
    #N = 1000
    print("Problem 801: Modular Fibonacci")
    print("N={}".format(N))
    print("The value of F(N) mod 1000000007 is {}".format(modFib(N)))

def modFib(N):
    """Fibonacci sequence modulo 1000000007"""
    return modFibRec(N, 0, 1, 1, 1)

def modFibRec(N, a, b, c, d):
    """Fibonacci sequence modulo 1000000007"""
    if N == 0:
        return a
    else:
        if N % 2 == 0:
            return modFibRec(N // 2, a, b, (c**2 + d**2) % 1000000007, (2*c*d + d**2) % 1000000007)
        else:
            return modFibRec(N // 2, b, (a + b) % 1000000007, c, d)

def modFib2(N):
    """Fibonacci sequence modulo 1000000007"""
    return modFibRec2(N, 0, 1)

def modFibRec2(N, a, b):
    """Fibonacci sequence modulo 1000000007"""
    if N == 0:
        return a
    else:
        return modFibRec2(N - 1, b, (a + b) % 1000000007)

def modFib3(N):
    """Fibonacci sequence modulo 1000000007"""
    return modFibRec3(N, 0, 1)

def modFibRec3(N, a, b):
    """Fibonacci sequence modulo 1000000007"""
    if N == 0:
        return a
    else:
        return modFibRec3(N - 1, b, (a + b) % 1000000007)

def modFib4(N):
    """Fibonacci sequence modulo 1000000007"""
    return modFibRec4(N, 0, 1)

def modFibRec4(N, a, b):
    """
