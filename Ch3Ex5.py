"""
Chapter 3, Exercise 5
Student Name: Alejandro Cabrera
Purpose: Use a nested-for loop to print the following pattern in row-major sequence
        XXXXX
        XXXXX
        XXXXX
        XXXXX
        XXXXX
"""

#starting from the 1st row and ending at the 5th row
for i in range(0,5):
    
    #within each row starting from the 1st col and ending at the 5th col
    for j in range(0,5):
        print("X",end="") #print each col

    #go on to the next row
    print()
    
