
from GUI import *
import pygame

size = width, height = 800, 800
BLACK = 0, 0, 0
pygame.init()

screen = pygame.display.set_mode(size)
gui = GUI(800,800)
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
                gui.on_left_mouse()
    screen.fill(BLACK)
    gui.draw(screen)
    pygame.display.flip()
quit()
