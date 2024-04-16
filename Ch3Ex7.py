"""
Chapter 3, Exercise 7
Student Name: Alejandro Cabrera
Purpose: Use a nested-for loop to print the following pattern in row-major sequence
        X X X
         X X 
        X X X
         X X 
        X X X
"""
#starting from the 1st row and ending at the 5th row
for i in range(0,5):
    
    #within each row starting from the 1st col and ending at the 5th col
    for j in range(0,5):
        #decide what character to print
        if((i+j)%2==0):
            print("X",end="") #print each col
        else:
            print(" ",end="")

    #go on to the next row
    print()
