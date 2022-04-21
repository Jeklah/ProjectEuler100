primeNr = 0
primeCnt = 0
prime = 0
while primeCnt <= 10002:
    primeNr += 1
    if primeNr % 1 == 0 and primeNr % 2 != 0 and primeNr % 3 != 0:
        primeCnt += 1
        prime = primeNr
        print(prime)
        if primeCnt == 10001:
            print(prime)
