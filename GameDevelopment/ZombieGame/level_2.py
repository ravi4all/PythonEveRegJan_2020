import pygame
from pygame.locals import *
import random, os
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

black = 0,0,0
white = 255,255,255
red = 255,0,0
blue = 0,0,255
yellow = 0,255,255

pygame.time.set_timer(USEREVENT,1000)

bgMusic = pygame.mixer.Sound('sounds/background.wav')
bgMusic.play()

def homeLevel_2():
    # pygame.mixer.music.load('sounds/background.wav')
    # pygame.mixer.music.play()
    bg = pygame.image.load("images/bg_main.jpg")
    bg = pygame.transform.scale(bg, (width, height))
    msg_1 = "Press SPACE to start Level 2"
    font = pygame.font.SysFont(None, 50)
    # font = pygame.font.Font('font_1.ttf', 50)
    text_1 = font.render(msg_1, True, white)
    msg_2 = "Level 2 Unlocked"
    text_2 = font.render(msg_2, True, white)
    msg_3 = "Press Q to Quit"
    text_3 = font.render(msg_3, True, white)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stageOne()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        screen.blit(bg, (0,0))
        screen.blit(text_1, (50,400))
        screen.blit(text_2, (300,200))
        screen.blit(text_3, (600, 400))
        pygame.display.update()

def stageOne():
    seconds = 0
    msg_1 = "Level 2"
    font = pygame.font.SysFont(None, 50)
    text_1 = font.render(msg_1, True, white)
    msg_2 = "Kill 20 zombies in 20 seconds"
    text_2 = font.render(msg_2, True, white)
    msg_3 = "to Unlock Level 3"
    text_3 = font.render(msg_3, True, white)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.USEREVENT:
                seconds += 1

        if seconds >= 5:
            main()

        screen.fill(black)
        screen.blit(text_1, (300, 100))
        screen.blit(text_2, (150, 200))
        screen.blit(text_3, (200, 250))
        pygame.display.update()

def gameOver():
    pass

def score(counter):
    msg = "Score : {}".format(counter)
    font = pygame.font.SysFont(None, 30)
    text = font.render(msg,True,yellow)
    screen.blit(text, (5,5))

def timer(seconds):
    msg = "Time Left : {}".format(seconds)
    font = pygame.font.SysFont(None, 30)
    text = font.render(msg, True, yellow)
    screen.blit(text, (200, 5))

def main():
    bgImg = pygame.image.load("images/background.png")

    aim = pygame.image.load("images/aim_pointer.png")
    aim_w = aim.get_width()
    aim_h = aim.get_height()

    zombie_path = 'zombie_images'
    zombie_dir = os.listdir(zombie_path)
    zombie_list = []
    for i in range(len(zombie_dir)):
        img = pygame.image.load(zombie_path+"/"+zombie_dir[i])
        zombie_list.append(img)

    zombieImage = random.choice(zombie_list)
    zombie_w = zombieImage.get_width()
    zombie_h = zombieImage.get_height()
    zombieX = random.randint(0,width - zombie_w)
    zombieY = random.randint(0,height - zombie_h)

    gunImg = pygame.image.load("images/gun_1.png")
    gun_w = gunImg.get_width()
    gun_h = gunImg.get_height()
    gunY = height -  gun_h

    gunshotSound = pygame.mixer.Sound('sounds/shot_sound.wav')
    zombieShotSound = pygame.mixer.Sound('sounds/zombie_shot.wav')

    counter = 0
    seconds = 30

    shotCount = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == USEREVENT:
                seconds -= 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                gunshotSound.play()
                if zombie_rect.colliderect(aim_rect):
                    shotCount += 1
                    zombieImage = pygame.transform.scale(zombieImage, (zombie_w//2,zombie_w//2))
                    zombieShotSound.play()
                    if shotCount == 3:
                        zombieImage = random.choice(zombie_list)
                        zombie_w = zombieImage.get_width()
                        zombie_h = zombieImage.get_height()
                        zombieX = random.randint(0, width - zombie_w)
                        zombieY = random.randint(0, height - zombie_h)
                        counter += 1
                        shotCount = 0

        aim_x,aim_y = pygame.mouse.get_pos()
        aim_x = aim_x - aim_w/2
        aim_y = aim_y - aim_h/2
        aim_rect = pygame.Rect(aim_x,aim_y,aim_w,aim_h)
        zombie_rect = pygame.Rect(zombieX, zombieY, zombie_w, zombie_h)
        # screen.fill(white)
        screen.blit(bgImg, (0,0))
        gunX,_ = pygame.mouse.get_pos()

        screen.blit(zombieImage, (zombieX, zombieY))
        screen.blit(aim, (aim_x,aim_y))
        screen.blit(gunImg, (gunX,gunY))

        # pygame.draw.rect(screen,red,aim_rect)
        # pygame.draw.rect(screen, red, zombie_rect)

        score(counter)
        timer(seconds)

        pygame.display.update()

# main()
homeLevel_2()