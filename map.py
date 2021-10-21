from wall import Wall
from space import Space
from seed import Seed
from food import Food
from pygame.surface import Surface
from pacman import Pacman
from GhostCyan import GhostCyan
from GhostMagenta import GhostMagenta
from GhostYellow import GhostYellow
from GhostWhite import GhostWhite
import GUI
import time


class Map:
    width, height, pixel_size = 28, 31, 21


    def __init__(self, height=height, width=width):
        self.field = [[] for i in range(height)]
        for i in range(height):
            self.field[i] = [0] * width
    def load(self, height=height, width=width, pixel_size=pixel_size):
        self.ghosts = []
        with open("concept.txt", 'r') as file:
            for i in range(height):
                line = file.readline().split()
                for j in range(width):
                    if line[j] == '.':
                        self.field[i][j] = Space(pixel_size * j, pixel_size * i+50)

                    if line[j].isnumeric():
                        self.field[i][j] = Wall(pixel_size * j, pixel_size * i+50, int(line[j]))

                    if line[j] == "+":
                        self.field[i][j] = Food(pixel_size * j, pixel_size * i+50) #small seed
                    if line[j] == "x":
                        self.field[i][j] = Seed(pixel_size * j, pixel_size * i+50) #big seed
                    if line[j] == "p":
                        self.pacman = Pacman(pixel_size * j, pixel_size * i+50)
                        self.field[i][j] = Space(pixel_size * j, pixel_size * i+50)
                    if line[j] == "g1":
                        self.ghostcyan = GhostCyan((0,0))
                        self.ghostcyan.rect.x = pixel_size * j
                        self.ghostcyan.rect.y = pixel_size * i+50
                        self.ghostcyan.startx = pixel_size * j
                        self.ghostcyan.starty = pixel_size * i+50

                        self.ghostcyan.pixel_size = self.pixel_size
                        self.field[i][j] = Space(pixel_size * j, pixel_size * i+50)
                        self.ghosts.append(self.ghostcyan)
                    if line[j] == "g2":
                        self.ghostmagenta = GhostMagenta((0,0))
                        self.ghostmagenta.rect.x = pixel_size * j
                        self.ghostmagenta.rect.y = pixel_size * i+50
                        self.ghostmagenta.startx = pixel_size * j
                        self.ghostmagenta.starty = pixel_size * i + 50

                        self.ghostmagenta.pixel_size = self.pixel_size
                        self.field[i][j] = Space(pixel_size * j, pixel_size * i+50)
                        self.ghosts.append(self.ghostmagenta)
                    if line[j] == "g3":
                        self.ghostyellow = GhostYellow((0,0))
                        self.ghostyellow.rect.x = pixel_size * j
                        self.ghostyellow.rect.y = pixel_size * i+50
                        self.ghostyellow.startx = pixel_size * j
                        self.ghostyellow.starty = pixel_size * i + 50

                        self.ghostyellow.pixel_size = self.pixel_size
                        self.field[i][j] = Space(pixel_size * j, pixel_size * i+50)
                        self.ghosts.append(self.ghostyellow)
                    if line[j] == "g4":
                        self.ghostwhite = GhostWhite((0,0))
                        self.ghostwhite.rect.x = pixel_size * j
                        self.ghostwhite.rect.y = pixel_size * i+50
                        self.ghostwhite.startx = pixel_size * j
                        self.ghostwhite.starty = pixel_size * i + 50

                        self.ghostwhite.pixel_size = self.pixel_size
                        self.field[i][j] = Space(pixel_size * j, pixel_size * i+50)
                        self.ghosts.append(self.ghostwhite)

    def screen_draw(self, screen: Surface, height=height, width=width):
        self.pacman.update()

        for ghost in self.ghosts:
            ghost.update()

        for i in range(height):
            for j in range(width):
                if type(self.field[i][j]) is not Space and self.pacman.rect.colliderect(self.field[i][j].rect):
                    if type(self.field[i][j]) is Wall:
                        self.pacman.check_Wall()
                    if type(self.field[i][j]) is Food:
                        self.field[i][j] = Space(self.pixel_size * j, self.pixel_size * i+50)
                        Food.score += 10
                        self.gui.on_score(Food.score, status=1)
                    if type(self.field[i][j]) is Seed:
                        self.field[i][j] = Space(self.pixel_size * j, self.pixel_size * i+50)
                        Food.score += 100
                        self.gui.on_score(Food.score, status=2)
                        self.pacman.god_mode()
                        

        for i in range(height):
            for j in range(width):
                for ghost in self.ghosts:
                    if type(self.field[i][j]) is not Space and ghost.rect.colliderect(self.field[i][j].rect):
                        if type(self.field[i][j]) is Wall:
                            ghost.check_Wall()



        for ghost in self.ghosts:
            if self.pacman.rect.colliderect(ghost.rect) and self.pacman.drug == False: #12121212
                self.pacman.check_Ghost()

            if self.pacman.rect.colliderect(ghost.rect) and self.pacman.drug == True and self.pacman.ficha == True:
                ghost.lives -= 1
                Fs = Food.score
                Food.score += 555
                if Fs + 555 == Food.score:
                    self.pacman.ficha = False
                # print(Food.score)
                self.gui.on_score(Food.score, status=3)

            if self.pacman.rect.colliderect(ghost.rect) and self.pacman.drug == True:
                ghost.lives -= 1
                Fs = Food.score
                Food.score += 555
                if Fs + 555 == Food.score:
                    self.pacman.ficha = False
                # print(Food.score)
                self.gui.on_score(Food.score, status=3)



        for i in range(height):
            for j in range(width):
                if self.field[i][j] != 0:
                    self.field[i][j].process_draw(screen)
        self.pacman.process_draw(screen)
        if self.ghostcyan.lives == 1:
            self.ghostcyan.draw(screen)
        if self.ghostmagenta.lives == 1:
            self.ghostmagenta.draw(screen)
        if self.ghostyellow.lives == 1:
            self.ghostyellow.draw(screen)
        if self.ghostwhite.lives == 1:
            self.ghostwhite.draw(screen)

    def check_wall(self, i, j):
        return type(self.field[i][j]) is Wall

    def key_up(self):
        self.pacman.key_up()

    def key_right(self):
        self.pacman.key_right()

    def key_left(self):
        self.pacman.key_left()

    def key_down(self):
        self.pacman.key_down()