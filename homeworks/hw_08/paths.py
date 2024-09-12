



pole=[]
FILE=open('data1','r')
for line in FILE:
    pole.append(line.replace('\n','').split(' '))
FILE.close()


Types=[[-1 for i in range(len(pole[0])+2)] for j in range(len(pole)+2)]


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




#light
#left
ll_count=0
ll_max=0
for y in range(len(Types)):
    x=1
    if Types[y][x] in [2,3,5]:
        actual_move=Types[y][x]
        last_move='x+1'
        color=1

        count=0
        while True:

            if Types[y][x] == 0 or Types[y][x]==-1:
                if x == len(Types[0])-1:
                    ll_count += 1
                    if count+1 > ll_max:
                        ll_max = count+1
                break

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

            if x == len(Types[0]) - 1:
                ll_count += 1
                if count + 1 > ll_max:
                    ll_max = count + 1
                break

            actual_move=Types[y][x]
            count+=1
            #print(actual_move,end=' ')
        #print()
print('light left-\t',ll_count,ll_max)




#light
#top
lt_count=0
lt_max=0
for x in range(len(Types[0])):
    y=1
    if Types[y][x] in [3,4,6]:
        actual_move=Types[y][x]
        last_move='y+1'
        color=1

        count=0
        while True:

            if Types[y][x] == 0 or Types[y][x]==-1:
                if y == len(Types)-1:
                    lt_count += 1
                    if count+1 > lt_max:
                        lt_max = count+1
                break

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

            if y == len(Types) - 1:
                lt_count += 1
                if count + 1 > lt_max:
                    lt_max = count + 1
                break

            actual_move=Types[y][x]
            count+=1
            #print(actual_move,end=' ')
        #print()
print('light top-\t',lt_count,lt_max)


#dark
#left
dl_count=0
dl_max=0
for y in range(len(Types)):
    x=1
    if Types[y][x] in [1,4,6]:
        actual_move=Types[y][x]
        last_move='x+1'
        color=0

        count=0
        while True:

            if Types[y][x] == 0 or Types[y][x]==-1:
                if x == len(Types[0])-1:
                    dl_count += 1
                    if count+1 > dl_max:
                        dl_max = count+1
                break

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

            if x == len(Types[0]) - 1:
                dl_count += 1
                if count + 1 > dl_max:
                    dl_max = count + 1
                break

            actual_move=Types[y][x]
            count+=1
            #print(actual_move,end=' ')
        #print()
print('dark left-\t',dl_count,dl_max)


#dark
#top
dt_count=0
dt_max=0
for x in range(len(Types[0])):
    y=1
    if Types[y][x] in [1,2,5]:
        actual_move=Types[y][x]
        last_move='y+1'
        color=0

        count=0
        while True:

            if Types[y][x] == 0 or Types[y][x]==-1:
                if y == len(Types)-1:
                    dt_count += 1
                    if count+1 > dt_max:
                        dt_max = count+1
                break

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

            if y == len(Types) - 1:
                dt_count += 1
                if count + 1 > dt_max:
                    dt_max = count + 1
                break

            actual_move=Types[y][x]
            count+=1
            #print(actual_move,end=' ')
        #print()
print('dark top-\t',dt_count,dt_max)

print('xd')