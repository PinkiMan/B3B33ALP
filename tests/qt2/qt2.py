# line1='2.6 -4.9 -4.75 1.65 -4.0 -1.35 3.7 -2.7 1.75 3.1 0.4 -1.15'
# line2='3.2 1.85 -2.55 -3.15 -0.4 -2.3 1.85 -3.0 1.15 3.25 -2.0 1.65'

line1 = input()
line2 = input()

X = line1.split(' ')
Y = line2.split(' ')

if len(X) != len(Y):
    print('ERROR')
    exit()

F = []

Biggest_Index = 0
Negative = 0
Minimum_Index = 0

for i in range(len(X)):
    x = float(X[i])
    y = float(Y[i])
    F.append(0.5 * (x ** 2) * (1 - y) ** 2 + (x - 2) ** 3 - 2 * y + x)
    if F[Biggest_Index] < F[-1]:
        Biggest_Index = i
    if F[-1] < 0:
        Negative += 1

    if F[Minimum_Index] * (float(X[Minimum_Index]) + 2) * (float(Y[Minimum_Index]) - 2) > F[-1] * (x + 2) * (y - 2):
        Minimum_Index = i

print(Biggest_Index, Negative, Minimum_Index)