def remainder(t, n):
    return bool(not (t % n) and remainder(t, n-1)) if n > 0 else True

i = 20
while not remainder(i, 20):
    i += 20

print(i)
