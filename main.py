import pygame
from pygame.locals import *
from Obstacles import Obstacles
from Interface import Interface
from Route import Road
from Joueur import Player
from random import randint, choice
import csv
import time

#Pygame Init
pygame.init()
pygame.mixer.init()

#Screen Size
hauteur = 1000
longueur = 750

#Class Initialisation
road=Road()
this_is_not_an_npc=Player()
omg_an_obstacle=Obstacles()
the_interface=Interface()

#Images Load
displayLogo = pygame.image.load("Images/logo.png")
background = pygame.image.load("Images/bg.png")
game_background = road.get_img()

#Screen Display
screen = pygame.display.set_mode((longueur,hauteur))
#Backgrouund resize
background = pygame.transform.scale(background, (750,1000))

#Game Name
pygame.display.set_caption('Car Race V1.0')

#Timer Logo
clock = pygame.time.Clock()
timerLogo = 0

#Game background
coordonnees_background=0
speed_timer = 0
speed_purcentage = 1

#Obstacles List
object_npc = []

#Game Loop
continuer = True
boot=True
jeu = False
leaderboard = False
selectMenu = False 
mainMenu = True

#Cars Selector 
count=0
boolCar1 = True
boolCar2 = False
boolCar3 = False
boolCar4 = False
boolCar5 = False	
boolCar6 = False
carButtonLeft = pygame.draw.circle(screen, (122, 110, 198), [400, 327.5], 10, 0)
carButtonRight = pygame.draw.circle(screen, (122, 110, 198), [549, 327.5], 10, 0)

#Diffs Selector
count2 = 0
boolDiff1 = True
boolDiff2 = False
boolDiff3 = False
boolDiff4 = False
diffButtonLeft = pygame.draw.circle(screen, (122, 110, 198), [400, 327.5], 10, 0)
diffButtonRight = pygame.draw.circle(screen, (122, 110, 198), [549, 327.5], 10, 0)

#Name Input 
active = False
typedText = 'Type your name..'
charLimit = 0
limit = 10

#User Database
databaseNeedLoad=True
databaseDone = False
testDatabasePassed = True
numberScore = 0
score=0

#Settings Menu Variables | SOON FEATURE..
musicOn=True

#Init Variables
roadCreate=False
collision = False

#Sounds Load
music = pygame.mixer.music.load("Sounds/music.mp3")
wood = pygame.mixer.Sound('Sounds/wood.mp3')
crash = pygame.mixer.Sound('Sounds/crash.mp3')
carburant = pygame.mixer.Sound('Sounds/carburant.mp3')

#BG Music
if musicOn: 
    pygame.mixer.music.play(-1)

