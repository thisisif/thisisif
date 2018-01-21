import tkinter


# menu
class Zaciatok:
    def __init__(self):
        self.canvas = tkinter.Canvas(width=1100, height=700, bg='darkturquoise')
        self.canvas.pack()
        self.pozadie = tkinter.PhotoImage(file='obrazky/pozadie.png')
        self.canvas.create_image(550, 350, image=self.pozadie)
        self.canvas.create_rectangle(850, 350, 1000, 400, fill='darkcyan', width='10')
        self.canvas.create_text(925, 375, text='1.úroveň', font='arial 15')
        self.canvas.create_rectangle(850, 420, 1000, 470, fill='darkcyan', width='10')
        self.canvas.create_text(925, 445, text='2.úroveň', font='arial 15')
        self.canvas.create_rectangle(850, 490, 1000, 540, fill='darkcyan', width='10')
        self.canvas.create_text(925, 515, text='3.úroveň', font='arial 15')
        self.canvas.create_rectangle(850, 560, 1000, 610, fill='darkcyan', width='10')
        self.canvas.create_text(925, 585, text='4.úroveň', font='arial 15')
        self.canvas.create_text(810, 650,
                                text='Potiahnutím krabice ponad políčko s číslom úrovne si vyberiete rozloženie',
                                font='arial 12')
        self.k = tkinter.PhotoImage(file='obrazky/krabica.png')
        self.krabicka = self.canvas.create_image(600, 375, image=self.k)
        self.canvas.bind('<B1-Motion>', self.vyber)
        animacia = self.canvas.create_image(275, 525)
        pole = [tkinter.PhotoImage(file=f'obrazky/pozadie{i}.png') for i in range(23)]
        i = 0
        self.x = True
        while self.x:
            self.canvas.itemconfig(animacia, image=pole[i])
            self.canvas.update()
            self.canvas.after(150)
            if i < 22:
                i += 1
            else:
                i = 0
        self.canvas.mainloop()

    def vyber(self, event):
        self.x = event.x
        self.y = event.y
        if self.x > 550:
            self.canvas.coords(self.krabicka, self.x, self.y)
            if (890 < event.x < 980) and (365 < event.y < 395):
                self.x = False
                self.canvas.destroy()
                self.roz = 'rozlozenie1.txt'
                Hrac(self.roz)
            elif (890 < event.x < 980) and (435 < event.y < 455):
                self.x = False
                self.canvas.destroy()
                self.roz = 'rozlozenie2.txt'
                Hrac(self.roz)
            elif (890 < event.x < 980) and (505 < event.y < 525):
                self.x = False
                self.canvas.destroy()
                self.roz = 'rozlozenie3.txt'
                Hrac(self.roz)
            elif (890 < event.x < 980) and (575 < event.y < 595):
                self.x = False
                self.canvas.destroy()
                self.roz = 'rozlozenie4.txt'
                Hrac(self.roz)


