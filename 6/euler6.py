sumOfSquare = 0
squareOfSum = 0
for x in range(1, 100):
    sumOfSquare += (x ** x)
    squareOfSum += x
    if x == 100:
        squareOfSum = squareOfSum ** squareOfSum
print(sumOfSquare)

print(sumOfSquare - squareOfSum)
