import pygame
import random, os
pygame.init()

width = 1000
height = 500

screen = pygame.display.set_mode((width,height))

black = 0,0,0
white = 255,255,255
red = 255,0,0
blue = 0,0,255

def homeScreeen():
    pass

def gameOver():
    pass

def score():
    pass

def timer():
    pass

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

    gunImg = pygame.image.load("images/gun.png")
    gun_w = gunImg.get_width()
    gun_h = gunImg.get_height()
    gunY = height -  gun_h

    gunshotSound = pygame.mixer.Sound('sounds/gunShot.wav')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                gunshotSound.play()
                if zombie_rect.colliderect(aim_rect):
                    zombieImage = random.choice(zombie_list)
                    zombie_w = zombieImage.get_width()
                    zombie_h = zombieImage.get_height()
                    zombieX = random.randint(0, width - zombie_w)
                    zombieY = random.randint(0, height - zombie_h)

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

        pygame.display.update()

main()