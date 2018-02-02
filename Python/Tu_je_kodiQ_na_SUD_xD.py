class Sudoku:
    def __init__(self, meno_suboru):
        self.pocet = 0
        self.tab = [[] for x in range(9)]
        riadky = []
        with open(meno_suboru, 'r') as subor:
            riadky += subor.read().split('\n')
        for i in range(len(riadky)):
            for j in range(len(riadky[i])):
                if riadky[i][j] != ' ':
                    self.tab[i].append(riadky[i][j])


    def __str__(self):
        rep = ''
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                rep = rep + str(self.tab[i][j] + ' ')
            rep = rep[:-1] + '\n'
        return rep

    def urob(self):
        sets = [{} for _ in range(81)]
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                if self.tab[i][j] == '.':
                    print(sets[i][j])

    def nahrad(self):
        pass

    def ries(self):
        pass

sud = Sudoku('subor1.txt')
# print(sud)

sud.urob()
