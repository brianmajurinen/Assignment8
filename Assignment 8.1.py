#Brian Majurinen
#Bellevue University CIS245
import os

#checking to see if the file path exists
filePath = input("Enter the exact path of the directory you would like to save this file to:")
pathExists = os.path.exists(filePath)
if pathExists is True:
    print("That is a valid directory")
else:
    print ("Invalid directory")
    quit()

#putting together the file name
fileName = input("Enter the name of the file you would like to use."
"A new file will be created. ")

totalFile = filePath + "/" + fileName
#print(totalFile) this was a test to see if the total filename would print
#Getting data from user
userName = input("What is your name?")
userAddress = input("What is your address?")
userPhone = input("What is your phone number?")
file1 = open("totalFile", "w")
file1.write(userName)
file1.write(userAddress)
file1.write(userPhone)
#Reading back the contents of the file
with open("totalFile", "r") as file1:
    print(file1.read())

file1.close()