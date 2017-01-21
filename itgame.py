# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pygame
from pygame.locals import *
  
# 2 - Initialize the game
pygame.init()
pygame.display.set_caption('小兔子大战')
width,height = 640,480
screen=pygame.display.set_mode((width, height))
  
# 3 - Load images
player = pygame.image.load("resources/images/dude.png")
  
# 4 - keep looping through
running = 1
while running:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw the screen elements
    screen.blit(player, (100,100))
    # 7 - update the screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit() 
            exit(0)
