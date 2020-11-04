import pygame

# Drawing with Pygame
# ask the user to give you a color
# create the window with that color
# What is the width and height of the window

pygame.init()

screen = pygame.display.set_mode((800,600)) # this is a tuple

# screen.fill((R,G,B))

black = (0,0,0)
screen.fill((255,117,117))

pygame.display.flip()
pygame.display.set_caption("Testing pygame")
run = True

while run:
    pygame.time.delay(1000)

    screen.fill((130,117,255))

    pygame.display.update()

    for event1 in pygame.event.get():
        print(event1)
        if event1.type == pygame.QUIT:
            run = False
pygame.time.delay(50)
pygame.quit()
