"""
Chapter 4, Exercise 4
Student Name: Alejandro Cabrera
Purpose: Read in all contents from an input file and display these contents on
        the screen
"""

#open the input file
inFile = open("num.txt","r")

"""
#Read in the entire contents
contents = inFile.read()    

#display the contents on the screen
print(contents, end="")

#no need to close an input file
"""
"""
#read in a line at a time and display this line on the screen
for line in inFile:
    print(line, end="")
"""
#read in a line at a time and display this line on the screen
while True:
    line = inFile.readline()
    if line == "":
        break #reached the end of the input file
    print(line, end="")
