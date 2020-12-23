#Aarian Dhanani
#Pixel run is an infinite running game where the player can try to avoid obstacles. There are 3 difficulty settings as well as a leaderboard.

import pygame
import random
from pygame.locals import *

#Left column = 137px
#Right column = 537px

#Starting the program
pygame.init()
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Pixel Run")

#Getting images
character = [pygame.image.load('pixelRun/character1.png'), pygame.image.load('pixelRun/character1.png'), pygame.image.load('pixelRun/character1.png'), pygame.image.load('pixelRun/character1.png'), pygame.image.load('pixelRun/character2.png'), pygame.image.load('pixelRun/character2.png'), pygame.image.load('pixelRun/character2.png'), pygame.image.load('pixelRun/character2.png'), pygame.image.load('pixelRun/character3.png'), pygame.image.load('pixelRun/character3.png'), pygame.image.load('pixelRun/character3.png'), pygame.image.load('pixelRun/character3.png'), pygame.image.load('pixelRun/character4.png'), pygame.image.load('pixelRun/character4.png'), pygame.image.load('pixelRun/character4.png'), pygame.image.load('pixelRun/character4.png')]
bg = pygame.image.load('pixelRun/newMenu2.png')
gameBG = pygame.image.load('pixelRun/gameBackgroundTesting.png')
alert = pygame.image.load('pixelRun/alert.png')
instructionsAlert = pygame.image.load('pixelRun/InstructionsAlert.png')
leaderboardAlert = pygame.image.load('pixelRun/leaderboard1.png')
menu1Images = [pygame.image.load('pixelRun/playNow.png'), pygame.image.load('pixelRun/Instructions.png'), pygame.image.load('pixelRun/Leaderboard.png'), pygame.image.load('pixelRun/quit.png')]
items = [pygame.image.load('pixelRun/riverAndOtherStuff.png'), pygame.image.load('pixelRun/item1.png'), pygame.image.load('pixelRun/item2.png'), pygame.image.load('pixelRun/item3.png')]
difficultyOption = [pygame.image.load('pixelRun/Easy.png'), pygame.image.load('pixelRun/Medium.png'), pygame.image.load('pixelRun/Hard.png')]
newLeaderboardScoreAlert = pygame.image.load('pixelRun/newLeaderboardScoreAlert.png')

#Defines the variable "white"
white = (255,255,255)

#Controls the menu
menuOn = 1

#Controls the score
score = 0

#Controls the character
CharacterX = 137
CharacterY = 526
frame = 0

#Variables for mouse position
mouseX = 0
mouseY = 0

#Controls items
itemOn = 0
itemX = 0
itemY = -417
itemNumber = 0

#Controls the background and background speed also controls item speeds
backgroundX = 0
backgroundY = -3200
backgroundSpeed = 40

