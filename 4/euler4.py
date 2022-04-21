ret = 0
for x in range(100, 999):
    for y in range(100, 999):
        palin = x * y
        if str(palin) == str(palin)[::-1] and palin > ret:
            ret = palin
print(ret)
