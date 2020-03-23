import pygame

pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width, height))

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255

x = 0
y = 0

moveX = 0
moveY = 0

bgImg = pygame.image.load("img_1.jpg")

img = pygame.Surface((50,50))
img.fill(white)
img_w = img.get_width()
img_h = img.get_height()
rect = img.get_rect()
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0

        elif event.type == pygame.KEYUP:
            moveX = 0
            moveY = 0

    # screen.fill(white)
    screen.blit(bgImg, (0,0))
    screen.blit(img, (x,y))

    x += moveX
    y += moveY

    if x > width - img_w:
        moveX = -1
    elif x < 0:
        moveX = 1
    elif y > height - img_h:
        moveY = -1
    elif y < 0:
        moveY = 1

    pygame.display.update()
