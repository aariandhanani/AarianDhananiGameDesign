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
