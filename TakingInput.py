import os

#We use the input function to take an input
#Wh have to have an assignment staement to store an input

fname = input("What is your name: ")
lname = input ("What is your last my friend: ")

print("Wasup, "+fname +lname)

initialname = fname [0] + "." + lname #adding strings is concatination 
print("Hi my son, "+initialname)

os.system("say "+fname +lname)