#This will display the score. It will also change the leaderboard if the score is in the top 3
def displayScore(score):
    name1 = ""
    score1 = ""
    name2 = ""
    score2 = ""
    name3 = ""
    score3 = ""
    global mouseX
    global mouseY
    global getPlayerName
    #Reading the file
    leaderboardFile = open("pixelRun/leaderboard.txt", "r")
    leaderboardFileText = leaderboardFile.readlines()
    name1 = leaderboardFileText[0]
    score1 = leaderboardFileText[1]
    name2 = leaderboardFileText[2]
    score2 = leaderboardFileText[3]
    name3 = leaderboardFileText[4]
    score3 = leaderboardFileText[5]
    leaderboardFile.close()
    #The if and two elif statements check if the score is eligible to be on the leaderboard
    if score > int(score1):
        name3 = name2
        score3 = score2
        name2 = name1
        score2 = score1
        name1 = ""
        score1 = score
        font = pygame.font.Font('pixelRun/PermanentMarker-Regular.ttf', 50)
        askPlayerName = "Please type 3 letters."
        text1 = font.render(askPlayerName, True, white)
        screen.blit(newLeaderboardScoreAlert, (99, 183))
        screen.blit(text1, (150, 284))
        pygame.display.update()
        getPlayerName = 0
        while getPlayerName != 3:
            #This next for loop is basically from https://stackoverflow.com/questions/14111381/how-to-get-text-input-from-user-in-pygame
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    if evt.unicode.isalpha():
                        name1 = name1 + evt.unicode
                        getPlayerName = getPlayerName + 1
        leaderboardFile = open("pixelRun/leaderboard.txt", "w")
        newLeaderboardFileText = name1 + "\n" + str(score1) + "\n" + name2 + str(score2) + name3 + str(score3)
        leaderboardFile.write(newLeaderboardFileText)
        leaderboardFile.close()
    elif score > int(score2):
        name3 = name2
        score3 = score2
        name2 = ""
        score2 = score
        font = pygame.font.Font('pixelRun/PermanentMarker-Regular.ttf', 50)
        askPlayerName = "Please type 3 letters."
        text2 = font.render(askPlayerName, True, white)
        screen.blit(newLeaderboardScoreAlert, (99, 183))
        screen.blit(text2, (150, 284))
        pygame.display.update()
        getPlayerName = 0
        while getPlayerName != 3:
            #This next for loop is basically from https://stackoverflow.com/questions/14111381/how-to-get-text-input-from-user-in-pygame
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    if evt.unicode.isalpha():
                        name2 = name2 + evt.unicode
                        getPlayerName = getPlayerName + 1
        leaderboardFile = open("pixelRun/leaderboard.txt", "w")
        newLeaderboardFileText = name1 + str(score1) + name2 + "\n" + str(score2) + "\n" + name3 + str(score3)
        leaderboardFile.write(newLeaderboardFileText)
        leaderboardFile.close()
    elif score > int(score3):
        name3 = ""
        score3 = score
        font = pygame.font.Font('pixelRun/PermanentMarker-Regular.ttf', 50)
        askPlayerName = "Please type 3 letters."
        text3 = font.render(askPlayerName, True, white)
        screen.blit(newLeaderboardScoreAlert, (99, 183))
        screen.blit(text3, (150, 284))
        pygame.display.update()
        getPlayerName = 0
        while getPlayerName != 3:
            #This next for loop is basically from https://stackoverflow.com/questions/14111381/how-to-get-text-input-from-user-in-pygame
            for evt in pygame.event.get():
                if evt.type == KEYDOWN:
                    if evt.unicode.isalpha():
                        name3 = name3 + evt.unicode
                        getPlayerName = getPlayerName + 1
        leaderboardFile = open("pixelRun/leaderboard.txt", "w")
        newLeaderboardFileText = name1 + str(score1) + name2 + str(score2) + name3 + "\n" + str(score3) + "\n"
        leaderboardFile.write(newLeaderboardFileText)

        leaderboardFile.close()

    #Sends the score alert
    alertOn = 1
    while alertOn == 1:
        font = pygame.font.Font('pixelRun/PermanentMarker-Regular.ttf', 50)
        scoreWords = "Your score was " + str(score) + "!"
        text = font.render(scoreWords, True, white)
        screen.blit(alert, (99, 183))
        screen.blit(text, (172, 284))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                #print(pygame.mouse.get_pos())
                (mouseX,mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX >= 99 and mouseX <= 187 and mouseY >= 183 and mouseY <= 271:
                    alertOn = 0

#Allows for the selection of the game difficulty
def gameDifficulty():
    global backgroundSpeed
    gameDifficultyOn = 1
    backgroundSpeed = 1
    while gameDifficultyOn == 1:
        font = pygame.font.Font('pixelRun/PermanentMarker-Regular.ttf', 50)
        screen.blit(alert, (99, 183))
        screen.blit(difficultyOption[0], (225, 251))
        screen.blit(difficultyOption[1], (225, 356))
        screen.blit(difficultyOption[2], (225, 461))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                #print(pygame.mouse.get_pos())
                (mouseX,mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX >= 99 and mouseX <= 187 and mouseY >= 183 and mouseY <= 271:
                    gameDifficultyOn = 0
                elif mouseX >= 225 and mouseX <= 575 and mouseY >= 251 and mouseY <= 339:
                    backgroundSpeed = 10
                    gameDifficultyOn = 0
                elif mouseX >= 225 and mouseX <= 575 and mouseY >= 356 and mouseY <= 444:
                    backgroundSpeed = 20
                    gameDifficultyOn = 0
                elif mouseX >= 225 and mouseX <= 575 and mouseY >= 461 and mouseY <= 549:
                    backgroundSpeed = 40
                    gameDifficultyOn = 0

#Displays the instructions
def instructions():
    global mouseX
    global mouseY
    alertOn = 1
    while alertOn == 1:
        screen.blit(instructionsAlert, (99, 183))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                #print(pygame.mouse.get_pos())
                (mouseX,mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX >= 99 and mouseX <= 187 and mouseY >= 183 and mouseY <= 271:
                    alertOn = 0

#Displays the leaderboard
def leaderboard():
    global mouseX
    global mouseY
    name1 = ""
    score1 = ""
    name2 = ""
    score2 = ""
    name3 = ""
    score3 = ""
    textName1 = ""
    textName2 = ""
    textName3 = ""
    leaderboardOn = 1
    leaderboardFile = open("pixelRun/leaderboard.txt", "r")
    leaderboardFileText = leaderboardFile.readlines()
    name1 = leaderboardFileText[0]
    score1 = leaderboardFileText[1]
    name2 = leaderboardFileText[2]
    score2 = leaderboardFileText[3]
    name3 = leaderboardFileText[4]
    score3 = leaderboardFileText[5]
    leaderboardFile.close()
    while leaderboardOn == 1:
        font = pygame.font.Font('pixelRun/PermanentMarker-Regular.ttf', 60)
        textName1 = font.render(name1 + score1, True, white)
        textName2 = font.render(name2 + score2, True, white)
        textName3 = font.render(name3 + score3, True, white)
        screen.blit(leaderboardAlert, (99, 183))
        screen.blit(textName1, (256, 300))
        screen.blit(textName2, (256, 380))
        screen.blit(textName3, (256, 459))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                #print(pygame.mouse.get_pos())
                (mouseX,mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX >= 99 and mouseX <= 187 and mouseY >= 183 and mouseY <= 271:
                    leaderboardOn = 0

#To draw the game. This helps with some movement/animations
def redrawGameWindow():
    global menuOn
    if menuOn == 0:
        global frame
        global itemY
        global score
        frame = frame + 1
        if frame == 15:
            frame = 0
        screen.blit(gameBG, (0,backgroundY))
        if itemOn == 1:
            if itemNumber == 0:
                itemY = itemY + backgroundSpeed
                screen.blit(items[0], (0, itemY))
                if itemY >= 95 and itemY <= 673 and CharacterX == 537:
                    screen.blit(alert, (99, 183))
                    displayScore(score)
                    menuOn = 1
            if itemNumber == 1:
                if itemY == -417:
                    itemY = -288
                if itemColumn == 1:
                    itemX = 22
                else:
                    itemX = 421
                itemY = itemY + backgroundSpeed
                screen.blit(items[1], (itemX, itemY))
                if itemY >= 249 and itemY <= 673 and CharacterX == 137 and itemColumn == 1:
                    displayScore(score)
                    menuOn = 1
                if itemY >= 249 and itemY <= 673 and CharacterX == 537 and itemColumn == 2:
                    displayScore(score)
                    menuOn = 1
            if itemNumber == 2:
                if itemY == -417:
                    itemY = -314
                if itemColumn == 1:
                    itemX = 54
                else:
                    itemX = 453
                itemY = itemY + backgroundSpeed
                screen.blit(items[2], (itemX, itemY))
                if itemY >= 212 and itemY <= 673 and CharacterX == 137 and itemColumn == 1:
                    displayScore(score)
                    menuOn = 1
                if itemY >= 212 and itemY <= 673 and CharacterX == 537 and itemColumn == 2:
                    displayScore(score)
                    menuOn = 1
            if itemNumber == 3:
                if itemY == -417:
                    itemY = -258
                if itemColumn == 1:
                    itemX = 43
                else:
                    itemX = 443
                itemY = itemY + backgroundSpeed
                screen.blit(items[3], (itemX, itemY))
                if itemY >= 268 and itemY <= 671 and CharacterX == 137 and itemColumn == 1:
                    displayScore(score)
                    menuOn = 1
                if itemY >= 268 and itemY <= 671 and CharacterX == 537 and itemColumn == 2:
                    displayScore(score)
                    menuOn = 1

        if backgroundSpeed == 10:
            score = score + 1
        elif backgroundSpeed == 20:
            score = score + 2
        elif backgroundSpeed == 40:
            score = score + 4
        screen.blit(character[frame], (CharacterX, CharacterY))
        pygame.display.update()

#To keep the game running
run = True

#The main while loop
while run:
    #while the menu is running
    while menuOn == 1:
        #Draws the menu
        screen.blit(bg, (0,0))
        screen.blit(menu1Images[0], (162,161))
        screen.blit(menu1Images[1], (162,319))
        screen.blit(menu1Images[2], (162,477))
        screen.blit(menu1Images[3], (162,635))
        pygame.display.update()


        #Controls the character
        CharacterX = 137
        CharacterY = 526
        frame = 0

        #Controls items
        itemOn = 0
        itemX = 0
        itemY = -417
        itemNumber = 0

        #Controls the background and background speed also controls item speeds
        backgroundX = 0
        backgroundY = -3200
        backgroundSpeed = 1

        #Controls the score
        score = 0

        #Checking for mouse movement/click
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                #print(pygame.mouse.get_pos())
                (mouseX,mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX >= 162 and mouseX <= 639 and mouseY >= 161 and mouseY <= 270:
                    gameDifficulty()
                    menuOn = 0
                    if backgroundSpeed == 1:
                        menuOn = 1
                elif mouseX >= 162 and mouseX <= 639 and mouseY >= 319 and mouseY <= 428:
                    instructions()
                elif mouseX >= 162 and mouseX <= 639 and mouseY >= 477 and mouseY <= 586:
                    leaderboard()
                elif mouseX >= 162 and mouseX <= 639 and mouseY >= 635 and mouseY <= 744:
                    menuOn = 0
                    run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    #These if and elif statements can change the CharacterX variable which then will allow the character to be in a certain column
    if keys[pygame.K_LEFT]:
        CharacterX = 137
    elif keys[pygame.K_RIGHT]:
        CharacterX = 537

    #Changes backgroundY which will allow the background to scroll
    backgroundY += backgroundSpeed

    #Resets the backgroundY so that the background can continue to scroll
    if backgroundY >= 0:
        backgroundY = -3200
    screen.blit(gameBG, (0,backgroundY))

    #This is to turn on an item
    if backgroundY % 500 == 0 and itemOn == 0:
        itemOn = 1
        itemNumber = random.randrange(0, 4)
        itemColumn = random.randrange(1,3)

    #This is to turn off an item
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
# https://www.geeksforgeeks.org/random-numbers-in-python/
# https://www.geeksforgeeks.org/python-display-text-to-pygame-window/
# https://www.codespeedy.com/read-a-specific-line-from-a-text-file-in-python/
# https://stackoverflow.com/questions/14111381/how-to-get-text-input-from-user-in-pygame
# https://fonts.google.com/specimen/Permanent+Marker?sidebar.open=true&selection.family=Permanent+Marker
# https://limezu.itch.io/serenevillagerevamped