while continuer:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            
        #Boot Logo
        screen.fill((255, 255, 255))
        while (timerLogo < 1500) and boot==True:
            taille_logo = displayLogo.get_size() 
            screen.blit(displayLogo, [longueur/2 - taille_logo[0]/2, (hauteur-100)/2 - taille_logo[1]/2]) 
            #Timer Logo
            dt = clock.tick(60) 
            timerLogo += dt
            pygame.display.flip() 
        boot=False
        
        
    while mainMenu:
        #Quit System
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                
            #Main Menu    
            the_interface.screenSetup(screen, (0,0,0), background, 0, 0)
            
            #Buttons Creation         
            button1 = the_interface.buttonCreation(screen, (longueur-250)/2, (hauteur/2)-100, (250, 50), (122, 110, 198), 28, "PLAY", (240, 240, 240), (longueur-64)/2, (hauteur/2)-88)
            button2 = the_interface.buttonCreation(screen, (longueur-250)/2, hauteur/2, (250, 50), (122, 110, 198), 28, "LEADERBOARD", (240, 240, 240), (longueur-220 )/2, (hauteur/2)+12)
            button3 = the_interface.buttonCreation(screen, (longueur-250)/2, (hauteur/2)+100, (250, 50), (122, 110, 198), 28, "QUIT", (240, 240, 240), (longueur-80)/2, (hauteur/2)+112)
            #Title
            the_interface.textDisplay(screen, 50, 'CAR RACE', (122, 110, 198), (longueur-260)/2, 200)
            
            #Update Display
            pygame.display.flip() 
        
            #Play Button
            x,y=pygame.mouse.get_pos()
            if button1.collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                selectMenu = True
                mainMenu = False
            
            #LeaderBoard Button
            x,y=pygame.mouse.get_pos()
            if button2.collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                leaderboard = True
                databaseNeedLoad=True
                mainMenu = False
            
            #Quit Button
            x,y=pygame.mouse.get_pos()
            if button3.collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                pygame.quit()
                       
    while selectMenu:
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
                selectMenu = False

                
        #Select Menu
            #BackGround
            the_interface.screenSetup(screen, (0,0,0), background, 0, 0)
            
            #Title
            the_interface.textDisplay(screen, 50, 'Are you ready ?', (122, 110, 198), (longueur-375)/2, 100)            
            
            #Ready button
            button = the_interface.buttonCreation(screen, (longueur-250)/2, (hauteur)-200, (250, 50), (122, 110, 198), 28, "READY", (240, 240, 240), (longueur-100)/2, (hauteur)-188)
            
            #Car Title
            the_interface.textDisplay(screen, 26, 'Your car :', (240, 240, 240), 140, 324)     
            
            #Car Previwer & Buttons
            if boolCar1:
                car1 = the_interface.carPreviewer(screen, "Images/PreviewCar1.png", (longueur/2)+50, 300)
                carButtonRight = the_interface.previewSelecterButton(screen, 549, 327.5)
                the_interface.textDisplay(screen, 15, 'Nissan Altima', (73, 92, 148), 422, 360)   

            if boolCar2:
                car1 = the_interface.carPreviewer(screen, "Images/PreviewCar2.png", (longueur/2)+50, 290)
                carButtonLeft = the_interface.previewSelecterButton(screen, 400, 327.5)
                carButtonRight = the_interface.previewSelecterButton(screen, 549, 327.5)
                the_interface.textDisplay(screen, 15, 'Ferrari 448', (255, 16, 16), 434, 360)   
                this_is_not_an_npc.vehicule = 1
            if boolCar3:
                car1 = the_interface.carPreviewer(screen, "Images/PreviewCar3.png", (longueur/2)+50, 300)
                carButtonLeft = the_interface.previewSelecterButton(screen, 400, 327.5)
                carButtonRight = the_interface.previewSelecterButton(screen, 549, 327.5)
                the_interface.textDisplay(screen, 15, 'Toyota Ae86', (178, 178, 178), 432, 360)
                this_is_not_an_npc.vehicule = 2
            if boolCar4:
                car1 = the_interface.carPreviewer(screen, "Images/PreviewCar4.png", (longueur/2)+50, 300)
                carButtonLeft = the_interface.previewSelecterButton(screen, 400, 327.5)
                carButtonRight = the_interface.previewSelecterButton(screen, 549, 327.5)
                the_interface.textDisplay(screen, 15, 'Ford Mustang', (72, 102, 118), 422, 360)
                this_is_not_an_npc.vehicule = 3
            if boolCar5:
                car1 = the_interface.carPreviewer(screen, "Images/PreviewCar5.png", (longueur/2)+50, 300)
                carButtonLeft = the_interface.previewSelecterButton(screen, 400, 327.5)
                carButtonRight = the_interface.previewSelecterButton(screen, 549, 327.5)
                the_interface.textDisplay(screen, 15, 'Green Batmobile', (97, 143, 132), 415, 360)
                this_is_not_an_npc.vehicule = 4
            if boolCar6:
                car1 = the_interface.carPreviewer(screen, "Images/PreviewCar6.png", (longueur/2)+50, 300)
                carButtonLeft = the_interface.previewSelecterButton(screen, 400, 327.5)
                the_interface.textDisplay(screen, 15, 'Pontiac Firebird', (199, 104, 94), 418, 360)
                this_is_not_an_npc.vehicule = 5
                
            #Diff Title
            the_interface.textDisplay(screen, 26, 'Your difficulty :', (240, 240, 240), 140, 454)  
                
            #Diff Previewer & Buttons
            if boolDiff1:
                diffButtonRight = the_interface.previewSelecterButton(screen, 549, 467.5)
                the_interface.textDisplay(screen, 24, 'Easy', (10, 176, 94), 446, 455)  
            if boolDiff2:
                diffButtonLeft = the_interface.previewSelecterButton(screen, 400, 467.5)
                diffButtonRight = the_interface.previewSelecterButton(screen, 549, 467.5)
                the_interface.textDisplay(screen, 24, 'Medium', (236, 176, 94), 428, 455)  
            if boolDiff3:
                diffButtonLeft = the_interface.previewSelecterButton(screen, 400, 467.5)
                diffButtonRight = the_interface.previewSelecterButton(screen, 549, 467.5)
                the_interface.textDisplay(screen, 24, 'Hard', (236, 85, 98), 445, 455)  
            if boolDiff4:
                diffButtonLeft = the_interface.previewSelecterButton(screen, 400, 467.5)
                the_interface.textDisplay(screen, 24, 'Extreme', (217, 17, 0), 425, 455)
                
            #Car Selecter
            x,y=pygame.mouse.get_pos()
            if carButtonRight.collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                if count >= 0 and count <= 4 :
                    count=count+1
                    if count == 1:
                        boolCar1=False
                        boolCar2=True
                    if count == 2:
                        boolCar2=False
                        boolCar3=True
                    if count == 3:
                        boolCar3=False
                        boolCar4=True
                    if count == 4:
                        boolCar4=False
                        boolCar5=True
                    if count == 5:
                        boolCar5=False
                        boolCar6=True
            if carButtonLeft.collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                if count >= 0 and count <= 5 :
                    if count == 1:
                        boolCar1=True
                        boolCar2= False
                        count=count-1
                    if count == 2:
                        boolCar2=True
                        boolCar3=False
                        count=count-1
                    if count == 3:
                        boolCar3=True
                        boolCar4=False
                        count=count-1
                    if count == 4:
                        boolCar4=True
                        boolCar5=False
                        count=count-1
                    if count == 5:
                        boolCar5=True
                        boolCar6=False
                        count=count-1

            #Diff Selecter
            if diffButtonRight.collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                if count2 >= 0 and count2 <= 2 :
                    count2=count2+1
                    if count2 == 1:
                        boolDiff1=False
                        boolDiff2=True
                    if count2 == 2:
                        boolDiff2=False
                        boolDiff3=True
                    if count2 == 3:
                        boolDiff3=False
                        boolDiff4=True
            if diffButtonLeft.collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                if count2 >= 0 and count2 <= 3 :
                    if count2 == 1:
                        boolDiff1=True
                        boolDiff2= False
                        count2=count2-1
                    if count2 == 2:
                        boolDiff2=True
                        boolDiff3=False
                        count2=count2-1
                    if count2 == 3:
                        boolDiff3=True
                        boolDiff4=False
                        count2=count2-1
                        
            #Name Title
            the_interface.textDisplay(screen, 26, 'Your name :', (240, 240, 240), 140, 554)
            
            #Name Input Rectangle
            nameInputer = pygame.Rect((348, 556), (200, 25))
            pygame.draw.rect(screen, (122, 110, 198), nameInputer)
            
            #Text Apparition
            if event.type == MOUSEBUTTONDOWN:
                if nameInputer.collidepoint(event.pos):
                    active = not active
                    typedText = ''
                    charLimit = 0
                else:
                    active = False
                    
            if event.type == KEYDOWN:
                if active:
                    if event.key == K_BACKSPACE:
                        if charLimit > 0:
                            charLimit-=1
                            typedText = typedText[:-1]
                        elif charLimit == 0:
                            limit = 10
                    else:
                        if charLimit < limit:
                            charLimit+=1
                            typedText = typedText + event.unicode
                            
            #Text Render
            surfaceText = pygame.font.Font('freesansbold.ttf', 22).render(typedText, True, (0,0,0))
            
            #Text Updater
            screen.blit(surfaceText, (nameInputer.x+3, nameInputer.y+1))
                 
            #Update Screen
            pygame.display.flip()
                   
            #Ready Button
            if button.collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                global PlayerName
                PlayerName = typedText
                jeu = True
                selectMenu = False
    
    while leaderboard:
        
        #Display Settings
        the_interface.screenSetup(screen, (0,0,0), background, 0, 0)
        
        #Quit
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
                leaderboard = False    
                            
            #Menu Title
            the_interface.textDisplay(screen, 50, 'Top 10 Players', (122, 110, 198), (longueur-350)/2, 100)
            
            #Load Database
            if databaseNeedLoad:            
                listeJoueurs = []
                with open('database.csv', newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=',')
                    for row in reader:
                        listeJoueurs.append(dict(row))
                        
                #Creating LeaderBoard Lists
                listeNom = []
                listeTop = []
                for Users in listeJoueurs:
                    for i,v in Users.items():
                        listeNom.append(v)
                for i in range (len(listeNom)):
                    if i%2 == 0:
                        listeTop.append((int(listeNom[i]), listeNom[i+1]))

                #Sorting all the scores 
                listeTopSorted=sorted(listeTop, reverse=True)  
                
                #Systeme anti-doublons
                nombreData=-1
                listeElement=[]
                listeDeVerification=[]
                for y in listeTopSorted:
                    listeElement.append(y[1])
                for element in listeElement:
                    nombreData+=1
                    if element in listeDeVerification:
                        del listeTopSorted[nombreData]
                        nombreData-=1
                    listeDeVerification.append(element)
                databaseNeedLoad=False

            #Top Displaying
            
            #Filling leaderboard if no data
            while len(listeTopSorted)  < 10:
                listeTopSorted.append((0,"/"))
                
            #Titles Nom / Score
            the_interface.textDisplay(screen, 23, "Name", (122, 110, 198), 250, 260)
            the_interface.textDisplay(screen, 23, "Score", (122, 110, 198), 425, 260)
            
            #Top1
            fontLeaderboard = pygame.font.Font('freesansbold.ttf', 20)
            the_interface.textDisplay(screen, 20, str(listeTopSorted[0][1]), (255,255,255), 240, 300)
            the_interface.textDisplay(screen, 20, str(listeTopSorted[0][0]), (255,255,255), 430, 300)       
            #Top2
            the_interface.textDisplay(screen, 20, str(listeTopSorted[1][1]), (255,255,255), 240, 325)
            the_interface.textDisplay(screen, 20, str(listeTopSorted[1][0]), (255,255,255), 430, 325)   
            #Top3
            the_interface.textDisplay(screen, 20, str(listeTopSorted[2][1]), (255,255,255), 240, 350)
            the_interface.textDisplay(screen, 20, str(listeTopSorted[2][0]), (255,255,255), 430, 350)         
            #Top4
            the_interface.textDisplay(screen, 20, str(listeTopSorted[3][1]), (255,255,255), 240, 375)
            the_interface.textDisplay(screen, 20, str(listeTopSorted[3][0]), (255,255,255), 430, 375)   
            #Top5
            the_interface.textDisplay(screen, 20, str(listeTopSorted[4][1]), (255,255,255), 240, 400)
            the_interface.textDisplay(screen, 20, str(listeTopSorted[4][0]), (255,255,255), 430, 400)  
            #Top6
            the_interface.textDisplay(screen, 20, str(listeTopSorted[5][1]), (255,255,255), 240, 425)
            the_interface.textDisplay(screen, 20, str(listeTopSorted[5][0]), (255,255,255), 430, 425)   
            #Top7
            the_interface.textDisplay(screen, 20, str(listeTopSorted[6][1]), (255,255,255), 240, 450)
            the_interface.textDisplay(screen, 20, str(listeTopSorted[6][0]), (255,255,255), 430, 450)          
            #Top8
            the_interface.textDisplay(screen, 20, str(listeTopSorted[7][1]), (255,255,255), 240, 475)
            the_interface.textDisplay(screen, 20, str(listeTopSorted[7][0]), (255,255,255), 430, 475)           
            #Top9
            the_interface.textDisplay(screen, 20, str(listeTopSorted[8][1]), (255,255,255), 240, 500)
            the_interface.textDisplay(screen, 20, str(listeTopSorted[8][0]), (255,255,255), 430, 500) 
            #Top10
            the_interface.textDisplay(screen, 20, str(listeTopSorted[9][1]), (255,255,255), 240, 525)
            the_interface.textDisplay(screen, 20, str(listeTopSorted[9][0]), (255,255,255), 430, 525) 
            
            #Main Menu Button
            button1 = the_interface.buttonCreation(screen, (longueur-250)/2, 750, (250, 50), (122, 110, 198), 28, "MAIN MENU", (240, 240, 240), (longueur/2)-80, 762)   
            x,y=pygame.mouse.get_pos()        
            if button1.collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                jeu = False
                leaderboard = False
                selectMenu=False
                mainMenu = True
                #print("Test Button")
            
            #Update Screen    
            pygame.display.flip() 

    while jeu:
        
        #Init Game Values   
        if roadCreate == False:
            fuel = this_is_not_an_npc.fuel/this_is_not_an_npc.maxFuel
            hp = this_is_not_an_npc.hp
            score=0
            roadCreate=True
            
        #Obstacles Apparition
        if randint(0,100//(count2+1)) == 1:
            if randint(0,3) == 1:
                omg_an_obstacle.plots()
                object_npc.append((omg_an_obstacle.rect, (randint(road.bordure,longueur-(road.bordure+omg_an_obstacle.width)),-450), omg_an_obstacle.damage, omg_an_obstacle.carburantAdd, omg_an_obstacle.appearence, omg_an_obstacle.speed))
            elif randint(0,3) == 1:
                omg_an_obstacle.voitureEnnemie1()
                object_npc.append((omg_an_obstacle.rect, (randint(road.bordure,longueur-(road.bordure+omg_an_obstacle.width)),-350), omg_an_obstacle.damage, omg_an_obstacle.carburantAdd, omg_an_obstacle.appearence, omg_an_obstacle.speed))
            elif randint(0,3) == 1:
                omg_an_obstacle.woodenBox()
                object_npc.append((omg_an_obstacle.rect, (randint(road.bordure,longueur-(road.bordure+omg_an_obstacle.width)),-250), omg_an_obstacle.damage, omg_an_obstacle.carburantAdd, omg_an_obstacle.appearence, omg_an_obstacle.speed))
            elif randint(0,3) == 1:
                omg_an_obstacle.voitureEnnemie2()
                object_npc.append((omg_an_obstacle.rect, (randint(road.bordure,longueur-(road.bordure+omg_an_obstacle.width)),-150), omg_an_obstacle.damage, omg_an_obstacle.carburantAdd, omg_an_obstacle.appearence, omg_an_obstacle.speed))
            elif randint(0,3*(count2+1)) == 1:
                omg_an_obstacle.jerrycan()
                object_npc.append((omg_an_obstacle.rect, (randint(road.bordure,longueur-(road.bordure+omg_an_obstacle.width)),-50), omg_an_obstacle.damage, omg_an_obstacle.carburantAdd, omg_an_obstacle.appearence, omg_an_obstacle.speed))    
                
        #Init Images
        this_is_not_an_npc.get_stats()
        screen.blit(game_background, (0,0+coordonnees_background))
        screen.blit(game_background, (0,500+coordonnees_background))
        screen.blit(game_background, (0,-500+coordonnees_background))
        this_is_not_an_npc.rect.move_ip(this_is_not_an_npc.x,this_is_not_an_npc.y)
        screen.blit(this_is_not_an_npc.appearence,this_is_not_an_npc.rect)


        #Speed Reduction Timer
        #Test
        #print(speed_timer)
        if speed_timer > 0:
            speed_timer -= 1
            #Test
            #print(speed_timer)
        if speed_timer == 0:
            speed_purcentage = 1

        #Game Over Test
        if this_is_not_an_npc.crash!=1:

            #Move the road
            coordonnees_background+=1
            numberScore+=0.125
            if coordonnees_background==500:
                coordonnees_background=0
            if numberScore%2 == 0:
                score+=1
                road.get_score(score)
                
            #Npc Movement System
            movement_obstacles = 0
            for i in object_npc:     
                #Test
                #screen.blit(i[4],i[1])
                #i[0].center = i[1][0],i[1][1]+1
                #print(object_npc[movement_obstacles])
                #                i[0].center = i[1][0],i[1][1]+1
                #i[0].move_ip(0,1)
                
                if not object_npc[movement_obstacles][0].colliderect(object_npc[movement_obstacles-1][0]) and not object_npc[movement_obstacles-0][0].colliderect(object_npc[movement_obstacles-2][0]):    
                    object_npc[movement_obstacles] = (i[0], (i[1][0],i[1][1]+1), i[2], i[3], i[4], i[5])                    
                    screen.blit(i[4],i[1])
                    #Test
                    #object_npc[movement_obstacles] = (i[0], (i[1][0],i[1][1]+1), i[2], i[3], i[4], i[5]) 
                    #i[0].center = i[1][0],i[1][1]+1
                    
                movement_obstacles += 1
                
                #Test
                #print(i[0][1])z
                #i[0].center = i[1][0],i[1][1]
                #Collision Objects
                #print("rect",i[0])
                
                #Collision Area
                if i[2] == 25:
                    i[0].center = i[1][0]+24,i[1][1]+24
                if i[3] !=0:
                    i[0].center = i[1][0]+17,i[1][1]+18
                if i[5] ==0.3:
                    i[0].center = i[1][0]+81,i[1][1]+20
                if i[5] ==0.8:
                    i[0].center = i[1][0]+34,i[1][1]+87
                if i[5] ==0.9:
                    i[0].center = i[1][0]+34,i[1][1]+70
                #Debug Collision Area aka Hitbox
                #pygame.draw.rect(screen, (128,128,128), i[0], 1)
                #pygame.draw.rect(screen, (128,128,128), this_is_not_an_npc.get_pos(), 1)
                
                #Collision System
                if this_is_not_an_npc.the_incredible_collision(i[0]) and collision == False:
                    #Test
                    #collision=True
                    #print("hp before",hp)
                    #print('damage need', i[2])
                    
                    result = road.gestion_PdV(i[2],hp,this_is_not_an_npc.crash)
                    #Debug Hp System
                    #print("hp after",result[0])
                    hp = result[0]
                    this_is_not_an_npc.crash = result[1]
                    
                    #Carburant
                    if i[3] != 0:
                        carburant.play()
                        del object_npc[movement_obstacles-1]
                        if (fuel + i[3]) <= 1.0:
                          fuel += i[3]
                          
                    #Plots   
                    if i[5] != 1:
                        speed_timer += 5
                        speed_purcentage = i[5]                       
                          
                    #WoodBox         
                    if i[2] == 25:
                        wood.play()
                        del object_npc[movement_obstacles-1]

                    #Vehicles
                    if i[2] == 75:
                        crash.play()
                        #print(object_npc[movement_obstacles-1])
                        object_npc[movement_obstacles-1] = (object_npc[movement_obstacles-1][0], object_npc[movement_obstacles-1][1], 0,object_npc[movement_obstacles-1][3], object_npc[movement_obstacles-1][4], object_npc[movement_obstacles-1][5])
                        time.sleep(0.1)
                        del object_npc [movement_obstacles-1]
                        
                #Object Despawn | When Out Of Screen
                if i[0][1] >= 1000:
                    del object_npc [movement_obstacles-1]

            #Player movement
            #Test
            #print("speed pourcentage:",speed_purcentage)
            this_is_not_an_npc.moving(speed_purcentage)

            #Collision Bordure
            if this_is_not_an_npc.x<=road.bordure:
                this_is_not_an_npc.move_right(1)
            elif this_is_not_an_npc.x>=longueur-(road.bordure+this_is_not_an_npc.width):
                this_is_not_an_npc.move_left(1)

            #Collision | Car Out Of Screen
            if this_is_not_an_npc.y>=hauteur:
                crash.play()
                this_is_not_an_npc.crash=1
            elif this_is_not_an_npc.y<=-25:
                crash.play()
                this_is_not_an_npc.crash=1
            
            #Fuel System
            result  = road.gestion_fuel(fuel,this_is_not_an_npc.crash)
            fuel = result[0]
            this_is_not_an_npc.crash = result[1]

        #Crash Menu & stuff
        else :
            
            #Game Over BG & Title & Buttons
            screen.blit(this_is_not_an_npc.game_over(),(this_is_not_an_npc.x,this_is_not_an_npc.y))
            road.game_over(screen)
            road.button1(screen)
            road.button2(screen)
            road.button3(screen)
            
            #LeaderBoard Score Saving
            
            #Playername Management System
            if PlayerName == "Type your name.." or PlayerName == "":
                nameRandom = 'Anonyme-'
                for i in range(2):
                    nameRandom = nameRandom + str(choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'))
                PlayerName=nameRandom
                
            #Database Loading
            if databaseDone !=True:
                listeJoueurs = []
                with open('database.csv', newline='', encoding='utf-8') as csvfile:
                    reader = csv.DictReader(csvfile, delimiter=',')
                    for row in reader:
                        listeJoueurs.append(dict(row))
                        
                #Adding the new Player
                listeTest=[]
                userExist=False
                for Users in listeJoueurs:
                    for i in Users.values():
                        numberTestListe=0
                        listeTest.append(i)
                        if i == PlayerName:
                            userExist=True   
                        if userExist:
                            for i in listeTest:
                                #Test
                                #print("test de i", i)
                                #print("valuer de nbr", numberTestListe)
                                if i == PlayerName:
                                    #Test
                                    #print("i selected ",i)
                                    #print("score i ",listeTest[numberTestListe-1])
                                    if score < int(listeTest[numberTestListe-1])  :
                                        testDatabasePassed=False     
                                numberTestListe+=1    
                #CSV Rewrite
                if testDatabasePassed:
                    listeJoueurs.append({"score": score, "nom": PlayerName})
                                
                with open('database.csv', 'w', newline='') as csvfile:
                    fieldnames = ['score', 'nom']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                    writer.writeheader()
                    for i in range(len(listeJoueurs)):
                        #Test
                        #print("test de l'etat de la liste", listeJoueurs[i])
                        writer.writerow(listeJoueurs[i])
                databaseDone = True
                
            #Rest Variables | For A New Game
            active = False
            typedText = 'Type your name..'
            charLimit = 0
            limit = 10
            
            #Game Over Button Interaction
            x,y=pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                
                #Leaderboard Button
                if road.button1(screen).collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    leaderboard=True
                    databaseNeedLoad=True
                    roadCreate = False
                    jeu=False
                    databaseDone = False
                    speed_timer = 0
                    speed_purcentage = 0
                    this_is_not_an_npc.__init__()
                    road.__init__()
                    object_npc = []
                    
                #Main Menu Button
                elif road.button2(screen).collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    menu=True
                    jeu=False
                    mainMenu = True
                    #Reset
                    roadCreate = False
                    databaseDone = False
                    speed_timer = 0
                    speed_purcentage = 0
                    this_is_not_an_npc.__init__()
                    road.__init__()
                    object_npc = []
                    
                #Quit Button
                elif road.button3(screen).collidepoint(x,y) and event.type == MOUSEBUTTONDOWN and event.button == 1:
                    continuer=False
                    jeu=False
        #Quit System
        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False
                jeu=False

        #Interface Management
        
        #NavBar Game
        navBar = the_interface.navBar(screen, longueur)
        #Hearts Management
        # jusqu'a 100 | modifier en fonction du joueur
        the_interface.heartSystem(screen, hp, 0, 10, "Images/Full_Heart.png", "Images/Half_Heart.png", "Images/Empty_Heart.png")
        
        #Fuel System
        the_interface.carburantSystem(screen, "Images/Fuel_tank_13x15.png", fuel)
        
        #Score System
        the_interface.scoreSystem(screen, score)
        
        #Effect System
        the_interface.effectSystem(screen, speed_timer)
        
        #Display Update
        pygame.display.flip()

pygame.quit()