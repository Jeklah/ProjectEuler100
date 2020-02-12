import math
import time

something = time.time()
def isPrime(num):
    if num == 2:
        return 1
    elif num % 2 == 0:
        return

    startNum = 3
    range = int(math.sqrt(num)) + 1
    while (startNum < range):
        if (num % startNum == 0):
            return 0
        startNum += 1
    return 1

N, T = 1, 3
while N < 10001:
    if isPrime(T):
        N +=1
    T += 2
print(T-2)
print(time.time() - something)
