# Note: Instead of using clock = pygame.time.clock(), I just have the same image next to each other in the list. I believe that this solves the frame issue.


import pygame

pygame.init()

# WIDTH = 960
# HEIGHT = 640

WIDTH = 1000
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # this is a tuple

# screen.fill((R,G,B))

walkLeft = [pygame.image.load("WalkLeft/1.png"), pygame.image.load("WalkLeft/1.png"), pygame.image.load("WalkLeft/2.png"), pygame.image.load("WalkLeft/2.png"), pygame.image.load("WalkLeft/3.png"), pygame.image.load("WalkLeft/3.png"), pygame.image.load("WalkLeft/4.png"), pygame.image.load("WalkLeft/4.png")]
walkRight = [pygame.image.load("WalkRight/1.png"), pygame.image.load("WalkRight/1.png"), pygame.image.load("WalkRight/2.png"), pygame.image.load("WalkRight/2.png"), pygame.image.load("WalkRight/3.png"), pygame.image.load("WalkRight/3.png"), pygame.image.load("WalkRight/4.png"), pygame.image.load("WalkRight/4.png")]

#background = pygame.image.load("brickWall copy.png")
background = pygame.image.load("modifiedMarioNew.png")

# image1 = pygame.image.load("1.png")
screen.fill((113, 96, 255))
pygame.display.set_caption("Game")

pygame.display.flip()

run = True
Jump = False
high = 10

backgroundX = 0

x = 100
y = 392
w = 50
h = 100
r = 50

leftImage = 0
rightImage = 0
leftOrRight = 1

# To control the frames
#clock = pygame.time.clock()

# control left and right movements. Instead of using this, I use leftOrRight
left = False
right = False

def redrawWindow():
    screen.blit(background, (backgroundX,0))
    if leftOrRight == 0:  
        screen.blit(walkLeft[leftImage], (x,y))
    else:
        screen.blit(walkRight[rightImage], (x,y))
    pygame.display.update()


while run:
    for event1 in pygame.event.get():
        if event1.type == pygame.QUIT:
            run = False

    #pygame.time.delay(100)

    
    pygame.display.update()


    keyboardKey = pygame.key.get_pressed()

    speed = 10

    #if keyboardKey[pygame.K_UP]:
        #y = y - speed

    #if keyboardKey[pygame.K_DOWN]:
        #y = y + speed
         
    if keyboardKey[pygame.K_LEFT] and x > speed:
        leftOrRight = 0
        if leftImage != 3:
            leftImage += 1
        else:
            leftImage = 0
        x = x - speed
        r = r - speed

    if keyboardKey[pygame.K_RIGHT] and x < WIDTH:
        leftOrRight = 1
        if rightImage != 3:
            rightImage += 1
        else:
            rightImage = 0
        x = x + speed
        r = r + speed

    #if keyboardKey[pygame.K_RIGHT] and x < WIDTH - w - speed:
        #leftOrRight = 1
        #if rightImage != 3:
            #rightImage += 1
        #else:
            #rightImage = 0
        #x = x + speed
        #r = r + speed
    

    if x > WIDTH:
        x = 400
        backgroundX = 1000

    if not(Jump):
        #if keyboardKey[pygame.K_UP] and y > speed:
            #y -= speed
        #if keyboardKey[pygame.K_DOWN] and y < HEIGHT - h - speed:
            #y += speed
        if keyboardKey[pygame.K_SPACE]:
            Jump = True
    else:
        if high >= -10:
            y -= ((high * abs(high)) / 2)
            high -= 1
        else:
            high = 10
            Jump = False

    redrawWindow()
    

pygame.quit()

# https://htmlcolorcodes.com/
