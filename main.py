import minimax

symbols = ["X", "O"]
class Game:
    def __init__(self, size):
        self.field = [[None  for i in range(size)] for j in range(size)]
        self.player = False
        self.size = size
    def move(self, x,y):
        if self.field[y][x] is not None:
            return False
        self.field[y][x] = self.player
        self.player = not self.player
        return True
    def possibile_moves(self):
        l = []
        
        for y in range(game.size):
            for x in range(game.size):
                if self.field[y][x] is None:
                    l.append((x,y))
        return l
    def result(self):
        for row in self.field:
            p = row[0]
            for e in row[1:]:
                if e != p:
                    p = None
                    break
            if p is not None:
                return p
        for x in range(len(self.field)):
            p = self.field[0][x]
            for y in range(1,len(self.field)):
                if self.field[y][x] != p:
                    p = None
                    break
            if p is not None:
                return p
        p0 = self.field[0][0]
        p1 = self.field[0][-1]
        for x in range(1,len(self.field)):
            if self.field[x][x] != p0:
                p0 = None
            if self.field[x][len(self.field)-1-x] != p1:
                p1 = None
        if p0 is not None:
            return p0
        if p1 is not None:
            return p1
        if len(self.possibile_moves()) == 0:
            return 0
        else:
            return None
    def clone(self):
        g = Game(0)
        g.field = [i[:] for i in self.field]
        g.player = self.player
        return g


if __name__ == '__main__':
    game = Game(9)
    #game.field = [
    #    [False, False, None],
    #    [True, False, True],
    #    [True, None, True],
    #]
    #game.result()1
    while True:
        #v, m = minimax.opt(game, 8, game.player)
        #x,y = m
        if not game.player or True:
            v, m = minimax.opt(game, 4, game.player)
            x,y = m
        else:
            x, y = input().split(" ")
            x, y = int(x), int(y)
        game.move(x,y)
        for r in game.field:
            s = ""
            for e in r:
                c = "#" if e is None else symbols[int(e)]
                s += c + " "
            print(s)
        g = game.result()
        print(g)
        if g is not None:
            exit()
        print("")