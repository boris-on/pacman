import pygame

import high_score



class Text:
    def __init__(self, font, size, text, antialias, colour, background):
        self.font = font
        self.size = size
        self.text = text
        self.antialias = antialias
        self.colour = colour
        self.background = background
        texts = pygame.font.SysFont(self.font, self.size)
        self.text = texts.render(self.text, self.antialias, self.colour, self.background)




    def text_draw(self, screen, x=10, y=10):
        screen.blit(self.text, (x, y))



class Button:
    def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font="arial", font_size=16,
                 font_clr=[0, 0, 0]):
        self.clr = clr
        self.size = size
        self.func = func
        self.surf = pygame.Surface(size)
        self.rect = self.surf.get_rect(center=position)

        if cngclr:
            self.cngclr = cngclr
        else:
            self.cngclr = clr

        if len(clr) == 4:
            self.surf.set_alpha(clr[3])

        self.font = pygame.font.SysFont(font, font_size)
        self.txt = text
        self.font_clr = font_clr
        self.txt_surf = self.font.render(self.txt, True, self.font_clr)
        self.txt_rect = self.txt_surf.get_rect(center=[wh//2 for wh in self.size])

    def draw(self, screen):
        self.mouseover()

        self.surf.fill(self.curclr)
        self.surf.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surf, self.rect)

    def mouseover(self):
        self.curclr = self.clr
        position = pygame.mouse.get_pos()
        if self.rect.collidepoint(position):
            self.curclr = self.cngclr

    def call_back(self, *args):
        if self.func:
            return self.func(*args)
    
    def try_clicked(self):
        position = pygame.mouse.get_pos()
        return self.rect.collidepoint(position)
    

class Lives(pygame.sprite.Sprite):
    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, 750))
    
        
class GUI:
    def __init__(self,displayw,displayh):    
        self.dw = displayw
        self.dh = displayh

        self.text1 = Text('arial', 20, "Score", True, (0, 0, 255), None)
        self.text_HIGHSCORE = Text('arial', 40, "HIGHSCORES:", True, (255, 255, 255), None)

        
        self.live1 = Lives(30, 'heart.png')
        self.live2 = Lives(80, 'heart.png')
        self.live3 = Lives(130, 'heart.png')
        
        self.button1 = Button(position=(390, 20), size=(60, 30), clr=(220, 220, 220), cngclr=(255, 0, 0),func=None,text='MENU')
        
        self.button_ReturnToMenu = Button(position=(700, 50), size=(100, 30), clr=(220, 220, 220), cngclr=(255, 0, 0),func=None,text='return to menu')
        self.game_over = False
        self.button_start = Button(position=(400, 200), size=(200, 100), clr=(220, 220, 220), cngclr=(255, 0, 0),func=None,text='START')
        self.button_score = Button(position=(400, 310), size=(200, 100), clr=(220, 220, 220), cngclr=(255, 0, 0),func=None,text='SCORE')
        self.button_quit = Button(position=(400, 420), size=(200, 100), clr=(220, 220, 220), cngclr=(255, 0, 0),func=None,text='QUIT')

        self.score = 0
        self.lives = 3
        self.go = False
        self.draw = self.draw_menu
        self.click = self.button_menu

    def draw_gui(self, screen):
        if self.lives ==3:
            screen.blit(self.live1.image, self.live1.rect)
            screen.blit(self.live2.image, self.live2.rect)
            screen.blit(self.live3.image, self.live3.rect)
        if self.lives==2:
            screen.blit(self.live1.image, self.live1.rect)
            screen.blit(self.live2.image, self.live2.rect)
        if self.lives ==1:
            screen.blit(self.live1.image, self.live1.rect)
        self.text1.text_draw(screen)
        text2 = Text('arial', 20, str(self.score), True, (0, 0, 255), None)
        self.button1.draw(screen)
        text2.text_draw(screen, x =80, y=10)


    def button_gui(self):
        if self.button1.try_clicked():
            self.draw = self.draw_menu
            self.click = self.button_menu
        
    def draw_menu(self, screen):
        self.button_start.draw(screen)
        self.button_score.draw(screen)
        self.button_quit.draw(screen)
        self.go = False

    def button_menu(self):
        if self.button_start.try_clicked():
            self.draw = self.draw_gui
            self.click = self.button_gui
            self.go = True
        if self.button_score.try_clicked():
            self.draw = self.draw_scores
            self.click = self.button_menu

        if self.button_quit.try_clicked():
            self.draw = self.draw_menu
            self.click = self.button_menu
            self.game_over = True

    def draw_scores(self, screen):
        scores = high_score.readScorefromFile()
        self.text_HIGHSCORE.text_draw(screen, 40, 40)
        self.button_ReturnToMenu.draw(screen)
        
    def on_left_mouse(self):
        if pygame.mouse.get_pressed()[0] and self.click is not None:
            self.click()
            
    def on_score(self, score, status):
        print(score)
        if status ==1:
            self.score += 10
        if status ==2:
            self.score += 100
        if status==3:
            self.score += 555

