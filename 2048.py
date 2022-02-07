class InsideGame:
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