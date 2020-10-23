import random
import time

score = 0
roundNumber = 1
option1 = "0"
option2 = "0"
playGame = "1"
player = 1
player1score = 0
player2score = 0
numberOfRounds = 0

playAgain1 = "yes"
playAgain2 = "yes"

temporaryRound = 0


gameWordsComputerScience = ['python', 'javascript', 'java', 'PHP', 'hardware', 'software', 'laptop', 'keyboard', 'monitor', 'PC', 'Dell', 'Apple', 'computer', 'charger', 'code']
gameWordsFruits = ['apple', 'banana', 'peach', 'blueberry', 'mango', 'strawberry', 'lemon', 'watermelon', 'cherry', 'orange', 'grapes', 'kiwi', 'pear', 'papaya', 'grapefruit']
gameWordsNintendoCharacters = ['Mario', 'Link', 'Luigi', 'Zelda', 'Diddy Kong', 'Peach', 'Donkey Kong', 'Bowser', 'Kirby', 'Bowser Jr.', 'Marth', 'Min Min', 'Daisy', 'Pikachu', 'Charizard']
gameWordsAppleProducts = ['iPhone', 'iPad', 'iMac', 'MacBook Pro', 'MacBook Air', 'MacBook', 'iPad Air', 'iPad Pro', 'HomePod', 'Apple Watch', 'Apple TV', 'Mac Pro', 'Mac Mini', 'iPad Mini', 'iMac Pro']

def quitGame():
    exit()

while playGame == "1":
    score = 0
    roundNumber = 1
    option1 = "0"
    option2 = "0"
    playGame = "1"
    player = 1
    player1score = 0
    player2score = 0
    numberOfRounds = 0
    playAgain1 = "yes"
    playAgain2 = "yes"
    temporaryRound = 0
    
    # option1 = 0
    # option2 = 0
    while option1 != "1" and option1 != "2" and option1 != "3": 
        print("____________________________________________________________")
        print("|                                                          |")
        print("|                 Welcome to Word Scramble                 |")
        print("|                     Choose an option                     |")
        print("|                                                          |")
        print("|                     1) Single Player                     |")
        print("|                     2) Multiplayer                       |")
        print("|                     3) Exit                              |")
        print("|                                                          |")
        print("____________________________________________________________")

        option1 = input("Input: ")

        if option1 == "3":
            quitGame()
        
        if option1 != "1" and option1 != "2" and option1 != "3":
            print("Please enter a valid input")


    while option2 != "1" and option2 != "2" and option2 != "3" and option2 != "4": 
        print("____________________________________________________________")
        print("|                                                          |")
        print("|                 Welcome to Word Scramble                 |")
        print("|                     Choose an option                     |")
        print("|                                                          |")
        print("|                  1) Computer Science                     |")
        print("|                  2) Fruits                               |")
        print("|                  3) Nintendo Characters                  |")
        print("|                  4) Apple Products                       |")
        print("|                                                          |")
        print("____________________________________________________________")

        option2 = input("Input: ")
        
        if option2 != "1" and option2 != "2" and option2 != "3" and option2 != "4":
            print("Please enter a valid input")

    if option2 == "1":
        option2 = gameWordsComputerScience

    if option2 == "2":
        option2 = gameWordsFruits

    if option2 == "3":
        option2 = gameWordsNintendoCharacters

    if option2 == "4":
        option2 = gameWordsAppleProducts

    if option1 == "1":
        print("Unscramble the word! You will be asked if you want to play again every 5 guesses.")
        while playAgain1 == "yes":
            word = random.choice(option2)
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
    else:
        player1score = 0
        player2score = 0
        player = 1
        
        print("Unscramble the word! Each player will have 5 guesses per round.")
        
        while playAgain2 == "yes":
            numberOfRounds = input("How many rounds would each player like to play? ")
            try:
                numberOfRounds = int(numberOfRounds)
            except ValueError:
                print("Invalid input! The number of rounds will be set to 1.")
                numberOfRounds = 1
            totalRounds = numberOfRounds
            while numberOfRounds != 0:
                if player == 1:
                    roundNumber = 1
                    print("_________________________Player 1_________________________")
                    print("Round", (1 + int(totalRounds)) - int(numberOfRounds))
                    while player == 1 and roundNumber <= 5:
                        word = random.choice(option2)
                        k = len(word)
                        scrambled = random.sample(word, k)
                        scramble = ""

                        for number in range(0, k):
                            scramble = scramble + scrambled[number]

                        print(scramble)
                        answer = input("Guess the word! ")
                        if answer == word:
                            player1score = player1score + 1
                            print("Correct! Your score is now", player1score)
                            # playAgain = input("Play again? ")
                            if roundNumber >= 5:
                                roundNumber = 10
                                player = 2
                            else:
                                roundNumber = roundNumber + 1
                        else:
                            player1score = player1score - 1
                            print("Incorrect. The word was", word, "and your score is now", player1score)
                            # playAgain = input("Play again? ")
                            if roundNumber >= 5:
                                roundNumber = 10
                                player = 2
                            else:
                                roundNumber = roundNumber + 1
                else:
                    roundNumber = 1
                    print("_________________________Player 2_________________________")
                    print("Round", (1 + int(totalRounds)) - int(numberOfRounds))
                    while player == 2 and roundNumber <= 5:
                        word = random.choice(option2)
                        k = len(word)
                        scrambled = random.sample(word, k)
                        scramble = ""

                        for number in range(0, k):
                            scramble = scramble + scrambled[number]

                        print(scramble)
                        answer = input("Guess the word! ")
                        if answer == word:
                            player2score = player2score + 1
                            print("Correct! Your score is now", player2score)
                            # playAgain = input("Play again? ")
                            if roundNumber >= 5:
                                roundNumber = 10
                                player = 1
                                numberOfRounds = numberOfRounds - 1
                            else:
                                roundNumber = roundNumber + 1
                        else:
                            player2score = player2score - 1
                            print("Incorrect. The word was", word, "and your score is now", player2score)
                            # playAgain = input("Play again? ")
                            if roundNumber >= 5:
                                roundNumber = 10
                                player = 1
                                numberOfRounds = numberOfRounds - 1
                            else:
                                roundNumber = roundNumber + 1
            if numberOfRounds == 0:
                print("_________________________Final scores_________________________")
                print("Player 1:", player1score)
                print("Player 2:", player2score)

                if player1score > player2score:
                    print("Player 1 wins!")
                elif player2score > player1score:
                    print("Player 2 wins!")
                else:
                    print("It's a tie!")

                playAgain2 = input("Would you like to play again? ")

#sources:
# https://www.geeksforgeeks.org/python-random-sample-function/#:~:text=sample()%20is%20an%20inbuilt,for%20random%20sampling%20without%20replacement.
# https://pynative.com/python-random-sample/
