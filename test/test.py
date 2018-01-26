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

class Test:

    def __init__(self, input_file):
        pass

    def __str__(self):
        return ''

    def start(self, pos_y, pos_x):
        pass

    def movement(self, sequence):
        return []

    def treasures(self):
        return 0

    def secret_doors(self, location_y, location_x):
        pass

if "name==main":
    t = Test('board.txt')
    print(t)
    t.start(3, 1)
    print(t)
    print('Value of trophies:', t.treasures())
    x = t.movement('udluldlurd')
    print(t)
    print('Gained score and collected trophies:', x)
