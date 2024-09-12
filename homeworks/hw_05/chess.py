#File=open('sachovnice.txt','r').read()
#open(sys.argv[1], "r")
import sys


pole=[]
f = open(sys.argv[1], "r")
for line in f:
    pole.append(list(map(int, line.split())))
f.close()


New_Final=pole



def Not_border(x,y):
    if x==0 or x==7 or y==0 or y==7:
        return False
    else:
        return True

def Find_Object(Array,Figure):
    pos=[]
    for X_index,x in enumerate(Array):
        for Y_index,y in enumerate(x):
            if y==Figure:
                pos.append([X_index,Y_index])
    return pos

def knight(y,x,Array,color):     #working

    """
    - T - T -
    T - - - T
    - - F - -
    T - - - T
    - T - T - 
    """

    if Array[y][x]==0:
        Array[y][x]=str(color*5)

    if y-1>=0:
        if x+2<=7:
            Array[y - 1][x + 2] = 'N'
        if x-2>=0:
            Array[y - 1][x - 2] = 'N'
    if y-2>=0:
        if x+1<=7:
            Array[y - 2][x + 1] = 'N'
        if x-1>=0:
            Array[y - 2][x - 1] = 'N'
    if y+2<=7:
        if x+1<=7:
            Array[y + 2][x + 1] = 'N'
        if x-1>=0:
            Array[y + 2][x - 1] = 'N'

    if y+1<=7:
        if x+2<=7:
            Array[y + 1][x + 2] = 'N'
        if x-2>=0:
            Array[y + 1][x - 2] = 'N'

def rook(y,x,Array,color,game):

    if Array[y][x] == 0:
        Array[y][x] =str(color*3)



    for Y in range(y-1,-1,-1):
        if game[Y][x]==0:
            Array[Y][x] = 'N'
        elif game[Y][x]=='N':
            pass
        elif game[Y][x]/abs(game[Y][x]) != color:
            Array[Y][x] = 'N'
            break
        elif game[Y][x]/abs(game[Y][x]) == color:
            break



    for Y in range(y+1,8,1):
        if game[Y][x] == 0:
            Array[Y][x] = 'N'
        elif game[Y][x]=='N':
            pass
        elif game[Y][x] / abs(game[Y][x]) != color:
            Array[Y][x] = 'N'
            break
        elif game[Y][x]/abs(game[Y][x]) == color:
            break


    for X in range(x-1,-1,-1):
        if game[y][X]==0:
            Array[y][X] = 'N'
        elif game[y][X]=='N':
            pass
        elif game[y][X] / abs(game[y][X]) != color:
            Array[y][X] = 'N'
            break
        elif game[y][X]/abs(game[y][X]) == color:
            break


    for X in range(x+1,8,1):
        if game[y][X]==0:
            Array[y][X] = 'N'
        elif game[y][X]=='N':
            pass
        elif game[y][X] / abs(game[y][X]) != color:
            Array[y][X] = 'N'
            break
        elif game[y][X]/abs(game[y][X]) == color:
            break

def pawn(y,x,Array,color,game,is_black=False):  #working
    if Array[y][x] == 0:
        Array[y][x] =str(color*6)

    if not is_black:
        if y-1>=0 and color==1:
            if x-1>=0:
                Array[y-1][x-1]='N'
            if x+1<=7:
                Array[y-1][x+1]='N'
        elif y+1<=7 and color==-1:
            if x-1>=0:
                Array[y+1][x-1]='N'
            if x+1<=7:
                Array[y+1][x+1]='N'

    else:
        if y-1>=0 and color==1:
            Array[y-1][x]='N'

        elif y+1<=7 and color==-1:
            Array[y+1][x]='N'

        if y-1>=0 and color==1:
            if x-1>=0:
                if game[y-1][x-1]<0:
                    Array[y-1][x-1]='N'
            if x+1<=7:
                if game[y-1][x+1]< 0:
                    Array[y-1][x+1]='N'
        elif y+1<=7 and color==-1:
            if x-1>=0:
                if game[y+1][x-1] > 0:
                    Array[y+1][x-1]='N'
            if x+1<=7:
                if game[y + 1][x - 1] > 0:
                    Array[y + 1][x - 1]='N'



