import pygame as pg
import sys
from button import Button

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 180, 0)

BUTTON_STYLE = {
        "hover_color": BLUE,
        "clicked_color": GREEN,
        "clicked_font_color": BLACK,
        "hover_font_color": ORANGE,
                }


pg.init()
sc = pg.display.set_mode((800, 600))

pg.mixer.music.load('pacman_beginning.wav')
pg.mixer.music.set_volume(0.4)
pg.mixer.music.play()
 
sound1 = pg.mixer.Sound('pacman_chomp.wav')

def SoundPlay():
    pg.mixer.music.pause()
    sound1.play()
    pg.time.delay(1400)
    pg.mixer.music.unpause()


button1 = Button((800 // 2 - 100, 600 // 2 - 65, 100, 50),
                  RED, pg.mixer.music.pause, text='Music pause', **BUTTON_STYLE)
button11 = Button((800 // 2, 600 // 2 - 65, 100, 50),
                  RED, pg.mixer.music.stop, text='Music stop', **BUTTON_STYLE)
button2 = Button((800 // 2 - 100, 600 // 2 - 15, 100, 50),
                  RED, pg.mixer.music.unpause, text='Music unpause', **BUTTON_STYLE)
button22 = Button((800 // 2, 600 // 2 - 15, 100, 50),
                  RED, pg.mixer.music.play, text='Music play', **BUTTON_STYLE)
button3 = Button((800 // 2 - 100, 600 // 2 + 35, 200, 50),
                  RED, SoundPlay, text='Play sound', **BUTTON_STYLE) # Надо будет менять кнопки, ибо эта стистема
button6 = Button((800 // 2 - 100, 600 // 2 + 85, 200, 50),           # не даёт вызывать функции с аргументами
                  RED, exit, text='Exit', **BUTTON_STYLE)            # Это если не дропать кнопки в общем
 
gameover = False
while not gameover:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            sys.exit()
        button1.check_event(i)
        button11.check_event(i)
        button2.check_event(i)
        button22.check_event(i)
        button3.check_event(i)
        button6.check_event(i)
        # elif i.type == pg.KEYUP:
        #   if i.key == pg.K_1:
        #      pg.mixer.music.pause()
        #        # pygame.mixer.music.stop()
        #    elif i.key == pg.K_2:
        #        pg.mixer.music.unpause()
        #        # pygame.mixer.music.play()
        #        pg.mixer.music.set_volume(0.2)
        #    elif i.key == pg.K_3:
        #        pg.mixer.music.unpause()
        #        # pygame.mixer.music.play()
        #        pg.mixer.music.set_volume(1)
        
        sc.fill(BLACK)
        button1.update(sc)
        button11.update(sc)
        button2.update(sc)
        button22.update(sc)
        button3.update(sc)
        button6.update(sc)
        pg.display.flip()
        pg.time.wait(10)
 
    pg.time.delay(20)