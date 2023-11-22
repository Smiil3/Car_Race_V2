from audioop import maxpp
import pygame
from pygame.locals import *

class Road:
    def __init__(self,bordure=40,score=0):
        self.bordure=bordure
        self.score=score
        self.img=pygame.image.load('Images/Road.png')

    def get_img(self):
        return self.img
    
    def get_score(self,x):
        self.score=x
        #return self.score

    def gestion_fuel(self, fuel, crash):
        if self.score%2==0:
            fuel-=0.0001
        if fuel<=0:
            crash=1
        return fuel, crash

    def gestion_PdV(self,damages, pv, crash):
        pv-=damages
        if pv<=0:
            crash=1
        return pv, crash
    def game_over(self,screen):

        transparent_bg = pygame.Surface((750,1000))
        transparent_bg.set_alpha(128)
        transparent_bg.fill((0,0,0))
        screen.blit(transparent_bg,(0,0))

        font_gameover = pygame.font.Font('freesansbold.ttf', 75)
        text_gameover = font_gameover.render('Game Over', True, (240, 240, 240))
        screen.blit(text_gameover, ((150, 200)))
        
    def button1(self,screen):

        button = pygame.Rect((250, 500), (250, 50))
        pygame.draw.rect(screen, (122, 110, 198), button)

        font = pygame.font.Font('freesansbold.ttf', 28)
        text = font.render('Leaderboard', True, (240, 240, 240))
        screen.blit(text, (290, 512.5))

        return button

    def button2(self,screen):

        button = pygame.Rect((250, 600), (250, 50))
        pygame.draw.rect(screen, (122, 110, 198), button)

        font = pygame.font.Font('freesansbold.ttf', 28)
        text = font.render('Menu',True, (240, 240, 240))
        screen.blit(text, (340, 612.5))

        return button

    def button3(self,screen):

        button = pygame.Rect((250, 700), (250, 50))
        pygame.draw.rect(screen, (122, 110, 198), button)

        font = pygame.font.Font('freesansbold.ttf', 28)
        text = font.render('Quit',True,(240,240,240))
        screen.blit(text, (345, 712.5))

        return button