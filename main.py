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

class StartMenu:
    def __init__(self, screen):
        self.screen = screen
        self.is_active = True
        # 使用支持中文的字体，这里使用微软雅黑
        try:
            self.font_big = pygame.font.Font("msyh.ttc", 74)  # 首选微软雅黑
            self.font_small = pygame.font.Font("msyh.ttc", 50)
        except:
            try:
                self.font_big = pygame.font.Font("simhei.ttf", 74)  # 备选黑体
                self.font_small = pygame.font.Font("simhei.ttf", 50)
            except:
                # 如果都找不到，使用系统默认字体
                self.font_big = pygame.font.SysFont("microsoft yahei", 74)
                self.font_small = pygame.font.SysFont("microsoft yahei", 50)
        
        self.title = self.font_big.render("迷宫冒险", True, white)
        self.start_text = self.font_small.render("按空格键开始游戏", True, white)
        self.quit_text = self.font_small.render("按 Q 退出游戏", True, white)
        
    def draw(self):
        self.screen.fill(black)
        # 绘制标题
        title_pos = (dsSize[0]//2 - self.title.get_width()//2, dsSize[1]//3)
        self.screen.blit(self.title, title_pos)
        # 绘制开始提示
        start_pos = (dsSize[0]//2 - self.start_text.get_width()//2, dsSize[1]//2)
        self.screen.blit(self.start_text, start_pos)
        # 绘制退出提示
        quit_pos = (dsSize[0]//2 - self.quit_text.get_width()//2, dsSize[1]//2 + 60)
        self.screen.blit(self.quit_text, quit_pos)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return "start"
                if event.key == pygame.K_q:
                    return "quit"
        return None

def main():
    pygame.init()
    ds = pygame.display.set_mode(dsSize)
    pygame.display.set_caption('迷宫冒险')
    clock = pygame.time.Clock()
    
    # 游戏状态
    game_state = "menu"
    start_menu = StartMenu(ds)
    
    # 初始化游戏对象
    maze = MazeGenerator.Maze(mazeSize)
    hero = character.Character(initPos[0], initPos[1], white)
    XiaoRed = character.Character(centre[1]*cellSize+MazePosx+cellSize//2,
                                centre[0]*cellSize+MazePosy+(cellSize-h)//2+radius, red)

    while True:
        if game_state == "menu":
            action = start_menu.handle_events()
            if action == "quit":
                sys.exit()
            elif action == "start":
                game_state = "playing"
            start_menu.draw()
            
        elif game_state == "playing":
            # 原来的游戏循环代码
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
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
            XiaoRed.draw(ds)
            hero.draw(ds)
            
            if hero.x == XiaoRed.x and hero.y == XiaoRed.y:
                ds.fill(white)
                font = pygame.font.Font(None, 50)
                text = "You win ! ! !"
                pos = (XiaoRed.x-100, XiaoRed.y-100)
                sur = font.render(text, True, red)
                ds.blit(sur, pos)
                
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()

    