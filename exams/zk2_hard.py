import sys

File = open(sys.argv[1], 'r')
# File=open('txt','r')
line = File.readline()

line = line.replace('\n', '').split(' ')

size_x = int(line[0])
size_y = int(line[1])
size_z = int(line[2])

line = File.readline()
line = line.replace('\n', '').split(' ')

start_x = int(line[0])
start_y = int(line[1])
start_z = int(line[2])

line = File.readline()
line = line.replace('\n', '').split(' ')

end_x = int(line[0])
end_y = int(line[1])
end_z = int(line[2])

Layers = []
for _ in range(int(size_z)):
    Y = []
    for _ in range(int(size_y)):
        X = []
        for _ in range(int(size_x)):
            X.append(None)
        Y.append(X)
    Layers.append(Y)

for line in File:
    line = line.replace('\n', '').split(' ')
    Layers[int(line[2])][int(line[1])][int(line[0])] = 1


def Find_Moves(Layers, z, y, x):
    Valid = []
    for z_move in (-1, 0, 1):
        for y_move in (-1, 0, 1):
            for x_move in (-1, 0, 1):
                if z + z_move >= 0 and z + z_move <= end_z and y + y_move >= 0 and y + y_move <= end_y and x + x_move >= 0 and x + x_move <= end_x:
                    if z_move != 0 or y_move != 0 or x_move != 0:
                        if Layers[z + z_move][y + y_move][x + x_move] == None:
                            if [z + z_move, y + y_move, x + x_move] not in Valid:
                                Valid.append([z + z_move, y + y_move, x + x_move])

    return Valid


class Cube:
    def __init__(self):
        self.X = None
        self.Y = None
        self.Z = None
        self.Parent_X = None
        self.Parent_Y = None
        self.Parent_Z = None


# xd=Find_Moves(Layers,start_z,start_y,start_x)
Final = []
Moves = []

Move_Obj = Cube()
Move_Obj.X = start_x
Move_Obj.Y = start_y
Move_Obj.Z = start_z
Moves.append(Move_Obj)
Final.append(Move_Obj)
Actual_Position = Move_Obj

Visited = []
while True:
    Valid_Moves = Find_Moves(Layers, Actual_Position.Z, Actual_Position.Y, Actual_Position.X)
    New = []
    for move in Valid_Moves:
        if move not in Visited:
            New.append(move)
            # Visited.append(move)
    if len(Moves) > 0:
        Moves.pop(0)
    for move in New:

        Move_Obj = Cube()
        Move_Obj.X = move[2]
        Move_Obj.Y = move[1]
        Move_Obj.Z = move[0]
        Move_Obj.Parent_X = Actual_Position.X
        Move_Obj.Parent_Y = Actual_Position.Y
        Move_Obj.Parent_Z = Actual_Position.Z
        if Move_Obj not in Final:
            Moves.append(Move_Obj)
            Final.append(Move_Obj)
    if len(Moves) == 0:
        print('NEEXISTUJE')
        exit()
    Actual_Position = Moves[0]
    if Actual_Position.Z == end_z and Actual_Position.Y == end_y and Actual_Position.X == end_x:
        break

Path = []
Target = Final[-1]
Path.append(Target)
while Target.Parent_Z != None:
    for move in Final:
        if move.X == Target.Parent_X and move.Y == Target.Parent_Y and move.Z == Target.Parent_Z:
            Final.pop(Final.index(move))
            Target = move
            Path.append(Target)
            break

Path.pop(-1)
for tag in Path[::-1]:
    print(tag.X, tag.Y, tag.Z)
# print('xd')