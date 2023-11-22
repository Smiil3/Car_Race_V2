'''
Ce module permet de gerer les differents affichages necessaires pour le bon fonctionnement du jeu.
Fait par Baescu Eduard TG-5
'''
import pygame
from pygame.locals import *

class Interface:
    def __init__(self) -> None:
        pass
    
    def buttonCreation(self, screen, buttonLength, buttonHeight, buttonPosition, buttonColor, fontSize, text, textColor, textDisplayPositionLenght, textDisplayPositionHeight):
        """Cette fonction prend en paramettre tous les paramettres necessaires pour creer un rectangle avec du text a l'interieur. 
        @argument:
            screen:Surface
            buttonLength:Float/Int
            buttonHeight:Float/Int
            buttonPosition:Tuple
            buttonColor:Tuple      
            fontSize:Int
            text:String
            textColor:Tuple
            textDisplayPositionLenght:Float/Int
            textDisplayPositionHeight:Float/Int
        @return:
            Rect
        @exemple:
        >>> buttonCreation(screen, (longueur-250)/2, (hauteur/2)-100, (250, 50), (122, 110, 198), 28, "PLAY", (240, 240, 240), (longueur-64)/2, (hauteur/2)-88)
        <rect(250, 400, 250, 50)>
        """
        button = pygame.Rect((buttonLength, buttonHeight), buttonPosition)
        pygame.draw.rect(screen, buttonColor, button)
        font = pygame.font.Font('freesansbold.ttf', fontSize)
        text = font.render(text, True, textColor)       
        screen.blit(text, ((textDisplayPositionLenght, textDisplayPositionHeight)))       
        return button
    
    def textDisplay(self, screen, tailleText, text, colorText, textDisplayPositionLenght, textDisplayPositionHeight):
        """Cette fonction prend en paramettre tous les paramettres necessaires pour creer et afficher du text. 
        @argument:
            screen:Surface
            tailleText:Float/Int
            text:String
            colorText:Tuple
            textDisplayPositionLenght:Float/Int
            textDisplayPositionHeight:Float/Int
        @return:
            None
        @exemple:
        >>> textDisplay(screen, 50, 'CAR RACE', (122, 110, 198), (longueur-260)/2, 200)
        None
        """
        font = pygame.font.Font('freesansbold.ttf', tailleText)
        text = font.render(text, True, colorText)
        screen.blit(text, (textDisplayPositionLenght, textDisplayPositionHeight))
        
    def screenSetup(self, screen, color, image, positionLenght, positionHeight):
        """Cette fonction prend en paramettre tous les paramettres necessaires pour creer un fond sombre avec une image par dessus. 
        @argument:
            screen:Surface
            color:Tuple      
            image:Surface
            positionLenght:Float/Int
            positionHeight:Float/Int
        @return:
            None
        @exemple:
        >>> screenSetup(screen, (0,0,0), background, 0, 0)
        None
        """
        screen.fill(color)
        screen.blit(image, (positionLenght, positionHeight))
        
    def carPreviewer(self, screen, path, positionLenght, positionHeight):
        """Cette fonction prend en paramettre tous les paramettres necessaires pour afficher une image. 
        @argument:
            screen:Surface
            path:String
            positionLenght:Float/Int
            positionHeight:Float/Int
        @return:
            None
        @exemple:
        >>> carPreviewer(screen, "Images/PreviewCar1.png", (longueur/2)+50, 300)
        None
        """
        car1 = pygame.image.load(path)
        screen.blit(car1, (positionLenght, positionHeight))
        return car1
    
    def previewSelecterButton(self, screen, pos1, pos2):
        """Cette fonction prend en paramettre tous les paramettres necessaires pour creer un cercle. 
        @argument:
            screen:Surface
            pos1:Float/Int
            pos2:Float/Int
        @return:
            Rect
        @exemple:
        >>> previewSelecterButton(screen, 549, 327.5)
        <rect(539, 317, 20, 20)>
        """
        button = pygame.draw.circle(screen, (122, 110, 198), [pos1, pos2], 10, 0)
        return button 
    
    def navBar(self, screen, longueur):
        """Cette fonction prend en paramettre tous les paramettres necessaires pour creer un rectangle. 
        @argument:
            screen:Surface
            longueur:Float/Int
        @return:
            Rect
        @exemple:
        >>> navBar(screen, longueur)
        <rect(0, 0, 750, 30)>
        """
        navBar = pygame.Rect((0, 0), (longueur, 30))
        pygame.draw.rect(screen, (222, 188, 246), navBar)
        return navBar
    def heartSystem(self, screen, hp, posHeartX, posHeartY, FullHeartPath, HalfHeartPath, EmptyHeartPath):
        """Cette fonction prend en paramettre tous les paramettres necessaires pour afficher differentes images en fonction de l'hp. 
        @argument:
            screen:Surface
            posHeartX:Float/Int
            posHeartY:Float/Int
            FullHeartPath:String
            HalfHeartPath:String
            EmptyHeartPath:String
        @return:
            None
        @exemple:
        >>> heartSystem(screen, hp, 0, 10, "Images/Full_Heart.png", "Images/Half_Heart.png", "Images/Empty_Heart.png")
        None
        """
        FullHeart = pygame.image.load(FullHeartPath)
        HalfHeart = pygame.image.load(HalfHeartPath)
        EmptyHeart = pygame.image.load(EmptyHeartPath)   
        #H1
        if hp >= 6:
            heartType = FullHeart
            screen.blit(heartType, (posHeartX+15, posHeartY)) #1 10HP
        elif hp >=0 and hp <=5:
            heartType = HalfHeart
            screen.blit(heartType, (posHeartX+15, posHeartY))       
        else:
            heartType = EmptyHeart
            screen.blit(heartType, (posHeartX+15, posHeartY)) 
        #2
        if hp >= 16:
            heartType = FullHeart
            screen.blit(heartType, (posHeartX+30, posHeartY)) #2
        elif hp >=10 and hp <=15:
            heartType = HalfHeart
            screen.blit(heartType, (posHeartX+30, posHeartY))  
        else:
            heartType = EmptyHeart
            screen.blit(heartType, (posHeartX+30, posHeartY)) 
        #3
        if hp >= 26:
            heartType = FullHeart
            screen.blit(heartType, (posHeartX+45, posHeartY)) #3
        elif hp >=20 and hp <=25:
            heartType = HalfHeart
            screen.blit(heartType, (posHeartX+45, posHeartY))  
        else:
            heartType = EmptyHeart
            screen.blit(heartType, (posHeartX+45, posHeartY)) 
        #4
        if hp >= 36:
            heartType = FullHeart
            screen.blit(heartType, (posHeartX+60, posHeartY)) #4
        elif hp >=30 and hp <=35:
            heartType = HalfHeart
            screen.blit(heartType, (posHeartX+60, posHeartY))  
        else:
            heartType = EmptyHeart
            screen.blit(heartType, (posHeartX+60, posHeartY)) 
        #5
        if hp >= 46:
            heartType = FullHeart
            screen.blit(heartType, (posHeartX+75, posHeartY)) #5
        elif hp >=40 and hp <=45:
            heartType = HalfHeart
            screen.blit(heartType, (posHeartX+75, posHeartY))  
        else:
            heartType = EmptyHeart
            screen.blit(heartType, (posHeartX+75, posHeartY)) 
        #6
        if hp >= 56:
            heartType = FullHeart
            screen.blit(heartType, (posHeartX+90, posHeartY)) #6
        elif hp >=60 and hp <=65:
            heartType = HalfHeart
            screen.blit(heartType, (posHeartX+90, posHeartY))  
        else:
            heartType = EmptyHeart
            screen.blit(heartType, (posHeartX+90, posHeartY)) 
        #7
        if hp >= 66:
            heartType = FullHeart
            screen.blit(heartType, (posHeartX+105, posHeartY)) #7
        elif hp >=60 and hp <=65:
            heartType = HalfHeart
            screen.blit(heartType, (posHeartX+105, posHeartY))  
        else:
            heartType = EmptyHeart
            screen.blit(heartType, (posHeartX+105, posHeartY)) 
        #8
        if hp >= 76:
            heartType = FullHeart
            screen.blit(heartType, (posHeartX+120, posHeartY)) #8
        elif hp >=70 and hp <=75:
            heartType = HalfHeart
            screen.blit(heartType, (posHeartX+120, posHeartY))  
        else:
            heartType = EmptyHeart
            screen.blit(heartType, (posHeartX+120, posHeartY))
        #9
        if hp >= 86:
            heartType = FullHeart
            screen.blit(heartType, (posHeartX+135, posHeartY)) #9
        elif hp >=80 and hp <=85:
            heartType = HalfHeart
            screen.blit(heartType, (posHeartX+135, posHeartY))  
        else:
            heartType = EmptyHeart
            screen.blit(heartType, (posHeartX+135, posHeartY)) 
        #10
        if hp >= 96:
            heartType = FullHeart
            screen.blit(heartType, (posHeartX+150, posHeartY)) #10  100HP
        elif hp >=90 and hp <=95:
            heartType = HalfHeart
            screen.blit(heartType, (posHeartX+150, posHeartY))      
        else:
            heartType = EmptyHeart
            screen.blit(heartType, (posHeartX+150, posHeartY))  
    
    def carburantSystem(self, screen, imagePaht, fuel):
        """Cette fonction prend en paramettre tous les paramettres necessaires pour creer un rectangle qui varie selon le fuel encadre par un autre rectangle non remplis. 
        @argument:
            screen:Surface
            imagePaht:String
            fuel:Float/Int
        @return:
            None
        @exemple:
        >>> carburantSystem(screen, "Images/Fuel_tank_13x15.png", fuel)
        None
        """
        screen.blit(pygame.image.load(imagePaht), (0+200, 10))  
        pygame.draw.rect(screen, (255,255,255), pygame.Rect(220,10,(200*fuel),10))
        pygame.draw.rect(screen, (128,128,128), pygame.Rect(220,10,200,10), 1)
        
    def scoreSystem(self, screen, score):
        """Cette fonction prend en paramettre tous les paramettres necessaires pour creer un texte qui change en fonction du score. 
        @argument:
            screen:Surface
            score:Float/Int
        @return:
            None
        @exemple:
        >>> scoreSystem(screen, score)
        None
        """
        screen.blit(pygame.font.Font('freesansbold.ttf', 15).render(f'Score: {str(score)}', True, (255, 255, 255)), ((670, 10)))
        
    def effectSystem(self, screen, speed_timer):
        """Cette fonction prend en paramettre tous les paramettres necessaires pour creer un rectangle avec du text a l'interieur. 
        @argument:
            screen:Surface
            speed_timer:Float/Int
        @return:
            None
        @exemple:
        >>> effectSystem(screen, speed_timer)
        None
        """
        #Display Duration In Seconds
        if speed_timer >100 and speed_timer < 1000:
            text=str(speed_timer)[:1]
        elif speed_timer >=1000:
            text=str(speed_timer)[:2]
        else:
            text="0"
        screen.blit(pygame.font.Font('freesansbold.ttf', 15).render(f'Slowness: {text}s', True, (255, 255, 255)), ((520, 10)))