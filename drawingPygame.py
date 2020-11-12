import pygame

pygame.init()

screen = pygame.display.set_mode((1000,600)) # this is a tuple

# screen.fill((R,G,B))

background = pygame.image.load("brickWall copy.png")
image1 = pygame.image.load("TheMemesTournamentLogo copy.png")
screen.fill((113, 96, 255))
pygame.display.set_caption("My Shapes")

pygame.display.flip()

run = True

x = 200
y = 200
w = 50
h = 100
r = 50

def draw():
    screen.blit(background, (0,0))

    pygame.draw.rect(screen, ((96, 255, 125)), (x,y,w,h)) # window, color, position (x and y values where rectangle begins, width and height

    pygame.draw.circle(screen, ((255, 96, 96)), (500,500),r,100) # window, color, position, radius, thickness

    pygame.display.update()
    
while run:
    for event1 in pygame.event.get():
        if event1.type == pygame.QUIT:
            run = False
    #pygame.time.delay(1000)

    # x = 200
    # y = 200
    # w = 50
    # h = 100
    # pygame.draw.rect(screen, ((96, 255, 125)), (x,y,w,h)) # window, color, position (x and y values where rectangle begins, width and height
    pygame.display.update()

    # pygame.draw.circle(screen, ((255, 96, 96)), (400,400),50,400) # window, color, position, radius, thickness

    keyboardKey = pygame.key.get_pressed()

    speed = 20

    if keyboardKey[pygame.K_UP]:
        y = y - speed

    if keyboardKey[pygame.K_DOWN]:
        y = y + speed
         
    if keyboardKey[pygame.K_LEFT]:
        x = x - speed

    if keyboardKey[pygame.K_RIGHT]:
        x = x + speed

    if keyboardKey[pygame.K_a]:
        w = w - speed
        
    if keyboardKey[pygame.K_d]:
        w = w + speed

    if keyboardKey[pygame.K_w]:
        h = h - speed

    if keyboardKey[pygame.K_s]:
        h = h + speed
        
    if keyboardKey[pygame.K_r]:
        r = r + speed

    if keyboardKey[pygame.K_SPACE]:
        for i in range (40):
            y = y - 5
            screen.blit(background, (0,0))
            # screen.fill((113, 96, 255))
            pygame.draw.rect(screen, ((96, 255, 125)), (x,y,w,h))
            pygame.draw.circle(screen, ((255, 96, 96)), (500,500),r,100)
            pygame.display.update()
        for i in range (20):
            y = y + 10
            screen.blit(background, (0,0))
            # screen.fill((113, 96, 255))
            pygame.draw.rect(screen, ((96, 255, 125)), (x,y,w,h))
            pygame.draw.circle(screen, ((255, 96, 96)), (500,500),r,100)
            pygame.display.update()

    #screen.blit(tempSprite,b)



    if (y > (600-h)):
        y = (600-h)
    if (y < 0):
        y = 0
    if (x > (1000-w)):
        x = (1000-w)
    if (x < 0):
        x = 0

    draw()
    #screen.fill((113, 96, 255))
    

pygame.quit()

# https://htmlcolorcodes.com/
