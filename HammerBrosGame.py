import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # this is a tuple

# screen.fill((R,G,B))

walkLeft = [pygame.image.load("WalkLeft/1.png"), pygame.image.load("WalkLeft/1.png"), pygame.image.load("WalkLeft/2.png"), pygame.image.load("WalkLeft/2.png"), pygame.image.load("WalkLeft/3.png"), pygame.image.load("WalkLeft/3.png"), pygame.image.load("WalkLeft/4.png"), pygame.image.load("WalkLeft/4.png")]
background = pygame.image.load("brickWall copy.png")
# image1 = pygame.image.load("1.png")
screen.fill((113, 96, 255))
pygame.display.set_caption("Game")

pygame.display.flip()

run = True
Jump = False
high = 10

x = 400
y = 400
w = 50
h = 100
r = 50

leftImage = 0

def redrawWindow():
    screen.blit(background, (0,0))
    screen.blit(walkLeft[leftImage], (x,y))
    pygame.display.update()


while run:
    for event1 in pygame.event.get():
        if event1.type == pygame.QUIT:
            run = False

    #pygame.time.delay(100)

    
    pygame.display.update()


    keyboardKey = pygame.key.get_pressed()

    speed = 5

    #if keyboardKey[pygame.K_UP]:
        #y = y - speed

    #if keyboardKey[pygame.K_DOWN]:
        #y = y + speed
         
    if keyboardKey[pygame.K_LEFT] and x > speed:
        if leftImage != 3:
            leftImage += 1
        else:
            leftImage = 0
        x = x - speed
        r = r - speed

    if keyboardKey[pygame.K_RIGHT] and x < WIDTH - w - speed:
        x = x + speed
        r = r + speed

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
