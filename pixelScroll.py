import pygame
#Pixel run will be an infinite running game where the player has to avoid obstacles.
#Original --> new scale is 1.5625
pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pixel Run")

walkRight = [pygame.image.load('WalkRight/1.png'), pygame.image.load('WalkRight/2.png'), pygame.image.load('WalkRight/3.png'), pygame.image.load('WalkRight/4.png')]
walkLeft = [pygame.image.load('WalkLeft/1.png'), pygame.image.load('WalkLeft/2.png'), pygame.image.load('WalkLeft/3.png'), pygame.image.load('WalkLeft/4.png')]
bg = pygame.image.load('pixelRun/newMenu2.png')
bg1 = pygame.image.load('pixelRun/newMenu2.png')
gameBG = pygame.image.load('pixelRun/gameBackgroundTesting.png')
menu1Images = [pygame.image.load('pixelRun/playNow.png'), pygame.image.load('pixelRun/Instructions.png'), pygame.image.load('pixelRun/Leaderboard.png'), pygame.image.load('pixelRun/quit.png')]


CharacterX = 50
CharacterY = 390
mouseX = 0
mouseY = 0
width = 40
height = 60
speed = 10
#to control the frames
clock = pygame.time.Clock()
menuOn = 1
gameOn = 0
selection = 0

backgroundX = 0
backgroundY = 0
backgroundSpeed = 15

Jump = False
high = 10
#control left and right move
left = False
right = False
#control my list
walkCount = 0

def redrawGameWindow():
    if menuOn == 0:
        global walkCount #it makes sure is using the global walkCount that created earlier

        screen.blit(gameBG, (0,backgroundY))
        if walkCount + 1 >= 12:
            walkCount = 0
        if left:
            screen.blit(walkLeft[walkCount//3], (x,y))
            walkCount += 1
        elif right:
            screen.blit(walkRight[walkCount//3], (x,y))
            walkCount += 1
        else:
            screen.blit(character, (x, y))
            walkCount = 0
        #screen.blit(character, (x, y))
        pygame.display.update()

run = True

screen.blit(bg, (0,backgroundY))
screen.blit(menu1Images[0], (162,161))
screen.blit(menu1Images[1], (162,319))
screen.blit(menu1Images[2], (162,477))
screen.blit(menu1Images[3], (162,635))
pygame.display.update()

while run:
    while menuOn == 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                #print(pygame.mouse.get_pos())
                (mouseX,mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX >= 162 and mouseX <= 639 and mouseY >= 161 and mouseY <= 270:
                    selection = 1
                    print(selection)
                    menuOn = 1
                    gameOn = 1
                elif mouseX >= 162 and mouseX <= 639 and mouseY >= 319 and mouseY <= 428:
                    selection = 2
                    print(selection)
                elif mouseX >= 162 and mouseX <= 639 and mouseY >= 477 and mouseY <= 586:
                    selection = 3
                    print(selection)
                elif mouseX >= 162 and mouseX <= 639 and mouseY >= 635 and mouseY <= 744:
                    selection = 4
                    print(selection)
                    
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    while gameOn == 1:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x > speed:
            #x -= speed
            left = True
            right = False
            backgroundY += backgroundSpeed
            screen.blit(bg, (0,backgroundY))
            #screen.blit(character, (x, y))

        elif keys[pygame.K_RIGHT] and x < WIDTH - speed - width:
            #x += speed
            left = False
            right = True
            backgroundY -= backgroundSpeed
            screen.blit(bg, (0,backgroundY))

        else:
            left = False
            right = False
            walkCount = 0

        if not(Jump):
            #if keys[pygame.K_UP] and y > speed:     # I need to substract to the y
                #y -= speed
            #if keys[pygame.K_DOWN] and y < HEIGHT - height - speed:    # I need to add to the y
                #y += speed
            if keys[pygame.K_SPACE]:
                Jump = True
                left = False
                right = False
                walkCount = 0
        else:
            if high >= -10:
                y -= (high * abs(high)) * 0.5
                high -= 1
            else:
                high = 10
                Jump = False


        #redrawGameWindow()

pygame.quit()

#Sources (I may or may not have used each one):
# https://stackoverflow.com/questions/16285889/pygame-mouse-get-pos-not-working/16286076
# https://www.pygame.org/docs/ref/mouse.html
# https://stackoverflow.com/questions/10990137/pygame-mouse-clicking-detection
# https://franuka.itch.io/
