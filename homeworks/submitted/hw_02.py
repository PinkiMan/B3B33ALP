"""soustava=15
x1='c9.83'
x2='4c.e027'"""

"""soustava = 3
x1 = '1.2222'
x2 = '0.0121'
"""

"""soustava=10
x1='12.0'
x2='5.0'"""

"""soustava=4
x1='10.1313'
x2='11.2302214'"""

"""soustava=33
x1='pm.ttnp1'
x2='l.e12w'"""

"""soustava=10
x1='132.0'
x2='12.0'"""

soustava = int(input())
x1 = str(input())
x2 = str(input())

if x1.count('.') > 1:
    print('ERROR')
    exit()

if x2.count('.') > 1:
    print('ERROR')
    exit()

if soustava > 36 or soustava < 2:
    print('ERROR')
    exit()

for ch in x1:
    if ch not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if not ord(ch.lower()) - 87 < soustava:
            print('ERROR')
            exit()
    else:
        if not int(ch) < soustava:
            print('ERROR')
            exit()

for ch in x2:
    if ch not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if not ord(ch.lower()) - 87 < soustava:
            print('ERROR')
            exit()
    else:
        if not int(ch) < soustava:
            print('ERROR')
            exit()

Delka = len(x1.split('.')[1]) + len(x2.split('.')[1])
x1_cele = x1.replace('.', '')
x2_cele = x2.replace('.', '')

x1_sum = []
for id, num in enumerate(x1_cele):
    if num not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        num = str(ord(num.lower()) - 87)
    x1_sum.append(num)

x2_sum = []
for id, num in enumerate(x2_cele):
    if num not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        num = str(ord(num.lower()) - 87)
    x2_sum.append(num)

sum_1 = []
for i in range(len(x2_sum)):
    for j in range(len(x1_sum)):
        sum_1.append(int(str(x1_sum[j])) * int(str(x2_sum[i])) * 10 ** (int(j)))

list1 = []
for i in range(len(x2_sum)):
    list2 = []
    for j in range(len(x1_sum)):
        list2.append(int(str(x1_sum[j])) * int(str(x2_sum[i])))
    list1.append(list2)

for index, part in enumerate(list1[::-1]):
    if index != 0:
        for i in range(index):
            part.append(0)

for i, x in enumerate(list1):
    list1[i] = x[::-1]

for index, part in enumerate(list1):
    if index != 0:
        for i in range(index):
            part.append(0)

for i, x in enumerate(list1):
    list1[i] = x[::-1]

sum_xd = []
for index in range(len(list1[0])):
    hl_ar = 0
    for j in range(len(list1)):
        hl_ar += list1[j][index]
    sum_xd.append(hl_ar)

sum_xd = sum_xd[::-1]
for index, x in enumerate(sum_xd):
    if not x < soustava - 1:
        sum_xd[index] = x % soustava
        if len(sum_xd) >= index + 2:
            sum_xd[index + 1] += x // soustava
        else:
            sum_xd.append(x // soustava)

sum_xd = sum_xd[::-1]
for item in range(len(sum_xd)):
    sum_xd[item] = str(sum_xd[item])

cele = ' '.join(sum_xd)

# print(cele)

List = []
for it in sum_xd:
    if int(it) > 9:
        xd = chr(int(it) + 87)
        List.append(xd)
    else:
        List.append(it)

List.insert(-Delka, '.')
Number = ''.join(List)
while Number[-1] == '0':
    Number = Number[:-1]

while Number[0] == '0':
    Number = Number[1:]
print(Number)

# sam(x1_dec_sum,x2_dec_sum)