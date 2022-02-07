class InsideGame:
    bg_color={
        '0':'\033[40m',
        '2': '\033[41m',
        '4': '\033[42m',
        '8': '\033[43m',
        '16': '\033[44m',
        '32': '\033[45m',
        '64': '\033[46m',
        '128': '\033[47m',
        '256': '\033[100m',
        '512': '\033[101m',
        '1024': '\033[102m',
        '2048': '\033[103m',
    }
    color={
        '0':'\033[97m',
        '2': '\033[97m',
        '4': '\033[97m',
        '8': '\033[30m',
        '16': '\033[97m',
        '32': '\033[97m',
        '64': '\033[97m',
        '128': '\033[30m',
        '256': '\033[97m',
        '512': '\033[37m',
        '1024': '\033[30m',
        '2048': '\033[30m',
        'ENDC' : '\033[0m',
    }
    def __init__(self,n=4):
        self.n=n
        self.gridCells=[[0]*self.n for i in range(n)]
        self.score=0
        self.moved=False
        self.slided=False
        self.merged=False
    def random_cell(self):
        cells=[]
        for i in range(self.n):
            for j in range(self.n):
                if(self.gridCells[i][j]==0):
                    cells.append((i,j))
        curr=random.choice(cells)
        self.gridCells[curr[0]][curr[1]]=random.choice([2,2,2,2,2,2,2,2,4])
    def print_grid(self):
        for i in range(self.n):
            for j in range(self.n):
                bg=self.bg_color.get(str(self.gridCells[i][j]))
                fg=self.color.get(str(self.gridCells[i][j]))
                x=" "*(5-len(str(self.gridCells[i][j])))+str(self.gridCells[i][j])+" "
                print(bg+fg+x+'\033[0m',end=" ")
            print()
            print()