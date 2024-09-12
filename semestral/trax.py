import time

import draw as Drawer
import sys
import random
import copy
import base as Base


# implement you player here. If you need to define some classes, do it also here. Only this file is to be submitted to Brute.
# define all functions here

class Move_Obj:
    def __init__(self):
        self.X = None
        self.Y = None
        self.Tile = None
        self.L_Cycles = None
        self.D_Cycles = None


class Player(Base.BasePlayer):
    def __init__(self, board, name, color):
        Base.BasePlayer.__init__(self, board, name, color)
        self.algorithmName = "MK6"
        self.Tiles = ['ldld', 'dldl', 'ddll', 'lddl', 'lldd', 'dlld']

    def move(self):
        Zero_Moves = []
        Win_Moves = []
        Tie_Moves = []
        Loss_Moves = []

        Moves = self.Generate_Combined()

        if len(Moves) == 0:
            return []

        for Move in Moves:
            Score = self.Move_Score(Move)
            if Score[0] != 0 or Score[1] != 0:
                if Score[0] > Score[1]:
                    Win_Moves.append([Move, Score])
                elif Score[0] == Score[1]:
                    Tie_Moves.append([Move, Score])
                elif Score[0] < Score[1]:
                    Loss_Moves.append([Move, Score])
            elif Score[0] == 0 and Score[1] == 0:
                Zero_Moves.append([Move, Score])

        Most_Score = 0
        Most_Score_Move = None
        # print('init',time.time() - start,end=' ')
        if len(Win_Moves) > 0:  # Zahraje vitezny tah kdyz bude za vice nez 15 bodu
            for Win_Move in Win_Moves:
                if Win_Move[1][0] > Most_Score:
                    Most_Score = Win_Move[1][0]
                    Most_Score_Move = Win_Move[0]
            if Most_Score > 10:
                # print('win', time.time() - start,end=' ')
                return Most_Score_Move

        if len(Zero_Moves) > 0:  # Zahraje tah tak aby oponent nemohl vyhrat
            return Zero_Moves[random.randint(0, len(Zero_Moves) - 1)][0]

            Clear_Moves = []
            False_Moves = []
            random.shuffle(Zero_Moves)

            Size = len(self.board)
            if Size > 10:
                Top = 10
            else:
                Top = 20

            if len(Zero_Moves) > Top:
                Maximum = Top
            else:
                Maximum = len(Zero_Moves)

            for Zero_Move in Zero_Moves[:Maximum]:
                board = [[None] * len(self.board[0]) for _ in range(len(self.board))]
                for y in range(len(self.board)):
                    for x in range(len(self.board[0])):
                        board[y][x] = self.board[y][x]
                for move in Zero_Move[0]:
                    board[move[0]][move[1]] = move[2]

                Can_Oponent_Win = False

                Deep_Moves = self.Generate_Combined(board)

                for Deep_move in Deep_Moves:
                    Score = self.Move_Score(Deep_move, board)
                    if Score[1] > 0:
                        Can_Oponent_Win = True
                        break
                if Can_Oponent_Win == False:
                    return Zero_Move[0]
                    # Clear_Moves.append(Zero_Move)
                else:
                    False_Moves.append(Zero_Move)

            if len(Clear_Moves) > 0:
                # print('LEN', Len,end=' ')
                return list(set(Zero_Moves) - set(False_Moves))[
                    random.randint(0, len(list(set(Zero_Moves) - set(False_Moves))) - 1)][0]

        if Most_Score != 0:
            # print('win', time.time() - start,end=' ')
            return Most_Score_Move

        if len(Tie_Moves) > 0:  # Zahraje tah tak aby oponent ziskal co nejmene bodu
            Least_Score = Tie_Moves[0][1][1]
            Least_Score_Move = Tie_Moves[0][0]
            for Tie_Move in Tie_Moves:
                if Tie_Move[1][1] < Least_Score:
                    Least_Score = Tie_Move[1][1]
                    Least_Score_Move = Tie_Move[0]

            # print('tie', time.time() - start, end=' ')
            return Least_Score_Move

        if len(Loss_Moves) > 0:  # Zahaje tah prohry tak aby oponent ziskal co nejmene bodu
            Least_Score = Loss_Moves[0][1][1]
            Least_Score_Move = Loss_Moves[0][0]
            for Loss_Move in Loss_Moves:
                if Loss_Move[1][1] < Least_Score:
                    Least_Score = Loss_Move[1][1]
                    Least_Score_Move = Loss_Move[0]

            # print('loss', time.time() - start)
            return Least_Score_Move

    def Move_Score(self, Move=[], Board=None):
        if Board == None:
            Board = self.board
        board = [[None] * len(Board[0]) for _ in range(len(Board))]
        for y in range(len(Board)):
            for x in range(len(Board[0])):
                board[y][x] = Board[y][x]
        for move in Move:
            board[move[0]][move[1]] = move[2]

        data = self.Cycles_Return(board)
        my_number_of_cycles = data[0 if self.myColor == 'l' else 1]
        enemy_number_of_cycles = data[0 if self.myColor == 'd' else 1]

        my_longest_cycle = data[2 if self.myColor == 'l' else 3]
        enemy_longest_cycle = data[2 if self.myColor == 'd' else 3]

        data_line = self.Line_Return(board)
        my_number_of_lines = data_line[0 if self.myColor == 'l' else 1]
        enemy_number_of_lines = data_line[0 if self.myColor == 'd' else 1]

        my_longest_line = data_line[2 if self.myColor == 'l' else 3]
        enemy_longest_line = data_line[2 if self.myColor == 'd' else 3]

        if (my_number_of_lines > 0 or my_number_of_cycles > 0) and (
                enemy_number_of_lines > 0 or enemy_number_of_cycles > 0):
            return (2 * my_longest_line + 2 * my_longest_cycle, enemy_longest_line + enemy_longest_cycle)

        elif (my_number_of_lines == 0 and my_number_of_cycles == 0) and (
                enemy_number_of_lines > 0 or enemy_number_of_cycles > 0):
            return (0, enemy_longest_line + enemy_number_of_cycles)

        elif (my_number_of_lines > 0 or my_number_of_cycles > 0) and (
                enemy_number_of_lines == 0 or enemy_number_of_cycles == 0):
            return (my_longest_line + my_longest_cycle, 0)

        return (0, 0)

    def Generate_Combined(self, Board=None):
        # Valid=[[[] for i in range(len(self.board[0]))] for j in range(len(self.board))]

        if Board == None:
            Board = self.board
        Valid_def, Forced_def = self.Valid_moves(Board)

        if len(Forced_def) > 0:
            return []
        if len(Valid_def) == 0:
            return []

        Lot = []
        while len(Valid_def) > 0:

            All_Moves = []
            # rnd=random.randint(0, len(Valid_def) - 1)
            Move = Valid_def[0]
            All_Moves.append(Move)

            board = [[None] * len(Board[0]) for _ in range(len(Board))]
            for y in range(len(Board)):
                for x in range(len(Board[0])):
                    board[y][x] = Board[y][x]
            row, col, tile = Move
            board[row][col] = tile

            Valid, Forced = self.Valid_moves(board)

            while len(Forced) > 0:
                for forced in Forced:
                    All_Moves.append(forced)
                for move in Forced:
                    row, col, tile = move
                    board[row][col] = tile
                Valid, Forced = self.Valid_moves(board)

            if self.Valid_moves(board, True) == True:
                if len(All_Moves) > 0:
                    Lot.append(All_Moves)

                Valid_def.pop(0)
            else:
                Valid_def.pop(0)
        return Lot

    def Cycle(self, local_x, local_y, Types, Colored, color):
        x = None
        y = None

        last_move = 0
        count = 0

        while not (x == local_x and y == local_y):
            count += 1
            if x == None and y == None:
                x = local_x
                y = local_y

            Colored[y][x] = 1

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

    def Cycles_Return(self, pole=None):
        if pole == None:
            pole = self.board

        Types = [[0 for i in range(len(pole[0]) + 2)] for j in range(len(pole) + 2)]
        Colors_d = [['' for i in range(len(pole[0]) + 2)] for j in range(len(pole) + 2)]
        Colors_l = [['' for i in range(len(pole[0]) + 2)] for j in range(len(pole) + 2)]

        for y, row in enumerate(pole):
            for x, tile in enumerate(row):
                if tile == 'none':
                    type = 0
                elif tile == 'ddll':
                    type = 1
                elif tile == 'lddl':
                    type = 2
                elif tile == 'lldd':
                    type = 3
                elif tile == 'dlld':
                    type = 4
                elif tile == 'ldld':
                    type = 5
                elif tile == 'dldl':
                    type = 6
                Types[y + 1][x + 1] = type
        # print('xd')

        d_cycles = 0
        d_longest = 0
        for y in range(1, len(Types) - 1):
            for x in range(1, len(Types[0]) - 1):
                if Colors_d[y][x] != 1:
                    value = self.Cycle(x, y, Types, Colors_d, 0)
                    if value is not None:
                        d_cycles += 1
                        if value > d_longest:
                            d_longest = value

        l_cycles = 0
        l_longest = 0
        for y in range(1, len(Types) - 1):
            for x in range(1, len(Types[0]) - 1):
                if Colors_l[y][x] != 1:
                    value = self.Cycle(x, y, Types, Colors_l, 1)
                    if value is not None:
                        l_cycles += 1
                        if value > l_longest:
                            l_longest = value

        # print(l_cycles, d_cycles, l_longest, d_longest)
        return (l_cycles, d_cycles, l_longest, d_longest)

    def Line_Return(self, pole=None):
        if pole == None:
            pole = self.board

        Types = [[-1 for i in range(len(pole[0]) + 2)] for j in range(len(pole) + 2)]

        for y, row in enumerate(pole):
            for x, tile in enumerate(row):
                if tile == 'none':
                    type = 0
                elif tile == 'ddll':
                    type = 1
                elif tile == 'lddl':
                    type = 2
                elif tile == 'lldd':
                    type = 3
                elif tile == 'dlld':
                    type = 4
                elif tile == 'ldld':
                    type = 5
                elif tile == 'dldl':
                    type = 6
                Types[y + 1][x + 1] = type

        # light
        # left
        ll_count = 0
        ll_max = 0
        for y in range(len(Types)):
            x = 1
            if Types[y][x] in [2, 3, 5]:
                actual_move = Types[y][x]
                last_move = 'x+1'
                color = 1

                count = 0
                while True:

                    if Types[y][x] == 0 or Types[y][x] == -1:
                        if x == len(Types[0]) - 1:
                            ll_count += 1
                            if count + 1 > ll_max:
                                ll_max = count + 1
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

                    actual_move = Types[y][x]
                    count += 1
                    # print(actual_move,end=' ')
                # print()
        # print('light left-\t', ll_count, ll_max)

        # light
        # top
        lt_count = 0
        lt_max = 0
        for x in range(len(Types[0])):
            y = 1
            if Types[y][x] in [3, 4, 6]:
                actual_move = Types[y][x]
                last_move = 'y+1'
                color = 1

                count = 0
                while True:

                    if Types[y][x] == 0 or Types[y][x] == -1:
                        if y == len(Types) - 1:
                            lt_count += 1
                            if count + 1 > lt_max:
                                lt_max = count + 1
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

                    actual_move = Types[y][x]
                    count += 1
                    # print(actual_move,end=' ')
                # print()
        # print('light top-\t', lt_count, lt_max)

        # dark
        # left
        dl_count = 0
        dl_max = 0
        for y in range(len(Types)):
            x = 1
            if Types[y][x] in [1, 4, 6]:
                actual_move = Types[y][x]
                last_move = 'x+1'
                color = 0

                count = 0
                while True:

                    if Types[y][x] == 0 or Types[y][x] == -1:
                        if x == len(Types[0]) - 1:
                            dl_count += 1
                            if count + 1 > dl_max:
                                dl_max = count + 1
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

                    actual_move = Types[y][x]
                    count += 1
                    # print(actual_move,end=' ')
                # print()
        # print('dark left-\t', dl_count, dl_max)

        # dark
        # top
        dt_count = 0
        dt_max = 0
        for x in range(len(Types[0])):
            y = 1
            if Types[y][x] in [1, 2, 5]:
                actual_move = Types[y][x]
                last_move = 'y+1'
                color = 0

                count = 0
                while True:

                    if Types[y][x] == 0 or Types[y][x] == -1:
                        if y == len(Types) - 1:
                            dt_count += 1
                            if count + 1 > dt_max:
                                dt_max = count + 1
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

                    actual_move = Types[y][x]
                    count += 1
                    # print(actual_move,end=' ')
                # print()
        # print('dark top-\t', dt_count, dt_max)

        return (ll_count + lt_count, dl_count + dt_count, ll_max + lt_max, dl_max + dt_max)

    def tiles_list(self, color, position):
        List = []
        for tile in self.Tiles:
            if list(tile)[position] == color:
                List.append(tile)
        return List

    def Valid_moves(self, board, Validness=False):
        Valid = []
        Forced = []

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 'none':
                    Moves = []
                    Positions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
                    for Index, Position in enumerate(Positions):
                        if (y + Position[0] >= 0 and y + Position[0] <= len(board) - 1) and (
                                x + Position[1] >= 0 and x + Position[1] <= len(board[0]) - 1):
                            if board[y + Position[0]][x + Position[1]] != 'none':
                                Moves.append([Index, board[y + Position[0]][x + Position[1]]])

                    if len(Moves) == 1:

                        color = Moves[0][1]
                        if Moves[0][0] == 0:
                            color = list(color)[2]
                        elif Moves[0][0] == 1:
                            color = list(color)[3]
                        elif Moves[0][0] == 2:
                            color = list(color)[0]
                        elif Moves[0][0] == 3:
                            color = list(color)[1]
                        tiles = self.tiles_list(color, Moves[0][0])

                        for tile in tiles:
                            Valid.append([y, x, tile])

                        # tile=tiles_list(list(board[y-Position[Moves[0]][0]][x-Position[Index][1]]))

                    elif len(Moves) == 2:

                        Move1 = Moves[0]
                        Move2 = Moves[1]

                        color1 = Move1[1]
                        if Move1[0] == 0:
                            color1 = list(color1)[2]
                        elif Move1[0] == 1:
                            color1 = list(color1)[3]
                        elif Move1[0] == 2:
                            color1 = list(color1)[0]
                        elif Move1[0] == 3:
                            color1 = list(color1)[1]
                        tiles1 = self.tiles_list(color1, Move1[0])

                        color2 = Move2[1]
                        if Move2[0] == 0:
                            color2 = list(color2)[2]
                        elif Move2[0] == 1:
                            color2 = list(color2)[3]
                        elif Move2[0] == 2:
                            color2 = list(color2)[0]
                        elif Move2[0] == 3:
                            color2 = list(color2)[1]
                        tiles2 = self.tiles_list(color2, Move2[0])

                        for first in tiles1:
                            for second in tiles2:
                                if first == second:
                                    if color1 == color2:
                                        Forced.append([y, x, first])
                                    else:
                                        Valid.append([y, x, first])


                    elif len(Moves) == 3:

                        Move1 = Moves[0]
                        Move2 = Moves[1]
                        Move3 = Moves[2]

                        color1 = Move1[1]
                        if Move1[0] == 0:
                            color1 = list(color1)[2]
                        elif Move1[0] == 1:
                            color1 = list(color1)[3]
                        elif Move1[0] == 2:
                            color1 = list(color1)[0]
                        elif Move1[0] == 3:
                            color1 = list(color1)[1]
                        tiles1 = self.tiles_list(color1, Move1[0])

                        color2 = Move2[1]
                        if Move2[0] == 0:
                            color2 = list(color2)[2]
                        elif Move2[0] == 1:
                            color2 = list(color2)[3]
                        elif Move2[0] == 2:
                            color2 = list(color2)[0]
                        elif Move2[0] == 3:
                            color2 = list(color2)[1]
                        tiles2 = self.tiles_list(color2, Move2[0])

                        color3 = Move3[1]
                        if Move3[0] == 0:
                            color3 = list(color3)[2]
                        elif Move3[0] == 1:
                            color3 = list(color3)[3]
                        elif Move3[0] == 2:
                            color3 = list(color3)[0]
                        elif Move3[0] == 3:
                            color3 = list(color3)[1]
                        tiles3 = self.tiles_list(color3, Move3[0])

                        for first in tiles1:
                            for second in tiles2:
                                for third in tiles3:
                                    if first == second and second == third:
                                        if color1 == color2 or color1 == color3 or color2 == color3:
                                            Forced.append([y, x, first])
                                        else:
                                            Valid.append([y, x, first])
                                    else:
                                        if Validness == True:
                                            return False


                    elif len(Moves) == 4:

                        Move1 = Moves[0]
                        Move2 = Moves[1]
                        Move3 = Moves[2]
                        Move4 = Moves[3]

                        color1 = Move1[1]
                        if Move1[0] == 0:
                            color1 = list(color1)[2]
                        elif Move1[0] == 1:
                            color1 = list(color1)[3]
                        elif Move1[0] == 2:
                            color1 = list(color1)[0]
                        elif Move1[0] == 3:
                            color1 = list(color1)[1]
                        tiles1 = self.tiles_list(color1, Move1[0])

                        color2 = Move2[1]
                        if Move2[0] == 0:
                            color2 = list(color2)[2]
                        elif Move2[0] == 1:
                            color2 = list(color2)[3]
                        elif Move2[0] == 2:
                            color2 = list(color2)[0]
                        elif Move2[0] == 3:
                            color2 = list(color2)[1]
                        tiles2 = self.tiles_list(color2, Move2[0])

                        color3 = Move3[1]
                        if Move3[0] == 0:
                            color3 = list(color3)[2]
                        elif Move3[0] == 1:
                            color3 = list(color3)[3]
                        elif Move3[0] == 2:
                            color3 = list(color3)[0]
                        elif Move3[0] == 3:
                            color3 = list(color3)[1]
                        tiles3 = self.tiles_list(color3, Move3[0])

                        color4 = Move4[1]
                        if Move4[0] == 0:
                            color4 = list(color4)[2]
                        elif Move4[0] == 1:
                            color4 = list(color4)[3]
                        elif Move4[0] == 2:
                            color4 = list(color4)[0]
                        elif Move4[0] == 3:
                            color4 = list(color4)[1]
                        tiles4 = self.tiles_list(color4, Move4[0])

                        for first in tiles1:
                            for second in tiles2:
                                for third in tiles3:
                                    for forth in tiles4:
                                        if first == second and second == third and third == forth:
                                            if color1 == color2 or color1 == color3 or color1 == color4 or color2 == color3 or color2 == color4 or color3 == color4:
                                                Forced.append([y, x, first])
                                            else:
                                                Valid.append([y, x, first])
                                        else:
                                            if Validness == True:
                                                return False

        if Validness == False:
            return Valid, Forced
        else:
            return True


