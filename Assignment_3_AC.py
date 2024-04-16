"""
Assignment 3
Student Name: Alejandro Cabrera
Purpose: Please write a program that reads in the contents from an input file
         called “in.txt” and write these contents to an output file called
         “out.txt”.
"""
inFile = open("in.txt","r") #open the input file
outFile = open("out.txt","w") #Open the output file

#Read in the entire contents from the input file
contents = inFile.read()    

#Write in the entire contents to the output file
outFile.write(contents)

#Close the output file
outFile.close()

