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

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # surface, color, [x,y,w,h]
    pygame.draw.rect(screen,red,[0,0,50,50])
    pygame.draw.circle(screen,red,[120,120],50)
    pygame.display.update()
