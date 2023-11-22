import pygame
from pygame.locals import *
import time

class Player:
    def __init__(self,vehicule=0,hp=120,fuel=100,maxFuel=100,speed=1,crash=0):
        self.hp=hp
        self.fuel=fuel
        self.maxFuel=maxFuel
        self.speed=speed
        self.vehicule=vehicule
        self.x=332.5
        self.y=800
        self.crash=crash
        self.smoke_counter=0

    #Car shift
    def altima(self):
        self.height = 150
        self.width = 75
        self.appearence=pygame.image.load("Images/Normal_Car.png")
        self.appearence=pygame.transform.scale(self.appearence, (self.width,self.height))
        self.rect = self.appearence.get_rect()
    def ferrari448 (self):
        self.hp=125
        self.speed=1+(1*0.5)
        self.height = 936//6
        self.width = 441//6
        self.appearence=pygame.image.load("Images/ferrari.png")
        self.appearence=pygame.transform.scale(self.appearence, (self.width,self.height))
        self.rect = self.appearence.get_rect()
    def toyota_ae86(self):
        self.maxFuel=(self.fuel*0.05)
        self.speed=1*2.5
        self.appearence=pygame.image.load("Images/Toyota_ae86.png")
        self.height = 582//4
        self.width = 222//4
        self.appearence=pygame.transform.scale(self.appearence, (self.width,self.height))
        self.rect = self.appearence.get_rect()
    def mustang(self):
        self.hp=130
        self.maxFuel=(self.fuel*0.05)
        self.speed=1*1.0
        self.height = 582//4
        self.width = 222//4
        self.appearence=pygame.image.load("Images/mustang.png")
        self.appearence=pygame.transform.scale(self.appearence, (self.width,self.height))
        self.rect = self.appearence.get_rect()
    def batmobile(self):
        self.hp=135
        self.maxFuel=(self.fuel*0.16)
        self.speed=1*1.5
        self.height = 532//4
        self.width = 245//4
        self.appearence=pygame.image.load("Images/batmobile.png")
        self.appearence=pygame.transform.scale(self.appearence, (self.width,self.height))
        self.rect = self.appearence.get_rect()
    def firebird(self):
        self.hp=140
        self.maxFuel=(self.fuel*0.07)
        self.speed=1*2.0
        self.height = 568//4
        self.width = 223//4
        self.appearence=pygame.image.load("Images/FireBird1.png")
        self.appearence=pygame.transform.scale(self.appearence, (self.width,self.height))
        self.rect = self.appearence.get_rect()

    #Car movement
    #Car movement
    def moving(self,speed_purcentage):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.move_right(speed_purcentage)
        if keys[pygame.K_a]:
            self.move_left(speed_purcentage)
        if keys[pygame.K_w]:
            self.move_up(speed_purcentage)
        if keys[pygame.K_s]:
            self.move_down(speed_purcentage)  
    def move_up(self,speed_purcentage):
        self.y -= self.speed * speed_purcentage
    def move_down(self,speed_purcentage):
        self.y += self.speed * speed_purcentage
    def move_left(self,speed_purcentage):
        self.x -= self.speed * speed_purcentage
    def move_right(self,speed_purcentage):
        self.x += self.speed * speed_purcentage

    #Get stats & appearance 
    def get_stats(self):
        if self.vehicule==0:
            self.altima()        
        elif self.vehicule==1:
            self.ferrari448()
        elif self.vehicule==2:
            self.toyota_ae86()
        elif self.vehicule==3:
            self.mustang()
        elif self.vehicule==4:
            self.batmobile()
        elif self.vehicule==5:
            self.firebird()
        return self.appearence

    def game_over(self):
        if self.smoke_counter==0:
            smoke=pygame.image.load("Images/Smoke_Frames/frame_0_100x100.png")
        if self.smoke_counter==1:
            smoke=pygame.image.load("Images/Smoke_Frames/frame_1_100x100.png")
        if self.smoke_counter==2:
            smoke=pygame.image.load("Images/Smoke_Frames/frame_2_100x100.png")
        if self.smoke_counter==3:
            smoke=pygame.image.load("Images/Smoke_Frames/frame_3_100x100.png")
        if self.smoke_counter==4:
            smoke=pygame.image.load("Images/Smoke_Frames/frame_4_100x100.png")
        if self.smoke_counter==5:
            smoke=pygame.image.load("Images/Smoke_Frames/frame_5_100x100.png")
        if self.smoke_counter==6:
            smoke=pygame.image.load("Images/Smoke_Frames/frame_6_100x100.png")
        self.smoke_counter+=1
        time.sleep(0.1)
        if self.smoke_counter==7:
            self.smoke_counter=0
        return smoke
    def get_pos(self):
        return self.rect
    def the_incredible_collision (self,object_rect):
        #print(self.rect)
        if self.rect.colliderect(object_rect):
            return True