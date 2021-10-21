import map
import pacman
from GUI import GUI
import pygame
from PacmanSounds import Sounds

size = width, height = 600, 800
BLACK = 0, 0, 0

pygame.init()
screen = pygame.display.set_mode(size)
gui = GUI(width, height)
field = map.Map()
field.load()
field.gui = gui
pacman.field = field



ghost_sound = Sounds(0.3)
ghost_sound.music_start()
pacman.sound = ghost_sound

map.field = field
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                field.pacman.key_left()
            if event.key == pygame.K_RIGHT:
                field.pacman.key_right()
            if event.key == pygame.K_UP:
                field.pacman.key_up()
            if event.key == pygame.K_DOWN:
                field.pacman.key_down()
            if event.key == pygame.K_SPACE:
                print("space")
            if event.key == pygame.K_ESCAPE:
                print("escape")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gui.on_left_mouse()
    screen.fill(BLACK)
    gui.draw(screen)
    if gui.go:
        field.screen_draw(screen)
    pygame.display.flip()
    if field.pacman.death and field.pacman.lives == 0:
        game_over = True
        # with open("scores.txt", "a") as file:
        #     file.write(f' {str(gui.score)}')
    if field.pacman.death and field.pacman.lives > 0:
        field.pacman.respawn()
        for ghost in field.ghosts:
            ghost.respawn()
        gui.lives -= 1
    if gui.game_over:
        game_over = True
pygame.quit()