def bishop(y,x,Array,color,game):
    if Array[y][x] == 0:
        Array[y][x] = str(color * 4)

    if x<y:
        p=x
    else:
        p=y

    for P in range(1,p+1,1):
        if game[y-P][x-P] == 0:
            Array[y-P][x-P] = 'N'
        elif game[y-P][x-P] == 'N':
            pass
        elif game[y-P][x-P] / abs(game[y-P][x-P]) != color:
            Array[y-P][x-P] = 'N'
            break
        elif game[y-P][x-P]/abs(game[y-P][x-P]) == color:
            break

    if x<7-y:
        p=x
    else:
        p=7-y

    for P in range(1,p+1,1):
        if game[y+P][x-P] == 0:
            Array[y+P][x-P] = 'N'
        elif game[y+P][x-P] == 'N':
            pass
        elif game[y+P][x-P] / abs(game[y+P][x-P]) != color:
            Array[y+P][x-P] = 'N'
            break
        elif game[y+P][x-P]/abs(game[y+P][x-P]) == color:
            break

    if 7-x<y:
        p=7-x
    else:
        p=y

    for P in range(1,p+1,1):
        if game[y-P][x+P] == 0:
            Array[y-P][x+P] = 'N'
        elif game[y-P][x+P] == 'N':
            pass
        elif game[y-P][x+P] / abs(game[y-P][x+P]) != color:
            Array[y-P][x+P] = 'N'
            break
        elif game[y-P][x+P]/abs(game[y-P][x+P]) == color:
            break

    if 7-x<7-y:
        p=7-x
    else:
        p=7-y

    for P in range(1,p+1,1):
        if game[y+P][x+P] == 0:
            Array[y+P][x+P] = 'N'
        elif game[y+P][x+P] == 'N':
            pass
        elif game[y+P][x+P] / abs(game[y+P][x+P]) != color:
            Array[y+P][x+P] = 'N'
            break
        elif game[y+P][x+P]/abs(game[y+P][x+P]) == color:
            break

def queen(y,x,Array,color,game):
    if Array[y][x] == 0:
        Array[y][x] = str(color * 2)

    for Y in range(y - 1, -1, -1):
        if game[Y][x] == 0:
            Array[Y][x] = 'N'
        elif game[Y][x] == 'N':
            pass
        elif game[Y][x] / abs(game[Y][x]) != color:
            Array[Y][x] = 'N'
            break
        elif game[Y][x] / abs(game[Y][x]) == color:
            break

    for Y in range(y + 1, 8, 1):
        if game[Y][x] == 0:
            Array[Y][x] = 'N'
        elif game[Y][x] == 'N':
            pass
        elif game[Y][x] / abs(game[Y][x]) != color:
            Array[Y][x] = 'N'
            break
        elif game[Y][x] / abs(game[Y][x]) == color:
            break

    for X in range(x - 1, -1, -1):
        if game[y][X] == 0:
            Array[y][X] = 'N'
        elif game[y][X] == 'N':
            pass
        elif game[y][X] / abs(game[y][X]) != color:
            Array[y][X] = 'N'
            break
        elif game[y][X] / abs(game[y][X]) == color:
            break

    for X in range(x + 1, 8, 1):
        if game[y][X] == 0:
            Array[y][X] = 'N'
        elif game[y][X] == 'N':
            pass
        elif game[y][X] / abs(game[y][X]) != color:
            Array[y][X] = 'N'
            break
        elif game[y][X] / abs(game[y][X]) == color:
            break

    if x < y:
        p = x
    else:
        p = y

    for P in range(1, p + 1, 1):
        if game[y - P][x - P] == 0:
            Array[y - P][x - P] = 'N'
        elif game[y - P][x - P] == 'N':
            pass
        elif game[y - P][x - P] / abs(game[y - P][x - P]) != color:
            Array[y - P][x - P] = 'N'
            break
        elif game[y - P][x - P] / abs(game[y - P][x - P]) == color:
            break

    if x < 7 - y:
        p = x
    else:
        p = 7 - y

    for P in range(1, p + 1, 1):
        if game[y + P][x - P] == 0:
            Array[y + P][x - P] = 'N'
        elif game[y + P][x - P] == 'N':
            pass
        elif game[y + P][x - P] / abs(game[y + P][x - P]) != color:
            Array[y + P][x - P] = 'N'
            break
        elif game[y + P][x - P] / abs(game[y + P][x - P]) == color:
            break

    if 7 - x < y:
        p = 7 - x
    else:
        p = y

    for P in range(1, p + 1, 1):
        if game[y - P][x + P] == 0:
            Array[y - P][x + P] = 'N'
        elif game[y - P][x + P] == 'N':
            pass
        elif game[y - P][x + P] / abs(game[y - P][x + P]) != color:
            Array[y - P][x + P] = 'N'
            break
        elif game[y - P][x + P] / abs(game[y - P][x + P]) == color:
            break

    if 7 - x < 7 - y:
        p = 7 - x
    else:
        p = 7 - y

    for P in range(1, p + 1, 1):
        if game[y + P][x + P] == 0:
            Array[y + P][x + P] = 'N'
        elif game[y + P][x + P] == 'N':
            pass
        elif game[y + P][x + P] / abs(game[y + P][x + P]) != color:
            Array[y + P][x + P] = 'N'
            break
        elif game[y + P][x + P] / abs(game[y + P][x + P]) == color:
            break


