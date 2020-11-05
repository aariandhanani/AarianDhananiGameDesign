import pygame

pygame.init()

# Ask for and set width and height
width = int(input("Width: "))
height = int(input("Height: "))

screen = pygame.display.set_mode((width,height))


# Ask for and set Color
# screen.fill((R,G,B))

R = int(input("Red: "))
G = int(input("Green: "))
B = int(input("Blue: "))

screen.fill((R,G,B))

pygame.display.flip()
pygame.display.set_caption("Testing pygame")


run = True
