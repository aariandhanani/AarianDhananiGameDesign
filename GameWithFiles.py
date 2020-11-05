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

#Opens the file with the words
def computerSciencewords(gameArray):
    myFile = open("gameCategories.txt", "r")

    gameArray = myFile.read().splitlines()

    allLines = myFile.readlines()

    # print(gameArray)

    # print(gameArray[1])

    myFile.close()

    # print(gameArray)

    return gameArray

# Changes and prints the leaderboard
def leaderboard(score):
    alreadyDone = 0
    score = 2
    myFile2 = open("highScores.txt", "r")

    lines = []

    lines = myFile2.readlines()

    myFile2.close()

    myFile1 = open("highScores.txt", "w")

    for leaderboardChange in range (1,11):
        temporary = lines[leaderboardChange]
        if(score > int(temporary[0]) and alreadyDone == 0):
            name = input("What is your name? ")
            lines[leaderboardChange] = (str(score) + ": " + name + "\n")
            # print(lines)
            myFile1.writelines(lines)
            alreadyDone = 1
    myFile1.close()

    myFile3 = open("highScores.txt", "r")

    print(myFile3.read())

    myFile3.close()

    # print(lines)

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
    playAgain1 = "no"
    temporaryRound = 0

    # Prints the menu
    while option != "1" and option != "2" and option != "3":
        print("____________________________________________________________")
        print("|                                                          |")
        print("|                 Welcome to Word Scramble                 |")
        print("|                     Choose an option                     |")
        print("|                                                          |")
        print("|                  1) New Game                             |")
        print("|                  2) High Scores                          |")
        print("|                  3) Exit Game                            |")
        print("|                                                          |")
        print("____________________________________________________________")

        option = input("Input: ")

        if option != "1" and option != "2" and option != "3":
            print("Please enter a valid input")

    if option == "1":
        gameArray = computerSciencewords(gameArray)
        playAgain1 == "yes"


    if option == "2":
        myFile3 = open("highScores.txt", "r")

        print(myFile3.read())

        myFile3.close()

    if option == "3":
         exit()

    # Single player
    if playAgain1 == "yes":
        print("Unscramble the word! You will be asked if you want to play again every 5 guesses.")
    while playAgain1 == "yes":
        word = random.choice(gameArray)
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
                leaderboard(score)
                playAgain1 = input("Type yes to play again. Type menu to return to the main menu. ")
                score = 0
                roundNumber = 1
            else:
                roundNumber = roundNumber + 1
        else:
            score = score - 1
            print("Incorrect. The word was", word, "and your score is now", score)
            # playAgain = input("Play again? ")
            if roundNumber == 5:
                leaderboard(score)
                playAgain1 = input("Type yes to play again. Type menu to return to the main menu. ")
                score = 0
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
# https://stackoverflow.com/questions/4719438/editing-specific-line-in-text-file-in-python
