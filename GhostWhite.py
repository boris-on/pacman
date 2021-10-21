import pygame
from random import choice
import Ghost


class GhostWhite(Ghost.Ghost):
    def __init__(self, screen_size):
        super().__init__()
        self.image = pygame.image.load("Pics/Ghost_white.png")
        self.rect = self.image.get_rect()
        self.rect.x = screen_size[0] // 2 + self.image.get_width() // 2
        self.rect.y = screen_size[1] // 2 - self.image.get_height() // 2
        self.speed = 1
        self.startx = self.rect.x
        self.starty = self.rect.y
        self.lives = 1
        self.y_val = 0
        self.x_val = 1

    def update(self):
        # self.x_val = randint(-self.speed, self.speed)
        # self.y_val = randint(-self.speed, self.speed)

        self.rect.x += self.x_val
        self.rect.y += self.y_val
        if self.lives == 1:
            if self.x_val > 0:
                self.image = pygame.image.load("Pics//Ghost_white//r.png")
            if self.x_val < 0:
                self.image = pygame.image.load("Pics//Ghost_white//l.png")
            if self.y_val > 0:
                self.image = pygame.image.load("Pics//Ghost_white//u.png")
            if self.y_val < 0:
                self.image = pygame.image.load("Pics//Ghost_white//d.png")
        # print(self.x_val)

    def check_Wall(self):
        self.rect.x -= self.x_val
        self.rect.y -= self.y_val
        if self.x_val == 0:

            # self.y_val = choice([-1, 0, 1])
            self.y_val = 0
            if self.y_val == 0:
                self.x_val = choice([-1, 1])
        else:
            # self.x_val = choice([-1, 0, 1])
            self.x_val = 0
            if self.x_val == 0:
                self.y_val = choice([-1, 1])
