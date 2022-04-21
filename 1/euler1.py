ret = 0

num = range(1,1000)
result = [x for x in num if x % 3 == 0 or x % 5 == 0]
for y in result:
    ret = ret + y

print(ret)
