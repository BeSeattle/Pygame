# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys, pygame
pygame.init()

size = width, height = 600, 540
speed = [2, 2]
background = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("resources/images/dude.png")
ballrect = ball.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
        	sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(background)
    screen.blit(ball, ballrect)
    pygame.display.flip()