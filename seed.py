import pygame
import map

class Seed:
    image = pygame.image.load('images//big.png')

    def __init__(self, x, y):
        self.rect = self.image.get_rect()
        self.rect.x = x+map.Map.pixel_size//2-self.rect.width //2
        self.rect.y = y+map.Map.pixel_size//2-self.rect.height //2

    def process_draw(self, screen):
        screen.blit(self.image, self.rect)
