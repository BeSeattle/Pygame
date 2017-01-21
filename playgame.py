# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pygame
from pygame.locals import *
  
# 2 - Initialize the game
pygame.init()
pygame.display.set_caption('小兔子大战')
size = width,height = 1000,600
screen=pygame.display.set_mode(size)`
coordinate = coordinate_x,coordinate_y = 100,100

# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
grass = pygame.image.load("resources/images/grass.png")
castle = pygame.image.load("resources/images/castle.png")

# 4 - keep looping through,这样才能保持兔子窗口一直显示
for game in range(1,50):
    # 5 - clear the screen before drawing it again
    screen.fill(0)

    # 6 - draw the screen elements,(**,**)代表的是元素的坐标
    for x in range(int(width/grass.get_width())+1):
        for y in range(int(height/grass.get_height())+1):
            screen.blit(grass, (x*100, y*100))

    screen.blit(castle, (0, 30))
    screen.blit(castle, (0, 135))
    screen.blit(castle, (0, 240))
    screen.blit(castle, (0, 345))
    screen.blit(castle, (0, 450))
    screen.blit(player, (coordinate))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit()
