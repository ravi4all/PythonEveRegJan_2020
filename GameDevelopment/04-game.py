import pygame

pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

black = 0,0,0
white = 255,255,255
red = 255,0,0
blue = 0,0,255

x = 0
y = 0
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    pygame.draw.rect(screen,red,[x,y,50,50])
    x += 1
    pygame.display.update()
