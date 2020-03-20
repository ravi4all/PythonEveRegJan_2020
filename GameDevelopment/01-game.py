import pygame

pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

black = 0,0,0
white = 255,255,255
red = 255,0,0
blue = 0,0,255

screen.fill(white)
pygame.display.update()