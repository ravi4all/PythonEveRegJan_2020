import pygame

pygame.init()

width = 1000
height = 400

screen = pygame.display.set_mode((width, height))

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255

x = 0
y = -50
moveX = 0

bgImg = pygame.image.load("world_1.png")
orig_w = bgImg.get_width()
orig_h = bgImg.get_height()
bgImg = pygame.transform.scale(bgImg,(orig_w*2, orig_h*2))

img = pygame.Surface((50,50))
img.fill(white)
rect = img.get_rect()
rect_x = 100
rect_y = height - 100
moveRect = True
moveRectX = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print(moveRectX, moveRect)
                if not moveRect:
                    moveRectX = 0
                    moveX = -1
                elif moveRect:
                    moveRectX = 1
            elif event.key == pygame.K_LEFT:
                moveX = 1

        elif event.type == pygame.KEYUP:
            moveX = 0
            moveRectX = 0

    screen.fill(white)
    screen.blit(bgImg, (x,y))
    screen.blit(img,(rect_x,rect_y))

    x += moveX
    rect_x += moveRectX

    if rect_x > 300:
        moveRect = False

    pygame.display.update()
