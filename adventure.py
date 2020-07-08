from time import sleep as s
import random
import pygame
import time

pygame.init()
#intro define function
def mainintro():
    #sets the dimension of the window and loads in the background
    window = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption("Practice Game")
    background = pygame.image.load('pixel6.png')

    #Transforms the background to desired dimensions
    background = pygame.transform.scale(background, (1000, 500))
    def text_object(text, font):
        textSurface = font.render(text, True, (255,255,255))
        return textSurface, textSurface.get_rect()
    
    #The requirements for the text to be displayed such as text font, position, and size
    def message_displays(text):
        largeText = pygame.font.SysFont('comicsans',70)
        TextSurf, TextRect = text_object(text, largeText)
        TextRect.center = ((1000/2),(500/2))
        window.blit(TextSurf, TextRect)
        pygame.display.update()
    #Sets the class for buttons that has to be clicked to start the game, instructions, and exit the game
    class button():
        def __init__(self, color, x,y,width,height, text=''):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text

        def draw(self,win,outline=False):
            if outline:
                pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                
            pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
            
            if self.text!= '':
                font = pygame.font.SysFont('comicsans', 20)
                text = font.render(self.text, 1, (0,0,0))
                window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        #The mouse click position
        def click(self, pos):
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
            return False
    #Repeat for 4 buttons that is required
    class button2(button):
        def draw(self,win,outline=False):
            if outline:
                pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
            if self.text!= '':
                font = pygame.font.SysFont('comicsans', 20)
                text = font.render(self.text, 1, (0,0,0))
                window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    class button3(button):
        def draw(self,win,outline=False):
            if outline:
                pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
            if self.text!= '':
                font = pygame.font.SysFont('comicsans', 20)
                text = font.render(self.text, 1, (0,0,0))
                window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    class button4(button):
        def draw(self,win,outline=False):
            if outline:
                pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
            if self.text!= '':
                font = pygame.font.SysFont('comicsans', 20)
                text = font.render(self.text, 1, (0,0,0))
                window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
    #Draws the start window
    def redrawindow():
        background2 = pygame.image.load('pixel7.jpg')
        background2 = pygame.transform.scale(background2, (1000, 500))
        window.blit(background2, (0,0))
        message_displays("Adventure Run")
        buttonstart.draw((255,255,255, 155))
        buttonquit.draw((255,255,255, 155))
        buttoninstruction.draw((255,255,255, 155))
    buttonstart = button((255,255,255, 155), 450, 440, 80,50, 'START')
    buttonquit = button2((255,255,255, 155), 20, 440, 70,50, 'EXIT')
    buttoninstruction = button3((255,255,255, 155), 850, 440, 130,50, 'INSTRUCTIONS')
    buttonback = button4((255,255,255), 20, 440, 70,50, 'GO BACK')

    #The while loop before the game start so checks if the start button is clicked or not
    def whileintro():
        global read
        intro = True
        read = False
        while intro:
                redrawindow()
                for event in pygame.event.get():
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if buttonstart.click(pos):
                            print("GAME START")
                            intro = False
                            read=False
                        if buttonquit.click(pos):
                            print("QUIT")
                            intro=False
                            quit()
                        if buttoninstruction.click(pos):
                            print("INSTRUCTIONS")
                            read = True
                            intro = False
                    if event.type == pygame.MOUSEMOTION:
                        if buttonstart.click(pos):
                               buttonstart.color = (255,0,0, 155)
                        elif buttonquit.click(pos):
                                buttonquit.color = (255,0,0)
                        elif  buttoninstruction.click(pos):
                            buttoninstruction.color = (255,0,0)
                        else:
                            buttonstart.color = (255,255,255, 155)
                            buttonquit.color = (255,255,255, 155)
                            buttoninstruction.color = (255,255,255, 155)
                    if event.type == pygame.QUIT:
                        exit()
                pygame.display.update()
    whileintro()
    #When player presses the instrucition button
    while read:
            instruction = pygame.image.load('instruction.png')
            instruction = pygame.transform.scale(instruction, (1000, 500))
            window.blit(instruction, (0,0))
            buttonback.draw((0,255,0))
            pygame.display.update()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttonback.click(pos):
                        whileintro()
                if event.type == pygame.MOUSEMOTION:
                    if buttonback.click(pos):
                        buttonback.color = (255,0,0)
                    else:
                        buttonback.color = (255,255,255)        
mainintro()

#The music,display,animation and basically everything in the game

