# Aarian Dhanani
# 10/16/20
# Simple game

import random
import time

name = input("What is your name? ")
print("Hello ", name)

gameWords = ['python', 'javascript', 'java', 'PHP', 'hardware', 'software', 'laptop', 'keyboard']

#use the choice method of the random function to pick a word

answer = input("Do you want to guess a word?")

while answer == "yes":
    word = random.choice(gameWords)
    guesses = ""
    turns = 5
    while turns > 0:
        for char in word:
            if char in guesses:
                print(char, end = "")
            else:
                print("_", end = "")
        print()
        guess = input("Guess a letter or word")
        guesses += guess
        turns-= 1
    
    answer= input("Do you want to play again?")

word = random.choice(gameWords)
print(word)

time.sleep(3)
