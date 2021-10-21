from random import randint
import pygame


class Ghost:
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.rect = self.image.get_rect()
        self.speed = 1
        self.startx = 0
        self.starty = 0

    def random_move(self):
        self.rect.x += randint(-self.speed, self.speed)
        self.rect.y += randint(-self.speed, self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def set_speed(self, new_speed):
        self.speed = new_speed

    def update(self):
        self.random_move()

    def collided(self, other):
        if self.rect.colliderect(other.rect):
            return True

    def respawn(self):
        self.rect.x = self.startx
        self.rect.y = self.starty