import sys

pole=[]
f = open(sys.argv[1], 'r')
size=list(map(int, f.readline().split()))

for i in range(size[1]):
    pole.append(list(map(int, f.readline().split())))

tiles=[]
for line in f:
    tiles.append(list(map(int, line.split())))
f.close()


Tiles=[]
for tile in tiles:
    dilek = []
    for i in range(0, len(tile), 2):
        dilek.append([tile[i], tile[i + 1]])
    Tiles.append(dilek)



NeW_Tiles=[]
index=1
for tile in Tiles:
    max_y = None
    min_y = None
    max_x = None
    min_x = None
    for item in tile:
        if max_y==None or max_y<item[1]:
            max_y=item[1]

        if min_y==None or min_y>item[1]:
            min_y=item[1]

        if max_x == None or max_x < item[0]:
            max_x = item[0]

        if min_x == None or min_x > item[0]:
            min_x = item[0]
    #print(min_y,max_y,min_x,max_x)
    NeW_Tiles.append([[0 for i in range(max_x-min_x+1)] for j in range(max_y-min_y+1)])
    for item in tile:
        NeW_Tiles[index-1][max_y-item[1]][item[0]]=index
    index += 1

del tile,dilek,f,i,line,tiles, min_x,max_x,max_y,min_y,item,index


def rotate(tile):
    new_tile=[[0 for i in range(len(tile))] for j in range(len(tile[0]))]
    for y in range(len(tile)):
        for x in range(len(tile[0])):
            new_tile[x][-y-1]=tile[y][x]
    return new_tile

tile=NeW_Tiles[0]


Valid_Moves=[]
for rotation in range(4):
    for move_y in range(size[1]-len(tile)+1):
        for move_x in range(size[0]-len(tile[0])+1):

            Valid_Move=True

            ubongo = [[0 for i in range(size[0])] for j in range(size[1])]
            for y in range(len(ubongo)):
                for x in range(len(ubongo[0])):
                    ubongo[y][x] = pole[y][x]

            for y in range(len(tile)):
                for x in range(len(tile[0])):
                    if ubongo[y+move_y][x+move_x]==0:
                        ubongo[y+move_y][x+move_x]=tile[y][x]

                    elif ubongo[y+move_y][x+move_x]!=0 and tile[y][x]!=0:
                        Valid_Move=False
                        break
                if not Valid_Move:
                    break
            if Valid_Move:
                Valid_Moves.append(ubongo)

    tile=rotate(tile)



Old_Valid=[]
for plane in range(len(Valid_Moves)):
    Old_Valid.append(Valid_Moves[plane])

for tile in NeW_Tiles[1:]:
    New_Valid = []
    for game in Old_Valid:
        for rotation in range(4):
            for move_y in range(size[1] - len(tile) + 1):
                for move_x in range(size[0] - len(tile[0]) + 1):

                    Valid_Move = True

                    ubongo = [[0 for i in range(size[0])] for j in range(size[1])]
                    for y in range(len(ubongo)):
                        for x in range(len(ubongo[0])):
                            ubongo[y][x] = game[y][x]

                    for y in range(len(tile)):
                        for x in range(len(tile[0])):
                            if ubongo[y + move_y][x + move_x] == 0:
                                ubongo[y + move_y][x + move_x] = tile[y][x]

                            elif ubongo[y + move_y][x + move_x] != 0 and tile[y][x] != 0:
                                Valid_Move = False
                                break
                        if not Valid_Move:
                            break
                    if Valid_Move:
                        New_Valid.append(ubongo)

            tile = rotate(tile)
    Old_Valid=[]
    for plane in range(len(New_Valid)):
        Old_Valid.append(New_Valid[plane])

for y in range(len(Old_Valid[0])):
    for x in range(len(Old_Valid[0][0])):
        print(Old_Valid[0][y][x],end=' ')
    print()