# Aarian Dhanani
# Lastest change to this program happened on October 30th, 2020

# ask the user for the name of the file to be created
# ask the user for the info to be saved in the file
# make a menu in which create fileName
# delete file
# add something to a file (to what file name)
#write something to a file(Give warning that all data will be lost)
#print what is in the file

#Please note that I used some code from previous programs

import os

fileName = " "
fileMenuOn = 1
option1 = "0"
question = " "

#To create a new file (or open an existing one)
def newFile():
    fileName = input("What is the name of the file you would like to create? Please note that if a file with this name already exists, a new file will not be created. ")
    fileName = fileName + ".txt"

    myFile = open(fileName, "w")

    question = input("Would you like to write something to this file (Please type yes if you would like to write something to this file)? ")
    if question == "yes":
        question = input("What you like to write to this file?")
        myFile.write(question)

    myFile.close()
    
    question = input("Would you like to read this file (Please type yes if you would like to read this file)? ")
    if question == "yes":
        myFile = open(fileName, "r")

        print(myFile.read())

        myFile.close()

# To delete a file 
def deleteFile():
    fileName = input("What is the name of the file you would like to delete? ")
    fileName = fileName + ".txt"
    if os.path.exists(fileName):
        os.remove(fileName)
        print("File deleted!")
    else:
        print("File not found. Returning to File Menu")

# To append something to a file
def appendFile():
    fileName = input("What is the name of the file you would like to write to? ")
    fileName = fileName + ".txt"
    question = input("What you like to write to this file?")
    myFile = open(fileName, "a")
    myFile.write(question)
    
    myFile.close()

# To overwrite a file
def overwriteFile():
    fileName = input("What is the name of the file you would like to create? Please note that if a file with this name already exists, a new file will not be created. ")
    fileName = fileName + ".txt"
    
    myFile = open(fileName, "w")

    question = input("Are you sure that you would like to overwrite this file? Previous data will likely be lost (Please type yes if you would like to overwrite this file. )? ")
    if question == "yes":
        question = input("What you like to write to this file? ")
        myFile.write(question)

    myFile.close()
    
    question = input("Would you like to read this file (Please type yes if you would like to read this file)? ")
    if question == "yes":
        myFile = open(fileName, "r")

        print(myFile.read())

        myFile.close()

# To read a file
def readFile():
    fileName = input("What is the name of the file you would like to read? ")
    fileName = fileName + ".txt"
    myFile = open(fileName, "r")

    print(myFile.read())

    myFile.close()
    

# The main menu
while option1 != "1" and option1 != "2" and option1 != "3" and option1 != "4" and option1 != "5" and option1 != "6": 
    print("____________________________________________________________")
    print("|                                                          |")
    print("|                   Welcome to File Menu                   |")
    print("|                     Choose an option                     |")
    print("|                                                          |")
    print("|                   1) Create a new file                   |")
    print("|                   2) Delete a file                       |")
    print("|                   3) Add something to a file             |")
    print("|                   4) Overwrite a file                    |")
    print("|                   5) Read and print a file               |")
    print("|                   6) Quit File Menu                      |")
    print("|                                                          |")
    print("____________________________________________________________")

    option1 = input("Input: ")
    
    #Exits the problem when the user inputs 6
    if option1 == "6":
        exit()
        
    if option1 != "1" and option1 != "2" and option1 != "3" and option1 != "4" and option1 != "5" and option1 != "6":
        print("Please enter a valid input")

    if option1 == "1":
        newFile()
    if option1 == "2":
        deleteFile()
    if option1 == "3":
        appendFile()
    if option1 == "4":
        overwriteFile()
    if option1 == "5":
        readFile()

    option1 = 0

