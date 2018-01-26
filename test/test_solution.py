class Test:

    def __init__(self, input_file):
        with open(input_file, 'r') as file:
            content = file.read()

        self.board = list()
        row = list()

        self.player_y = 0
        self.player_x = 0

        self.rows = 0
        self.columns = 0

        for i in range(len(content)):
            if content[i] != '\n':
                row.append(content[i])
            else:
                self.board.append(row)
                row = list()
                self.rows += 1

        self.columns = len(self.board[0])

    def __str__(self):
        repr = ''
        for i in range(self.rows):
            for j in range(self.columns):
                repr += self.board[i][j]
            repr += '\n'
        return repr

    def start(self, pos_y, pos_x):
        self.board[pos_y][pos_x] = 'P'
        self.player_y = pos_y
        self.player_x = pos_x

    def movement(self, sequence):
        value = 0
        count = 0
        trophy_list = [value, count]
        for i in range(len(sequence)):
            if sequence[i] == 'u':
                while self.player_y > 0:
                    if self.board[self.player_y - 1][self.player_x] == 'X':
                        break
                    elif self.board[self.player_y - 1][self.player_x] == '_':
                        self.board[self.player_y - 1][self.player_x] = 'P'
                        if self.board[self.player_y][self.player_x] == 'P':
                            self.board[self.player_y][self.player_x] = '_'
                    elif self.board[self.player_y - 1][self.player_x] == 'o':
                        trophy_list[0] += 50
                        trophy_list[1] += 1
                        self.board[self.player_y - 1][self.player_x] = 'P'
                        if self.board[self.player_y][self.player_x] == 'P':
                            self.board[self.player_y][self.player_x] = '_'
                    elif self.board[self.player_y - 1][self.player_x] == 'O':
                        if self.player_y - 2 < 0 or self.board[self.player_y - 2][self.player_x] == 'X':
                            trophy_list[0] += 100
                            trophy_list[1] += 1
                            self.board[self.player_y - 1][self.player_x] = 'P'
                            self.board[self.player_y][self.player_x] = '_'
                        else:
                            trophy_list[0] += 50
                            trophy_list[1] += 1
                            self.board[self.player_y - 1][self.player_x] = 'o'
                            self.board[self.player_y][self.player_x] = '_'
                    self.player_y -= 1
                    self.secret_doors(self.player_y, self.player_x)
            elif sequence[i] == 'd':
                pass
            elif sequence[i] == 'l':
                pass
            else:
                pass

        return trophy_list

    def treasures(self):
        count = 0
        for i in self.board:
            for j in i:
                if j == 'O':
                    count += 100
                elif j == 'o':
                    count += 50
                else:
                    pass
        return count

    def secret_doors(self, location_y, location_x):
        for i in range(location_y - 1, location_y + 2):
            for j in range(location_x - 1, location_x + 2):
                if self.board[i][j] == 'x':
                    self.board[i][j] = '_'

if "name==main":
    t = Test('board.txt')
    print(t)
    t.start(3, 1)
    print(t)
    print('Value of trophies:', t.treasures())
    x = t.movement('udluldlurd')
    print(t)
    print('Gained score and collected trophies:', x)