def king(y,x,Array,color,game):
    if Array[y][x] == 0:
        Array[y][x] =str(color*1)
    if x-1>=0:
        if game[y][x-1] == 0:
            Array[y][x-1] = 'N'
        elif game[y][x-1] == 'N':
            pass
        elif game[y][x-1] / abs(game[y][x-1]) != color:
            Array[y][x-1] = 'N'

        if y-1>=0:
            if game[y-1][x - 1] == 0:
                Array[y-1][x - 1] = 'N'
            elif game[y-1][x - 1] == 'N':
                pass
            elif game[y-1][x - 1] / abs(game[y-1][x - 1]) != color:
                Array[y-1][x - 1] = 'N'


        if y+1<=7:
            if game[y+1][x - 1] == 0:
                Array[y+1][x - 1] = 'N'
            elif game[y+1][x - 1] == 'N':
                pass
            elif game[y+1][x - 1] / abs(game[y+1][x - 1]) != color:
                Array[y+1][x - 1] = 'N'

    if x+1<=7:
        if game[y][x+1] == 0:
            Array[y][x+1] = 'N'
        elif game[y][x+1] == 'N':
            pass
        elif game[y][x+1] / abs(game[y][x+1]) != color:
            Array[y][x+1] = 'N'

        if y - 1 >= 0:
            if game[y - 1][x + 1] == 0:
                Array[y - 1][x + 1] = 'N'
            elif game[y - 1][x +1] == 'N':
                pass
            elif game[y - 1][x + 1] / abs(game[y - 1][x + 1]) != color:
                Array[y - 1][x + 1] = 'N'

        if y + 1 <= 7:
            if game[y + 1][x + 1] == 0:
                Array[y + 1][x + 1] = 'N'
            elif game[y + 1][x + 1] == 'N':
                pass
            elif game[y + 1][x + 1] / abs(game[y + 1][x + 1]) != color:
                Array[y + 1][x + 1] = 'N'

    if y - 1 >= 0:
        if game[y - 1][x ] == 0:
            Array[y - 1][x ] = 'N'
        elif game[y - 1][x ] == 'N':
            pass
        elif game[y - 1][x ] / abs(game[y - 1][x ]) != color:
            Array[y - 1][x ] = 'N'

    if y + 1<= 7:
        if game[y + 1][x] == 0:
            Array[y + 1][x] = 'N'
        elif game[y + 1][x] == 'N':
            pass
        elif game[y + 1][x] / abs(game[y + 1][x]) != color:
            Array[y + 1][x] = 'N'

Mat=True

White=[]
Black=[]

for y,row in enumerate(New_Final):
    for x,item in enumerate(row):
        if item>0:
            White.append([y,x,item])

        elif item<0:
            Black.append([y,x,abs(item),item/abs(item)])


