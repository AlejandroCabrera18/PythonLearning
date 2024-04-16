"""
Chapter 3, Exercise 6
Student Name: Alejandro Cabrera
Purpose: Use a nested-while loop to print the following pattern in row-major sequence
        XXXXX
        XXXXX
        XXXXX
        XXXXX
        XXXXX
"""
i=0 #starting from the 1st row

while i < 5: #ending at the 5th row
    j=0 #within each row starting from the 1st col
    while j < 5: #ending at the 5th col
        print("X",end="") #print each col
        j+=1 #increment the column

    print()#go on to the next row
    i+=1 #increment the row
