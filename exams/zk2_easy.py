line = input()

# line='137 171 84393 2775592 1828515 1640975 225 114'

Nums_s = line.split(' ')
Nums_N = []
for num in Nums_s:
    Nums_N.append(int(num))

Max_Num = max(Nums_N)
if len(Nums_N) % 2 == 0:
    Half = len(Nums_N) / 2
else:
    Half = (len(Nums_N) + 1) / 2


def Euclid(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a = a % b
        a, b = b, a
    return a


Results = []

for Index, Nums1 in enumerate(Nums_N):
    List = Nums_N[:]
    for Num2 in Nums_N:
        a = Euclid(Nums1, Num2)
        if a not in Results:
            Results.append(a)

Data = []
for Res in Results:
    # print(' ')
    count = 0
    for Num in Nums_N:
        x = Euclid(Res, Num)
        if x == Res:
            count += 1
    Data.append([Res, count])
    # print(Res,count)

Valid = []
for data in Data:
    if data[1] >= Half:
        Valid.append(data[0])

print(max(Valid))

# print('x')