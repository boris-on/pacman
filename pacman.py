
import map

import pygame
import time



class Pacman():
    image = pygame.image.load('images//o.png')
    moveX, moveY = 0, 0
    r = True
    def __init__(self, x, y):
        self.rect = self.image.get_rect()
        self.rect.x = x + map.Map.pixel_size // 2 - self.rect.width // 2
        self.rect.y = y + map.Map.pixel_size // 2 - self.rect.height // 2
        self.startx = self.rect.x
        self.starty = self.rect.y
        self.directionX = 0
        self.directionY = 0
        self.speed = 1
        self.wallx = 0
        self.wally = 0
        self.death = False
        self.lives = 3
        self.direction = 'r'
        self.state = 1
        self.drug = False
        self.ficha = True

    def process_draw(self, screen):
        screen.blit(self.image, self.rect)

    def key_up(self):
        self.directionY = -self.speed
        self.directionX = 0
        self.direction = 'u'

    def key_right(self):
        self.directionX = self.speed
        self.directionY = 0
        self.direction = 'r'

    def key_left(self):
               
        self.directionX = -self.speed
        self.directionY = 0
        self.direction = 'l'

    def key_down(self):
        self.directionY = self.speed
        self.directionX = 0
        self.direction = 'd'

    def god_mode(self):
        self.drug = True
        self.god_start = time.time()
        print("God Mode ON")

    def check_Wall(self):
        self.rect.x -= self.directionX
        self.rect.y -= self.directionY
        self.directionX = 0
        self.directionY = 0

    def update(self):
        # print("images//pacman//{}//{}.png".format(self.direction, self.state))
        self.image = pygame.image.load("images//pacman//{}//{}.png".format(self.direction, self.state))
        self.state += 1
        self.state %= 3 + 1
        if self.state ==0:
            self.state=1
        self.wallx = field.width * field.pixel_size
        self.wally = field.height * field.pixel_size

        if self.rect.x > self.wallx + field.width:
            self.rect.x = 4
        if self.rect.x < -2 - field.width:
            self.rect.x = 586
        if self.rect.y > 702:
            self.rect.y = 4
        if self.rect.y < -2 - field.height:
            self.rect.y = 702

        self.rect.x += self.directionX
        self.rect.y += self.directionY
        pygame.time.delay(10)
        if self.drug and time.time() - self.god_start > 7:
            self.drug = False
            print("God Mode OFF")

    def check_Ghost(self):
        # print("столкновение с гостом")
        sound.sound_col()
        # self.speed = 0
        self.directionX = 0
        self.directionY = 0
        pygame.time.delay(1000)
        self.death = True
        self.lives -= 1

    def respawn(self):
        self.rect.x = self.startx
        self.rect.y = self.starty
        self.death =  False
