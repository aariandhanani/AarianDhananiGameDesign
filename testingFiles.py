# Aarian Dhanani
# 10/28/20
#
# Learning about files
#
# open/create
# close
# write "w"
# append "a"
# read "r"

import os, time

myFile = open("newFile.txt", "w") #Opens a file if it exists and if it doesn't exist it will create a file

myFile.write("Hello")

myFile.close()


myFile = open("newFile.txt", "r")

print(myFile.read())

myFile.close()


myFile = open("newFile.txt", "a")

myFile.write("\nOk")

myFile.close()


myFile = open("newFile.txt", "r")

print(myFile.read())

myFile.close()

time.sleep(1)
os.remove("newFile.txt")

if os.path.exists("2playergame.py"):
    print("yes")
else:
    print("no")

if os.path.exists("/Users/aariandhanani/Desktop/AarianGameDesign2020/AarianDhananiGameDesign/GameDesignDiscordBot/index.js"):
    print("yes")
else:
    print("no")

myFile = open("newFile.txt", "w")

for i in range(10):
    word = "This is line number " + str(i + 1) + "\n"
    myFile.write(word)

myFile.close()

myFile = open("newFile.txt", "r")

print(myFile.read())

myFile.close()

#Ask user for the name of the file to be created
#Ask the user for info to be saved in the file
#Create a menu where you ask if you want to create a file or delete a file or add something to a file or  write something to a file (with a warning), or print what is in a file
# https://www.guru99.com/reading-and-writing-files-in-python.html
