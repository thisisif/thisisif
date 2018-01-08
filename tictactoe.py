from tkinter import Frame, Canvas, Button, ALL, Tk, messagebox
import random

class TicTacToe:

    def __init__(self, master):
        self.size = 6
        self.length = 40
        self.frame = Frame(master)
        self.frame.pack()
        self.canvas = Canvas(self.frame, width=self.size * self.length, height=self.size * self.length)
        self.canvas.pack()
        self.frameb = Frame(self.frame)
        self.frameb.pack()
        self.Start = Button(self.frameb, text='Start Game', height=4, command=self.start, bg='white', fg='black')
        self.Start.pack()
        self.turn = ''
        self.player_symbol = ''
        self.computer_symbol = ''

    def starting(self):
        self.total = self.size ** 2
        if random.random() < 0.5:
            return 1
        else:
            return 0

    def start(self):
        self.canvas.delete(ALL)
        self.clicked = [['' for _ in range(self.size)] for _ in range(self.size)]
        self.playing = True
        self.board()
        if random.random() < 0.5:
            self.player_symbol = 'X'
            self.computer_symbol = 'O'
        else:
            self.player_symbol = 'O'
            self.computer_symbol = 'X'
        if self.starting():
            self.turn = 'player'
            messagebox.showinfo('Start', self.turn + ' is starting you have the ' + self.player_symbol + ' symbol')
        else:
            self.turn = 'computer'
            messagebox.showinfo('Start', self.turn + ' is starting you have the ' + self.player_symbol + ' symbol')
            self.computer_start()
        self.canvas.bind("<ButtonPress-1>", self.player)

    def board(self):
        for i in range(self.size):
            for j in range(self.size):
                self.canvas.create_rectangle(i * self.length, j * self.length, (i + 1) * self.length,
                                             (j + 1) * self.length, width=1, outline='black', fill='light yellow')

    def player(self, event):
        if self.playing:
            if self.turn == 'player':
                i = event.y // self.length
                j = event.x // self.length
                if 0 <= i < self.size and 0 <= j < self.size:
                    if self.clicked[i][j] == '':
                        if self.player_symbol == 'X':
                            self.cross(i, j)
                        else:
                            self.circle(i, j)

                        self.clicked[i][j] = self.player_symbol
                        self.total -= 1

                        if self.check_left():
                            self.turn = 'computer'

                            if self.check_win(self.player_symbol):
                                self.playing = False
                                messagebox.showinfo('Victory', 'You Won!!')

                            if self.playing:
                                if self.total >= 1:
                                    self.computer_move()
                        else:
                            messagebox.showinfo('Draw', 'Nobody Wins!!')
                        print(self.clicked)

    def computer_move(self):
        i = j = 0
        while self.clicked[i][j] != '':
            i = random.randint(0, self.size - 1)
            j = random.randint(0, self.size - 1)

        if self.computer_symbol == 'X':
            self.cross(i, j)
        else:
            self.circle(i, j)

        self.clicked[i][j] = self.computer_symbol
        self.total -= 1
        if self.check_left():
            self.turn = 'player'
            if self.check_win(self.computer_symbol):
                self.playing = False
                messagebox.showinfo('Loss', 'You Lose!!')
        else:
            messagebox.showinfo('Draw', 'Nobody Wins!!')

    def computer_start(self):
        middle = (self.size // 2)

        if self.computer_symbol == 'X':
            self.cross(middle, middle)
        else:
            self.circle(middle, middle)

        self.clicked[middle][middle] = self.computer_symbol
        self.total -= 1
        self.turn = 'player'

    def circle(self, x, y):
        self.canvas.create_oval(y * self.length + 5, x * self.length + 5,
                                (y + 1) * self.length - 5, (x + 1) * self.length - 5, width=5, outline='red')

    def cross(self, x, y):
        self.canvas.create_line([(y * self.length) + (self.length // 2), (x * self.length) + (self.length // 2),
                                    ((y + 1) * self.length) - 5, (x * self.length) + 5,
                                    (y * self.length) + 5, ((x + 1) * self.length) - 5,
                                    (y * self.length) + (self.length // 2), (x * self.length) + (self.length // 2),
                                    ((y + 1) * self.length) - 5, ((x + 1) * self.length) - 5,
                                    (y * self.length) + 5, (x * self.length) + 5], width=5, fill='blue')

    def check_left(self):
        if self.total == 0:
            self.playing = False
        return self.total

    def check_win(self, symbol):
        for i in range(self.size):
            count = 0
            for j in range(self.size):
                if self.clicked[i][j] == symbol:
                    count += 1
                if count == self.size:
                    return True

        for j in range(self.size):
            count = 0
            for i in range(self.size):
                if self.clicked[i][j] == symbol:
                    count += 1
                if count == self.size:
                    return True

        count = 0
        for i in range(self.size):
            if self.clicked[i][i] == symbol:
                count += 1
            if count == self.size:
                return True

        count = 0
        for i in range(self.size):
            if self.clicked[i][self.size - 1 - i] == symbol:
                count += 1
            if count == self.size:
                return True

root = Tk()
root.title('Tic Tac Toe')
app = TicTacToe(root)
root.mainloop()