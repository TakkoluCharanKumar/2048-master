import os
import random
import time
import getkey

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
    def transpose(self):
        self.gridCells=[list(t) for t in zip(*self.gridCells)]
    def slide(self):
        self.slided=False
        temp=[[0]*self.n for i in range(self.n)]
        for i in range(self.n):
            count=0
            for j in range(self.n):
                if(self.gridCells[i][j]!=0):
                    temp[i][count]=self.gridCells[i][j]
                    if count!=j:
                        self.slided=True
                    count+=1
        self.gridCells=temp
    def merge(self):
        self.merged=False
        for i in range(self.n):
            for j in range(self.n-1):
                if(self.gridCells[i][j]==self.gridCells[i][j+1] and self.gridCells[i][j]!=0):
                    self.gridCells[i][j]*=2
                    self.gridCells[i][j+1]=0
                    self.score+=self.gridCells[i][j]
                    self.merged=True
    def reverse(self):
        for index in range(self.n):
            i=0
            j=self.n-1
            while(i<j):
                self.gridCells[index][i],self.gridCells[index][j]=self.gridCells[index][j],self.gridCells[index][i]
                i+=1
                j-=1
    def can_merge(self):
        for i in range(self.n):
            for j in range(self.n-1):
                if self.gridCells[i][j]==self.gridCells[i][j+1]:
                    return True
        for i in range(self.n-1):
            for j in range(self.n):
                if(self.gridCells[i+1][j]==self.gridCells[i][j]):
                    return True
        return False
    def check_status(self):
        for i in range(self.n):
            for j in range(self.n):
                if(self.gridCells[i][j]==2048):
                    return True
        return False
class Game:
    def __init__(self,inside):
        self.inside=inside
    def start(self):
        self.inside.random_cell()
        self.inside.random_cell()
        print("1-Left\n2-Right\n3-Up\n4-Down")
        self.play()
    def play(self):
        while(True):
            self.inside.slided=False
            self.inside.merged=False
            self.inside.moved=False
            os.system('clear')
            self.inside.print_grid()
            key=getkey.getkey()
            if(key=='1' or key==getkey.keys.LEFT):
                self.inside.slide()
                self.inside.merge()
                self.inside.moved=self.inside.slided or self.inside.merged
                self.inside.slide()
            elif(key=='2' or key==getkey.keys.RIGHT):
                self.inside.reverse()
                self.inside.slide()
                self.inside.merge()
                self.inside.moved=self.inside.slided or self.inside.merged
                self.inside.slide()
                self.inside.reverse()
            elif(key=='3' or key==getkey.keys.UP):
                self.inside.transpose()
                self.inside.slide()
                self.inside.merge()
                self.inside.moved=self.inside.slided or self.inside.merged
                self.inside.slide()
                self.inside.transpose()
            elif(key=='4' or key==getkey.keys.DOWN):
                self.inside.transpose()
                self.inside.reverse()
                self.inside.slide()
                self.inside.merge()
                self.inside.moved=self.inside.slided or self.inside.merged
                self.inside.slide()
                self.inside.reverse()
                self.inside.transpose()
            elif(key=='0'):
                exit(0)
            else:
                pass
            if(self.inside.check_status()==True):
                self.inside.print_grid()
                print('\033[31m'+"won")
                return
            flag=0
            for i in range(self.inside.n):
                for j in range(self.inside.n):
                    if(self.inside.gridCells[i][j]==0):
                        flag=1
                        break
            if not(flag or self.inside.can_merge()):
                print("Game Over")
                return 
            time.sleep(0.1)
            if(self.inside.moved):
                self.inside.random_cell()
n=int(input("Enter the no of the grids:"))
inside=InsideGame(n)
x=Game(inside)
x.start()