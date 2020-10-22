import random
import time

#menu to agree and choose a game to play (topics)

score = 0
roundNumber = 1
option1 = 0
option2 = 0

playAgain = "yes"


gameWordsComputerScience = ['python', 'javascript', 'java', 'PHP', 'hardware', 'software', 'laptop', 'keyboard', 'monitor', 'PC', 'Dell', 'Apple', 'computer', 'charger', 'code']
gameWordsFruits = ['apple', 'banana', 'peach', 'blueberry', 'mango', 'strawberry', 'lemon', 'watermelon', 'cherry', 'orange', 'grapes', 'kiwi', 'pear', 'papaya', 'grapefruit']
gameWordsNintendoCharacters = ['Mario', 'Link', 'Luigi', 'Zelda', 'Diddy Kong', 'Peach', 'Donkey Kong', 'Bowser', 'Kirby', 'Bowser Jr.', 'Marth', 'Min Min', 'Daisy', 'Pikachu', 'Charizard']
gameWordsAppleProducts = ['iPhone', 'iPad', 'iMac', 'MacBook Pro', 'MacBook Air', 'MacBook', 'iPad Air', 'iPad Pro', 'HomePod', 'Apple Watch', 'Apple TV', 'Mac Pro', 'Mac Mini', 'iPad Mini', 'iMac Pro']

while option1 != "1" and option1 != "2": 
    print("____________________________________________________________")
    print("|                                                          |")
    print("|                 Welcome to Word Scramble                 |")
    print("|                     Choose an option                     |")
    print("|                                                          |")
    print("|                     1) Single Player                     |")
    print("|                     2) MultiPlayer                       |")
    print("|                                                          |")
    print("____________________________________________________________")

    option1 = input("Input: ")
    
    if option1 != "1" and option1 != "2":
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


        


print("Unscramble the word! You will be asked if you want to play again every 5 guesses.")

while playAgain == "yes":
    word = random.choice(gameWords)
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
            playAgain = input("Play again? ")
            roundNumber = 1
        else:
            roundNumber = roundNumber + 1
    else:
        score = score - 1
        print("Incorrect. The word was", word, "and your score is now", score)
        # playAgain = input("Play again? ")
        if roundNumber == 5:
            playAgain = input("Play again? ")
            roundNumber = 1
        else:
            roundNumber = roundNumber + 1

#sources:
# https://www.geeksforgeeks.org/python-random-sample-function/#:~:text=sample()%20is%20an%20inbuilt,for%20random%20sampling%20without%20replacement.
# https://pynative.com/python-random-sample/
