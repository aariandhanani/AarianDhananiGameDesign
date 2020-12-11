import pygame
#Pixel run will be an infinite running game where the player has to avoid obstacles.
#Original --> new scale is 1.5625

#Left column = 137px
#Right column = 537px

pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pixel Run")
 
character = [pygame.image.load('pixelRun/character1.png'), pygame.image.load('pixelRun/character1.png'), pygame.image.load('pixelRun/character1.png'), pygame.image.load('pixelRun/character1.png'), pygame.image.load('pixelRun/character2.png'), pygame.image.load('pixelRun/character2.png'), pygame.image.load('pixelRun/character2.png'), pygame.image.load('pixelRun/character2.png'), pygame.image.load('pixelRun/character3.png'), pygame.image.load('pixelRun/character3.png'), pygame.image.load('pixelRun/character3.png'), pygame.image.load('pixelRun/character3.png'), pygame.image.load('pixelRun/character4.png'), pygame.image.load('pixelRun/character4.png'), pygame.image.load('pixelRun/character4.png'), pygame.image.load('pixelRun/character4.png')]
bg = pygame.image.load('pixelRun/newMenu2.png')
bg1 = pygame.image.load('pixelRun/newMenu2.png')
gameBG = pygame.image.load('pixelRun/gameBackgroundTesting.png')
menu1Images = [pygame.image.load('pixelRun/playNow.png'), pygame.image.load('pixelRun/Instructions.png'), pygame.image.load('pixelRun/Leaderboard.png'), pygame.image.load('pixelRun/quit.png')]
items = [pygame.image.load('pixelRun/riverAndOtherStuff.png')]


CharacterX = 137
CharacterY = 526
frame = 0
mouseX = 0
mouseY = 0
width = 40
height = 60
speed = 10
#to control the frames
clock = pygame.time.Clock()
menuOn = 0
gameOn = 1
selection = 0
newCharacter = pygame.image.load('pixelRun/riverAndOtherStuff.png')
itemOn = 0
itemY = -417

backgroundX = 0
backgroundY = -3200
backgroundSpeed = 10
 
Jump = False
high = 10
#control left and right move
left = False
right = False
#control my list
walkCount = 0
 
def redrawGameWindow():
    if menuOn == 0:
        global frame
        global itemY
        frame = frame + 1
        if frame == 15:
            frame = 0
        screen.blit(gameBG, (0,backgroundY))
        if itemOn == 1:
            itemY = itemY + backgroundSpeed
            screen.blit(items[0], (0, itemY))
        screen.blit(character[frame], (CharacterX, CharacterY))
        pygame.display.update()
 
run = True
     
#screen.blit(gameBG, (0,backgroundY))
#screen.blit(menu1Images[0], (162,161))
#screen.blit(menu1Images[1], (162,319))
#screen.blit(menu1Images[2], (162,477))
#screen.blit(menu1Images[3], (162,635))
#pygame.display.update()

while run:          
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
     
    if keys[pygame.K_LEFT]:
        CharacterX = 137
    elif keys[pygame.K_RIGHT]:
        CharacterX = 537

    backgroundY += backgroundSpeed
    if backgroundY >= 0:
        backgroundY = -3200
    screen.blit(gameBG, (0,backgroundY))
    if backgroundY % 500 == 0:
        itemOn = 1
    if itemY > 800:
        itemOn = 0
        itemY = -417
        
        
    redrawGameWindow()
 
pygame.quit()

#Sources (I may or may not have used each one):
# https://stackoverflow.com/questions/16285889/pygame-mouse-get-pos-not-working/16286076
# https://www.pygame.org/docs/ref/mouse.html
# https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection
# https://franuka.itch.io/
