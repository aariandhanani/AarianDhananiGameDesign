import pygame
import math
import random
import time

# setup display
pygame.init()
WIDTH, HEIGHT = 800, 800
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game! Press a in the menu for leaderboard file text.")

# setup  button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65

# set up fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

# load images.
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# game variables
hangman_status = 0
words = ["IDE", "REPLIT", "PYTHON", "PYGAME", "JAVA", "INT", "STRING"]
word = random.choice(words)
guessed = []

# colors
WHITE = (255,255,255)
BLACK = (0,0,0)
    
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

mouseX = 0
mouseY = 0
start_ticks=pygame.time.get_ticks()
difficulty = 0
menuOn = 1
menuBG = pygame.image.load("pixelRun/gameBackgroundTesting.png")
bgY = -3200

def draw():
    global menuOn
    global start_ticks
    global hangman_status
    global difficulty
    global bgY
    while menuOn == 1:
        win.blit(menuBG, (0,bgY))
        bgY = bgY + 2
        if bgY == 0:
            bgY = -3200
        text = TITLE_FONT.render("HANGMAN", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, 20)) # Notice centering
        text = TITLE_FONT.render("Try to guess the word!", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, 100)) # Notice centering
        
        pygame.draw.rect(win, BLACK, (200,200,400,100)) # window, color, position (x and y values where rectangle begins, width and height
        text = TITLE_FONT.render("Easy", 1, WHITE)
        win.blit(text, (WIDTH/2 - text.get_width()/2, 225)) # Notice centering
        
        pygame.draw.rect(win, BLACK, (200,350,400,100)) # window, color, position (x and y values where rectangle begins, width and height
        text = TITLE_FONT.render("Medium", 1, WHITE)
        win.blit(text, (WIDTH/2 - text.get_width()/2, 375)) # Notice centering
        
        pygame.draw.rect(win, BLACK, (200,500,400,100)) # window, color, position (x and y values where rectangle begins, width and height
        text = TITLE_FONT.render("Hard", 1, WHITE)
        win.blit(text, (WIDTH/2 - text.get_width()/2, 525)) # Notice centering

        pygame.draw.rect(win, BLACK, (200,650,400,100)) # window, color, position (x and y values where rectangle begins, width and height
        text = TITLE_FONT.render("Exit", 1, WHITE)
        win.blit(text, (WIDTH/2 - text.get_width()/2, 675)) # Notice centering

        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                #print(pygame.mouse.get_pos())
                (mouseX,mouseY) = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                if mouseX >= 200 and mouseX <= 600 and mouseY >= 200 and mouseY <= 300:
                    start_ticks=pygame.time.get_ticks()
                    difficulty = 1
                    menuOn = 0
                elif mouseX >= 200 and mouseX <= 600 and mouseY >= 350 and mouseY <= 450:
                    start_ticks=pygame.time.get_ticks()
                    difficulty = 2
                    menuOn = 0
                elif mouseX >= 200 and mouseX <= 600 and mouseY >= 500 and mouseY <= 600:
                    start_ticks=pygame.time.get_ticks()
                    difficulty = 3
                    menuOn = 0
                elif mouseX >= 200 and mouseX <= 600 and mouseY >= 650 and mouseY <= 750:
                    pygame.quit()
        keys = pygame.key.get_pressed()

        #These if and elif statements can change the CharacterX variable which then will allow the character to be in a certain column
        if keys[pygame.K_a]:
            leaderboardFile = open("leaderboard copy.txt", "r")
            leaderboardFileText = leaderboardFile.read()
            leaderboardFile.close()
            print(leaderboardFileText)
        pygame.display.update()


    else:
        win.fill(WHITE)

        # draw title
        text = TITLE_FONT.render("HANGMAN", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, 20)) # Notice centering

        # draw instructions
        text = TITLE_FONT.render("Try to guess the word!", 1, BLACK)
        win.blit(text, (WIDTH/2 - text.get_width()/2, 100)) # Notice centering

        # draw word
        display_word = ""
        for letter in word:
            if letter in guessed:
                display_word += letter + " "
            else:
                display_word += "_ "
        text = WORD_FONT.render(display_word, 1, BLACK)
        win.blit(text, (400, 200))

        # draw buttons
        for letter in letters:
            x, y, ltr, visible = letter
            if visible:
                pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
                text = LETTER_FONT.render(ltr, 1, BLACK)
                win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

        win.blit(images[hangman_status], (150, 100))

        if difficulty == 2:
            seconds = 60 - int((pygame.time.get_ticks()-start_ticks)/1000)
            text = TITLE_FONT.render(str(seconds), 1, BLACK)
            win.blit(text, (10, 50)) # Notice centering
            if seconds == 0:
                hangman_status = 6
        if difficulty == 3:
            seconds = 30 - int((pygame.time.get_ticks()-start_ticks)/1000)
            text = TITLE_FONT.render(str(seconds), 1, BLACK)
            win.blit(text, (10, 50)) # Notice centering
            if seconds == 0:
                hangman_status = 6
        pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status
    

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("You WON!")
            leaderboardFile = open("leaderboard copy.txt", "a")
            seconds = int((pygame.time.get_ticks()-start_ticks)/1000)
            leaderboardFile.write("\n" + str(seconds))
            leaderboardFile.close()

            pygame.quit()
            break

        if hangman_status == 6:
            display_message("You LOST!")
            pygame.quit()
            break

while True:

    main()
pygame.quit()

#Source:
#https://stackoverflow.com/questions/30720665/countdown-timer-in-pygame
