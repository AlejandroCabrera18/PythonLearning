"""
Assignment 2
Student Name: Alejandro Cabrera
Purpose: Use a nested-while loop to print the following pattern in row-major sequence
        xooooox
        oxoooxo
        ooxoxoo
        oooxooo
        ooxoxoo
        oxoooxo
        xooooox
"""

#starting from the 1st row and ending at the 7th row
row = 1
while row <= 7:
    
    #within each row starting from the 1st col and ending at the 7th col
    col = 1
    while col <= 8:
        if((row+col)%8==0 or row==col): #checks if the position should print 'x' or 'o'
            print("x",end="") #prints a 'x' in the location
        else:
            print("o",end="") #prints an 'o' in the location
        col += 1
    #go on to the next row
    print()
    row += 1
