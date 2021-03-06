class Kuriatko:

    def __init__(self, input_file):
        with open(input_file, 'r') as f:
            suborik = f.read()
        self.pos_x = 0
        self.pos_y = 0

        self.ploska = []    #plôška
        riadocek = []
        self.pocet_riadockov = 0
        for i in range(len(suborik)):
            if suborik[i] != '\n':
                riadocek += suborik[i]
            else:
                self.ploska.append(riadocek)
                self.pocet_riadockov += 1
                riadocek = []
        if len(self.ploska) > 0:
            self.znaky_riadocku = len(self.ploska[0])

    def __str__(self):
        ploska = ''
        for i in range(self.pocet_riadockov):
            for j in range(self.znaky_riadocku):
                ploska += self.ploska[i][j]
            ploska += '\n'
        # ploska = ploska[:-1]
        return ploska

    def start(self, pos_y, pos_x):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.ploska[self.pos_y][self.pos_x] = 'P'

    def movement(self, sequence):
        self.sucet = 0
        for i in range(len(sequence)):
            if sequence == 'u':
                while self.pos_x >= 0:
                    if self.ploska[self.pos_x][self.pos_y] == 'X':
                        break
                    elif self.ploska[self.pos_y - 1][self.pos_x] == 'x':
                        self.ploska[self.pos_y][self.pos_x] = '_'
                    elif self.ploska[self.pos_y - 1][self.pos_x] == 'O':
                        self.ploska[self.pos_y][self.pos_x] = 'o'
                        self.sucet += 100
                    elif self.ploska[self.pos_y - 1][self.pos_x] == 'o':
                        self.ploska[self.pos_y][self.pos_x] = ' '
                        self.sucet += 50
                    self.pos_x -= 1
                self.pos_x += 1
                self.ploska[self.pos_y][self.pos_x] = 'P'

            elif sequence == 'l':
                while self.pos_y < self.znaky_riadocku:
                    if self.ploska[self.pos_x][self.pos_y - 1] == 'X':
                        break
                    elif self.ploska[self.pos_y][self.pos_x - 1] == 'x':
                        self.ploska[self.pos_y][self.pos_x] = '_'
                    elif self.ploska[self.pos_y][self.pos_x - 1] == 'O':
                        self.ploska[self.pos_y][self.pos_x] = 'o'
                        self.sucet += 100
                    elif self.ploska[self.pos_y][self.pos_x - 1] == 'o':
                        self.ploska[self.pos_y][self.pos_x] = ' '
                        self.sucet += 50
                    self.pos_y -= 1
                self.pos_y += 1
                self.ploska[self.pos_y][self.pos_x] = 'P'

            elif sequence == 'r':
                while self.pos_x < self.pocet_riadockov:
                    if self.ploska[self.pos_y][self.pos_x + 1] == 'X':
                        break
                    elif self.ploska[self.pos_y][self.pos_x + 1] == 'x':
                        self.ploska[self.pos_y][self.pos_x] = '_'
                    elif self.ploska[self.pos_y][self.pos_x + 1] == 'O':
                        self.ploska[self.pos_y][self.pos_x] = 'o'
                        self.sucet += 100
                    elif self.ploska[self.pos_y][self.pos_x + 1] == 'o':
                        self.ploska[self.pos_y][self.pos_x] = ' '
                        self.sucet += 50
                    self.pos_y += 1
                self.pos_y -= 1
                self.ploska[self.pos_y][self.pos_x] = 'P'

            else:
                while self.pos_y >= 0:
                    if self.ploska[self.pos_y + 1][self.pos_x] == 'X':
                        break
                    elif self.ploska[self.pos_y + 1][self.pos_x] == 'x':
                        self.ploska[self.pos_y][self.pos_x] = '_'
                    elif self.ploska[self.pos_y + 1][self.pos_x] == 'O':
                        self.ploska[self.pos_y][self.pos_x] = 'o'
                        self.sucet += 100
                    elif self.ploska[self.pos_y + 1][self.pos_x] == 'o':
                        self.ploska[self.pos_y][self.pos_x] = ' '
                        self.sucet += 50
                    self.pos_x += 1
                self.pos_x -= 1
                self.ploska[self.pos_y][self.pos_x] = 'P' #TU JE PEKME POSADENY A NELUBI SA MU :((((((((((((((
        return self.sucet

      #  funkcia movement dostava postupnost prikazov pre pohyb hraca
       # a vrati hodnotu ziskanych trofeji a pocet prejdenych trofeji ako zoznam
       #  for i in range(len(sequence)):
       #          if sequence[i] == 'u':
       #              if self.ploska[self.pos_y - 1][self.pos_x] == 'o':
       #                  self.sucet += 50
       #                  self.ploska[self.pos_y][self.pos_x] = '_'
       #              elif self.ploska[self.pos_y - 1][self.pos_x] == 'O':
       #                  self.sucet += 100
       #                  self.ploska[self.pos_y][self.pos_x] = 'o'
       #              for j in range(len(self.doors)):
       #                  if self.doors[i] == [self.pos_y + 1][self.pos_x]:
       #                      if self.ploska[self.pos_y + 1][self.pos_x] == ' ':
       #                          self.ploska[self.pos_y][self.pos_x] = '_'
       #
       #          elif sequence[i] == 'l':
       #              if self.ploska[self.pos_y][self.pos_x - 1] == 'o':
       #                  self.sucet += 50
       #                  self.ploska[self.pos_y][self.pos_y] = ' '
       #              elif self.ploska[self.pos_x][self.pos_y] == 'O':
       #                  self.sucet += 100
       #                  self.ploska[self.pos_x][self.pos_x] = 'o'
       #              for j in range(len(self.doors)):
       #                  if self.doors[i] == [self.pos_y][self.pos_y - 1]:
       #                      if self.ploska[self.pos_y][self.pos_y - 1] == ' ':
       #                          self.ploska[self.pos_y][self.pos_y] = '_'
       #
       #          elif sequence[i] == 'r':
       #              if self.ploska[self.pos_y][self.pos_y + 1] == 'o':
       #                  self.sucet += 50
       #                  self.ploska[self.pos_y][self.pos_y] = ' '
       #              elif self.ploska[self.pos_y][self.pos_y] == 'O':
       #                  self.sucet += 100
       #                  self.ploska[self.pos_y][self.pos_y] = 'o'
       #              for j in range(len(self.doors)):
       #                  if self.doors[i] == [self.pos_y][self.pos_y + 1]:
       #                      if self.ploska[self.pos_y][self.pos_y + 1] == ' ':
       #                          self.ploska[self.pos_y][self.pos_y] = '_'
      #                 self.pos_x += 1
     #                  self.secret.doors(self.pos_y, self.pos_x)
       #
       #          elif sequence[i] == 'd':
       #              if self.ploska[self.pos_y - 1][self.pos_y] == 'o':
       #                  self.sucet += 50
       #                  self.ploska[self.pos_y][self.pos_y] = ' '
       #              elif self.ploska[self.pos_y][self.pos_y] == 'O':
       #                  self.sucet += 100
       #                  self.ploska[self.pos_y][self.pos_y] = 'o'
       #              for j in range(len(self.doors)):
       #                  if self.doors[i] == [self.pos_y - 1][self.pos_y]:
       #                      if self.ploska[self.pos_y - 1][self.pos_y] == ' ':
       #                          self.ploska[self.pos_y][self.pos_y] = '_'

        # return []

    def treasures(self):
        # funkcia treasures vrati sucet ceny trofeji, 'O' ma hodnotu 100, 'o' ma hodnotu 50
        sucet = 0
        # self.mala_trofej = 'o'
        # self.velka_trofej = 'O'
        for i in range(self.pocet_riadockov):
            for j in range(self.znaky_riadocku):
                if self.ploska[i][j] == 'o':
                    sucet += 50
                elif self.ploska[i][j] == 'O':
                    sucet += 100
                else:
                    pass

        return sucet

    def secret_doors(self, location_y, location_x):
        for i in range(location_y - 1, location_y + 2):
            for j in range(location_x - 1, location_x + 2):
                if self.ploska[i][j] == 'x':
                    self.ploska[i][j] = '_'
        # funkcia secret_doors skontroluje vsetkych 8 policok okolo
        # aktualnej pozicie hraca a ak su na niektorom policku tajne
        # dvere tak sa nahradia _, funkcia prijima ako parameter aktualnu poziciu hraca


if __name__ == '__main__':
    t = Kuriatko('board.txt')
    print(t)
    t.start(3, 1)
    print(t)
    print('Value of trophies:', t.treasures())
    x = t.movement('udluldlurd')
    print(t)
    print('Gained score and collected trophies:', x)