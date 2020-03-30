import pygame
import random

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

img = pygame.Surface((50,50))
img.fill(black)
img_w = img.get_width()
img_h = img.get_height()
rect = img.get_rect()

frogImg = pygame.image.load("frog.png")
frog_w = frogImg.get_width()
frog_h = frogImg.get_height()

frogX = random.randint(0, width - frog_w)
frogY = random.randint(0, height - frog_h)

snakeList = []
snakeLength = 1

def snake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(screen,black, [snakeList[i][0],
                         snakeList[i][1], img_w,img_h])

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

    screen.fill(white)
    screen.blit(img, (x,y))
    screen.blit(frogImg, (frogX,frogY))

    frogRect = pygame.Rect(frogX,frogY,frog_w,frog_h)
    snakeRect = pygame.Rect(x,y,img_w,img_h)

    x += moveX
    y += moveY

    snakeHead = []
    snakeHead.append(x)
    snakeHead.append(y)

    snakeList.append(snakeHead)

    if len(snakeList) > snakeLength:
        del snakeList[0]

    print(snakeList)
    snake(snakeList)

    if x > width:
        x = -img_w
    elif x < -img_w:
        x = width
    elif y > height:
        y = -img_h
    elif y < -img_h:
        y = height

    if frogRect.colliderect(snakeRect):
        frogX = random.randint(0, width - frog_w)
        frogY = random.randint(0, height - frog_h)
        snakeLength += 10

    pygame.display.update()
