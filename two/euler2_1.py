ret = 0
n1 = 1
n2 = 2

while n1 < 4000000:
    if n1 % 2 == 0:
        ret += n1
    nth = n1 + n2
    n1 = n2
    n2 = nth

print(ret)
