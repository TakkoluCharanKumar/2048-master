class InsideGame:
    def __init__(self,n=4):
        self.n=n
        self.gridCells=[[0]*self.n for i in range(n)]
        self.score=0
        self.moved=False
        self.slided=False
        self.merged=False