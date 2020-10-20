# Aarian Dhanani
# 10/16/20
# Simple game

import random
import time

name = input("What is your name? ")
print("Hello ", name)

gameWords = ['python', 'javascript', 'java', 'PHP', 'hardware', 'software', 'laptop', 'keyboard', 'monitor', 'PC', 'Dell', 'Apple']

#use the choice method of the random function to pick a word

answer = input("Do you want to guess a word? ")
win = "no"
checkWord = ""

while answer == "yes":
    word = random.choice(gameWords)
    guesses = ""
    turns = 5
    win = "no"
    
    while turns > 0 and win == "no":
        if checkWord != word:
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
                print("GAME OVER! The word was", word)
        else:
            turns = 0


    answer = input("Do you want to play again? ")

# word = random.choice(gameWords)
# print(word)

time.sleep(3)
# Sources:
# https://stackoverflow.com/questions/4877844/how-would-i-check-a-string-for-a-certain-letter-in-python
