"""
Assignment 4
Student Name: Alejandro Cabrera
Purpose: program in which the main function is calling a function to
         print positive integers from 1 to N recursively, where N ≥ 1
"""

def main():
    """The main function of the program"""

    #prompt for the value of n
    num = int(input("Please enter a positive integer: "))

    #csll the recursive function
    printToN(num)


def printToN(n):
    """Print positive integers from 1 to n recursively"""
    if(n==1):
        print(1) #base case
    else:
        printToN(n-1)#recursive case
        print(n)
        return
    
#entry point of execution
main()
