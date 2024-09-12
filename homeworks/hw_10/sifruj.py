
def fast_exp(b, e, m):
    r = 1
    if 1 & e:
        r = b
    while e:
        e >>= 1
        b = (b * b) % m
        if e & 1: r = (r * b) % m
    return r



""" Vstupy z brute"""
n=854757130933
e=339289
Vstup='Slava! Mate to hotove.'
"""Konec vstupu"""


List=[Vstup[i:i+4] for i in range(0, len(Vstup), 4)]
Len=len(Vstup)%4
List[-1]+='\0\0'

Keys=[]
for package in List:
    x = ((ord(package[0]) * 256 + ord(package[1])) * 256 + ord(package[2])) * 256 + ord(package[3])
    a=fast_exp(x,e,n)
    Keys.append(a)
    print(a,end=' ')
print('xd')