# hracia plocha obsahuje:
# X -> stena
# x -> tajne dvere, ktore sa otvoria ked je postavicka v ich blizkosti
# _ -> prazdne policko
# O/o -> velky poklad/ maly poklad
# P -> postavicka hraca
#
# ak hrac prejde cez malu trofej na jej mieste bude potom prazdne policko a ziska 50 bodov, 1 prejdena trofej
# ak hrac prejde cez velku trofej na jej mieste bude potom policko s malou trofejou a ziska 50 bodov, 1 prejdena trofej
# ak hrac ukonci svoj pohyb v danom smere na policku s velkou trofejou,
# tak sa z plochy trofej uplne vymaze a hrac ziska 100 bodov, 2 prejdene trofeje
#
# funkcia start umiestni hraca do hracej plochy

# funkcia treasures vrati sucet ceny trofeji, 'O' ma hodnotu 100, 'o' ma hodnotu 50

# funkcia movement dostava postupnost prikazov pre pohyb hraca
# a vrati hodnotu ziskanych trofeji a pocet prejdenych trofeji ako zoznam

# funkcia secret_doors skontroluje vsetkych 8 policok okolo aktualnej pozicie hraca a ak su na niektorom policku tajne
# dvere tak sa nahradia _, funkcia prijima ako parameter aktualnu poziciu hraca

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
            if sequence[i] == 'u':
                while self.pos_y > 0:
                    if self.ploska[self.pos_y - 1][self.pos_x] == 'X':
                        break
                    elif self.ploska[self.pos_y - 1][self.pos_x] == 'o':
                        self.sucet += 50
                        self.ploska[self.pos_y - 1][self.pos_x] = 'P'
                        if self.ploska[self.pos_y][self.pos_x] == 'P':
                            self.ploska[self.pos_y][self.pos_x] = '_'
                    elif self.ploska[self.pos_y - 1][self.pos_x] == 'O':
                        self.ploska[self.pos_y - 1][self.pos_x] = 'P'
                        self.ploska[self.pos_y][self.pos_x] = '_'
                        self.sucet += 100
                        self.ploska[self.pos_y - 1][self.pos_x] = 'o'
                    elif self.ploska[self.pos_y - 1][self.pos_x] == '_':
                        self.ploska[self.pos_y - 1][self.pos_x] = 'P'
                        self.ploska[self.pos_y][self.pos_x] = '_'
                    self.pos_y -= 1
                self.pos_y -= 1
                self.secret_doors(self.pos_y, self.pos_x)

            elif sequence[i] == 'l':
                while self.pos_x > 0:
                    if self.ploska[self.pos_y][self.pos_x - 1] == 'X':
                        break
                    elif self.ploska[self.pos_y][self.pos_x - 1] == 'o':
                        self.sucet += 50
                        self.ploska[self.pos_y][self.pos_x - 1] = 'P'
                        if self.ploska[self.pos_y][self.pos_x] == 'P':
                            self.ploska[self.pos_y][self.pos_x] = '_'
                    elif self.ploska[self.pos_y][self.pos_x - 1] == 'O':
                        self.ploska[self.pos_y][self.pos_x - 1] = 'P'
                        self.ploska[self.pos_y][self.pos_x] = '_'
                        self.sucet += 100
                        self.ploska[self.pos_y][self.pos_x - 1] = 'o'
                    elif self.ploska[self.pos_y][self.pos_x - 1] == '_':
                        self.ploska[self.pos_y][self.pos_x - 1] = 'P'
                        self.ploska[self.pos_y][self.pos_x] = '_'
                    self.pos_x -= 1
                self.pos_x -= 1
                self.secret_doors(self.pos_y, self.pos_x)


            elif sequence[i] == 'r':
                while self.pos_x > 0:
                    if self.ploska[self.pos_y][self.pos_x + 1] == 'X':
                        break
                    elif self.ploska[self.pos_y][self.pos_x + 1] == 'o':
                        self.sucet += 50
                        self.ploska[self.pos_y][self.pos_x + 1] = 'P'
                        if self.ploska[self.pos_y][self.pos_x] == 'P':
                            self.ploska[self.pos_y][self.pos_x] = '_'
                    elif self.ploska[self.pos_y][self.pos_x + 1] == 'O':
                        self.ploska[self.pos_y][self.pos_x + 1] = 'P'
                        self.ploska[self.pos_y][self.pos_x] = '_'
                        self.sucet += 100
                        self.ploska[self.pos_y][self.pos_x + 1] = 'o'
                    elif self.ploska[self.pos_y][self.pos_x + 1] == '_':
                        self.ploska[self.pos_y][self.pos_x + 1] = 'P'
                        self.ploska[self.pos_y][self.pos_x] = '_'
                    self.pos_x += 1
                self.pos_x += 1
                self.secret_doors(self.pos_y, self.pos_x)


            elif sequence[i] == 'd':
                while self.pos_y > 0:
                    if self.ploska[self.pos_y + 1][self.pos_x] == 'X':
                        break
                    elif self.ploska[self.pos_y + 1][self.pos_x] == 'o':
                        self.sucet += 50
                        self.ploska[self.pos_y + 1][self.pos_x] = 'P'
                        if self.ploska[self.pos_y][self.pos_x] == 'P':
                            self.ploska[self.pos_y][self.pos_x] = '_'
                    elif self.ploska[self.pos_y + 1][self.pos_x] == 'O':
                        self.ploska[self.pos_y + 1][self.pos_x] = 'P'
                        self.ploska[self.pos_y][self.pos_x] = '_'
                        self.sucet += 100
                        self.ploska[self.pos_y + 1][self.pos_x] = 'o'
                    elif self.ploska[self.pos_y + 1][self.pos_x] == '_':
                        self.ploska[self.pos_y + 1][self.pos_x] = 'P'
                        self.ploska[self.pos_y][self.pos_x] = '_'
                    self.pos_y += 1
                self.pos_y += 1
                self.secret_doors(self.pos_y, self.pos_x)

            else:
                pass
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

       #          elif sequence[i] == 'l':
       #              if self.ploska[self.pos_y][self.pos_x - 1] == 'o':
       #                  self.sucet += 50
       #                  self.ploska[self.pos_y][self.pos_y] = ' '
       #              elif self.ploska[self.pos_x][self.pos_y] == 'O':
       #                  self.sucet += 100
       #                  self.ploska[self.pos_x][self.pos_x] = 'o'
       #              for j in range(len(self.doors)):
       #                  if self.doors[i] == [self.pos_y][self.pos_y - 1]:

       #          elif sequence[i] == 'r':
       #              if self.ploska[self.pos_y][self.pos_y + 1] == 'o':
       #                  self.sucet += 50
       #                  self.ploska[self.pos_y][self.pos_y] = ' '
       #              elif self.ploska[self.pos_y][self.pos_y] == 'O':
       #                  self.sucet += 100
       #                  self.ploska[self.pos_y][self.pos_y] = 'o'

      #                 self.pos_x += 1
     #                  self.secret.doors(self.pos_y, self.pos_x)
       #
       #          elif sequence[i] == 'd':
       #              if self.ploska[self.pos_y - 1][self.pos_y] == 'o':
       #                  self.sucet += 50
       #                  self.ploska[self.pos_y][self.pos_y] = ' '
       #              elif self.ploska[self.pos_y][self.pos_y] == 'O':


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
    x = t.movement('')
    print(t)
print('Gained score and collected trophies:', x)