"""
Assignment 2
Student Name: Alejandro Cabrera
Purpose: Use a nested-for loop to print the following pattern in row-major sequence
        xooooox
        oxoooxo
        ooxoxoo
        oooxooo
        ooxoxoo
        oxoooxo
        xooooox
"""

#starting from the 1st row and ending at the 7th row
for row in range(1,8):
    
    #within each row starting from the 1st col and ending at the 7th col
    for col in range(1,8):
        if((row+col)%8==0 or row==col): #checks if the position should print 'x' or 'o'
            print("x",end="") #prints a 'x' in the location
        else:
            print("o",end="") #prints an 'o' in the location

    #go on to the next row
    print()
    