if __name__ == "__main__":
    # call you functions from this block:
    for _ in range(10):
        boardRows = 9
        boardCols = boardRows
        board = [["none"] * boardCols for _ in range(boardRows)]

        board[boardRows // 2][boardCols // 2] = ["lldd", "dlld", "ddll", "lddl", "dldl", "ldld"][random.randint(0, 5)]
        """board=[['dldl','dldl','dldl','dldl','dldl'],
               ['dldl','dldl','dldl','dldl','dldl'],
               ['dldl','dldl','none','lddl','dldl'],
               ['dldl','ldld','ldld','dldl','dldl'],
               ['dldl','dldl','dldl','dldl','dldl']]"""

        d = Drawer.Drawer()

        p1 = Player(board, "player1", 'l');
        p2 = Player(board, "player2", 'd');

        # test game. We assume that both player play correctly. In Brute/Tournament case, more things will be checked
        # like types of variables, validity of moves, etc...

        idx = 0
        d.draw(p1.board, "Images/move-{:04d}.png".format(idx))
        idx += 1
        print('Start:', p1.myColor, end=' ')
        Min = None
        Max = None
        Avg = 0
        Avg_Count = 0
        while True:

            # call player for his move
            start = time.time()
            # print(p1.myColor,end=' ')
            rmove = p1.move()
            Time = time.time() - start
            if Min == None or Time < Min:
                Min = Time
            if Max == None or Time > Max:
                Max = Time
            Avg += Time
            Avg_Count += 1

            # print('\t',Time)

            # rmove is: [ [r1,c1,tile1], ... [rn,cn,tile] ]
            # write to board of both players
            for move in rmove:
                row, col, tile = move
                p1.board[row][col] = tile
                p2.board[row][col] = tile

            # make png with resulting board
            d.draw(p1.board, "Images/move-{:04d}.png".format(idx))
            idx += 1

            if len(rmove) == 0:
                print('Win:', p1.myColor, '\n', "Full")
                print(p1.Move_Score())
                print(round(Min, 3), round(Avg / Avg_Count, 3), round(Max, 3))
                print()
                break

            data = p2.Cycles_Return()
            if data[0] > 0 or data[1] > 0:
                print('Win:', p1.myColor, "Cycle")
                print(p1.Move_Score())
                print(round(Min, 3), round(Avg / Avg_Count, 3), round(Max, 3))
                print()
                break

            data_lines = p2.Line_Return()
            if data[0] > 0 or data[1] > 0:
                print('Win:', p1.myColor, "Line")
                print(p1.Move_Score())
                print(round(Min, 3), round(Avg / Avg_Count, 3), round(Max, 3))
                print()
                break

            p1, p2 = p2, p1  # switch players