# zapnutie časovača, ked sa zapne hracia plocha, funkcia koniec spravi, že sa vrátime do Zaciatoka
class Hrac:

    def __init__(self, rozlozenie):
        self.canvas = tkinter.Canvas(width=1100, height=700, bg='powderblue')
        self.canvas.pack()
        self.plocha = []
        self.suradnice_C = []
        self.rozlozenie = rozlozenie
        with open(self.rozlozenie) as subor:
            for riadok, i in enumerate(subor):
                pole = []
                for stlpec, j in enumerate(i.strip()):
                    pole.append(j)
                    if j == 'C':
                        self.suradnice_C.append((riadok, stlpec))
                    if j == 'P':
                        self.poz_x = stlpec
                        self.poz_y = riadok
                self.plocha.append(pole)
        self.sekundy = self.canvas.create_text(1005, 490, font='arial 40')
        self.cas = 0
        self.kroky = 0
        self.x = 0
        self.y = 0
        self.p = tkinter.PhotoImage(file='obrazky/worker.png')
        self.sipka_h = tkinter.PhotoImage(file="obrazky/sipka_hore.png")
        self.sipka_d = tkinter.PhotoImage(file="obrazky/sipka_dole.png")
        self.sipka_vp = tkinter.PhotoImage(file="obrazky/sipka_vpravo.png")
        self.sipka_vl = tkinter.PhotoImage(file="obrazky/sipka_vlavo.png")
        self.hore = self.canvas.create_image(1000, 70, image=self.sipka_h)
        self.dole = self.canvas.create_image(1000, 150, image=self.sipka_d)
        self.vpravo = self.canvas.create_image(1040, 110, image=self.sipka_vp)
        self.vlavo = self.canvas.create_image(960, 110, image=self.sipka_vl)
        self.canvas.create_rectangle(920, 300, 1090, 400, width=5, fill='white')
        self.canvas.create_text(1005, 320, text='Vyhnite sa bombe', font='arial')
        self.canvas.create_text(1005, 360, text='Presuňte všetky', font='arial')
        self.canvas.create_text(1005, 380, text='krabice na X', font='arial')
        self.canvas.create_rectangle(920, 420, 1090, 520, width=5, fill='white')
        self.canvas.create_text(1005, 450, text='Počet sekúnd:', font='arial')
        self.stena0 = tkinter.PhotoImage(file='obrazky/stena0.png')
        self.stena1 = tkinter.PhotoImage(file='obrazky/stena1.png')
        self.stena2 = tkinter.PhotoImage(file='obrazky/stena2.png')
        self.stena3 = tkinter.PhotoImage(file='obrazky/stena3.png')
        self.krabica = tkinter.PhotoImage(file='obrazky/krabica.png')
        self.ciel = tkinter.PhotoImage(file='obrazky/ciel.png')
        self.b = tkinter.PhotoImage(file='obrazky/0.gif')
        if self.rozlozenie == 'rozlozenie1.txt':
            self.canvas.create_rectangle(10, 20, 910, 670, fill='darkgrey', outline='')
        elif self.rozlozenie == 'rozlozenie2.txt':
            self.canvas.create_rectangle(10, 20, 910, 670, fill='lightgreen', outline='')
        elif self.rozlozenie == 'rozlozenie3.txt':
            self.canvas.create_rectangle(10, 20, 910, 670, fill='moccasin', outline='')
        elif self.rozlozenie == 'rozlozenie4.txt':
            self.canvas.create_rectangle(10, 20, 910, 670, fill='khaki', outline='')
        y = 50
        for i in self.plocha:
            x = 40
            for j in i:
                if (j == 'X') and (self.rozlozenie == 'rozlozenie1.txt'):
                    self.canvas.create_image(x, y, image=self.stena0)
                elif (j == 'X') and (self.rozlozenie == 'rozlozenie2.txt'):
                    self.canvas.create_image(x, y, image=self.stena1)
                elif (j == 'X') and (self.rozlozenie == 'rozlozenie3.txt'):
                    self.canvas.create_image(x, y, image=self.stena2)
                elif (j == 'X') and (self.rozlozenie == 'rozlozenie4.txt'):
                    self.canvas.create_image(x, y, image=self.stena3)
                elif j == 'K':
                    self.canvas.create_image(x, y, image=self.krabica)
                elif j == 'P':
                    self.x = x
                    self.y = y
                elif j == 'C':
                    self.canvas.create_image(x, y, image=self.ciel)
                elif j == 'B':
                    self.bomba = self.canvas.create_image(x, y, image=self.b)
                elif j == ' ' and (self.rozlozenie == 'rozlozenie1.txt'):
                    self.canvas.create_rectangle(x - 30, y - 30, x + 30, y + 30, fill='darkgrey', outline='')
                elif j == ' ' and (self.rozlozenie == 'rozlozenie2.txt'):
                    self.canvas.create_rectangle(x - 30, y - 30, x + 30, y + 30, fill='lightgreen', outline='')
                elif j == ' ' and (self.rozlozenie == 'rozlozenie3.txt'):
                    self.canvas.create_rectangle(x - 30, y - 30, x + 30, y + 30, fill='moccasin', outline='')
                elif j == ' ' and (self.rozlozenie == 'rozlozenie4.txt'):
                    self.canvas.create_rectangle(x - 30, y - 30, x + 30, y + 30, fill='khaki', outline='')
                x += 60
            y += 60

        self.postavicka = self.canvas.create_image(self.x, self.y, image=self.p)
        self.canvas.bind_all('<Left>', self.dolava)
        self.canvas.bind_all('<Right>', self.doprava)
        self.canvas.bind_all('<Up>', self.hore1)
        self.canvas.bind_all('<Down>', self.dole1)
        self.canvas.mainloop()

    def doprava(self, event):
        if self.plocha[self.poz_y][self.poz_x + 1] == ' ':
            if (self.poz_y, self.poz_x) in self.suradnice_C:
                self.plocha[self.poz_y][self.poz_x] = 'C'
            else:
                self.plocha[self.poz_y][self.poz_x] = ' '
            self.canvas.move(self.postavicka, 60, 0)
            self.plocha[self.poz_y][self.poz_x + 1] = 'P'
            self.poz_x += 1
            self.kroky += 1
        elif self.plocha[self.poz_y][self.poz_x + 1] == 'X':
            pass
        elif self.plocha[self.poz_y][self.poz_x + 1] == 'B':
            print('Narazil si na bombu, prehral si!')
            self.koniec()
        elif self.plocha[self.poz_y][self.poz_x + 1] == 'C':
            if (self.poz_y, self.poz_x) in self.suradnice_C:
                self.plocha[self.poz_y][self.poz_x] = 'C'
            else:
                self.plocha[self.poz_y][self.poz_x] = ' '
            self.canvas.move(self.postavicka, 60, 0)
            self.plocha[self.poz_y][self.poz_x + 1] = 'P'
            self.poz_x += 1
            self.kroky += 1
        elif self.plocha[self.poz_y][self.poz_x + 1] == 'K':
            if self.plocha[self.poz_y][self.poz_x + 2] == 'K' or self.plocha[self.poz_y][self.poz_x + 2] == 'X':
                pass
            elif self.plocha[self.poz_y][self.poz_x + 2] == ' ' or self.plocha[self.poz_y][self.poz_x + 2] == 'C':
                self.plocha[self.poz_y][self.poz_x + 2] = 'K'
                self.plocha[self.poz_y][self.poz_x + 1] = 'P'
                if (self.poz_y, self.poz_x) in self.suradnice_C:
                    self.plocha[self.poz_y][self.poz_x] = 'C'
                else:
                    self.plocha[self.poz_y][self.poz_x] = ' '
                self.kroky += 1
            elif self.plocha[self.poz_y][self.poz_x + 2] == 'B':
                self.koniec()

    def dolava(self, event):
        if self.plocha[self.poz_y][self.poz_x - 1] == ' ':
            if (self.poz_y, self.poz_x) in self.suradnice_C:
                self.plocha[self.poz_y][self.poz_x] = 'C'
            else:
                self.plocha[self.poz_y][self.poz_x] = ' '
            self.canvas.move(self.postavicka, -60, 0)
            self.plocha[self.poz_y][self.poz_x - 1] = 'P'
            self.poz_x -= 1
            self.kroky += 1
        elif self.plocha[self.poz_y][self.poz_x - 1] == 'X':
            pass
        elif self.plocha[self.poz_y][self.poz_x - 1] == 'B':
            print('Narazil si na bombu, prehral si!')
            self.koniec()
        elif self.plocha[self.poz_y][self.poz_x - 1] == 'C':
            if (self.poz_y, self.poz_x) in self.suradnice_C:
                self.plocha[self.poz_y][self.poz_x] = 'C'
            else:
                self.plocha[self.poz_y][self.poz_x] = ' '
            self.canvas.move(self.postavicka, -60, 0)
            self.plocha[self.poz_y][self.poz_x - 1] = 'P'
            self.poz_x -= 1
            self.kroky += 1
        elif self.plocha[self.poz_y][self.poz_x - 1] == 'K':
            if self.plocha[self.poz_y][self.poz_x - 2] == 'K' or self.plocha[self.poz_y][self.poz_x - 2] == 'X':
                pass
            elif self.plocha[self.poz_y][self.poz_x - 2] == ' ' or self.plocha[self.poz_y][self.poz_x - 2] == 'C':
                self.plocha[self.poz_y][self.poz_x - 2] = 'K'
                self.plocha[self.poz_y][self.poz_x - 1] = 'P'
                if (self.poz_y, self.poz_x) in self.suradnice_C:
                    self.plocha[self.poz_y][self.poz_x] = 'C'
                else:
                    self.plocha[self.poz_y][self.poz_x] = ' '
                self.kroky += 1
            elif self.plocha[self.poz_y][self.poz_x - 2] == 'B':
                self.koniec()

    def hore1(self, event):
        if self.plocha[self.poz_y - 1][self.poz_x] == ' ':
            if (self.poz_y, self.poz_x) in self.suradnice_C:
                self.plocha[self.poz_y][self.poz_x] = 'C'
            else:
                self.plocha[self.poz_y][self.poz_x] = ' '
            self.canvas.move(self.postavicka, 0, -60)
            self.plocha[self.poz_y - 1][self.poz_x] = 'P'
            self.poz_y -= 1
            self.kroky += 1
        elif self.plocha[self.poz_y - 1][self.poz_x] == 'X':
            pass
        elif self.plocha[self.poz_y - 1][self.poz_x] == 'B':
            print('Narazil si na bombu, prehral si!')
            self.koniec()
        elif self.plocha[self.poz_y - 1][self.poz_x] == 'C':
            if (self.poz_y, self.poz_x) in self.suradnice_C:
                self.plocha[self.poz_y][self.poz_x] = 'C'
            else:
                self.plocha[self.poz_y][self.poz_x] = ' '
            self.canvas.move(self.postavicka, 0, -60)
            self.plocha[self.poz_y - 1][self.poz_x] = 'P'
            self.poz_y -= 1
            self.kroky += 1
        elif self.plocha[self.poz_y - 1][self.poz_x] == 'K':
            if self.plocha[self.poz_y - 2][self.poz_x] == 'K' or self.plocha[self.poz_y - 2][self.poz_x] == 'X':
                pass
            elif self.plocha[self.poz_y - 2][self.poz_x] == ' ' or self.plocha[self.poz_y - 2][self.poz_x] == 'C':
                self.plocha[self.poz_y - 2][self.poz_x] = 'K'
                self.plocha[self.poz_y - 1][self.poz_x] = 'P'
                if (self.poz_y, self.poz_x) in self.suradnice_C:
                    self.plocha[self.poz_y][self.poz_x] = 'C'
                else:
                    self.plocha[self.poz_y][self.poz_x] = ' '
                self.kroky += 1
            elif self.plocha[self.poz_y - 2][self.poz_x] == 'B':
                self.koniec()

    def dole1(self, event):
        if self.plocha[self.poz_y + 1][self.poz_x] == ' ':
            if (self.poz_y, self.poz_x) in self.suradnice_C:
                self.plocha[self.poz_y][self.poz_x] = 'C'
            else:
                self.plocha[self.poz_y][self.poz_x] = ' '
            self.canvas.move(self.postavicka, 0, 60)
            self.plocha[self.poz_y + 1][self.poz_x] = 'P'
            self.poz_y += 1
            self.kroky += 1
        elif self.plocha[self.poz_y + 1][self.poz_x] == 'X':
            pass
        elif self.plocha[self.poz_y + 1][self.poz_x] == 'B':
            print('Narazil si na bombu, prehral si!')
            self.koniec()
        elif self.plocha[self.poz_y + 1][self.poz_x] == 'C':
            if (self.poz_y, self.poz_x) in self.suradnice_C:
                self.plocha[self.poz_y][self.poz_x] = 'C'
            else:
                self.plocha[self.poz_y][self.poz_x] = ' '
            self.canvas.move(self.postavicka, 0, 60)
            self.plocha[self.poz_y + 1][self.poz_x] = 'P'
            self.poz_y += 1
            self.kroky += 1
        elif self.plocha[self.poz_y + 1][self.poz_x] == 'K':
            if self.plocha[self.poz_y + 2][self.poz_x] == 'K' or self.plocha[self.poz_y + 2][self.poz_x] == 'X':
                pass
            elif self.plocha[self.poz_y + 2][self.poz_x] == ' ' or self.plocha[self.poz_y + 2][self.poz_x] == 'C':
                self.plocha[self.poz_y + 2][self.poz_x] = 'K'
                self.plocha[self.poz_y + 1][self.poz_x] = 'P'
                if (self.poz_y, self.poz_x) in self.suradnice_C:
                    self.plocha[self.poz_y][self.poz_x] = 'C'
                else:
                    self.plocha[self.poz_y][self.poz_x] = ' '
                self.kroky += 1
            elif self.plocha[self.poz_y + 2][self.poz_x] == 'B':
                self.koniec()

    def koniec(self):
        bezi = False
        self.canvas.destroy()

