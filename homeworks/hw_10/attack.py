import sys


def fast_exp(base, exp, mod):
    ret = 1
    if 1 & exp:
        ret = base
    while exp:
        exp >>= 1
        base = (base * base) % mod
        if exp & 1: ret = (ret * base) % mod
    return ret

def Euclid(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a = a % b
        a, b = b, a
    return a

def Euclid_bet(a, b):
    Aa, Ba = 1, 0
    Ab, Bb = 0, 1
    if b > a:
        a, b = b, a
        Aa, Ab = Ab, Aa
        Ba, Bb = Bb, Ba
    while b > 0:
        Aa = Aa - (a // b) * Ab
        Ba = Ba - (a // b) * Bb
        a = a % b
        a, b = b, a
        Aa, Ab = Ab, Aa
        Ba, Bb = Bb, Ba
    return (a, Aa, Ba)

def primeFactors(n):
    list=[]
    c = 2
    while (n > 1):
        if (n % c == 0):
            list.append(c)
            n = n / c
        else:
            c = c + 1
    return list

def Num_2_Word(Number):
    first = Number % 256
    second = int(((Number - first) / 256) % 256)
    third = int(((((Number - first) / 256) - second) / 256) % 256)
    four = int((((((Number - first) / 256) - second) / 256) - third) / 256)
    string = chr(four) + chr(third) + chr(second) + chr(first)
    #print(string, end='')
    return string


Test_Words=['Tento', 'predmet', 'proste', 'nejlepsi', 'genialni']


n=int(sys.argv[1])
Line=input()
"""n=865149046207
Line='352566354542 704277294015 506632666345 494928356066 824421528359 325069048254 839239812833 536096809854 278474205010'
"""


Line=Line.split(' ')

p,q=primeFactors(n)
fin=(p-1)*(q-1)

E_Valid=[]
Special=[]
for i in range(2**18,2**20+1):
    if Euclid(i,fin)==1:
        E_Valid.append(i)



End=False

for e in E_Valid:
    if End:
        break

    data=Euclid_bet(e,fin)
    d=data[1]%fin


    string=''
    for Num in Line:
        Num = int(Num)

        xm = fast_exp(Num, d, n)
        string += str(Num_2_Word(xm))



    for word in Test_Words:
        if word in string:
            string=string.replace('\0','')
            print(string,end='')
            End=True
            break
