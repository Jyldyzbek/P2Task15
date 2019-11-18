a = int(input('Vedite vash vozrast: '))

b = []
c = []
for s in range(0, a+1):
    if s % 2 == 0:
        b.append(s)
    elif s % 2 != 0:
        c.append(s)
    else:
        None
print(b)
print(c)