a = Zaciatok()

    # def pohyb(self, event):
    #     self.pocet_cielov = 0
    #     for riadok, i in enumerate(self.plocha):
    #         for stlpec, j in enumerate(i):
    #             if j == 'C':
    #                 self.pocet_cielov += 1
    #             if j == 'P':
    #                 self.poz_x = stlpec
    #                 self.poz_y = riadok
    #     if self.pocet_cielov == 0:
    #         print('Presunul si všetky krabice na správne miesto, vyhral si!')
    #         self.koniec()
    #     else:
    #         # vpravo
    #         if (1015 < event.x < 1065) and (112 < event.y < 130):
    #             if self.plocha[self.poz_y][self.poz_x + 1] == ' ':
    #                 if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                     self.plocha[self.poz_y][self.poz_x] = 'C'
    #                 else:
    #                     self.plocha[self.poz_y][self.poz_x] = ' '
    #                 self.canvas.move(self.postavicka, 60, 0)
    #                 self.plocha[self.poz_y][self.poz_x + 1] = 'P'
    #                 self.poz_x += 1
    #                 self.kroky += 1
    #             elif self.plocha[self.poz_y][self.poz_x + 1] == 'X':
    #                 pass
    #             elif self.plocha[self.poz_y][self.poz_x + 1] == 'B':
    #                 print('Narazil si na bombu, prehral si!')
    #                 self.koniec()
    #             elif self.plocha[self.poz_y][self.poz_x + 1] == 'C':
    #                 if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                     self.plocha[self.poz_y][self.poz_x] = 'C'
    #                 else:
    #                     self.plocha[self.poz_y][self.poz_x] = ' '
    #                 self.canvas.move(self.postavicka, 60, 0)
    #                 self.plocha[self.poz_y][self.poz_x + 1] = 'P'
    #                 self.poz_x += 1
    #                 self.kroky += 1
    #             elif self.plocha[self.poz_y][self.poz_x + 1] == 'K':
    #                 if self.plocha[self.poz_y][self.poz_x + 2] == 'K' or self.plocha[self.poz_y][self.poz_x + 2] == 'X':
    #                     pass
    #                 elif self.plocha[self.poz_y][self.poz_x + 2] == ' ' or self.plocha[self.poz_y][self.poz_x + 2] == 'C':
    #                     self.plocha[self.poz_y][self.poz_x + 2] = 'K'
    #                     self.plocha[self.poz_y][self.poz_x + 1] = 'P'
    #                     if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                         self.plocha[self.poz_y][self.poz_x] = 'C'
    #                     else:
    #                         self.plocha[self.poz_y][self.poz_x] = ' '
    #                     self.kroky += 1
    #                 elif self.plocha[self.poz_y][self.poz_x + 2] == 'B':
    #                     self.koniec()
    #
    #         # vlavo
    #         elif (935 < event.x < 985) and (112 < event.y < 130):
    #             if self.plocha[self.poz_y][self.poz_x - 1] == ' ':
    #                 if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                     self.plocha[self.poz_y][self.poz_x] = 'C'
    #                 else:
    #                     self.plocha[self.poz_y][self.poz_x] = ' '
    #                 self.canvas.move(self.postavicka, -60, 0)
    #                 self.plocha[self.poz_y][self.poz_x - 1] = 'P'
    #                 self.poz_x -= 1
    #                 self.kroky += 1
    #             elif self.plocha[self.poz_y][self.poz_x - 1] == 'X':
    #                 pass
    #             elif self.plocha[self.poz_y][self.poz_x - 1] == 'B':
    #                 print('Narazil si na bombu, prehral si!')
    #                 self.koniec()
    #             elif self.plocha[self.poz_y][self.poz_x - 1] == 'C':
    #                 if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                     self.plocha[self.poz_y][self.poz_x] = 'C'
    #                 else:
    #                     self.plocha[self.poz_y][self.poz_x] = ' '
    #                 self.canvas.move(self.postavicka, -60, 0)
    #                 self.plocha[self.poz_y][self.poz_x - 1] = 'P'
    #                 self.poz_x -= 1
    #                 self.kroky += 1
    #             elif self.plocha[self.poz_y][self.poz_x - 1] == 'K':
    #                 if self.plocha[self.poz_y][self.poz_x - 2] == 'K' or self.plocha[self.poz_y][self.poz_x - 2] == 'X':
    #                     pass
    #                 elif self.plocha[self.poz_y][self.poz_x - 2] == ' ' or self.plocha[self.poz_y][self.poz_x - 2] == 'C':
    #                     self.plocha[self.poz_y][self.poz_x - 2] = 'K'
    #                     self.plocha[self.poz_y][self.poz_x - 1] = 'P'
    #                     if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                         self.plocha[self.poz_y][self.poz_x] = 'C'
    #                     else:
    #                         self.plocha[self.poz_y][self.poz_x] = ' '
    #                     self.kroky += 1
    #                 elif self.plocha[self.poz_y][self.poz_x - 2] == 'B':
    #                     self.koniec()
    #
    #         # hore
    #         elif (980 < event.x < 1020) and (45 < event.y < 95):
    #             if self.plocha[self.poz_y - 1][self.poz_x] == ' ':
    #                 if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                     self.plocha[self.poz_y][self.poz_x] = 'C'
    #                 else:
    #                     self.plocha[self.poz_y][self.poz_x] = ' '
    #                 self.canvas.move(self.postavicka, 0, -60)
    #                 self.plocha[self.poz_y - 1][self.poz_x] = 'P'
    #                 self.poz_y -= 1
    #                 self.kroky += 1
    #             elif self.plocha[self.poz_y - 1][self.poz_x] == 'X':
    #                 pass
    #             elif self.plocha[self.poz_y - 1][self.poz_x] == 'B':
    #                 print('Narazil si na bombu, prehral si!')
    #                 self.koniec()
    #             elif self.plocha[self.poz_y - 1][self.poz_x] == 'C':
    #                 if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                     self.plocha[self.poz_y][self.poz_x] = 'C'
    #                 else:
    #                     self.plocha[self.poz_y][self.poz_x] = ' '
    #                 self.canvas.move(self.postavicka, 0, -60)
    #                 self.plocha[self.poz_y - 1][self.poz_x] = 'P'
    #                 self.poz_y -= 1
    #                 self.kroky += 1
    #             elif self.plocha[self.poz_y - 1][self.poz_x] == 'K':
    #                 if self.plocha[self.poz_y - 2][self.poz_x] == 'K' or self.plocha[self.poz_y - 2][self.poz_x] == 'X':
    #                     pass
    #                 elif self.plocha[self.poz_y - 2][self.poz_x] == ' ' or self.plocha[self.poz_y - 2][self.poz_x] == 'C':
    #                     self.plocha[self.poz_y - 2][self.poz_x] = 'K'
    #                     self.plocha[self.poz_y - 1][self.poz_x] = 'P'
    #                     if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                         self.plocha[self.poz_y][self.poz_x] = 'C'
    #                     else:
    #                         self.plocha[self.poz_y][self.poz_x] = ' '
    #                     self.kroky += 1
    #                 elif self.plocha[self.poz_y - 2][self.poz_x] == 'B':
    #                     self.koniec()
    #
    #         # dole
    #         elif (980 < event.x < 1020) and (125 < event.y < 175):
    #             if self.plocha[self.poz_y + 1][self.poz_x] == ' ':
    #                 if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                     self.plocha[self.poz_y][self.poz_x] = 'C'
    #                 else:
    #                     self.plocha[self.poz_y][self.poz_x] = ' '
    #                 self.canvas.move(self.postavicka, 0, 60)
    #                 self.plocha[self.poz_y + 1][self.poz_x] = 'P'
    #                 self.poz_y += 1
    #                 self.kroky += 1
    #             elif self.plocha[self.poz_y + 1][self.poz_x] == 'X':
    #                 pass
    #             elif self.plocha[self.poz_y + 1][self.poz_x] == 'B':
    #                 print('Narazil si na bombu, prehral si!')
    #                 self.koniec()
    #             elif self.plocha[self.poz_y + 1][self.poz_x] == 'C':
    #                 if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                     self.plocha[self.poz_y][self.poz_x] = 'C'
    #                 else:
    #                     self.plocha[self.poz_y][self.poz_x] = ' '
    #                 self.canvas.move(self.postavicka, 0, 60)
    #                 self.plocha[self.poz_y + 1][self.poz_x] = 'P'
    #                 self.poz_y += 1
    #                 self.kroky += 1
    #             elif self.plocha[self.poz_y + 1][self.poz_x] == 'K':
    #                 if self.plocha[self.poz_y + 2][self.poz_x] == 'K' or self.plocha[self.poz_y + 2][self.poz_x] == 'X':
    #                     pass
    #                 elif self.plocha[self.poz_y + 2][self.poz_x] == ' ' or self.plocha[self.poz_y + 2][self.poz_x] == 'C':
    #                     self.plocha[self.poz_y + 2][self.poz_x] = 'K'
    #                     self.plocha[self.poz_y + 1][self.poz_x] = 'P'
    #                     if (self.poz_y, self.poz_x) in self.suradnice_C:
    #                         self.plocha[self.poz_y][self.poz_x] = 'C'
    #                     else:
    #                         self.plocha[self.poz_y][self.poz_x] = ' '
    #                     self.kroky += 1
    #                 elif self.plocha[self.poz_y + 2][self.poz_x] == 'B':
    #                     self.koniec()
    #         else:
    #             pass
    #         self.canvas.update()
    #         print(self.plocha)

