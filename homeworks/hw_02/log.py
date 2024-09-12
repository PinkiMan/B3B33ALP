x = float(input())

if x > 1:
    x1 = 0
    x2 = x
elif x < 1:
    x1 = -(1 / x)
    x2 = 0


while abs(x1 - x2) >= 0.000000001:
    if 2 ** ((x1 + x2) / 2) < x:
        x1 = (x1 + x2) / 2
    else:
        x2 = (x1 + x2) / 2


print(str((x1 + x2) / 2))