def main(): #main processes AND loops
    #Loads and plays the music
    pygame.mixer.pre_init(44100,16,2,4096)
    pygame.init()
    pygame.mixer.music.load("Arcade Game Music Type Beat (Hip-HopRB Instrumental).mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)
    score = 0

    #sets the dimension of the window and loads in the background
    window = pygame.display.set_mode((1000, 500))
    pygame.display.set_caption("Practice Game")
    background = pygame.image.load('pixel6.png')

    #Transforms the background to desired dimensions
    background = pygame.transform.scale(background, (1000, 500))

    #Loads all the jump animation
    jumpv1 = [pygame.image.load('adventurer-jump-00.png'),pygame.image.load('adventurer-jump-01.png'),pygame.image.load('adventurer-jump-02.png'),pygame.image.load('adventurer-jump-03.png'), pygame.image.load('adventurer-smrslt-00.png'),pygame.image.load('adventurer-smrslt-01.png'),pygame.image.load('adventurer-smrslt-02.png'),pygame.image.load('adventurer-smrslt-03.png')]
    jumpv2 = [pygame.image.load('adventurer-smrslt-00.png'),pygame.image.load('adventurer-smrslt-01.png'),pygame.image.load('adventurer-smrslt-02.png'),pygame.image.load('adventurer-smrslt-03.png')]
    jumpv3 = [pygame.image.load('adventurer-smrslt-00.png'),pygame.image.load('adventurer-smrslt-01.png'),pygame.image.load('adventurer-smrslt-02.png'),pygame.image.load('adventurer-smrslt-03.png')]
    jumpv4 = [pygame.image.load('adventurer-smrslt-00.png'),pygame.image.load('adventurer-smrslt-01.png'),pygame.image.load('adventurer-smrslt-02.png'),pygame.image.load('adventurer-smrslt-03.png')]
    jump = jumpv1+jumpv2+jumpv3+jumpv4

    #running animation
    run = [pygame.image.load('adventurer-run-00.png'), pygame.image.load('adventurer-run-01.png'),pygame.image.load('adventurer-run-02.png'),pygame.image.load('adventurer-run-03.png')]

    #sliding animation
    slide = [pygame.image.load('adventurer-slide-00.png'),pygame.image.load('adventurer-slide-01.png'),pygame.image.load('adventurer-stand-00.png'),pygame.image.load('adventurer-stand-01.png'),pygame.image.load('adventurer-stand-02.png')]

    #attacking animation
    firstattack = [pygame.image.load('adventurer-attack3-00.png'),pygame.image.load('adventurer-attack3-01.png'),pygame.image.load('adventurer-attack3-02.png'),pygame.image.load('adventurer-attack3-03.png'),pygame.image.load('adventurer-attack3-04.png'),pygame.image.load('adventurer-attack3-05.png')]
    secondattack = [pygame.image.load('adventurer-attack2-00.png'),pygame.image.load('adventurer-attack2-01.png'),pygame.image.load('adventurer-attack2-02.png'),pygame.image.load('adventurer-attack2-03.png'),pygame.image.load('adventurer-attack2-04.png'),pygame.image.load('adventurer-attack2-05.png')]
    thirdattack = [pygame.image.load('adventurer-attack1-00.png'),pygame.image  .load('adventurer-attack1-01.png'),pygame.image.load('adventurer-attack1-02.png'),pygame.image.load('adventurer-attack1-03.png'), pygame.image.load('adventurer-attack1-04.png')]
    attack = firstattack+secondattack+ thirdattack

    #falling animation
    falling = [pygame.image.load('adventurer-fall-00.png'), pygame.image.load('adventurer-fall-01.png')]                               

    #resizes all the adventuruer images to specified dimensions
    for i in range (20):
        jump[i] = pygame.transform.scale(jump[i],(90,90))
    for i in range(3):
        run[i] = pygame.transform.scale(run[i],(90,90))
    for i in range (4): 
        slide[i] = pygame.transform.scale(slide[i],(90,90))
    for i in range (1):
        falling[i] = pygame.transform.scale(falling[i],(90,90))
    for i in range(16):
        attack[i] = pygame.transform.scale(attack[i],(90,90))
        
    #Sets up the background for the scrolling effect
    background_x = 0
    background_2 = background.get_width()
    clock = pygame.time.Clock()
    
    def text_objects(text, font):
        textSurface = font.render(text, True, (0,0,0))
        return textSurface, textSurface.get_rect()

    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf',30)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((1000/2),(500/2))
        window.blit(TextSurf, TextRect)
        pygame.display.update()
    
    def death():
        message_display('You DIED   '+'score:'+str(score))
    class button():
        def __init__(self, color, x,y,width,height, text=''):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text

        def draw(self,win,outline=False):
            if outline:
                pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
                
            pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
            
            if self.text!= '':
                font = pygame.font.SysFont('comicsans', 20)
                text = font.render(self.text, 1, (0,0,0))
                window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

        def click(self, pos):
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
            return False
    class button2(button):
        def draw(self,win,outline=False):
            if outline:
                pygame.draw.rect(window, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            pygame.draw.rect(window, self.color, (self.x,self.y,self.width,self.height),0)
            if self.text!= '':
                font = pygame.font.SysFont('comicsans', 20)
                text = font.render(self.text, 1, (0,0,0))
                window.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def deathwindow():
        background2 = pygame.image.load('pixel7.jpg')
        background2 = pygame.transform.scale(background2, (1000, 500))
        window.blit(background2, (0,0))
        death()
        buttonstart.draw((0,0,255))
        buttonquit.draw((255,0,0))  
    buttonstart = button((255,0,0, 155), 450, 440, 80,50, 'START')
    buttonquit = button2((255,0,255, 155), 20, 440, 70,50, 'EXIT')
    #Fade effect on each level. Fills the screen with white then fades to black afterwards.
    def fade(width, height): 
        fade = pygame.Surface((width, height))
        fade.fill((0,0,0))
        for alpha in range(0,300):
            fade.set_alpha(alpha)
            fadein()
            window.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(2)
    def fadein():
        window.fill((255,255,255))
    #Repeat of the process above but backwards (black --> white)
    def fade2(width, height): 
        fade2 = pygame.Surface((width, height))
        fade2.fill((255,255,255))
        for alpha in range(0,300):
            fade2.set_alpha(alpha)
            fadein2()
            window.blit(fade2, (0,0))
            pygame.display.update()
            pygame.time.delay(2)
    def fadein2():
        window.fill((0,0,0))
    #This class is for the ghost monster that spawns in level 1 that can only be killed by the sword
    class ghost(object):
        ghost_animation = [pygame.image.load('imgg.png'),pygame.image.load('imgg.png')]
        def __init__(self, x,y,height):
            self.x = x
            self.y =y
            self.height = height
            self.hitbox = (x,y,100,100)
            self.count = 0
            
        def draw(self, window):
            if level >=1:
                self.hitbox_enemy = pygame.Rect(self.x, self.y, 45, 60)
            if self.count >=1:
                self.count = 0
            self.count +=1
            if level >=1:
                window.blit(pygame.transform.scale(self.ghost_animation[self.count], (45,60)), (self.x, self.y)) 
##                pygame.draw.rect(window, (255,0,0), self.hitbox_enemy, 2)

    #The class for the eyeball monster that spawns in level 2
    class eye(object):
        eye_load = pygame.image.load('obstc2.png')
        def __init__(self, x,y,width2, height2):
            self.x = x
            self.y =y
            self.hitbox_enemy = pygame.Rect(x,y,200,100)
            
        def draw(self, window):
            if level >=2:
                self.hitbox_enemy = pygame.Rect(self.x, self.y, 65, 65)
            if level >=2:
                window.blit(pygame.transform.scale(self.eye_load, (65,65)), (self.x, self.y)) 
##                pygame.draw.rect(window, (255,0,0), self.hitbox_enemy, 2)

    #The adventruer/main character
    class player(object):
        def __init__(self, x,y):
            self.vel = 0.5
            self.running = True
            self.jumping = True
            self.sliding = True
            self.attacking = True
            self.isJump = False
            self. jumps = True
            self.fall = True
            self.player_x = 40
            self.player_y = 378
            self.x = 40
            self.y = 378
            self.width = 378
            self.speed = 0.6
            self.jumpcount = 10
            self.jumpingcount = 0
            self.runcount = 0
            self.attackcount = 0
            self.slidecount = 0       
            self.fallspeed = 0.3
            self.fallingcount = 0
            self.hitbox_running = pygame.Rect(self.player_x,self.player_y,90,90)
            self.hitbox_sliding = pygame.Rect(45,self.player_y+47,65,45)
            self.hitbox_falling = pygame.Rect(self.player_x+30,self.player_y,35,80)
            self.hitbox_jumping = pygame.Rect(self.player_x+20,self.player_y+20,52,55)
            self.hitbox_attacking = pygame.Rect(58,405,47,70)
            self.hitbox_sword = pygame.Rect(108, 405, 20, 50)

        #The movement of the character
        def movement(self, window):
            time = 20
            pygame.time.delay(time)
            if self.runcount >= 3:
                self.runcount = 0

            if self.running == True:
                window.blit(run[self.runcount],(int(self.player_x),int(self.player_y)))
                self.runcount +=1
                self.hitbox_running = pygame.Rect(self.player_x+30,self.player_y+20,48,70)
##                pygame.draw.rect(window,(255,0,0),self.hitbox_running, 2)

            #If the down key is pressed
            if (keys[pygame.K_DOWN]):
                if self.player_y == 378:
                    self.running = False
                    if self.slidecount >= 4:
                        self.slidecount = 0
                    
                    if self.sliding:  
                        window.blit(slide[self.slidecount],(int(self.player_x),int(self.player_y)))
                        self.slidecount +=1
##                        pygame.draw.rect(window,(255,0,0),self.hitbox_sliding, 2)
            
                #If the down key is pressed mid air
                if (keys[pygame.K_DOWN]) and self.player_y < self.width:
                
                    self.running = False
                    self.jumping = False
                    self.fallspeed += 0.2

                    if self.fallingcount >= 1:
                        self.fallingcount = 0
                    if self.fall:
                        window.blit(falling[self.fallingcount], (int(self.player_x),int(self.player_y)))
                        self.hitbox_falling = pygame.Rect(self.player_x+30,self.player_y,35,80)
##                        pygame.draw.rect(window,(255,0,0),self.hitbox_falling, 2)                    
                        self.fallingcount +=1
                        
            #If "p" is pressed           
            if keys[pygame.K_p] :
                self.fallspeed = 0.3
                self.running = False
                self.jumping = False
                self.sliding = False
                self.fall = False

                if self.attackcount >= 16:
                        self.attackcount = 0
                    
                if self.attacking: 
                    window.blit(attack[self.attackcount],(int(self.player_x),int(self.player_y)))
                    self.attackcount += 1
                    self.hitbox_attacking = pygame.Rect(self.player_x+30,self.player_y+20,38,70)
                    self.hitbox_sword = pygame.Rect(self.player_x+72, self.player_y+20, 20, 50)
##                    pygame.draw.rect(window,(255,0,0),self.hitbox_attacking, 2)
##                    pygame.draw.rect(window,(255,0,0),self.hitbox_sword, 2)
                

            #If UP arrow is pressed 
            if keys[pygame.K_UP]:
                self.fallspeed = 0.3
                self.running = False
                if self.jumpingcount >= 20:
                    self.jumpingcount = 0
                    
                if self.jumping and self.player_y < self.width:  
                    window.blit(jump[self.jumpingcount],(int(self.player_x),int(self.player_y)))
                    self.hitbox_jumping = pygame.Rect((self.player_x+20),(self.player_y+20),52,55)
##                    pygame.draw.rect(window,(255,0,0),self.hitbox_jumping, 2)
                    self.jumpingcount +=1
                    self.fallspeed = 0.3

            #When each of the key is let gone of     
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.running = True
                    self.jumping = True
                    self.attacking = True
                    self.fallspeed = 0.3
                    
                if event.key == pygame.K_UP:
                    self.running=True
                if event.key == pygame.K_p:
                    self.running = True
                    self.jumping = True
                    self.sliding = True
                    self.fall = True
    pygame.time.set_timer(pygame.USEREVENT+5,random.randint(0, 3000))

    #Sets the class for most enemies and acts as\ the "parent class"
    class enemy(object):

        walkleft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]
        for i in range(10):
            walkleft[i] = pygame.transform.scale(walkleft[i],(70,70))
       
        def __init__(self,enemy_x,enemy_y, end):
            self.x = enemy_x
            self.y = enemy_y             
            self.end = end

            self.path = [self.x,self.end]
            self.walkcount = 0
            self.vel = 4
            self.hitbox = pygame.Rect(self.x,self.y-15,90,90)
            self.fireball_fire = True

        def draw_enemy(self,window):
            self.move()
            if self.walkcount+1 >= 33:
                self.walkcount = 0
                self.vel+=0.2
            #walking right
            if self.vel > 0 and level >= 3:
                window.blit(self.walkleft[self.walkcount//3], (self.x,self.y-15))
                self.walkcount += 1
            #walking left
            if self.vel < 0 and level >=3:
                window.blit(self.walkleft[self.walkcount//3], (self.x,self.y))
                self.walkcount -= 1
            if self.x < -100 and event.type == pygame.USEREVENT+5:
                self.x = 1050
            if level >= 3:
                self.hitbox = pygame.Rect(self.x+25,self.y-15,41,70)
    ##                pygame.draw.rect(window, (255,0,0),self.hitbox,2)
                
        def move(self):
            if self.vel > 0:
                #see if position + movement space is < the end, then it is able to move
                if self.x + self.vel < self.path[1]:
                    self.x -= self.vel
                #past end point and turns 180
                else:
                    self.vel = self.vel*-1
                    self.walkcount = 0
            #see if position is smaller than starting position
            else:
                if self.x - self.vel > self.path[0]:
                    #vel is already negative
                    self.x += self.vel
                else:
                   #Truns 180 agian
                   self.vel = self.vel* -1
                   self.walkcount = 0
    pygame.time.set_timer(pygame.USEREVENT+6,random.randint(0, 3000))

    #Sets the class for the sorcerer which shoots lightning
    class sorcerer(enemy):
            walkleft = [pygame.image.load('sorcerer_01.png'),pygame.image.load('sorcerer_01.png'),pygame.image.load('sorcerer_01.png'), pygame.image.load('sorcerer_02.png'),pygame.image.load('sorcerer_02.png'),pygame.image.load('sorcerer_02.png'),pygame.image.load('sorcerer_03.png'),pygame.image.load('sorcerer_03.png'),pygame.image.load('sorcerer_03.png'),pygame.image.load('sorcerer_04.png'),pygame.image.load('sorcerer_04.png'),pygame.image.load('sorcerer_04.png'),pygame.image.load('sorcerer_05.png'),pygame.image.load('sorcerer_05.png'),pygame.image.load('sorcerer_05.png'),pygame.image.load('sorcerer_06.png'),pygame.image.load('sorcerer_06.png'),pygame.image.load('sorcerer_06.png'),pygame.image.load('sorcerer_07.png'),pygame.image.load('sorcerer_07.png'),pygame.image.load('sorcerer_07.png'),pygame.image.load('sorcerer_08.png'),pygame.image.load('sorcerer_08.png'),pygame.image.load('sorcerer_08.png'),pygame.image.load('sorcerer_09.png'),pygame.image.load('sorcerer_09.png'),pygame.image.load('sorcerer_09.png')]
            for i in range (27):
                walkleft[i] = pygame.transform.scale(walkleft[i],(140,140))
            def draw_enemy(self,window):
                self.move()
                if self.walkcount >=27:
                    self.walkcount = 0
                #walking left
                if self.vel > 0 and level >= 1:
                    window.blit(self.walkleft[self.walkcount], (self.x,350))
                    self.walkcount += 1
                    self.vel+=0.008
                    pygame.display.update()
                    
                    if self.x < -120 and event.type == pygame.USEREVENT+6:
                        self.x = 1100
                    if level >=1:
                        self.hitbox = pygame.Rect(self.x+20,self.y-40,70,110)
##                        pygame.draw.rect(window, (255,0,0),self.hitbox,2)                
                        pygame.display.update()               
    pygame.time.set_timer(pygame.USEREVENT+7,random.randint(0, 3000))  

    #Sets the image for the wizard which is in the air
    class wizard(enemy):
        walkleft = [pygame.image.load('wizard-fly-forward_04.gif'), pygame.image.load('wizard-fly-forward_04.gif'), pygame.image.load('wizard-fly-forward_04.gif'), pygame.image.load('wizard-fly-forward_04.gif'), pygame.image.load('wizard-fly-forward_04.gif'), pygame.image.load('wizard-fly-forward_05.gif'), pygame.image.load('wizard-fly-forward_04.gif'), pygame.image.load('wizard-fly-forward_04.gif'), pygame.image.load('wizard-fly-forward_05.gif'), pygame.image.load('wizard-fly-forward_04.gif'), pygame.image.load('wizard-fly-forward_04.gif'), pygame.image.load('wizard-fly-forward_04.gif'), pygame.image.load('wizard-fly-forward_05.gif'),pygame.image.load('wizard-fly-forward_04.gif'), pygame.image.load('wizard-fly-forward_04.gif'),pygame.image.load('wizard-fly-forward_05.gif')]
        for i in range(16):
            walkleft[i] = pygame.transform.scale(walkleft[i],(70,70))  
        def draw_enemy(self,window):
            self.move()
            if self.walkcount >= 16:
                self.walkcount = 0
            #walking left
            if self.vel > 0 and level >= 1:
                window.blit(self.walkleft[self.walkcount], (self.x,370))
                if self.x < 800:
                    window.blit(self.walkleft[self.walkcount], (self.x,370))
                self.walkcount += 1
                self.vel+=0.002
                pygame.display.update()
                
            if self.x < -120 and event.type == pygame.USEREVENT+7:
                self.x = 1100
            if level >= 1:
                self.hitbox = (self.x+20,self.y-30,40,70)
##                pygame.draw.rect(window, (255,0,0),self.hitbox,2)
                pygame.display.update()


    pygame.time.set_timer(pygame.USEREVENT+7,random.randint(1000, 3000))

    #Sets the animation for the dragon at level 4 and is the final enemy
    class dragon(enemy):
        dragon_idle = [pygame.image.load('dragon_1.gif'), pygame.image.load('dragon_2.gif'), pygame.image.load('dragon_3.gif'), pygame.image.load('dragon_4.gif'), pygame.image.load('dragon_5.gif'), pygame.image.load('dragon_6.gif')]
        dragon_attack = [pygame.image.load('dragon_attack_1.gif'), pygame.image.load('dragon_attack_2.gif'), pygame.image.load('dragon_attack_3.gif'),pygame.image.load('dragon_attack_4.gif'),pygame.image.load('dragon_attack_5.gif'),pygame.image.load('dragon_attack_6.gif'),pygame.image.load('dragon_attack_7.gif'),pygame.image.load('dragon_attack_18.gif'),pygame.image.load('dragon_attack_9.gif'),pygame.image.load('dragon_attack_10.gif'),pygame.image.load('dragon_attack_11.gif'),pygame.image.load('dragon_attack_12.gif'),pygame.image.load('dragon_attack_13.gif'),pygame.image.load('dragon_attack_14.gif'),pygame.image.load('dragon_attack_15.gif'),pygame.image.load('dragon_attack_16.gif'),pygame.image.load('dragon_attack_17.gif'),pygame.image.load('dragon_attack_18.gif')]
        dragon_fire = [pygame.image.load('dragon_fire_1.gif'), pygame.image.load('dragon_fire_1.gif'),pygame.image.load('dragon_fire_2.gif'),pygame.image.load('dragon_fire_3.gif'),pygame.image.load('dragon_fire_4.gif'),pygame.image.load('dragon_fire_5.gif'),pygame.image.load('dragon_fire_6.gif'),pygame.image.load('dragon_fire_7.gif'),pygame.image.load('dragon_fire_8.gif'),pygame.image.load('dragon_fire_9.gif'),pygame.image.load('dragon_fire_10.gif'),pygame.image.load('dragon_fire_11.gif'),pygame.image.load('dragon_fire_12.gif'),pygame.image.load('dragon_fire_13.gif'),pygame.image.load('dragon_fire_14.gif'),pygame.image.load('dragon_fire_15.gif'),pygame.image.load('dragon_fire_16.gif'),pygame.image.load('dragon_fire_17.gif'),pygame.image.load('dragon_fire_18.gif')]
        walkleft = dragon_idle+dragon_attack+dragon_attack+dragon_fire
        for i in range (60):
            walkleft[i] = pygame.transform.scale(walkleft[i],(200,176))
        def draw_enemy(self,window):
            self.move()
            if self.walkcount >= 60:
                self.walkcount = 0
            #walking left
            if self.vel > 0 and level >= 4:
                window.blit(self.walkleft[self.walkcount], (self.x,300))
                self.walkcount += 1
                self.vel+=0.002
                pygame.display.update()
            if self.x < -120 and event.type ==  pygame.USEREVENT+7:
                self.x = 1100
            if level >= 4:
                self.hitbox = (self.x+87,self.y-60,54,100)
##                pygame.draw.rect(window, (255,0,0),self.hitbox,2)
                pygame.display.update()
                
    #The class for the fireball 
    class fireball(enemy):
        fireball_v1 = [pygame.image.load('fireball_1.gif'),pygame.image.load('fireball_2.gif'),pygame.image.load('fireball_3.gif'),pygame.image.load('fireball_4.gif'),pygame.image.load('fireball_5.gif'),pygame.image.load('fireball_6.gif'),pygame.image.load('fireball_7.gif'),pygame.image.load('fireball_8.gif'),pygame.image.load('fireball_9.gif'),pygame.image.load('fireball_10.gif')]
        fireball_v2 = [pygame.image.load('fireball_11.gif'),pygame.image.load('fireball_12.gif'),pygame.image.load('fireball_13.gif'),pygame.image.load('fireball_14.gif'),pygame.image.load('fireball_15.gif'),pygame.image.load('fireball_16.gif'),pygame.image.load('fireball_17.gif'),pygame.image.load('fireball_18.gif'),pygame.image.load('fireball_19.gif'),pygame.image.load('fireball_20.gif')]
        fireball_v3 = [pygame.image.load('fireball_21.gif'),pygame.image.load('fireball_22.gif'),pygame.image.load('fireball_23.gif'),pygame.image.load('fireball_24.gif'),pygame.image.load('fireball_25.gif'),pygame.image.load('fireball_26.gif'),pygame.image.load('fireball_27.gif'),pygame.image.load('fireball_28.gif'),pygame.image.load('fireball_29.gif'),pygame.image.load('fireball_30.gif')]
        fireball_v4 = [pygame.image.load('fireball_31.gif'),pygame.image.load('fireball_32.gif'),pygame.image.load('fireball_33.gif'),pygame.image.load('fireball_34.gif'),pygame.image.load('fireball_35.gif'),pygame.image.load('fireball_36.gif'),pygame.image.load('fireball_37.gif'),pygame.image.load('fireball_38.gif'),pygame.image.load('fireball_39.gif'),pygame.image.load('fireball_40.gif')]
        fireball_v5 = [pygame.image.load('fireball_41.gif'),pygame.image.load('fireball_42.gif'),pygame.image.load('fireball_43.gif'),pygame.image.load('fireball_44.gif'),pygame.image.load('fireball_45.gif'),pygame.image.load('fireball_46.gif'),pygame.image.load('fireball_47.gif'),pygame.image.load('fireball_48.gif'),pygame.image.load('fireball_49.gif'),pygame.image.load('fireball_50.gif')]
        fireball_v6 = [pygame.image.load('fireball_51.gif'),pygame.image.load('fireball_52.gif'),pygame.image.load('fireball_53.gif'),pygame.image.load('fireball_54.gif'),pygame.image.load('fireball_55.gif'),pygame.image.load('fireball_56.gif'),pygame.image.load('fireball_57.gif'),pygame.image.load('fireball_58.gif'),pygame.image.load('fireball_59.gif'),pygame.image.load('fireball_60.gif')]
        fireball_attack =  fireball_v1+ fireball_v2+ fireball_v3+ fireball_v4+ fireball_v5+ fireball_v6
        
        def draw_enemy(self,window):
            if self.walkcount >= 60:
                self.walkcount = 0
            #walking left
            if self.fireball_fire: 
                if self.vel > 0 and level >=1 and((keys[pygame.K_o] and fireball.hitbox[1] <= adventurer.player_y+31)) or self.x > -160:
                        self.hitbox = pygame.Rect(self.x+25,self.y,160,32)
##                        pygame.draw.rect(window, (255,0,0),self.hitbox,2)
                        self.x += self.vel+15
                        if self.x > 20:
                            window.blit(self.fireball_attack[self.walkcount], (self.x,410))
                            self.x += self.vel
                            self.walkcount += 1

    #Draws all of the images/animations on to the screen
    def keepdrawing():
        window.blit(background, (background_x,0))
        window.blit(background, (background_2,0))
        
        for draw_ghost in ghost_list:
            draw_ghost.draw(window)
        for draw_eye in eye_list:
            draw_eye.draw(window)

        adventurer.movement(window)
        attacker.draw_enemy(window)
        wizard.draw_enemy(window)
        dragon.draw_enemy(window)
        fireball.draw_enemy(window)
        sorcerer.draw_enemy(window)

        #Draws the score to the top right corner
        score_text = score_font.render("score: " + str(score), 3, (255,255,255))
        window.blit(score_text,(900,10))
        pygame.display.update()

    ghost_list = []
    eye_list = []

    #Sets the definition for the score such as font and size
    score_font = pygame.font.SysFont("Arial",15,True)

    #Makes instances of the enemies/attacks
    attacker = enemy(950,407,951)
    adventurer = player(40,387)
    wizard = wizard(905,407,951)
    dragon = dragon(905,407, 951)
    fireball = fireball(-160,407, 951)
    sorcerer = sorcerer(905,407,951)

    #Velocity of the background
    vel_background = 2
    #Timer for random spawns of monsters as well as score increase
    pygame.time.set_timer(pygame.USEREVENT+1,(10000))
    pygame.time.set_timer(pygame.USEREVENT+2,random.randint(3000, 5000))
    pygame.time.set_timer(pygame.USEREVENT+3,(100))

    run_program = True
    run_death = False
    level = 1
    #Main loop
    while run_program:
        clock.tick(60)
        #When the x coordinate becomes less than the width of the background, it switches position.
        background_x -= vel_background
        background_2 -= vel_background
        if background_x < background.get_width() * -1:
            background_x = background.get_width()
        if background_2 < background.get_width() * -1:
            background_2 = background.get_width()
        keys = pygame.key.get_pressed()

        #Sets the levels and if the score is between 100 and 110 it will transition into level 2
        if score >= 100 and score <= 110:
                level = 2
                attacker.vel = 5
                score+=11
                fade(1000,500)
                pygame.display.update()
                fade2(1000,500)
                score = 111
                background = pygame.image.load('Battleground1.png')
                background = pygame.transform.scale(background, (1000, 500))
                
        #Sets the levels and if the score is between 250 and 260 it will transition into level 3
        if score >= 250 and score <= 260:
                level = 3
                attacker.vel = 6
                score+=11
                fade(1000,500)
                pygame.display.update()
                fade2(1000,500)
                score = 261
                background = pygame.image.load('Battleground2.png')
                background = pygame.transform.scale(background, (1000, 500))
                
        #Sets the levels and if the score is between 400 and 410 it will transition into level 4
        if score >= 400 and score <= 410:
                level = 4
                attacker.vel = 7
                score+=11
                fade(1000,500)
                pygame.display.update()
                fade2(1000,500)
                score = 411
                background = pygame.image.load('Battleground4.png')
                background = pygame.transform.scale(background, (1000, 500))     


    #Checks the hitbox of the characters movement with the goblin
        if adventurer.player_y > 376:
            if adventurer.hitbox_running.colliderect(attacker.hitbox):
                    run_program = False
                    run_death = True

        if  (keys[pygame.K_p]):
            if adventurer.hitbox_sword.colliderect(attacker.hitbox)and event.type == pygame.USEREVENT+7:
                attacker.x = 1050

        if  (keys[pygame.K_DOWN]):
            if adventurer.player_y >= 377:
                if adventurer.hitbox_falling.colliderect(attacker.hitbox) or (adventurer.hitbox_sliding.colliderect(attacker.hitbox)):
                    run_program = False
                    run_death = True
                    print("hit")
                    
        if fireball.hitbox.colliderect(attacker.hitbox):
                attacker.x = 1050
                fireball.x = -160
                fireball.hitbox[0] = -160

    #Checks the hitox of the characters movement with the wizard 
        if adventurer.player_y > 376:
            if adventurer.hitbox_running.colliderect(wizard.hitbox):
                    run_program = False
                    run_death = True
                    print("hit")
 
        if fireball.hitbox.colliderect(wizard.hitbox):
                wizard.x = 1050
                fireball.hitbox[0] = -160
                fireball.x = -160
                print("lol")

        if  (keys[pygame.K_p]): 
            if adventurer.hitbox_sword.colliderect(wizard.hitbox):
                wizard.x = 1050

        if  (keys[pygame.K_DOWN]):
            if adventurer.player_y >= 377:
                if adventurer.hitbox_falling.colliderect(wizard.hitbox) or (adventurer.hitbox_sliding.colliderect(wizard.hitbox)):
                    run_program = False
                    run_death = True
                    print("hit")

    #Checks the hitboxes of the character with the attack/movement of the dragon
        if adventurer.player_y > 376:
            if adventurer.hitbox_running.colliderect(dragon.hitbox):
                    run_program = False
                    run_death = True
                    print("hit")

        if  (keys[pygame.K_p]):
            if adventurer.hitbox_sword.colliderect(dragon.hitbox):
                dragon.x = 1000
                score+=1

        if fireball.hitbox.colliderect(dragon.hitbox):
                dragon.x = 1050
                fireball.x = -160
                fireball.hitbox[0] = -160
        if  (keys[pygame.K_DOWN]):
            if adventurer.player_y >= 377:
                if adventurer.hitbox_falling.colliderect(dragon.hitbox) or (adventurer.hitbox_sliding.colliderect(dragon.hitbox)):
                    run_program = False
                    run_death = True
                    print("hit")

        if adventurer.player_y > 376:
            if adventurer.hitbox_running.colliderect(dragon.hitbox):
                    run_program = False
                    run_death = True
                    print("hit")

    #Checks the movements of the character with the hitboxes of the sorcerer
        if adventurer.player_y > 376:
            if adventurer.hitbox_running.colliderect(sorcerer.hitbox):
                    run_program = False
                    run_death = True

        if  (keys[pygame.K_p]):
            if adventurer.hitbox_sword.colliderect(sorcerer.hitbox):
                sorcerer.x = 1050

        if  (keys[pygame.K_DOWN]):
            if adventurer.player_y >= 377:
                if adventurer.hitbox_falling.colliderect(sorcerer.hitbox) or (adventurer.hitbox_sliding.colliderect(sorcerer.hitbox)):
                    run_program = False
                    run_death = True
                    print("hit")
        if fireball.hitbox.colliderect(sorcerer.hitbox):
                sorcerer.x = 1050
                sorcerer.hitbox[0] = 1050
                fireball.x = -160
                fireball.hitbox[0] = -160
                print("110")

    #For ever eyeball that is appended into its list it checks the hitboxes of the character and the eye and checks if they collide
        for draw_eye in eye_list:
            if adventurer.player_y > 376:
                if adventurer.hitbox_running.colliderect(draw_eye.hitbox_enemy):
                    run_program = False
                    run_death = True
                    print("hit")

            if  (keys[pygame.K_p]):
                if adventurer.hitbox_sword.colliderect(draw_eye.hitbox_enemy):
                    eye_list.pop(eye_list.index(draw_eye))
                    score+=1
                    
            if fireball.hitbox.colliderect(draw_eye.hitbox_enemy):
                eye_list.pop(eye_list.index(draw_eye))
                fireball.x = -160

            if  (keys[pygame.K_DOWN]):
                if adventurer.player_y >= 377:
                    if adventurer.hitbox_falling.colliderect(draw_eye.hitbox_enemy) or (adventurer.hitbox_sliding.colliderect(draw_eye.hitbox_enemy)):
                        run_program = False
                        run_death = True
                        print("hit")           
            draw_eye.x -=4
            if draw_eye.x < -100:
                eye_list.pop(eye_list.index(draw_eye))

    #For every ghost that is in the list, it checks for the if the ghost and the character collide 
        for draw_ghost in ghost_list:
            if adventurer.player_y > 376:
                if adventurer.hitbox_running.colliderect(draw_ghost.hitbox_enemy):
                    run_program = False
                    run_death = True
                    print("hit")
            if  (keys[pygame.K_p]):
                if adventurer.hitbox_sword.colliderect(draw_ghost.hitbox_enemy):
                    ghost_list.pop(ghost_list.index(draw_ghost))
                    score+=1

            draw_ghost.x -= 8
            if draw_ghost.x < -100:
               ghost_list.pop(ghost_list.index(draw_ghost))
           
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                exit()
            if event.type == pygame.USEREVENT+1:
                vel_background+=0.1
            if event.type == pygame.USEREVENT+2:
                r = random.randint(0,1)
                if r==0:
                    new_eye = eye(1050, 390, 64,64)
                    eye_list.append(new_eye)
                if r==1:
                    new_ghost = ghost(1050,390,64)
                    ghost_list.append(new_ghost)
            if event.type == pygame.USEREVENT+3:
                score+=1

        #The jumping feature
        if not(adventurer.isJump):
        
            if keys[pygame.K_UP]:
                adventurer.isJump =True
                
        else:
            
            if adventurer.jumpcount >= -10:
        
                neg=1
                if adventurer.player_y > adventurer.width:
                    adventurer.player_y = adventurer.width
                if adventurer.jumpcount <0:
                    neg = -1
    ##                s(0.01)
                adventurer.player_y -= (adventurer.jumpcount**2)*adventurer.fallspeed*neg*2
    ##            s(0.01)
                adventurer.jumpcount -=1
                
                if adventurer.player_y > adventurer.width:
                    adventurer.player_y=adventurer.width

            else:
                adventurer.isJump = False
                adventurer.jumpcount = 10
                if adventurer.player_y > adventurer.width:
                    player_y = adventurer.width
                    adventurer.fallspeed = 0.05
        keepdrawing()
    #Death loop
    while run_death:
            pygame.mixer.music.stop()
            clock.tick(60)
            deathwindow()
            pygame.display.update()
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if buttonstart.click(pos):
                        print("GAME START")
                        #Pressing start again will start main() all over again
                        main()
                    if buttonquit.click(pos):
                        print("QUIT")
                        quit()
                if event.type == pygame.MOUSEMOTION:
                    if buttonstart.click(pos):
                           buttonstart.color = (255,0,0, 155)
                    elif buttonquit.click(pos):
                            buttonquit.color = (255,0,0,155)
                    else:
                        buttonstart.color = (255,255,255)
                        buttonquit.color = (255,255,255)
                if event.type == pygame.QUIT:
                        exit()
#main is started
main()
