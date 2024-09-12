
class Point:
    def __init__(self):
        self.X=None
        self.Y=None
        self.Parent_X=None
        self.Parent_Y=None
        #self.Pole=None

def Find_Moves(y,x,board,Restricted=[]):
    Size_x=len(board[0])
    Size_y=len(board)

    Valid=[]
    Moves=[(-2,-1),(-2,1),(-1,2),(1,2),(2,-1),(2,1),(-1,-2),(1,-2)]
    for Move in Moves:
        if y+Move[0]>=0 and y+Move[0]<Size_y and x+Move[1]>=0 and x+Move[1]<Size_x:
            if board[y+Move[0]][x+Move[1]] in ['0','4']:
                if [y+Move[0],x+Move[1]] not in Restricted:
                    Pnt=Point()
                    Pnt.Y=y+Move[0]
                    Pnt.X=x+Move[1]
                    Pnt.Parent_Y=y
                    Pnt.Parent_X=x
                    Valid.append(Pnt)
                    Restricted.append([y+Move[0],x+Move[1]])
    return Valid,Restricted


import sys,time
File=open(sys.argv[1],'r')
#start = time.time()
#File=open('pole','r')
#print('file',time.time()-start)

Pole=[]
for row in File:
    Pole.append(row.replace('\n','').split(' '))
#print('data',time.time()-start)

#print(Find_Moves(4,2,Pole,Restricted))

Start=Point()
for y in range(len(Pole)):
    for x in range(len(Pole[0])):
        if Pole[y][x]=='2':
            Start.X = x
            Start.Y = y

#print('start',time.time()-start)
Used=[]
Buffer=[]

#4,2
Valid,Restricted=Find_Moves(Start.Y,Start.X,Pole)
Exist=False
Final=[]
Final.append(Start)
while len(Valid)>0:
    Actual_item=Valid[0]
    Final.append(Actual_item)
    if Pole[Actual_item.Y][Actual_item.X]!='4':
        Pole[Actual_item.Y][Actual_item.X]='H'
    else:
        Exist=True
        break

    New_Valid,Restricted = Find_Moves(Actual_item.Y,Actual_item.X, Pole,Restricted)
    Valid.pop(0)
    for Mov in New_Valid:
        Valid.append(Mov)
#print('final',time.time()-start)
if not Exist:
    print('NEEXISTUJE')
    exit()

Target=Final[-1]
Final.pop(-1)
Last=[]
Last.append(Target)
while Start not in Last:
    for Item in Final[::-1]:
        if Item.X==Target.Parent_X and Item.Y==Target.Parent_Y:
            Last.append(Item)
            Final.pop(Final.index(Item))
            break
    Target = Last[-1]
#print('last',time.time()-start)
Last.pop(-1)
for item in Last[::-1]:
    print(item.Y,item.X,end=' ')
#print('print',time.time()-start)






"""Final=[]
while len(Valid)>0:
    Actual_item=Valid[0]

    if Pole[Actual_item[0]][Actual_item[1]]!='4':
        Pole[Actual_item[0]][Actual_item[1]]='H'
    else:
        break

    Final.append([Actual_item[0],Actual_item[1]])
    New_Valid=Find_Moves(Actual_item[0],Actual_item[1],Pole,Restricted)
    for Mov in New_Valid:
        Valid.append(Mov)
    Valid.pop(0)"""



