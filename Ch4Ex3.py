"""
Chapter 4, Exercise 3
Student Name: Alejandro Cabrera
Purpose: Generate 10 random integers, between 1 - 100, and append them
        to an output file
"""
from random import * #for the randint function

outFile = open("num.txt","a") #Open the output file

for i in range (10): #generate and write random integers to the output file
    num = randint(1,100)
    outFile.write(str(num) + "\n")

outFile.close() #close the output file

