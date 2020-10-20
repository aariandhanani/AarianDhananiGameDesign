# Aarian Dhanani
# 10/16/20
# Simple game

import random
import time
#print("  _____\n  |   |\n  O   |\n /|\   |\n / \\  |\n      |\n  ____|")



#name = input("What is your name? ")
#print("Hello ", name)

gameWords = ['python', 'javascript', 'java', 'PHP', 'hardware', 'software', 'laptop', 'keyboard', 'monitor', 'PC', 'Dell', 'Apple']

# Use the choice method of the random function to pick a word

answer = input("Do you want to guess a word? ")
win = "no"
checkWord = ""

# Function to print the hangman image
def hangman(turns):
    if turns == 6:
        print("  _____\n  |   |\n      |\n      |\n      |\n      |\n  ____|")
    if turns == 5:
        print("  _____\n  |   |\n  O   |\n      |\n      |\n      |\n  ____|")
    if turns == 4:
        print("  _____\n  |   |\n  O   |\n  |   |\n      |\n      |\n  ____|")
    if turns == 3:
        print("  _____\n  |   |\n  O   |\n  |   |\n /    |\n      |\n  ____|")
    if turns == 2:
        print("  _____\n  |   |\n  O   |\n  |   |\n / \\  |\n      |\n  ____|")
    if turns == 1:
        print("  _____\n  |   |\n  O   |\n /|   |\n / \\  |\n      |\n  ____|")
    if turns == 0:
        print("  _____\n  |   |\n  O   |\n /|\  |\n / \\  |\n      |\n  ____|")
    
# Main while loop which makes sure that the user answers yes to play the game or to play again
while answer == "yes":
    word = random.choice(gameWords)
    guesses = ""
    turns = 6
    win = "no"

    # While loop to make sure that turns is greater than 0 and that the user hasn't won yet
    while turns > 0 and win == "no":
        if checkWord != word:
            hangman(turns)
            for char in word:
                if char in guesses:
                    print(char, end = "")
                    checkWord += char
                else:
                    print("_", end = "")
                    checkWord += "_"
            print()

            if checkWord == word:
                print("You win! You had", turns, " extra chances left!")
                win = "yes"
            else:
                guess = input("Guess a letter or word. ")

                guesses += guess
            
                if guess in word:
                    print("You have", turns, "extra chances left.")
                else:
                    turns-=1
                    print("You have", turns, "extra chances left.")
            
            if checkWord == word:
                win = "yes"
            else:
                checkWord = ""

            if turns == 0:
                hangman(turns)
                print("GAME OVER! The word was", word)
                
        else:
            turns = 0

    answer = input("Do you want to play again? ")

# word = random.choice(gameWords)
# print(word)

time.sleep(3)
# Sources:
# https://stackoverflow.com/questions/4877844/how-would-i-check-a-string-for-a-certain-letter-in-python
