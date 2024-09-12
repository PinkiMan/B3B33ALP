


def Cycle(local_x,local_y,Types,Colored,color):
    x = None
    y = None

    last_move = 0
    count = 0

    while not (x == local_x and y == local_y):
        count += 1
        if x == None and y == None:
            x = local_x
            y = local_y

        Colored[y][x]=1

        if Types[y][x] == 0:
            return None

        elif Types[y][x] == 1:
            if color == 0:
                if last_move != 'y+1':
                    y -= 1
                    last_move = 'y-1'
                else:
                    x -= 1
                    last_move = 'x-1'
            else:
                if last_move != 'y-1':
                    y += 1
                    last_move = 'y+1'
                else:
                    x += 1
                    last_move = 'x+1'

        elif Types[y][x] == 2:
            if color == 0:
                if last_move != 'x-1':
                    x += 1
                    last_move = 'x+1'
                else:
                    y -= 1
                    last_move = 'y-1'
            else:
                if last_move != 'x+1':
                    x -= 1
                    last_move = 'x-1'
                else:
                    y += 1
                    last_move = 'y+1'

        elif Types[y][x] == 3:
            if color == 0:
                if last_move != 'y-1':
                    y += 1
                    last_move = 'y+1'
                else:
                    x += 1
                    last_move = 'x+1'
            else:
                if last_move != 'y+1':
                    y -= 1
                    last_move = 'y-1'
                else:
                    x -= 1
                    last_move = 'x-1'

        elif Types[y][x] == 4:
            if color == 0:
                if last_move != 'x+1':
                    x -= 1
                    last_move = 'x-1'
                else:
                    y += 1
                    last_move = 'y+1'
            else:
                if last_move != 'x-1':
                    x += 1
                    last_move = 'x+1'
                else:
                    y -= 1
                    last_move = 'y-1'

        elif Types[y][x] == 5:
            if color == 0:
                if last_move != 'y+1':
                    y -= 1
                    last_move = 'y-1'
                else:
                    y += 1
                    last_move = 'y+1'
            else:
                if last_move != 'x+1':
                    x -= 1
                    last_move = 'x-1'
                else:
                    x += 1
                    last_move = 'x+1'

        elif Types[y][x] == 6:
            if color == 0:
                if last_move != 'x+1':
                    x -= 1
                    last_move = 'x-1'
                else:
                    x += 1
                    last_move = 'x+1'
            else:
                if last_move != 'y+1':
                    y -= 1
                    last_move = 'y-1'
                else:
                    y += 1
                    last_move = 'y+1'

    return count



import sys
pole=[]
FILE=open(sys.argv[1],'r')
for line in FILE:
    pole.append(line.replace('\n','').split(' '))
FILE.close()

Types=[[0 for i in range(len(pole[0])+2)] for j in range(len(pole)+2)]
Colors_d=[['' for i in range(len(pole[0])+2)] for j in range(len(pole)+2)]
Colors_l=[['' for i in range(len(pole[0])+2)] for j in range(len(pole)+2)]

for y,row in enumerate(pole):
    for x,tile in enumerate(row):
        if tile=='none':
            type=0
        elif tile=='ddll':
            type=1
        elif tile=='lddl':
            type=2
        elif tile=='lldd':
            type=3
        elif tile=='dlld':
            type=4
        elif tile=='ldld':
            type=5
        elif tile=='dldl':
            type=6
        Types[y+1][x+1]=type
#print('xd')

d_cycles=0
d_longest=0
for y in range(1,len(Types)-1):
    for x in range(1,len(Types[0])-1):
        if Colors_d[y][x]!=1:
            value=Cycle(x,y,Types,Colors_d,0)
            if value is not None:
                d_cycles+=1
                if value>d_longest:
                    d_longest=value

l_cycles=0
l_longest=0
for y in range(1,len(Types)-1):
    for x in range(1,len(Types[0])-1):
        if Colors_l[y][x]!=1:
            value=Cycle(x,y,Types,Colors_l,1)
            if value is not None:
                l_cycles+=1
                if value>l_longest:
                    l_longest=value

print(l_cycles,d_cycles,l_longest,d_longest)
