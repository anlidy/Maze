import pygame
import random
from color import *

radius = 6
dx = 2
dy = 10
dsSize = (860,780)
mazeSize = (800,700)
cellSize = 34
h = 2 * radius + dy
Maze_rows = 19
Maze_cols = 23
UP,DOWN = -1,1
LEFT,RIGHT = -2,2 
MazePosx,MazePosy = (dsSize[0] // 2 - mazeSize[0] // 2 ,dsSize[1] // 2 - mazeSize[1] // 2+40)


class cell:
    def __init__(self,r,c):
        self.r = r
        self.c = c
        self.visited = False
        self.walls = {UP:False,DOWN:False,LEFT:False,RIGHT:False}
        self.ball = False
        

class Maze:
    def __init__(self,size,rows=Maze_rows,cols=Maze_cols):
        self.size = size
        self.rows = rows
        self.cols = cols
        self.maze = [[cell(r,c) for c in range(Maze_cols)] for r in range(Maze_rows)]
        self.score = 10
        self.make_maze()
        self.cage()

    def make_maze(self,r0=0,c0=0):
        direction = {UP: (-1, 0),DOWN: (1, 0),LEFT:(0, -1),RIGHT:(0, 1)}
        currentCell = self.maze[r0][c0]
        currentCell.visited = True
        visitedPath = [currentCell]
        while visitedPath:
            currentCell = visitedPath[-1]
            unvisNeighbors = []
            for d,(dr,dc) in direction.items():
                r,c = currentCell.r + dr,currentCell.c + dc
                if (0 <= r < self.rows) and (0 <= c < self.cols):
                    cell = self.maze[r][c]
                    if not cell.visited:
                        unvisNeighbors.append((d,cell))
            if unvisNeighbors:
                x,y = random.choice(unvisNeighbors)    
                visitedPath.append(y)
                currentCell.walls[x] = True
                y.visited = True
                rd = random.randint(0,100)
                if rd<5: y.ball = True
                y.walls[-x] = True
            elif len(visitedPath):
                visitedPath.pop()

    def running(self,x,y,way):
        cx = (x - MazePosx) // cellSize
        cy = (y - MazePosy) // cellSize
        if 0 <= cx < self.cols and 0 <= cy < self.rows:
            cell = self.maze[cy][cx]
            if way == 'W' and cell.walls[UP]:
                return True
            elif way == 'S' and cell.walls[DOWN]:
                return True
            elif way == 'A' and cell.walls[LEFT]:
                return True
            elif way == 'D' and cell.walls[RIGHT]:
                return True
            else:
                return False
        else: return True

    def checkBall(self,x,y):
        cx = (x - MazePosx) // cellSize
        cy = (y - MazePosy) // cellSize
        if 0 <= cx < self.cols and 0 <= cy < self.rows:
            cell = self.maze[cy][cx]
            if cell.ball:
                self.score+=1
                cell.ball=False
    
    def clash(self,x,y,way):
        if self.score < 5:return
        self.score -= 5
        cx = (x - MazePosx) // cellSize
        cy = (y - MazePosy) // cellSize
        if 0 <= cx < self.cols and 0 <= cy < self.rows:
            cell = self.maze[cy][cx]
            cell.walls[way] = True
            ncell = None
            if way==UP and cy-1>=0:
                ncell = self.maze[cy-1][cx]
            if way==DOWN and cy+1<self.cols:
                ncell = self.maze[cy+1][cx] 
            if way==LEFT and cx-1>=0:
                ncell = self.maze[cy][cx-1]
            if way==RIGHT and cx+1<self.rows:
                ncell = self.maze[cy][cx+1]
            if ncell:
                ncell.walls[-way] = True     
              
    def cage(self):
        for r,col in enumerate(self.maze):
            for c,cell in enumerate(col):
                for way in cell.walls.keys():
                    #if (r,c) in central zone
                    if 8<=r<11 and 10<=c<13:
                        cell.walls[way] = False
                        ncell = None
                        if way==UP and c-1>=0:
                            ncell = self.maze[r-1][c]
                        if way==DOWN and r+1<self.cols:
                            ncell = self.maze[r+1][c] 
                        if way==LEFT and c-1>=0:
                            ncell = self.maze[r][c-1]
                        if way==RIGHT and c+1<self.rows:
                            ncell = self.maze[r][c+1]
                        if ncell:
                            ncell.walls[-way] = False     

                

    def draw(self,ds):
        for r,col in enumerate(self.maze):
            for c,cell in enumerate(col):
                x = c * cellSize + MazePosx
                y = r * cellSize + MazePosy     
                if cell.ball:pygame.draw.circle(ds,red,(x+cellSize//2,y+cellSize//2),radius)           
                for way,iss in cell.walls.items():
                    if not iss:
                        if way == UP:
                            pygame.draw.line(ds,white,(x,y),(x+cellSize,y))
                        if way == DOWN:
                            pygame.draw.line(ds,white,(x,y+cellSize),(x+cellSize,y+cellSize))
                        if way == LEFT:
                            pygame.draw.line(ds,white,(x,y),(x,y+cellSize))
                        if way == RIGHT:
                            pygame.draw.line(ds,white,(x+cellSize,y),(x+cellSize,y+cellSize))   

        font = pygame.font.Font(None, 24)
        scoreText = f"Scores = {self.score}  ----------- Eat red balls to get scores ! ! ! Up to 5 can use 'clash' skill by pressing SPACE! ! ! "
        scoreText1 = f"Save central the XiaoRed to get win ! ! !  Come On ! ! !"
        scoreSurface = font.render(scoreText, True, white)
        scoreSurface1 = font.render(scoreText1, True, white)
        scorePos = (10, 10)
        scorePos1 = (10, 40) 
        ds.blit(scoreSurface,scorePos)
        ds.blit(scoreSurface1,scorePos1)