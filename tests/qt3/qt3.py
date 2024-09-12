line = input()
nums = line.split(' ')
Coords = []
for x in range(0, len(nums), 2):
    Coords.append([float(nums[x]), float(nums[x + 1])])


def Dist_From_Zero(x, y):
    return (x ** 2 + y ** 2) ** (0.5)


def Dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (0.5)


Circle_Index = None
for Index, Point in enumerate(Coords):
    Circle_r = Dist_From_Zero(Point[0], Point[1])
    Temp = Coords[:]
    Temp.pop(Index)
    In = 0
    for Test in Temp:
        if Dist_From_Zero(Test[0], Test[1]) <= Circle_r:
            In += 1
    if In + 1 == (len(Coords) / 2):
        Circle_Index = Index
        break

X = 0
Y = 0
for Point in Coords:
    X += Point[0]
    Y += Point[1]

Tx = X / len(Coords)
Ty = Y / len(Coords)

Closest_Index = 0
Closest = Dist(Coords[0][0], Coords[0][1], Tx, Ty)
for Index, Point in enumerate(Coords):
    if Dist(Point[0], Point[1], Tx, Ty) < Closest:
        Closest = Dist(Point[0], Point[1], Tx, Ty)
        Closest_Index = Index
print(Closest_Index, Circle_Index)
# print('y')