for figure in Black:
    Array_Black=[[0 for i in range(8)] for j in range(8)]
    if figure[2]==2:
        queen(figure[0],figure[1],Array_Black,-1,New_Final)
    if figure[2]==3:
        rook(figure[0],figure[1],Array_Black,-1,New_Final)
    if figure[2]==4:
        bishop(figure[0],figure[1],Array_Black,-1,New_Final)
    if figure[2]==5:
        knight(figure[0],figure[1],Array_Black,-1)
    if figure[2]==6:
        pawn(figure[0],figure[1],Array_Black,-1,New_Final,True)

    Game_Edit=[item. copy() for item in New_Final]


    for y in range(len(Array_Black)):
        for x in range(len(Array_Black[y])):
            if Array_Black[y][x]=='N':
                Game_Edit[y][x]=int(figure[2]*figure[3])


    #print('xd')
    White_2=[]
    for y, row in enumerate(New_Final):
        for x, item in enumerate(row):
            if item > 0 and Game_Edit[y][x]==item:
                White_2.append([y, x, item])


    Array_White=Game_Edit
    for figure_white in White_2:
        if figure_white[2] == 1:
            king(figure_white[0], figure_white[1], Array_White, 1, Game_Edit)
        if figure_white[2] == 2:
            queen(figure_white[0], figure_white[1], Array_White, 1, Game_Edit)
        if figure_white[2] == 3:
            rook(figure_white[0], figure_white[1], Array_White, 1, Game_Edit)
        if figure_white[2] == 4:
            bishop(figure_white[0], figure_white[1], Array_White, 1, Game_Edit)
        if figure_white[2] == 5:
            knight(figure_white[0], figure_white[1], Array_White, 1)
        if figure_white[2] == 6:
            pawn(figure_white[0], figure_white[1], Array_White, 1,Game_Edit)

    kin = Find_Object(New_Final, -1)[0]
    if Game_Edit[kin[0]][kin[1]]!=-1:
        #print('alespon sach')
        pass
    else:
        #print('garde nebo nic')
        Mat=False


#print('šach: '+str(Mat)+', takže to je mat: '+str(not Mat))







Array=[[0 for i in range(8)] for j in range(8)]

for figure in White:
    Array_Black=[[0 for i in range(8)] for j in range(8)]
    if figure[2] == 1:
        king(figure[0], figure[1], Array, 1, New_Final)
    if figure[2]==2:
        queen(figure[0],figure[1],Array,1,New_Final)
    if figure[2]==3:
        rook(figure[0],figure[1],Array,1,New_Final)
    if figure[2]==4:
        bishop(figure[0],figure[1],Array,1,New_Final)
    if figure[2]==5:
        knight(figure[0],figure[1],Array,1)
    if figure[2]==6:
        pawn(figure[0],figure[1],Array,1,New_Final)



kin=Find_Object(New_Final,-1)
yk = kin[0][0]
xk = kin[0][1]


Garde=False


for row in New_Final:
    if -2 in row:
        q=True
        que=Find_Object(New_Final,-2)
        for items in que:
            if Array[items[0]][items[1]]=='N':
                Garde=True


Sach=False
if Array[yk][xk]=='N':
    if yk-1>=0:
        if Array[yk-1][xk]!='N' and New_Final[yk-1][xk]==0:
            Sach=True
        if xk-1>=0:
            if Array[yk - 1][xk-1] != 'N' and New_Final[yk - 1][xk-1] == 0:
                Sach = True
        if xk + 1 <= 7:
            if Array[yk - 1][xk + 1] != 'N' and New_Final[yk - 1][xk + 1] == 0:
                Sach = True
    if xk - 1 >= 0:
        if Array[yk][xk - 1] != 'N' and New_Final[yk - 1][xk - 1] == 0:
            Sach = True
    if xk + 1 <= 7:
        if Array[yk][xk + 1] != 'N' and New_Final[yk][xk + 1] == 0:
            Sach = True

    if yk+1<=7:
        if Array[yk+1][xk]!='N' and New_Final[yk+1][xk]==0:
            Sach=True
        if xk-1>=0:
            if Array[yk +1][xk-1] != 'N' and New_Final[yk + 1][xk-1] == 0:
                Sach = True
        if xk + 1 <= 7:
            if Array[yk + 1][xk + 1] != 'N' and New_Final[yk + 1][xk + 1] == 0:
                Sach = True


    #mat rika neni to mat a sach ze jo, tak to neni mat a je to sach
    #mat rika ze to neni mat a sach rika ze to neni mat tak je to sach

    if not Sach==False or Mat==False:
        print('SACH')
    else:
        print('MAT')
elif Garde:
    print('GARDE')
else:
    print('NO')




