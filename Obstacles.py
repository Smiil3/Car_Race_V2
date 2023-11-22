'''
Ce module permet de gerer les differents paramettres des obstacles necessaires pour le bon fonctionnement du jeu.
Fait par Baescu Eduard TG-5
'''
import pygame
from pygame.locals import *

class Obstacles:
    def __init__(self,damage=25, speed=1, carburantAdd=0):
        self.damage=damage
        self.speed=speed
        self.carburantAdd=carburantAdd
    def woodenBox(self):
        """Cette fonction permet de initialiser les paramettres de la woodenbox.
        """
        self.damage=25
        self.carburantAdd = 0
        self.speed=1
        self.appearence=pygame.image.load("Images/Wooden_Box.png")
        self.height = self.appearence.get_height()//1
        self.width = self.appearence.get_width()//1
        self.rect = self.appearence.get_rect()
    def plots(self):
        """Cette fonction permet de initialiser les paramettres des plots.
        """
        self.damage=0
        self.speed=0.3
        self.carburantAdd = 0
        self.appearence=pygame.image.load("Images/Building_Plots.png")
        self.height = self.appearence.get_height()//1*2
        self.width = self.appearence.get_width()//1*2
        self.appearence=pygame.transform.scale(self.appearence, (self.width,self.height))
        self.rect = self.appearence.get_rect()
    def jerrycan(self):
        """Cette fonction permet de initialiser les paramettres de la jerrycan.
        """
        self.damage=0
        self.speed=1
        self.carburantAdd = 0.2
        self.appearence=pygame.image.load("Images/Fuel_tank.png")
        self.height = self.appearence.get_height()//1*1.5
        self.width = self.appearence.get_width()//1*1.5
        self.appearence=pygame.transform.scale(self.appearence, (self.width,self.height))
        self.rect = self.appearence.get_rect()
    def voitureEnnemie1(self):
        """Cette fonction permet de initialiser les paramettres de la voitureEnnemie1.
        """
        self.damage=75
        self.carburantAdd = 0
        self.speed=0.8
        self.appearence=pygame.image.load("Images/Illegal_Vehicule.png")
        self.height = self.appearence.get_height()//4
        self.width = self.appearence.get_width()//4
        self.appearence=pygame.transform.scale(self.appearence, (self.width,self.height))
        self.rect = self.appearence.get_rect()
    def voitureEnnemie2(self):
        """Cette fonction permet de initialiser les paramettres de la voitureEnnemie2.
        """
        self.damage=75
        self.speed=0.9
        self.appearence=pygame.image.load("Images/Military_Vehicule.png")
        self.carburantAdd = 0
        self.height = self.appearence.get_height()//4
        self.width = self.appearence.get_width()//4
        self.appearence=pygame.transform.scale(self.appearence, (self.width,self.height))
        self.rect = self.appearence.get_rect()