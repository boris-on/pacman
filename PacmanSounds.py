import pygame as pg

class Sounds:
    
    def __init__(self, volume):
        self.volume = volume
    
    def sound_col(self):
        col_sound = pg.mixer.Sound('pacman_death.wav')
        col_sound.play()
    
    def music_start(self):
        pg.mixer.music.load('pacman_beginning.wav')
        pg.mixer.music.set_volume(self.volume)
        pg.mixer.music.play()
    
    def music_stop(self):
        pg.mixer.music.stop()
        
