import pygame
import sys
import map, GhostYellow, GhostCyan, GhostWhite, GhostMagenta
from class_work import white_square
from PacmanSounds import Sounds

size = width, height = 800, 600
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0

field_width = 28
field_height = 31
field_pixel_size = 21

class PyGameObject:
    def __init__(self, x, y, s, m):
        self.x = x
        self.y = y
        self.s = s
        self.m = m
        self.r = 1
        self.color = (255, 255, 255)
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.s, self.m), 5)
    
    def update(self):
        self.s += self.r
        self.m += self.r
        if self.s > 100:
            self.r *= -1
        elif self.s < -100:
            self.r *= -1
            

class Program:
    def main(self):
        pygame.init()
        screen = pygame.display.set_mode(size)
        gameover = False
        platform = PyGameObject(400, 300, 50 ,50)
        moveSpeed = 0

        field = map.Map()
        field.load()
        ghost_sound = Sounds(0.3)
        ghost_sound.music_start()

        #ghosts created & added the ghost-list
        ghosts = []
        ghost_spawn_point = (field_width * field_pixel_size, field_height * field_pixel_size)
        ghosts.append(GhostCyan.GhostCyan(ghost_spawn_point))
        ghosts.append(GhostMagenta.GhostMagenta(ghost_spawn_point))
        ghosts.append(GhostYellow.GhostYellow(ghost_spawn_point))
        ghosts.append(GhostWhite.GhostWhite(ghost_spawn_point))

        square = white_square(3)
        square_movement = [0, 0]

        while not gameover:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameover = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        square_movement[0] = 1
                    if event.key == pygame.K_LEFT:
                        square_movement[0] = -1
                    if event.key == pygame.K_UP:
                        square_movement[1] = -1
                    if event.key == pygame.K_DOWN:
                        square_movement[1] = +1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        square_movement[0] = 0
                    if event.key == pygame.K_LEFT:
                        square_movement[0] = 0
                    if event.key == pygame.K_UP:
                        square_movement[1] = 0
                    if event.key == pygame.K_DOWN:
                        square_movement[1] = 0

            for ghost in ghosts:
                ghost.update()

            square.move(square_movement)

            for ghost in ghosts:
                if (ghost.collided(square)):
                    ghost_sound.sound_col()
                    square.move_to_start()
                    square.died()



            screen.fill(black)
            field.screen_draw(screen)

            for ghost in ghosts:
                ghost.draw(screen)

            square.draw(screen)

            pygame.display.flip()
            pygame.time.wait(5)
        sys.exit()


if __name__ == "__main__":
    Program().main()
