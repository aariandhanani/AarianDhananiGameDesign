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

myFile = open("newFile.txt", "w") #Opens a file if it exists and if it doesn't exist it will create a file

myFile.write("Hello")

myFile.close()


myFile = open("newFile.txt", "r")

print(myFile.read())

myFile.close()


myFile = open("newFile.txt", "a") #Opens a file if it exists and if it doesn't exist it will create a file

myFile.write("\nOk")

myFile.close()


myFile = open("newFile.txt", "r")

print(myFile.read())

myFile.close()


# https://www.guru99.com/reading-and-writing-files-in-python.html
