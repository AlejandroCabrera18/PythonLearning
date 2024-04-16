"""
Chapter 3, Exercise 8
Student Name: Alejandro Cabrera
Purpose: Use a nested-while loop to print the following pattern in row-major sequence
        X X X
         X X 
        X X X
         X X 
        X X X
"""
i=0 #starting from the 1st row
while i<5: #ending at the 5th row
    j=0 #within each row starting from the 1st col
    while j<5: #ending at the 5th col
        #decide what character to print
        if((i+j)%2==0):
            print("X",end="") #print each X
        else:
            print(" ",end="") #print each space
        j+=1 #increment column
    #go on to the next row
    print()
    i+=1 #increment row
