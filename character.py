import pygame
from color import *

radius = 6
dx = 2
dy = 10
cellSize = 34

class Character:
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
       
    def draw(self,ds):
        pygame.draw.circle(ds,self.color,(self.x,self.y),radius)    
        pygame.draw.polygon(ds,self.color,[(self.x-radius,self.y+radius+dx),(self.x+radius,self.y+radius+dx),(self.x,self.y+radius+dy)])
        #print((self.x,self.y))

         
        
    def move(self,way):
        if way == 'A':self.x -= cellSize
        elif way == 'D':self.x += cellSize
        elif way == 'W':self.y -= cellSize
        elif way == 'S': self.y += cellSize
        else: pass

        