import pygame
import sys
import character
import MazeGenerator
from color import *


dsSize = (860,780)
mazeSize = (800,700)
cellSize = 34
radius = 6
dx = 2
dy = 10
UP,DOWN = -1,1
LEFT,RIGHT = -2,2 
h = 2 * radius + dy
MazePosx,MazePosy = (dsSize[0] // 2 - mazeSize[0] // 2 ,dsSize[1] // 2 - mazeSize[1] // 2 + 40)
initPos = (MazePosx+cellSize//2,MazePosy+(cellSize-h)//2+radius)
centre = (9,11) 
pygame.init()
ds = pygame.display.set_mode(dsSize)
pygame.display.set_caption('maze')

clock = pygame.time.Clock()
#clock.tick(60)

maze = MazeGenerator.Maze(mazeSize)
hero = character.Character(initPos[0],initPos[1],white)

XiaoRed = character.Character(centre[1]*cellSize+MazePosx+cellSize//2,centre[0]*cellSize+MazePosy+(cellSize-h)//2+radius,red)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            if  maze.running(hero.x,hero.y,'W'):
                hero.move('W')
                maze.checkBall(hero.x,hero.y)
            else: 
                if keys[pygame.K_SPACE]:
                    maze.clash(hero.x,hero.y,UP)    
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            if  maze.running(hero.x,hero.y,'A'):
                hero.move('A')
                maze.checkBall(hero.x,hero.y)
            else: 
                if keys[pygame.K_SPACE]:
                    maze.clash(hero.x,hero.y,LEFT)    
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            if  maze.running(hero.x,hero.y,'S'):
                hero.move('S')
                maze.checkBall(hero.x,hero.y)
            else: 
                if keys[pygame.K_SPACE]:
                    maze.clash(hero.x,hero.y,DOWN)    
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            if  maze.running(hero.x,hero.y,'D'):
                hero.move('D')
                maze.checkBall(hero.x,hero.y)
            else: 
                if keys[pygame.K_SPACE]:
                    maze.clash(hero.x,hero.y,RIGHT)    
    
    ds.fill(black)
    maze.draw(ds)
    hero.draw(ds)
    XiaoRed.draw(ds)
    
    pygame.display.flip()     

    clock.tick(60)

    