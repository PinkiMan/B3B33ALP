a = int(input())
b = int(input())

suma = 0
if a <= b:
    for i in range(a, b + 1):
        suma += i ** 3


else:
    for i in range(b, a + 1):
        suma += i ** 3

print(suma)
