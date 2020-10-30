# Aarian Dhanani

option = 0

import random
import time

# Defining Variables
score = 0
roundNumber = 1
option = "0"
playGame = "1"
player = 1
player1score = 0
player2score = 0
numberOfRounds = 0

playAgain1 = "yes"

temporaryRound = 0

def computerSciencewords(gameArray):
    myFile = open("gameCategories.txt", "r")

    gameArray = myFile.read().splitlines()

    allLines = myFile.readlines()

    print(gameArray)

    print(gameArray[1])

    myFile.close()

    print(gameArray)

# Main menu with the games
while playGame == "1":
    gameArray = []
    score = 0
    roundNumber = 1
    option = "0"
    playGame = "1"
    player = 1
    player1score = 0
    player2score = 0
    numberOfRounds = 0
    playAgain1 = "yes"
    temporaryRound = 0

    # Menu 2 to select game category
    while option != "1" and option != "2" and option != "3" and option != "4" and option != "5":
        print("____________________________________________________________")
        print("|                                                          |")
        print("|                 Welcome to Word Scramble                 |")
        print("|                     Choose an option                     |")
        print("|                                                          |")
        print("|                  1) Computer Science                     |")
        print("|                  2) Fruits                               |")
        print("|                  3) Nintendo Characters                  |")
        print("|                  4) Apple Products                       |")
        print("|                  5) Exit Game                            |")
        print("|                                                          |")
        print("____________________________________________________________")

        option = input("Input: ")

        if option != "1" and option != "2" and option != "3" and option != "4" and option != "5":
            print("Please enter a valid input")

    if option == "1":
        gameArray = computerSciencewords(gameArray)

    # if option == "2":
    #     option = gameWordsFruits
    #
    # if option == "3":
    #     option = gameWordsNintendoCharacters
    #
    # if option == "4":
    #     option = gameWordsAppleProducts

    if option == "5":
        exit()

    # Single player
    print("Unscramble the word! You will be asked if you want to play again every 5 guesses.")
    while playAgain1 == "yes":
        word = random.choice(option)
        k = len(word)
        scrambled = random.sample(word, k)
        scramble = ""

        for number in range(0, k):
            scramble = scramble + scrambled[number]

        print(scramble)
        answer = input("Guess the word! ")
        if answer == word:
            score = score + 1
            print("Correct! Your score is now", score)
            # playAgain = input("Play again? ")
            if roundNumber == 5:
                playAgain1 = input("Type yes to play again. Type menu to return to the main menu. ")
                roundNumber = 1
            else:
                roundNumber = roundNumber + 1
        else:
            score = score - 1
            print("Incorrect. The word was", word, "and your score is now", score)
            # playAgain = input("Play again? ")
            if roundNumber == 5:
                playAgain1 = input("Type yes to play again. Type menu to return to the main menu. ")
                roundNumber = 1
            else:
                roundNumber = roundNumber + 1

# sources (I might have or might not have used each source):
# https://www.geeksforgeeks.org/python-random-sample-function/#:~:text=sample()%20is%20an%20inbuilt,for%20random%20sampling%20without%20replacement.
# https://pynative.com/python-random-sample/
# https://discuss.atom.io/t/block-indent/25676
# https://www.codespeedy.com/read-a-specific-line-from-a-text-file-in-python/#:~:text=This%20is%20the%20easiest%20way%20to%20read%20a,hold%20the%20lines%20as%20an%20Object%20all_lines%20
# https://stackoverflow.com/questions/12330522/how-to-read-a-file-without-newlines
# https://www.programiz.com/python-programming/methods/list/remove
# https://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index
