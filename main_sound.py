from map import Map
from PacmanSounds import Sounds
import pygame

size = width, height = 600, 800
BLACK = 0, 0, 0
field = Map()
field.load()
pygame.init()
screen = pygame.display.set_mode(size)
music1 = Sounds(0.3)
music_on = 0

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
            elif event.key == pygame.K_RIGHT:
                print("right")
            elif event.key == pygame.K_UP:
                print("up")
            elif event.key == pygame.K_DOWN:
                print("down")
            elif event.key == pygame.K_SPACE:
                if music_on == 0:
                    music1.music_start()
                    music_on = 1
                else:
                    music1.music_stop()
                    music_on = 0
            elif event.key == pygame.K_ESCAPE:
                print("escape") 
    screen.fill(BLACK)
    field.screen_draw(screen)
    pygame.display.flip()
pygame.quit()