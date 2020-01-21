num = range(1,1000)
result = []
ret = 0

for x in num:
    if x % 3 == 0:
        result.append(x)
    elif x % 5 == 0:
        result.append(x)

for y in result:
    ret = ret + y

print(ret)
