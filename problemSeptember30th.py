str = "Here are the instructions to install Drivers\n1. After the download is completed go to where you saved the folder.\n(By default everything you download from the Internet is saved to the Downloads folder)\n2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again.\n3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon.\n4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below:\n*setup application\n*Asussetup\n*pnpinstal64\n*pnputil\n*Igxpin\n5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up."

#Source: https://www.programiz.com/python-programming/methods/string/count#:~:text=The%20string%20count()%20method,substring%20is%20present%20in%20it.
numberOfDrivers = str.count("Drivers")
print(numberOfDrivers)

print(len(str))

str = str.replace("Extract", "EXTRACT")

str = str.replace("setup", "SETUP")
str = str.replace("Setup", "SETUP")

indexOf4 = str.find("4")
print("The index of 4 is: ", end = "")
print(indexOf4)

indexOfFirstEnter = str.find("\n")
print(indexOfFirstEnter)

print()
print(str)

# Here are the instructions to install Drivers
# 1. After the download is completed go to where you saved the folder.
# (By default everything you download from the Internet is saved to the Downloads folder)
# 2. Right click on the folder and choose ''Extract All'' and then choose ''Extract'' again.
# 3. Once all the contents have been extracted you may delete/disregard the folder with the zip icon.
# 4. Next, open and Run the SETUP file. (In most cases it is a setup.exe file OR one listed below:
# *setup application
# *Asussetup
# *pnpinstal64
# *pnputil
# *Igxpin
# 5. Please choose to 'repair' or 'update' the existing installation (driver) IF any one of those options do appear during the set up.
# •	Find how many times the word Drivers is used
# •	How long in your Strint
# •	Replace Extract with EXTRACT
# •	Replace setup or Setup with SETUP
# •	Find  ‘4’
