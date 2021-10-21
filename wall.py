import pygame

class Wall:


    def __init__(self, x, y, type_wall):
        self.image = pygame.image.load('images//walls//{}.png'.format(type_wall))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def process_draw(self, screen):
        screen.blit(self.image, self.rect)

