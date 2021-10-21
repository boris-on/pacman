import pygame

class white_square:
    def __init__(self, lives):
        self.lives = lives
        self.rect = pygame.Rect(30, 30, 30, 30)
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 255, 255))
        self.alive = True

    def draw(self, screen):
        if self.alive:
            screen.blit(self.surf, self.rect)

    def move(self, movement):
        self.rect.x += movement[0]
        self.rect.y += movement[1]

    def move_to_start(self):
        self.rect.x = 30
        self.rect.y = 30

    def died(self):
        self.lives -= 1
        if self.lives <= 0:
            self.alive = False