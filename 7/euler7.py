primeNr = 0
primeCnt = 0
while primeCnt <= 10002:
    primeNr += 1
    if (primeNr % primeNr == 0) and (primeNr % 1 == 0) and (primeNr % 2 != 0):
        primeCnt += 1
        if primeCnt == 10001:
            print(primeNr)
